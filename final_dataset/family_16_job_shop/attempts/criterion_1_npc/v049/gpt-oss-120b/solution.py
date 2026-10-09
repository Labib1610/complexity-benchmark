import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    J = next(it)
    M = next(it)

    jobs = []                     # list of list of (machine, time)
    total_ops = 0
    for _ in range(J):
        o = next(it)
        ops = []
        for __ in range(o):
            mach = next(it) - 1   # zero based
            dur = next(it)
            ops.append((mach, dur))
        jobs.append(ops)
        total_ops += o

    # pre‑compute remaining processing times per job
    rem_job = [[0] * (len(job) + 1) for job in jobs]
    for idx, job in enumerate(jobs):
        s = 0
        for p in range(len(job) - 1, -1, -1):
            s += job[p][1]
            rem_job[idx][p] = s

    # pre‑compute remaining processing times per machine
    # for each job position we need the sum of remaining durations on each machine
    # we can store a list of length M for each job position
    rem_mach = [ [0]*M for _ in range(total_ops+1) ]   # not used directly
    # easier: for each machine keep total remaining time over all jobs
    # we will recompute it on the fly from job positions (fast enough)
    # but to keep O(j+m) we compute per machine sums each bound evaluation.

    # state
    job_pos = [0] * J
    job_ready = [0] * J
    machine_free = [0] * M
    scheduled = 0
    cur_makespan = 0
    best = float('inf')

    # helper: lower bound
    def lower_bound():
        # job wise
        lb = cur_makespan
        for i in range(J):
            p = job_pos[i]
            if p < len(jobs[i]):
                lb = max(lb, job_ready[i] + rem_job[i][p])
        # machine wise
        # compute remaining time per machine
        rem_per_m = [0] * M
        for i in range(J):
            p = job_pos[i]
            for k in range(p, len(jobs[i])):
                mach, dur = jobs[i][k]
                rem_per_m[mach] += dur
        for k in range(M):
            lb = max(lb, machine_free[k] + rem_per_m[k])
        return lb

    # main dfs
    def dfs():
        nonlocal scheduled, cur_makespan, best
        if scheduled == total_ops:
            if cur_makespan < best:
                best = cur_makespan
            return
        if lower_bound() >= best:
            return

        # collect candidates
        cand = []
        for i in range(J):
            p = job_pos[i]
            if p == len(jobs[i]):
                continue
            mach, dur = jobs[i][p]
            start = job_ready[i] if job_ready[i] > machine_free[mach] else machine_free[mach]
            finish = start + dur
            cand.append((finish, i, mach, dur, start))

        cand.sort()          # earliest finish first
        for finish, i, mach, dur, start in cand:
            # apply
            old_job_ready = job_ready[i]
            old_mach_free = machine_free[mach]
            old_makespan = cur_makespan

            job_ready[i] = finish
            machine_free[mach] = finish
            job_pos[i] += 1
            scheduled += 1
            if finish > cur_makespan:
                cur_makespan = finish

            dfs()

            # undo
            scheduled -= 1
            job_pos[i] -= 1
            job_ready[i] = old_job_ready
            machine_free[mach] = old_mach_free
            cur_makespan = old_makespan

    dfs()
    print(best)

if __name__ == "__main__":
    solve()