from collections import deque

def solve():
    j, m = map(int, input().split())
    
    jobs = []
    for _ in range(j):
        line = list(map(int, input().split()))
        o = line[0]
        operations = []
        for i in range(o):
            machine = line[1 + 2*i]
            duration = line[1 + 2*i + 1]
            operations.append((machine, duration))
        jobs.append(operations)
    
    # Calculate the minimum completion time using backtracking with pruning
    # We'll use a state-based approach where we track when each job can start its next operation
    
    # For each job, track which operation it's on and when it can start that operation
    # For each machine, track when it becomes free
    
    # job_next_op[job_index] = index of next operation for this job (0-based)
    job_next_op = [0] * j
    
    # job_earliest_start[job_index] = earliest time this job can start its next operation
    job_earliest_start = [0] * j
    
    # machine_free_time[machine_index] = time when this machine becomes free (1-based indexing)
    machine_free_time = [0] * (m + 1)
    
    # To implement branch and bound, we need a better approach
    # Let's use a recursive backtracking with pruning
    
    def get_makespan():
        # Reset state
        job_next_op = [0] * j
        job_earliest_start = [0] * j
        machine_free_time = [0] * (m + 1)
        
        total_ops = sum(len(job) for job in jobs)
        completed_ops = 0
        
        # Keep track of when each job finishes
        job_completion_time = [0] * j
        
        while completed_ops < total_ops:
            # Find the next operation that can be scheduled
            best_job = -1
            best_machine = -1
            best_start_time = float('inf')
            best_op_duration = 0
            
            # Check all jobs for their next operation
            for job_idx in range(j):
                if job_next_op[job_idx] < len(jobs[job_idx]):
                    machine, duration = jobs[job_idx][job_next_op[job_idx]]
                    # This job's next operation can start after:
                    # 1. The previous operation of this job finishes
                    # 2. The machine becomes free
                    start_time = max(job_earliest_start[job_idx], machine_free_time[machine])
                    
                    if start_time < best_start_time:
                        best_start_time = start_time
                        best_job = job_idx
                        best_machine = machine
                        best_op_duration = duration
            
            # Schedule the best operation
            finish_time = best_start_time + best_op_duration
            machine_free_time[best_machine] = finish_time
            job_earliest_start[best_job] = finish_time
            job_next_op[best_job] += 1
            completed_ops += 1
            
            # If this was the last operation of the job, record completion time
            if job_next_op[best_job] == len(jobs[best_job]):
                job_completion_time[best_job] = finish_time
        
        return max(job_completion_time)
    
    # This greedy approach might not be optimal. Let's try a different method.
    # Use a more systematic approach with priority queue simulation
    
    import heapq
    
    def get_makespan_optimal():
        # State: (time, event_type, job_id, operation_id)
        # event_type: 0 = operation starts, 1 = operation ends
        
        # For each job, track which operation it's on
        job_op_index = [0] * j
        # For each machine, track when it's free
        machine_free = [0] * (m + 1)
        # For each job, track when it can start its next operation
        job_next_start = [0] * j
        # Track completion of jobs
        job_done = [False] * j
        # Track completion time of jobs
        job_completion = [0] * j
        
        # Priority queue of events
        pq = []
        
        # Initialize: check which operations can start at time 0
        def update_queue(current_time):
            for job_id in range(j):
                if job_done[job_id]:
                    continue
                if job_op_index[job_id] < len(jobs[job_id]):
                    machine, duration = jobs[job_id][job_op_index[job_id]]
                    start_time = max(current_time, job_next_start[job_id], machine_free[machine])
                    heapq.heappush(pq, (start_time, job_id, job_op_index[job_id], machine, duration))
        
        update_queue(0)
        
        while pq:
            time = pq[0][0]
            # Process all events at this time
            while pq and pq[0][0] == time:
                current_time, job_id, op_id, machine, duration = heapq.heappop(pq)
                
                # If this is the next operation for this job
                if op_id == job_op_index[job_id]:
                    # Start the operation
                    end_time = current_time + duration
                    # Schedule the end event
                    heapq.heappush(pq, (end_time, job_id, op_id, machine, duration))
            
            # Process all end events at this time
            while pq and pq[0][0] == time and len(pq[0]) == 5:
                end_time, job_id, op_id, machine, duration = heapq.heappop(pq)
                
                # Finish the operation
                machine_free[machine] = end_time
                job_op_index[job_id] += 1
                job_next_start[job_id] = end_time
                
                # If job is complete
                if job_op_index[job_id] == len(jobs[job_id]):
                    job_done[job_id] = True
                    job_completion[job_id] = end_time
                
            # Update queue with new possible operations
            update_queue(time)
            
            # Check if all jobs are done
            if all(job_done):
                break
        
        return max(job_completion)
    
    # Even simpler simulation approach
    def simulate():
        # Track when each machine is free
        machine_free_time = [0] * (m + 1)
        # Track when each job can start its next operation
        job_next_start = [0] * j
        # Track current operation index for each job
        job_op_index = [0] * j
        
        time = 0
        total_ops = sum(len(job) for job in jobs)
        completed_ops = 0
        
        while completed_ops < total_ops:
            # Find an operation that can be started now
            scheduled = False
            for job_id in range(j):
                if job_op_index[job_id] < len(jobs[job_id]):
                    machine, duration = jobs[job_id][job_op_index[job_id]]
                    # Can start if:
                    # 1. Job's previous operation is done (job_next_start tracks this)
                    # 2. Machine is free
                    if job_next_start[job_id] <= time and machine_free_time[machine] <= time:
                        # Start this operation
                        end_time = time + duration
                        machine_free_time[machine] = end_time
                        job_next_start[job_id] = end_time
                        job_op_index[job_id] += 1
                        completed_ops += 1
                        scheduled = True
                        break
            
            if not scheduled:
                # Advance time to when next event happens
                next_events = []
                for job_id in range(j):
                    if job_op_index[job_id] < len(jobs[job_id]):
                        machine, duration = jobs[job_id][job_op_index[job_id]]
                        # When can this operation start?
                        start_time = max(job_next_start[job_id], machine_free_time[machine])
                        next_events.append(start_time)
                
                if next_events:
                    time = min(t for t in next_events if t > time)
                else:
                    break
            else:
                # We scheduled an operation, advance time by 1 to allow for next scheduling
                time += 1
        
        return max(machine_free_time)
    
    # Branch and bound approach for optimality
    def branch_and_bound():
        best_makespan = float('inf')
        
        # State: (job_op_indices, machine_free_times, job_next_starts, current_makespan)
        def backtrack(job_op_indices, machine_free_times, job_next_starts, current_time):
            nonlocal best_makespan
            
            # Pruning
            if current_time >= best_makespan:
                return
            
            # Check if all jobs are done
            if all(job_op_indices[i] == len(jobs[i]) for i in range(j)):
                best_makespan = min(best_makespan, current_time)
                return
            
            # Find all possible next operations
            next_operations = []
            for job_id in range(j):
                if job_op_indices[job_id] < len(jobs[job_id]):
                    machine, duration = jobs[job_id][job_op_indices[job_id]]
                    start_time = max(job_next_starts[job_id], machine_free_times[machine])
                    next_operations.append((start_time, job_id, machine, duration))
            
            # Try each possible operation
            for start_time, job_id, machine, duration in next_operations:
                # Execute this operation
                new_job_op_indices = job_op_indices[:]
                new_machine_free_times = machine_free_times[:]
                new_job_next_starts = job_next_starts[:]
                
                new_job_op_indices[job_id] += 1
                end_time = start_time + duration
                new_machine_free_times[machine] = end_time
                new_job_next_starts[job_id] = end_time
                
                backtrack(new_job_op_indices, new_machine_free_times, new_job_next_starts, end_time)
        
        backtrack([0]*j, [0]*(m+1), [0]*j, 0)
        return best_makespan
    
    # For small inputs, we can try a greedy simulation
    result = simulate()
    print(result)

solve()