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
    total_tasks = 0
    for _ in range(j):
        o = int(next(it))
        tasks = []
        for __ in range(o):
            eq = int(next(it)) - 1
            dur = int(next(it))
            tasks.append((eq, dur))
        jobs.append(tasks)
        total_tasks += o

    # simple list scheduling to get an initial upper bound
    job_pos = [0] * j
    job_ready = [0] * j
    mach_ready = [0] * m
    cur_time = 0
    remaining = total_tasks
    while remaining:
        # collect all ready tasks
        ready = []
        for idx in range(j):
            p = job_pos[idx]
            if p < len(jobs[idx]):
                eq, dur = jobs[idx][p]
                start = max(job_ready[idx], mach_ready[eq])
                ready.append((start, idx, eq, dur))
        # pick the one with smallest start (break ties arbitrarily)
        start, idx, eq, dur = min(ready, key=lambda x: x[0])
        cur_time = max(cur_time, start + dur)
        job_ready[idx] = start + dur
        mach_ready[eq] = start + dur
        job_pos[idx] += 1
        remaining -= 1
    best = cur_time

    # precompute remaining total time per job for lower bound
    rem_job_sum = [ [0]*(len(jobs[i])+1) for i in range(j) ]
    for i in range(j):
        s = 0
        for p in range(len(jobs[i])-1, -1, -1):
            s += jobs[i][p][1]
            rem_job_sum[i][p] = s

    # lower bound function
    def lower_bound(job_pos, job_ready, mach_ready):
        # max of each job's remaining work added to its ready time
        lb = 0
        for i in range(j):
            if job_pos[i] < len(jobs[i]):
                lb = max(lb, job_ready[i] + rem_job_sum[i][job_pos[i]])
        # also each machine's remaining work
        mach_rem = [0]*m
        for i in range(j):
            for p in range(job_pos[i], len(jobs[i])):
                eq, dur = jobs[i][p]
                mach_rem[eq] += dur
        for eq in range(m):
            lb = max(lb, mach_ready[eq] + mach_rem[eq])
        return lb

    # recursive search
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def dfs(state):
        # state: (tuple(job_pos), tuple(job_ready), tuple(mach_ready))
        job_pos, job_ready, mach_ready = state
        if sum(job_pos) == total_tasks:
            return max(job_ready)  # all done, makespan
        # prune with lower bound
        lb = lower_bound(job_pos, job_ready, mach_ready)
        if lb >= best:
            return float('inf')
        # generate ready tasks
        candidates = []
        for i in range(j):
            p = job_pos[i]
            if p < len(jobs[i]):
                eq, dur = jobs[i][p]
                start = max(job_ready[i], mach_ready[eq])
                candidates.append((start, i, eq, dur))
        # order candidates by earliest start
        candidates.sort(key=lambda x: x[0])
        best_local = float('inf')
        for start, i, eq, dur in candidates:
            new_job_ready = list(job_ready)
            new_mach_ready = list(mach_ready)
            new_job_ready[i] = start + dur
            new_mach_ready[eq] = start + dur
            new_job_pos = list(job_pos)
            new_job_pos[i] += 1
            res = dfs((tuple(new_job_pos), tuple(new_job_ready), tuple(new_mach_ready)))
            if res < best_local:
                best_local = res
                # global prune
                if best_local < best:
                    nonlocal best
                    best = best_local
            if best_local <= lb:  # cannot improve further
                break
        return best_local

    # start recursion
    init_state = (tuple([0]*j), tuple([0]*j), tuple([0]*m))
    dfs(init_state)
    print(best)

if __name__ == "__main__":
    solve()