import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    J = next(it)
    M = next(it)
    jobs = []
    total_steps = 0
    for _ in range(J):
        o = next(it)
        steps = []
        for __ in range(o):
            w = next(it) - 1          # zero‑based
            d = next(it)
            steps.append((w, d))
        jobs.append(steps)
        total_steps += o

    # pre‑compute remaining processing time per job and per machine
    rem_job = [sum(d for _, d in job) for job in jobs]
    rem_mach = [0] * M
    for job in jobs:
        for w, d in job:
            rem_mach[w] += d

    best = float('inf')

    # current indices of next step for each job
    idx = [0] * J
    # current finish times
    job_finish = [0] * J
    mach_finish = [0] * M

    # remaining sums that will be updated during recursion
    rem_job_cur = rem_job[:]
    rem_mach_cur = rem_mach[:]

    def lower_bound() -> int:
        # at least the max of:
        # - each job's current finish + its remaining work
        # - each machine's current finish + its remaining work
        lb = 0
        for j in range(J):
            lb = max(lb, job_finish[j] + rem_job_cur[j])
        for m in range(M):
            lb = max(lb, mach_finish[m] + rem_mach_cur[m])
        return lb

    def dfs(scheduled: int):
        nonlocal best
        if scheduled == total_steps:
            best = min(best, max(job_finish))
            return
        # prune by lower bound
        if lower_bound() >= best:
            return

        # generate candidates: jobs whose next step is ready
        candidates = []
        for j in range(J):
            if idx[j] < len(jobs[j]):
                w, d = jobs[j][idx[j]]
                start = max(job_finish[j], mach_finish[w])
                candidates.append((start, j, w, d))
        # order by earliest possible start (heuristic)
        candidates.sort()
        for start, j, w, d in candidates:
            # schedule this step
            finish = start + d

            # update state
            prev_job_finish = job_finish[j]
            prev_mach_finish = mach_finish[w]
            prev_rem_job = rem_job_cur[j]
            prev_rem_mach = rem_mach_cur[w]

            job_finish[j] = finish
            mach_finish[w] = finish
            idx[j] += 1
            rem_job_cur[j] -= d
            rem_mach_cur[w] -= d

            dfs(scheduled + 1)

            # backtrack
            idx[j] -= 1
            job_finish[j] = prev_job_finish
            mach_finish[w] = prev_mach_finish
            rem_job_cur[j] = prev_rem_job
            rem_mach_cur[w] = prev_rem_mach

    dfs(0)
    print(best)

if __name__ == "__main__":
    solve()