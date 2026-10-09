import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    m = int(next(it))
    jobs = []
    total_ops = 0
    for _ in range(j):
        p = int(next(it))
        ops = []
        for __ in range(p):
            bay = int(next(it)) - 1
            dur = int(next(it))
            ops.append((bay, dur))
        jobs.append(ops)
        total_ops += p

    # precompute remaining total time per job and per machine for lower bound
    job_rem = [sum(d for _, d in ops) for ops in jobs]
    mach_rem = [0] * m
    for ops in jobs:
        for bay, d in ops:
            mach_rem[bay] += d

    best = [float('inf')]

    # state
    next_idx = [0] * j          # next operation index for each job
    job_ready = [0] * j         # time when job is ready for its next op
    mach_free = [0] * m         # time when each machine becomes free

    def lower_bound(cur_mk):
        # simple bound: max of current makespan, remaining per job, remaining per machine
        lb = cur_mk
        for i in range(j):
            rem = sum(d for _, d in jobs[i][next_idx[i]:])
            lb = max(lb, job_ready[i] + rem)
        for k in range(m):
            rem = 0
            for i in range(j):
                for op in jobs[i][next_idx[i]:]:
                    if op[0] == k:
                        rem += op[1]
            lb = max(lb, mach_free[k] + rem)
        return lb

    def dfs(done):
        if done == total_ops:
            cur_mk = max(mach_free)
            if cur_mk < best[0]:
                best[0] = cur_mk
            return
        # prune
        cur_mk = max(mach_free)
        if cur_mk >= best[0]:
            return
        if lower_bound(cur_mk) >= best[0]:
            return

        # collect all jobs that have a pending operation
        for i in range(j):
            if next_idx[i] >= len(jobs[i]):
                continue
            bay, dur = jobs[i][next_idx[i]]
            start = max(job_ready[i], mach_free[bay])
            finish = start + dur

            # apply
            prev_job_ready = job_ready[i]
            prev_mach_free = mach_free[bay]
            prev_next = next_idx[i]

            job_ready[i] = finish
            mach_free[bay] = finish
            next_idx[i] += 1

            dfs(done + 1)

            # backtrack
            job_ready[i] = prev_job_ready
            mach_free[bay] = prev_mach_free
            next_idx[i] = prev_next

    dfs(0)
    print(best[0])

if __name__ == "__main__":
    solve()