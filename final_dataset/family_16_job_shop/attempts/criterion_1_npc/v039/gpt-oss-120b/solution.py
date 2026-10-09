import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    J = int(next(it))          # number of components (jobs)
    M = int(next(it))          # number of machines (facilities)

    jobs = []                  # list of list[(machine, duration)]
    for _ in range(J):
        o = int(next(it))
        ops = []
        for _ in range(o):
            fac = int(next(it)) - 1          # to 0‑based
            dur = int(next(it))
            ops.append((fac, dur))
        jobs.append(ops)

    # ----- pre‑compute remaining processing time for each job -----
    rem_job = []
    for ops in jobs:
        L = len(ops)
        suffix = [0] * (L + 1)
        for i in range(L - 1, -1, -1):
            suffix[i] = suffix[i + 1] + ops[i][1]
        rem_job.append(suffix)                # suffix[pos] = remaining time

    # ----- total remaining time per machine (initial) ----------
    rem_mach = [0] * M
    for ops in jobs:
        for fac, dur in ops:
            rem_mach[fac] += dur

    # mutable state
    pos = [0] * J                     # next operation index per job
    job_end = [0] * J                 # finishing time of last scheduled op per job
    mach_end = [0] * M                # when each machine becomes free

    total_ops = sum(len(j) for j in jobs)
    best = [float('inf')]             # list to allow write inside nested function

    # ----- lower bound function -----
    def lower_bound() -> int:
        lb_job = 0
        for j in range(J):
            cur = job_end[j] + rem_job[j][pos[j]]
            if cur > lb_job:
                lb_job = cur
        lb_mach = 0
        for m in range(M):
            cur = mach_end[m] + rem_mach[m]
            if cur > lb_mach:
                lb_mach = cur
        return lb_job if lb_job > lb_mach else lb_mach

    # ----- depth‑first search -----
    def dfs(scheduled: int):
        if scheduled == total_ops:
            cur_makespan = max(job_end) if J else 0
            if cur_makespan < best[0]:
                best[0] = cur_makespan
            return

        # collect ready jobs
        ready = []
        for j in range(J):
            if pos[j] < len(jobs[j]):
                fac, dur = jobs[j][pos[j]]
                est = job_end[j] if job_end[j] > mach_end[fac] else mach_end[fac]
                ready.append((est, j, fac, dur))

        # order by earliest possible start time
        ready.sort(key=lambda x: x[0])

        for est, j, fac, dur in ready:
            start = est
            finish = start + dur

            # apply
            old_pos = pos[j]
            old_job_end = job_end[j]
            old_mach_end = mach_end[fac]
            old_rem_mach = rem_mach[fac]

            pos[j] += 1
            job_end[j] = finish
            mach_end[fac] = finish
            rem_mach[fac] -= dur

            # pruning
            if lower_bound() < best[0]:
                dfs(scheduled + 1)

            # undo
            pos[j] = old_pos
            job_end[j] = old_job_end
            mach_end[fac] = old_mach_end
            rem_mach[fac] = old_rem_mach

    dfs(0)
    print(best[0])

if __name__ == "__main__":
    solve()