from collections import deque
import sys

def solve():
    j, m = map(int, input().split())
    
    jobs = []
    for _ in range(j):
        line = list(map(int, input().split()))
        o = line[0]
        ops = []
        for i in range(o):
            machine = line[1 + 2*i]
            duration = line[1 + 2*i + 1]
            ops.append((machine, duration))
        jobs.append(ops)
    
    # Calculate a good upper bound using a greedy approach
    def greedy_bound():
        # For each machine, keep track of when it becomes free
        machine_end_time = [0] * (m + 1)
        job_end_times = [0] * j
        
        for job_idx in range(j):
            job = jobs[job_idx]
            current_time = job_end_times[job_idx]
            
            for machine, duration in job:
                # The operation can start at the max of:
                # 1. When the previous operation of this job finished
                # 2. When this machine becomes free
                start_time = max(current_time, machine_end_time[machine])
                end_time = start_time + duration
                machine_end_time[machine] = end_time
                current_time = end_time
            
            job_end_times[job_idx] = current_time
            
        return max(job_end_times)
    
    upper_bound = greedy_bound()
    
    # Branch and bound with backtracking
    # State: for each job, we know how many operations have been scheduled
    # For each machine, we know the scheduled operations (start, end times)
    
    def backtrack(job_ops_done, machine_schedules, current_max_end_time):
        # job_ops_done: list for each job, how many ops scheduled
        # machine_schedules: list for each machine, list of (start, end) times
        # current_max_end_time: current makespan
        
        if current_max_end_time >= upper_bound:
            return float('inf')
        
        # Check if all jobs are done
        all_done = True
        for i in range(j):
            if job_ops_done[i] < len(jobs[i]):
                all_done = False
                break
        
        if all_done:
            return current_max_end_time
        
        # Find the next operation to schedule
        result = float('inf')
        
        for job_idx in range(j):
            if job_ops_done[job_idx] < len(jobs[job_idx]):
                op_idx = job_ops_done[job_idx]
                machine, duration = jobs[job_idx][op_idx]
                
                # Determine earliest start time for this operation
                # It must be after:
                # 1. The previous operation of the same job
                # 2. All existing operations on the same machine
                
                earliest_start = 0
                if op_idx > 0:
                    # Previous operation of same job must finish first
                    earliest_start = current_max_end_time  # This is a simplification
                
                # Actually, let's think more carefully:
                # The start time must be after the end of previous operation of same job
                prev_job_end = 0
                if op_idx > 0:
                    # We need to find when the previous operation of this job ends
                    # This requires tracking more state - let's use a different approach
                
                # Let's track end time of each job's previous operation
                job_last_end = [0] * j  # This should be part of our state
                # Since it's complex, let's restructure...
        
        return result
    
    # Let's try a different approach: Branch and bound with proper state tracking
    def get_makespan(schedule):
        # schedule[i] is a list of (machine, start, duration) for job i
        machine_timelines = [[] for _ in range(m + 1)]
        
        for job_ops in schedule:
            for machine, start, duration in job_ops:
                machine_timelines[machine].append((start, start + duration))
        
        max_end = 0
        for timeline in machine_timelines:
            for _, end in timeline:
                max_end = max(max_end, end)
        
        return max_end
    
    # Use branch and bound
    best_makespan = upper_bound
    
    def dfs(job_idx, op_idx, job_end_times, machine_next_free):
        nonlocal best_makespan
        
        if job_idx == j:
            # All jobs scheduled
            makespan = max(job_end_times)
            best_makespan = min(best_makespan, makespan)
            return
        
        if op_idx == len(jobs[job_idx]):
            # Move to next job
            dfs(job_idx + 1, 0, job_end_times, machine_next_free)
            return
            
        if max(job_end_times) >= best_makespan:
            return  # Pruning
            
        machine, duration = jobs[job_idx][op_idx]
        
        # Earliest this operation can start:
        # max(previous operation of same job end time, machine availability)
        start_time = max(job_end_times[job_idx], machine_next_free[machine])
        end_time = start_time + duration
        
        # Update state
        old_job_end = job_end_times[job_idx]
        old_machine_free = machine_next_free[machine]
        
        job_end_times[job_idx] = end_time
        machine_next_free[machine] = end_time
        
        # Recurse
        dfs(job_idx, op_idx + 1, job_end_times, machine_next_free)
        
        # Backtrack
        job_end_times[job_idx] = old_job_end
        machine_next_free[machine] = old_machine_free
    
    # Initialize
    job_end_times = [0] * j
    machine_next_free = [0] * (m + 1)
    
    dfs(0, 0, job_end_times, machine_next_free)
    
    print(best_makespan)

solve()