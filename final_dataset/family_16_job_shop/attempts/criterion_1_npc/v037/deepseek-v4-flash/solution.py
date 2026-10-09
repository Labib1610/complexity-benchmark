import sys

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
    
    total_ops = sum(len(job) for job in jobs)
    # Precompute for each job: list of (machine, duration, job_id, op_index)
    all_ops = []
    for job_id, ops in enumerate(jobs):
        for op_idx, (machine, duration) in enumerate(ops):
            all_ops.append((machine, duration, job_id, op_idx))
    
    # Upper bound: sum of all durations (worst case sequential)
    upper_bound = sum(d for _, d, _, _ in all_ops)
    
    best = upper_bound
    
    # For pruning: earliest possible start for each operation
    # We'll compute lower bound as max of machine load and job chain length
    machine_load = [0] * m
    job_chain = [0] * j
    for machine, duration, job_id, op_idx in all_ops:
        machine_load[machine] += duration
        job_chain[job_id] += duration
    lower_bound = max(max(machine_load), max(job_chain))
    
    # Backtracking search
    # State: for each job, next operation index to schedule
    # For each machine, next available time
    # For each job, next available time (after previous op)
    
    job_next_op = [0] * j
    machine_free = [0] * m
    job_free = [0] * j
    
    # We'll schedule operations one by one, choosing among available ones
    # Available: job_next_op < len(jobs[job_id]) and job_free[job_id] <= current_time? 
    # Actually we can do DFS over all possible orders.
    
    # To speed up, we can use a priority: schedule the job with earliest possible start
    # But simple DFS with pruning should work for n<=50.
    
    # We'll do DFS: at each step, pick an operation that can start now (job_free <= current_time)
    # But we don't have a global time; we can simulate by choosing next op to schedule.
    
    # Alternative: use recursive search that schedules one operation at a time,
    # maintaining current makespan as max of machine_free and job_free.
    
    # We'll implement a DFS that tries all possible next operations.
    
    # Precompute for each job the list of operations
    # We'll use a recursive function that schedules operations in any order
    # respecting job order.
    
    # To prune: if current makespan >= best, return.
    
    # We'll keep track of scheduled count.
    
    def dfs(scheduled_count, current_makespan):
        nonlocal best
        if current_makespan >= best:
            return
        if scheduled_count == total_ops:
            best = current_makespan
            return
        
        # Try to schedule any job whose next operation is available
        # Available means job_free[job_id] <= current_makespan? Actually we can start
        # an operation at time max(job_free[job_id], machine_free[machine]).
        # We'll just try all jobs that have remaining ops.
        
        # To reduce branching, we can sort by earliest possible start time.
        candidates = []
        for job_id in range(j):
            if job_next_op[job_id] < len(jobs[job_id]):
                machine, duration = jobs[job_id][job_next_op[job_id]]
                start_time = max(job_free[job_id], machine_free[machine])
                candidates.append((start_time, job_id, machine, duration))
        
        # Sort by start time to try earliest first
        candidates.sort()
        
        for start_time, job_id, machine, duration in candidates:
            # Schedule this operation
            old_job_free = job_free[job_id]
            old_machine_free = machine_free[machine]
            old_next_op = job_next_op[job_id]
            
            new_start = max(old_job_free, old_machine_free)
            finish = new_start + duration
            job_free[job_id] = finish
            machine_free[machine] = finish
            job_next_op[job_id] += 1
            
            new_makespan = max(current_makespan, finish)
            
            dfs(scheduled_count + 1, new_makespan)
            
            # Backtrack
            job_free[job_id] = old_job_free
            machine_free[machine] = old_machine_free
            job_next_op[job_id] = old_next_op
    
    dfs(0, 0)
    print(best)

if __name__ == "__main__":
    solve()