from collections import defaultdict
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
    
    # Generate all possible schedules by trying all permutations of operations
    # This is infeasible for large inputs, but with j <= 10 and total ops <= 50,
    # we can use a backtracking approach
    
    # We'll use a recursive backtracking with pruning
    
    # For each job, we track which operation index it's currently at
    job_op_index = [0] * j
    
    # For each machine, we track when it becomes free
    machine_end_time = [0] * (m + 1)  # 1-indexed
    
    # For each job, we track when its previous operation finished
    job_end_time = [0] * j
    
    # To track the minimum makespan found so far
    min_makespan = [float('inf')]
    
    def backtrack():
        # Check if all jobs are completed
        if all(job_op_index[i] == len(jobs[i]) for i in range(j)):
            makespan = max(job_end_time)
            min_makespan[0] = min(min_makespan[0], makespan)
            return
        
        # Pruning: if current max end time is already >= best found, no point continuing
        current_max = max(job_end_time + machine_end_time)
        if current_max >= min_makespan[0]:
            return
            
        # Find all possible next operations
        for job_id in range(j):
            if job_op_index[job_id] < len(jobs[job_id]):
                op_idx = job_op_index[job_id]
                machine, duration = jobs[job_id][op_idx]
                
                # The start time of this operation is max of:
                # 1. When the previous operation of this job finished
                # 2. When this machine becomes free
                start_time = max(job_end_time[job_id], machine_end_time[machine])
                end_time = start_time + duration
                
                # Make the move
                job_op_index[job_id] += 1
                old_job_end = job_end_time[job_id]
                old_machine_end = machine_end_time[machine]
                
                job_end_time[job_id] = end_time
                machine_end_time[machine] = end_time
                
                # Recurse
                backtrack()
                
                # Undo the move
                job_op_index[job_id] -= 1
                job_end_time[job_id] = old_job_end
                machine_end_time[machine] = old_machine_end
    
    backtrack()
    print(min_makespan[0])

solve()