import sys
from collections import deque

def solve():
    j, m, T = map(int, input().split())
    
    jobs = []
    for _ in range(j):
        line = list(map(int, input().split()))
        o = line[0]
        operations = []
        for i in range(o):
            machine = line[1 + 2*i] - 1  # Convert to 0-indexed
            duration = line[1 + 2*i + 1]
            operations.append((machine, duration))
        jobs.append(operations)
    
    # Binary search on the makespan
    # But since we need to check if makespan <= T, we can use a decision procedure
    
    # We'll use a greedy approach with priority queues to try to fit within T
    # This is actually a scheduling problem that can be solved with a greedy algorithm
    # or we can model it as a constraint satisfaction problem
    
    # Let's try a greedy approach: for each job, we try to schedule its operations
    # as early as possible, respecting precedence and machine constraints
    
    # We'll use a simulation approach
    
    # For each machine, we keep track of when it becomes free
    machine_free_time = [0] * m
    
    # For each job, we keep track of when its previous operation finishes
    job_prev_finish = [0] * j
    
    # Store the start times
    start_times = [[] for _ in range(j)]
    
    # Event queue: (time, event_type, job_id, op_id)
    # event_type: 0 = operation starts, 1 = operation finishes
    events = []
    
    # We need to determine the order in which to schedule operations
    # A simple heuristic is to process jobs in some order and schedule each operation
    # as early as possible
    
    # Let's try a greedy approach where we process jobs in order and schedule each operation
    # at the earliest time it can start
    
    current_time = 0
    
    # For each job, keep track of which operation we're on
    job_op_index = [0] * j
    
    # Keep track of which operations are waiting to be scheduled
    # An operation can be scheduled if its machine is free and its job's previous operation is done
    waiting_ops = []  # (job_id, op_id, machine, duration)
    
    # Initialize: all first operations are waiting
    for job_id in range(j):
        if jobs[job_id]:  # If job has operations
            machine, duration = jobs[job_id][0]
            waiting_ops.append((job_id, 0, machine, duration))
    
    # Function to find the next operation that can be scheduled
    def find_next_schedulable():
        best_time = float('inf')
        best_op = None
        for i, (job_id, op_id, machine, duration) in enumerate(waiting_ops):
            # Earliest time this operation can start:
            # max(machine free time, previous operation finish time for this job)
            start_time = max(machine_free_time[machine], job_prev_finish[job_id])
            if start_time < best_time:
                best_time = start_time
                best_op = i
        return best_op, best_time
    
    scheduled_count = 0
    total_ops = sum(len(job) for job in jobs)
    
    # Timeline of events
    timeline = []  # (start_time, end_time, job_id, op_id, machine)
    
    while scheduled_count < total_ops:
        # Find the next operation to schedule
        op_idx, start_time = find_next_schedulable()
        
        if op_idx is None or start_time > T:
            print("NO")
            return
            
        job_id, op_id, machine, duration = waiting_ops.pop(op_idx)
        end_time = start_time + duration
        
        if end_time > T:
            print("NO")
            return
            
        # Schedule this operation
        start_times[job_id].append(start_time)
        timeline.append((start_time, end_time, job_id, op_id, machine))
        
        # Update state
        machine_free_time[machine] = end_time
        job_prev_finish[job_id] = end_time
        scheduled_count += 1
        
        # Add next operation of this job to waiting list, if any
        if op_id + 1 < len(jobs[job_id]):
            next_op_id = op_id + 1
            next_machine, next_duration = jobs[job_id][next_op_id]
            waiting_ops.append((job_id, next_op_id, next_machine, next_duration))
    
    # Check if all operations finished within deadline
    max_end_time = max(event[1] for event in timeline) if timeline else 0
    if max_end_time > T:
        print("NO")
        return
        
    print("YES")
    for times in start_times:
        print(' '.join(map(str, times)))

solve()