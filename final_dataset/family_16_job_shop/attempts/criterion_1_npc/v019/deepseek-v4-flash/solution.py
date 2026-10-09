def solve():
    j, m = map(int, input().split())
    jobs = []
    for _ in range(j):
        parts = list(map(int, input().split()))
        o = parts[0]
        ops = []
        ptr = 1
        for __ in range(o):
            mach = parts[ptr] - 1
            dur = parts[ptr+1]
            ops.append((mach, dur))
            ptr += 2
        jobs.append(ops)
    
    total_ops = sum(len(r) for r in jobs)
    best = float('inf')
    
    # For pruning: compute remaining total duration for each job, and each machine.
    # Actually lower bound computation can be done on fly.
    
    # We'll do DFS.
    # Each state: progress[i] = next phase index,
    #            finish_job[i] = time when last phase of elixir i finished (prev)
    #            machine_free[m] = time until machine m is free.
    # Also, we can precompute suffix sums of durations for each job and each machine to compute lower bound.
    
    # Precompute suffix sums for jobs (remaining duration from progress).
    suffix_dur_job = []
    for ops in jobs:
        s = 0
        arr = []
        for dur in [d for _, d in ops][::-1]:
            s += dur
            arr.append(s)
        suffix_dur_job.append(arr[::-1])
    # For machines: suffix sum per machine? But we need for each progress state, the sum of remaining durations on each machine across all unscheduled phases.
    # We can compute on the fly: when at a progress state, sum durations for phases >= progress for each elixir for each machine.
    
    def lower_bound(progress, finish_job, machine_free):
        lb = 0
        # Job bound: finish_job[i] (time of last finished phase before progress) + remaining durations
        for i in range(j):
            if progress[i] < len(jobs[i]):
                # sum of remaining phases durations
                rem = sum(d for _, d in jobs[i][progress[i]:])
                lb = max(lb, finish_job[i] + rem)
        # Machine bound: for each machine m, machine_free[m] + sum of remaining durations on m
        # To compute remaining durations on m, we have to sum over all jobs and phases >= progress.
        rem_machine = [0]*m
        for i in range(j):
            for k in range(progress[i], len(jobs[i])):
                mach, dur = jobs[i][k]
                rem_machine[mach] += dur
        for mm in range(m):
            lb = max(lb, machine_free[mm] + rem_machine[mm])
        return lb
    
    # Also compute initial machine_free = [0]*m, finish_job = [0]*j, progress = [0]*j.
    # Search:
    
    def dfs(progress, finish_job, machine_free, scheduled):
        nonlocal best
        # scheduled count
        if scheduled == total_ops:
            # makespan is max of finish_job (should be max of machine_free too)
            makespan = max(machine_free)
            if makespan < best:
                best = makespan
            return
        # lower bound
        lb = lower_bound(progress, finish_job, machine_free)
        if lb >= best:
            return
        
        # choose an operation to schedule next: pick any elixir with next phase not done
        # Optionally we can apply heuristic: choose operation with earliest possible start time? 
        # Or to reduce branching, try ordering by some heuristic.
        # We can iterate all ready elixirs.
        for i in range(j):
            if progress[i] < len(jobs[i]):
                mach, dur = jobs[i][progress[i]]
                earliest = max(finish_job[i], machine_free[mach])
                start = earliest
                end = start + dur
                # update state
                old_prog = progress[i]
                old_finish = finish_job[i]
                old_machine_free = machine_free[mach]
                progress[i] += 1
                finish_job[i] = end
                machine_free[mach] = end
                dfs(progress, finish_job, machine_free, scheduled+1)
                # recover
                progress[i] = old_prog
                finish_job[i] = old_finish
                machine_free[mach] = old_machine_free
    
    dfs([0]*j, [0]*j, [0]*m, 0)
    print(best)