import sys
sys.setrecursionlimit(10000)



def solve():
    data = sys.stdin.read().strip().split()
    if not data: return
    it = iter(data)
    j = int(next(it)); m = int(next(it))
    jobs = []
    total_ops = 0
    for _ in range(j):
        o = int(next(it))
        ops = []
        for __ in range(o):
            a = int(next(it)); d = int(next(it))
            ops.append((a-1, d))  # 0-index machine
        jobs.append(ops)
        total_ops += o
    # Precompute suffix sums for each job
    suffix = []
    for ops in jobs:
        suf = [0]*(len(ops)+1)
        for i in range(len(ops)-1, -1, -1):
            suf[i] = suf[i+1] + ops[i][1]
        suffix.append(suf)
    # Total machine work
    machine_total = [0]*m
    for ops in jobs:
        for a,d in ops:
            machine_total[a] += d
    # Initial upper bound: greedy list scheduling
    # We'll simulate: at each step, among jobs with remaining ops, pick the one with smallest earliest start time (max(job_ready, machine_free[machine])).
    job_ready = [0]*j
    machine_free = [0]*m
    job_next = [0]*j
    remaining_machine = machine_total[:]
    # We'll just do a simple loop until all done
    while True:
        best_job = -1
        best_start = None
        for i in range(j):
            if job_next[i] < len(jobs[i]):
                a,d = jobs[i][job_next[i]]
                start = max(job_ready[i], machine_free[a])
                if best_job == -1 or start < best_start:
                    best_start = start
                    best_job = i
        if best_job == -1:
            break
        a,d = jobs[best_job][job_next[best_job]]
        start = max(job_ready[best_job], machine_free[a])
        finish = start + d
        job_ready[best_job] = finish
        machine_free[a] = finish
        job_next[best_job] += 1
        remaining_machine[a] -= d
    best = max(job_ready)
    # Now DFS
    # We'll use recursion with memoization
    visited = set()
    # We'll pass job_ready, machine_free, job_next as lists; convert to tuple for memo.
    def dfs(job_ready, machine_free, job_next):
        nonlocal best
        # Compute current makespan
        cur_max = max(job_ready)
        if cur_max >= best:
            return
        # Check if all done
        if all(job_next[i] == len(jobs[i]) for i in range(j)):
            best = cur_max
            return
        # Compute lower bound
        lb = cur_max
        for i in range(j):
            if job_next[i] < len(jobs[i]):
                lb = max(lb, job_ready[i] + suffix[i][job_next[i]])
        # For machines, we need remaining work on each machine
        # We can compute from job_next: for each machine, sum durations of ops not yet scheduled.
        rem_machine = [0]*m
        for i in range(j):
            for k in range(job_next[i], len(jobs[i])):
                a,d = jobs[i][k]
                rem_machine[a] += d
        for a in range(m):
            lb = max(lb, machine_free[a] + rem_machine[a])
        if lb >= best:
            return
        # Memoization
        state = (tuple(job_ready), tuple(machine_free), tuple(job_next))
        if state in visited:
            return
        visited.add(state)
        # Generate candidates: jobs with remaining ops
        candidates = []
        for i in range(j):
            if job_next[i] < len(jobs[i]):
                a,d = jobs[i][job_next[i]]
                start = max(job_ready[i], machine_free[a])
                candidates.append((start, i))
        # Sort by start time ascending, then maybe by remaining work descending
        candidates.sort(key=lambda x: (x[0], -suffix[x[1]][job_next[x[1]]])))
        for start, i in candidates:
            a,d = jobs[i][job_next[i]]
            # start already computed
            finish = start + d
            # Save old values
            old_job_ready = job_ready[i]
            old_machine_free = machine_free[a]
            old_next = job_next[i]
            # Update
            job_ready[i] = finish
            machine_free[a] = finish
            job_next[i] += 1
            dfs(job_ready, machine_free, job_next)
            # Restore
            job_ready[i] = old_job_ready
            machine_free[a] = old_machine_free
            job_next[i] = old_next
    # Start DFS
    job_ready = [0]*j
    machine_free = [0]*m
    job_next = [0]*j
    dfs(job_ready, machine_free, job_next)
    print(best)



if __name__ == "__main__":
    solve()