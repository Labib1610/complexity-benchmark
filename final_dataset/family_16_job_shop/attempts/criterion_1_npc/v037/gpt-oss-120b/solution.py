import sys

def solve() -> None:
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    it = iter(data)
    J = next(it)          # number of jobs
    M = next(it)          # number of machines

    jobs = []
    for _ in range(J):
        o = next(it)
        ops = []
        for __ in range(o):
            mach = next(it) - 1          # zero based
            dur = next(it)
            ops.append((mach, dur))
        jobs.append(ops)

    # suffix sums of remaining durations for each job
    suffix = []
    for ops in jobs:
        n = len(ops)
        suff = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suff[i] = suff[i + 1] + ops[i][1]
        suffix.append(suff)

    # total remaining processing time per machine (initially all operations)
    total_machine = [0] * M
    for ops in jobs:
        for mach, dur in ops:
            total_machine[mach] += dur

    # ---------- greedy upper bound ----------
    def greedy_upper() -> int:
        jp = [0] * J                 # next operation index per job
        jf = [0] * J                 # finish time of last scheduled op of each job
        mf = [0] * M                 # free time of each machine
        rm = total_machine[:]        # remaining processing per machine
        makespan = 0
        total_ops = sum(len(j) for j in jobs)

        for _ in range(total_ops):
            best_start = 10**9
            best_j = best_m = best_d = -1
            for j in range(J):
                pos = jp[j]
                if pos < len(jobs[j]):
                    m, d = jobs[j][pos]
                    start = jf[j] if jf[j] > mf[m] else mf[m]
                    if start < best_start:
                        best_start = start
                        best_j, best_m, best_d = j, m, d
            finish = best_start + best_d
            jp[best_j] += 1
            jf[best_j] = finish
            mf[best_m] = finish
            rm[best_m] -= best_d
            if finish > makespan:
                makespan = finish
        return makespan

    best = greedy_upper()           # current best makespan (upper bound)

    # ---------- branch and bound ----------
    job_pos = [0] * J               # next operation to schedule per job
    job_finish = [0] * J            # time when current job becomes ready for next op
    machine_free = [0] * M          # when each machine becomes free
    remaining_machine = total_machine[:]   # still unscheduled work per machine

    sys.setrecursionlimit(10000)

    INF = 10 ** 9

    def dfs() -> None:
        nonlocal best

        # all operations scheduled ?
        if all(job_pos[j] == len(jobs[j]) for j in range(J)):
            makespan = max(job_finish)            # all jobs finished
            if makespan < best:
                best = makespan
            return

        # lower bound based on remaining work
        lb = 0
        for j in range(J):
            est = job_finish[j] + suffix[j][job_pos[j]]
            if est > lb:
                lb = est
        for m in range(M):
            est = machine_free[m] + remaining_machine[m]
            if est > lb:
                lb = est
        if lb >= best:
            return

        # collect ready operations and the smallest possible start time among them
        min_start = INF
        ready = []
        for j in range(J):
            pos = job_pos[j]
            if pos < len(jobs[j]):
                m, d = jobs[j][pos]
                start = job_finish[j] if job_finish[j] > machine_free[m] else machine_free[m]
                ready.append((j, m, d, start))
                if start < min_start:
                    min_start = start

        # branch only on operations that can start at the earliest time
        for j, m, d, start in ready:
            if start != min_start:
                continue

            # schedule operation
            old_job_finish = job_finish[j]
            old_machine_free = machine_free[m]
            old_rem = remaining_machine[m]

            job_pos[j] += 1
            job_finish[j] = start + d
            machine_free[m] = start + d
            remaining_machine[m] = old_rem - d

            dfs()

            # backtrack
            job_pos[j] -= 1
            job_finish[j] = old_job_finish
            machine_free[m] = old_machine_free
            remaining_machine[m] = old_rem

    dfs()
    print(best)


if __name__ == "__main__":
    solve()