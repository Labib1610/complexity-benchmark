import sys
from collections import deque

def solve():
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
        for _ in range(o):
            machine = int(next(it)) - 1
            duration = int(next(it))
            ops.append((machine, duration))
        jobs.append(ops)
    
    # State: (job_op_index for each job)
    # job_op_index[i] = k means job i is waiting to start operation k (0-indexed)
    # If job i is finished, job_op_index[i] = len(jobs[i])
    
    # For each machine, track when it becomes free
    # For each job, track when its previous operation finished
    
    # BFS/DP approach
    # State: tuple of (op_idx for each job)
    # For each state, track: machine_free_time[m], job_finish_time[j]
    
    # Initial state
    init_state = tuple(0 for _ in range(j))
    
    # BFS queue: (state, machine_free_times, job_prev_finish_times)
    # Use dict to track best makespan for each state
    # But machine_free_times and job_finish_times matter for transitions
    
    # Actually, for each state, we need to track the minimum time to reach it
    # But the "time" depends on which operations we choose to schedule
    
    # Let's use a priority queue (Dijkstra-like) or BFS with proper state tracking
    
    # State representation:
    # (op_indices, machine_free_times, job_finish_times)
    # But this is too large
    
    # Better: For each state (op_indices), we track the earliest time each machine is free
    # and when each job finished its last operation
    
    # Actually, let's think differently:
    # At any state, we can choose to schedule any operation that is "ready"
    # An operation is ready if it's the next operation for its job
    
    # We need to find the minimum makespan
    
    # Let's use BFS with states and track minimum time to reach each state
    # State: (op_indices_tuple)
    # For each state, we need to know: for each machine, when is it free?
    # And for each job, when did its last op finish?
    
    # These values are determined by the path taken, not just the state
    # So we need to track them as part of the state or use a different approach
    
    # Alternative: Use a priority queue where we track:
    # (current_time, state, machine_free_times, job_finish_times)
    # And expand by scheduling one operation at a time
    
    # But we need to be careful about when to schedule operations
    # We can schedule an operation as soon as:
    # 1. The job's previous operation is done
    # 2. The machine is free
    
    # The start time of an operation = max(job_finish_time[job], machine_free_time[machine])
    
    # Let's use a priority queue approach
    # State: (op_indices, machine_free_times_tuple, job_finish_times_tuple)
    # We use a set to track visited states to avoid revisiting
    
    from heapq import heappush, heappop
    
    # Initial state
    init_machine_free = tuple(0 for _ in range(m))
    init_job_finish = tuple(0 for _ in range(j))
    
    # Priority queue: (current_time, op_indices, machine_free, job_finish)
    # We process states in order of current_time
    # current_time is the time when the last scheduled operation finished
    
    # Actually, we should track the makespan (max of all finish times)
    # and try to minimize it
    
    # Let's use a different approach:
    # State: (op_indices, machine_free_times, job_finish_times)
    # We use BFS/priority queue to explore all possible schedules
    # and track the minimum makespan when all jobs are finished
    
    # To reduce state space, we can note that:
    # - machine_free_times and job_finish_times are monotonic
    # - For a given op_indices state, we want to minimize these times
    
    # Let's use a dict to track, for each op_indices state, the best (machine_free, job_finish) seen
    # "Best" means component-wise <= (since smaller is better)
    
    # Actually, let's just do a straightforward BFS/priority queue
    # with proper deduplication
    
    # visited: dict from op_indices to list of (machine_free, job_finish) pairs
    # where we've seen this state with these times
    
    # But checking dominance is complex. Let's try a simpler approach first.
    
    # Since total operations <= 50 and j, m <= 10, the state space is manageable
    
    # Let's use a priority queue where we track:
    # (makespan_so_far, op_indices, machine_free, job_finish)
    # makespan_so_far = max of all operation finish times seen so far
    # We want to minimize the final makespan
    
    # Actually, let's track current_time as the time when we're making decisions
    # But operations can start at different times...
    
    # Let me reconsider. The key insight is:
    # At any point, we have a set of "ready" operations (next operation for each unfinished job)
    # We can choose to schedule any subset of them (respecting machine constraints)
    # But since each machine can only run one operation at a time, we schedule one at a time
    
    # So the algorithm is:
    # 1. Start with all jobs at operation 0, all machines free at time 0
    # 2. At each step, pick a ready operation and schedule it
    # 3. Update state and repeat
    # 4. Track minimum makespan when all jobs are finished
    
    # Use priority queue with (current_time, state, machine_free, job_finish)
    # But current_time is tricky because we might have multiple operations ready at different times
    
    # Better: Use a priority queue where we always process the next "event"
    # An event is when a machine becomes free or a job's previous operation finishes
    
    # Actually, let's use a simpler BFS approach:
    # State: (op_indices, machine_free_times, job_finish_times)
    # For each state, generate all possible next states by scheduling one ready operation
    # Use a priority queue ordered by the maximum finish time so far
    
    # To avoid revisiting states, we can use a set of (op_indices, machine_free, job_finish)
    # But this might be too large
    
    # Let's try without deduplication first and see if it's fast enough
    # Given the constraints (j <= 10, m <= 10, total ops <= 50), it should be manageable
    
    # Actually, let's use a smarter state representation
    # We can use a priority queue where:
    # - Priority is the makespan (max finish time)
    # - State includes op_indices, machine_free, job_finish
    
    # And we use a visited set to avoid revisiting the same (op_indices, machine_free, job_finish)
    
    # Let's implement this
    
    pq = []
    # (priority, op_indices, machine_free, job_finish)
    # priority = max(machine_free + any ongoing ops, job_finish)
    # Actually, priority should be the current makespan estimate
    
    # For initial state, all machines are free at time 0, all jobs are ready
    # makespan = 0 (no operations scheduled yet)
    
    heappush(pq, (0, init_state, init_machine_free, init_job_finish))
    
    visited = set()
    visited.add((init_state, init_machine_free, init_job_finish))
    
    best_makespan = float('inf')
    
    while pq:
        makespan, op_indices, machine_free, job_finish = heappop(pq)
        
        # Check if all jobs are finished
        all_done = all(op_indices[i] == len(jobs[i]) for i in range(j))
        if all_done:
            best_makespan = min(best_makespan, makespan)
            continue
        
        # If current makespan is already >= best found, skip
        if makespan >= best_makespan:
            continue
        
        # Find all ready operations
        ready_ops = []
        for i in range(j):
            if op_indices[i] < len(jobs[i]):
                op_idx = op_indices[i]
                machine, duration = jobs[i][op_idx]
                ready_ops.append((i, op_idx, machine, duration))
        
        # Try scheduling each ready operation
        for job_id, op_idx, machine, duration in ready_ops:
            # Calculate start time
            start_time = max(job_finish[job_id], machine_free[machine])
            end_time = start_time + duration
            
            # New state
            new_op_indices = list(op_indices)
            new_op_indices[job_id] += 1
            new_op_indices = tuple(new_op_indices)
            
            new_machine_free = list(machine_free)
            new_machine_free[machine] = end_time
            new_machine_free = tuple(new_machine_free)
            
            new_job_finish = list(job_finish)
            new_job_finish[job_id] = end_time
            new_job_finish = tuple(new_job_finish)
            
            new_makespan = max(makespan, end_time)
            
            new_state = (new_op_indices, new_machine_free, new_job_finish)
            if new_state not in visited:
                visited.add(new_state)
                heappush(pq, (new_makespan, new_op_indices, new_machine_free, new_job_finish))
    
    print(best_makespan)

solve()