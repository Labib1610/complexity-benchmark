import sys
from heapq import heappush, heappop

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    j = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    jobs = []
    for _ in range(j):
        o = int(data[idx]); idx += 1
        ops = []
        for _ in range(o):
            machine = int(data[idx]) - 1; idx += 1
            duration = int(data[idx]); idx += 1
            ops.append((machine, duration))
        jobs.append(ops)
    
    # State: (time, job_progress, machine_free_times)
    # job_progress[i] = number of completed operations for job i
    # machine_free_times[k] = time when machine k becomes free
    
    initial_progress = tuple(0 for _ in range(j))
    initial_machines = tuple(0 for _ in range(m))
    
    # Use Dijkstra-like search on state space
    # State: (time, progress, machine_times)
    # We want to minimize the maximum completion time
    
    # For pruning, track best known machine_times configuration for each progress
    best = {}
    
    heap = [(0, initial_progress, initial_machines)]
    best[(initial_progress, initial_machines)] = 0
    
    result = float('inf')
    
    while heap:
        time, progress, machines = heappop(heap)
        
        # Skip if we've found a better path to this state
        key = (progress, machines)
        if key in best and best[key] < time:
            continue
        
        # Check if all jobs are complete
        all_done = True
        for i in range(j):
            if progress[i] < len(jobs[i]):
                all_done = False
                break
        
        if all_done:
            result = time
            break
        
        # Generate next states by choosing which operation to schedule next
        # We can schedule any job's next operation that can start
        
        # For each job, its next operation can start at max(time, job_ready_time)
        # job_ready_time is when the previous operation of that job finished
        # But we need to track that... 
        
        # Actually, let's reconsider. The state needs to track when each job is ready
        # for its next operation. Let me redefine the state.
        
        # State: (job_ready_times, machine_free_times)
        # job_ready_times[i] = time when job i can start its next operation
        # machine_free_times[k] = time when machine k is free
        
        # But this state space might be too large. Let me think differently.
        
        # Alternative: Since operations are non-preemptive and we want optimal schedule,
        # we can use a different approach.
        
        # Let me restart with a cleaner state representation
        break
    
    # Restart with cleaner approach
    # State: (job_ready_times tuple, machine_free_times tuple)
    # job_ready_times[i] = earliest time job i can start next operation
    # machine_free_times[k] = earliest time machine k is free
    
    best2 = {}
    initial_job_ready = tuple(0 for _ in range(j))
    initial_machine_free = tuple(0 for _ in range(m))
    
    heap2 = [(0, initial_job_ready, initial_machine_free)]
    best2[(initial_job_ready, initial_machine_free)] = 0
    
    while heap2:
        time, job_ready, machine_free = heappop(heap2)
        
        key = (job_ready, machine_free)
        if key in best2 and best2[key] < time:
            continue
        
        # Check if all done
        all_done = True
        for i in range(j):
            if job_ready[i] < float('inf'):
                all_done = False
                break
        
        if all_done:
            print(time)
            return
        
        # Find all schedulable operations
        # An operation (job i, step k) is schedulable if job_ready[i] is not inf
        # It can start at max(job_ready[i], machine_free[machine])
        
        # To reduce branching, try scheduling each job's next operation
        # But we need to consider that we might want to delay some operations
        
        # Key insight: at any point, we should schedule at least one operation
        # The question is which one and when
        
        # For each job with remaining operations, its next op can start at
        # start_time = max(job_ready[i], machine_free[machine])
        # This is the earliest possible start time
        
        # We generate states by choosing one operation to schedule next
        # The operation starts at its earliest possible time
        
        # But this might miss optimal schedules where delaying helps...
        # Actually for this problem, scheduling at earliest possible time
        # for the chosen operation should be sufficient because we explore
        # all choices of which operation to schedule
        
        found_schedulable = False
        
        for i in range(j):
            if job_ready[i] == float('inf'):
                continue
            step = 0
            # Count completed operations for job i
            # We need to track this... but job_ready doesn't directly tell us
            # Actually if job_ready[i] is not inf, it means job i has more operations
            # and can start the next one at job_ready[i]
            # But we don't know which step... 
            
            # Hmm, we need to track progress too
            pass
        
        # Let me include progress in the state
        break
    
    # Final approach: State includes (progress, job_ready, machine_free)
    # But progress can be derived if we track job_ready properly
    # Actually, let's just track (progress, machine_free) and derive job_ready
    # Wait, we can't derive job_ready from progress alone
    
    # Let's track: (progress, machine_free) where job_ready is implicitly
    # the completion time of the last operation of each job
    # But we don't store that...
    
    # OK let me just track (progress, machine_free, job_ready) but that's 3 tuples
    # Actually (progress, machine_free) should be enough if we also store
    # the completion times... no.
    
    # Simplest correct approach: track (progress, machine_free, last_completion)
    # where last_completion[i] = when job i finished its last operation (= when it can start next)
    
    # But this state space could be huge. Let me think about bounds.
    # j <= 10, m <= 10, total ops <= 50
    # progress: each job has up to 50 ops, so progress space is huge
    # But total ops is 50, so sum of progress <= 50
    
    # Let me try a different approach: branch and bound / DFS with memoization
    
    # Actually, let's use the approach where state = (progress, machine_free)
    # and job_ready[i] = completion time of last op of job i
    # We need to store this... 
    
    # Let me just store (progress, machine_free, job_ready) as the state
    # and use Dijkstra
    
    # To make states comparable, we can normalize: the actual values matter
    # but we can use the max time as the priority
    
    # Let me try yet another approach: since total ops <= 50, we can try
    # a DFS with memoization where state = (progress, machine_free)
    # and we compute the minimum makespan from that state
    
    # For memoization, machine_free values matter. But we can normalize
    # by subtracting the minimum (since relative differences matter, not absolute)
    
    # Actually for correctness, absolute times matter for job_ready
    # But if we track (progress, machine_free, job_ready), we can normalize
    # by subtracting min of all times from all entries
    
    # Let me implement this
    
    from functools import lru_cache
    
    # We can't use lru_cache with tuples of varying content easily
    # Let's use a dict for memoization
    
    # State: (progress_tuple, machine_free_tuple, job_ready_tuple)
    # All normalized by subtracting the minimum time
    
    # Actually, let's think about what matters:
    # - progress: which operations are done
    # - For each job, when it can start next operation
    # - For each machine, when it's free
    
    # The relative timing matters. We can normalize by subtracting min.
    
    # But the state space might still be too large. Let's try.
    
    memo = {}
    
    def dfs(progress, machine_free, job_ready):
        # Check if all done
        all_done = all(progress[i] == len(jobs[i]) for i in range(j))
        if all_done:
            return 0
        
        # Normalize: subtract min of all times
        all_times = list(machine_free) + list(job_ready)
        min_time = min(all_times)
        if min_time > 0:
            machine_free = tuple(t - min_time for t in machine_free)
            job_ready = tuple(t - min_time for t in job_ready)
        
        key = (progress, machine_free, job_ready)
        if key in memo:
            return memo[key]
        
        best_makespan = float('inf')
        
        # Try scheduling each job's next operation
        for i in range(j):
            if progress[i] >= len(jobs[i]):
                continue
            machine, duration = jobs[i][progress[i]]
            start = max(job_ready[i], machine_free[machine])
            finish = start + duration
            
            new_progress = list(progress)
            new_progress[i] += 1
            new_progress = tuple(new_progress)
            
            new_machine_free = list(machine_free)
            new_machine_free[machine] = finish
            new_machine_free = tuple(new_machine_free)
            
            new_job_ready = list(job_ready)
            new_job_ready[i] = finish
            new_job_ready = tuple(new_job_ready)
            
            sub_result = dfs(new_progress, new_machine_free, new_job_ready)
            best_makespan = min(best_makespan, max(finish, sub_result + min_time) if min_time > 0 else max(finish, sub_result))
        
        # Wait, the normalization is causing issues. Let me think again.
        # If we normalize by subtracting min_time, then the actual finish time
        # is finish + min_time. And the sub_result is relative to the normalized state.
        # So the total makespan from the original state would be:
        # max(finish, min_time + sub_result) where finish is the actual finish time
        # But after normalization, finish becomes finish - min_time
        # So actual finish = (finish - min_time) + min_time = finish
        # And sub_result is the makespan from the normalized state
        # So total = max(finish, min_time + sub_result)
        
        # Hmm, this is getting complicated. Let me not normalize and just use
        # the raw values. The state space might be larger but let's try.
        pass
    
    # Let me restart with a simpler approach without normalization
    # and just use iterative deepening or branch and bound
    
    # Actually, let me try the Dijkstra approach properly
    
    # State: (job_ready, machine_free) - both tuples
    # job_ready[i] = inf if job i is done
    # Priority: max of all times (or just the max time in the state)
    
    # When all job_ready are inf, we're done
    
    # For each state, try scheduling each not-done job's next operation
    # The next operation for job i is at step = number of ops done
    # But we don't track step directly... 
    
    # We need to track step. Let me add progress to the state.
    # State: (progress, job_ready, machine_free)
    
    # This is getting messy. Let me just write a clean solution.
    
    # Clean solution using Dijkstra on (progress, machine_free, job_ready)
    
    INF = float('inf')
    
    # Initial state
    init_progress = tuple(0 for _ in range(j))
    init_job_ready = tuple(0 for _ in range(j))
    init_machine_free = tuple(0 for _ in range(m))
    
    # Priority queue: (max_time, progress, job_ready, machine_free)
    # where max_time = max(max(job_ready), max(machine_free))
    
    def get_max(job_ready, machine_free):
        return max(max(job_ready), max(machine_free))
    
    init_max = get_max(init_job_ready, init_machine_free)
    
    heap = [(init_max, init_progress, init_job_ready, init_machine_free)]
    visited = {}
    
    while heap:
        max_time, progress, job_ready, machine_free = heappop(heap)
        
        key = (progress, job_ready, machine_free)
        if key in visited:
            continue
        visited[key] = max_time
        
        # Check if all done
        all_done = all(progress[i] == len(jobs[i]) for i in range(j))
        if all_done:
            print(max_time)
            return
        
        # Try scheduling each job's next operation
        for i in range(j):
            if progress[i] >= len(jobs[i]):
                continue
            
            machine, duration = jobs[i][progress[i]]
            start = max(job_ready[i], machine_free[machine])
            finish = start + duration
            
            new_progress = list(progress)
            new_progress[i] += 1
            new_progress = tuple(new_progress)
            
            new_job_ready = list(job_ready)
            new_job_ready[i] = finish
            new_job_ready = tuple(new_job_ready)
            
            new_machine_free = list(machine_free)
            new_machine_free[machine] = finish
            new_machine_free = tuple(new_machine_free)
            
            new_max = max(max_time, finish)
            
            new_key = (new_progress, new_job_ready, new_machine_free)
            if new_key not in visited or visited.get(new_key, INF) > new_max:
                heappush(heap, (new_max, new_progress, new_job_ready, new_machine_free))
    
    print(0)

solve()