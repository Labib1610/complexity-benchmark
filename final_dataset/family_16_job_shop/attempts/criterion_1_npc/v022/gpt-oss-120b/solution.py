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
    for _ in range(j):
        o = int(next(it))
        ops = []
        for __ in range(o):
            core = int(next(it)) - 1
            dur = int(next(it))
            ops.append((core, dur))
        jobs.append(ops)

    # precompute remaining sums per job from each position
    rem_job = []
    for ops in jobs:
        n = len(ops)
        pref = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            pref[i] = pref[i + 1] + ops[i][1]
        rem_job.append(pref)   # pref[pos] = sum of durations from pos onward

    # initial upper bound: schedule jobs one after another (naive)
    job_time = [0] * j
    machine_time = [0] * m
    for idx in range(j):
        for core, dur in jobs[idx]:
            start = max(job_time[idx], machine_time[core])
            finish = start + dur
            job_time[idx] = finish
            machine_time[core] = finish
    best = max(job_time)

    # initial state
    pos = [0] * j
    job_time = [0] * j
    machine_time = [0] * m
    rem_machine = [0] * m
    total_rem = 0
    for idx, ops in enumerate(jobs):
        for core, dur in ops:
            rem_machine[core] += dur
            total_rem += dur

    # recursion
    from functools import lru_cache

    # encode state as tuple(pos) + tuple(job_time) + tuple(machine_time) maybe too big.
    # We'll use simple recursion with pruning, no memo.

    def dfs(total_remain):
        nonlocal best
        if total_remain == 0:
            makespan = max(job_time)
            if makespan < best:
                best = makespan
            return

        # lower bound
        lb = 0
        for i in range(j):
            est = job_time[i] + rem_job[i][pos[i]]
            if est > lb:
                lb = est
        for c in range(m):
            est = machine_time[c] + rem_machine[c]
            if est > lb:
                lb = est
        if lb >= best:
            return

        # generate candidates
        candidates = []
        for i in range(j):
            if pos[i] < len(jobs[i]):
                core, dur = jobs[i][pos[i]]
                start = job_time[i] if job_time[i] > machine_time[core] else machine_time[core]
                candidates.append((start, i, core, dur))
        # sort by earliest start to improve pruning
        candidates.sort()
        for start, i, core, dur in candidates:
            # schedule this operation
            finish = start + dur
            # backup
            old_job_time = job_time[i]
            old_machine_time = machine_time[core]
            old_pos = pos[i]
            old_rem_machine = rem_machine[core]

            job_time[i] = finish
            machine_time[core] = finish
            pos[i] += 1
            rem_machine[core] -= dur

            dfs(total_remain - dur)

            # restore
            job_time[i] = old_job_time
            machine_time[core] = old_machine_time
            pos[i] = old_pos
            rem_machine[core] = old_rem_machine

    dfs(total_rem)
    print(best)

if __name__ == "__main__":
    solve()