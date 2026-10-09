import sys

def solve():
    data = sys.stdin.read().strip().split()
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
            machine = int(data[idx]); idx += 1
            duration = int(data[idx]); idx += 1
            ops.append((machine - 1, duration))
        jobs.append(ops)
    
    # Total operations
    total_ops = sum(len(job) for job in jobs)
    
    # For each job, track next operation index
    job_ptr = [0] * j
    # Machine available time
    machine_free = [0] * m
    # Job completion time
    job_done = [0] * j
    
    best = [float('inf')]
    
    # Precompute operation list with job id and op index
    op_list = []
    for job_id, ops in enumerate(jobs):
        for op_idx, (mac, dur) in enumerate(ops):
            op_list.append((job_id, op_idx, mac, dur))
    
    # Sort operations by some heuristic? We'll just DFS in order of job/op.
    # But we can also try to schedule in order of job index.
    
    # We'll do DFS over operations in a fixed order (job by job, op by op)
    # But to find min makespan, we can try all possible orders? Too many.
    # Instead, we can use a priority queue simulation with backtracking.
    
    # Simpler: Use a recursive search that at each step picks the next operation
    # of some job that hasn't finished, and tries to start it as early as possible.
    
    # We'll use a recursive function that schedules operations one by one.
    # At each step, we choose a job whose next operation can start earliest.
    
    # To find minimum makespan, we can use branch and bound.
    
    # Let's implement a DFS that schedules operations in order of job index,
    # but with pruning: if current max completion >= best, prune.
    
    # We'll track:
    # job_next_op[j] = index of next operation for job j
    # machine_avail[m] = time when machine m is free
    # job_avail[j] = time when job j is free for next op
    
    job_next_op = [0] * j
    machine_avail = [0] * m
    job_avail = [0] * j
    
    def dfs(scheduled_count, current_makespan):
        if scheduled_count == total_ops:
            best[0] = min(best[0], current_makespan)
            return
        if current_makespan >= best[0]:
            return
        
        # Find the job with the earliest available next operation start time
        # among jobs that still have operations left.
        min_start = float('inf')
        chosen_job = -1
        for job_id in range(j):
            if job_next_op[job_id] < len(jobs[job_id]):
                mac, dur = jobs[job_id][job_next_op[job_id]]
                start_time = max(job_avail[job_id], machine_avail[mac])
                if start_time < min_start:
                    min_start = start_time
                    chosen_job = job_id
        
        if chosen_job == -1:
            return
        
        mac, dur = jobs[chosen_job][job_next_op[chosen_job]]
        start_time = max(job_avail[chosen_job], machine_avail[mac])
        finish_time = start_time + dur
        
        # Save state
        old_job_avail = job_avail[chosen_job]
        old_machine_avail = machine_avail[mac]
        old_next_op = job_next_op[chosen_job]
        
        # Update
        job_avail[chosen_job] = finish_time
        machine_avail[mac] = finish_time
        job_next_op[chosen_job] += 1
        
        dfs(scheduled_count + 1, max(current_makespan, finish_time))
        
        # Restore
        job_avail[chosen_job] = old_job_avail
        machine_avail[mac] = old_machine_avail
        job_next_op[chosen_job] = old_next_op
    
    dfs(0, 0)
    print(best[0])

if __name__ == "__main__":
    solve()