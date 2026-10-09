import sys
from itertools import permutations

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
            machine = int(data[idx]) - 1  # 0-based
            duration = int(data[idx+1])
            idx += 2
            ops.append((machine, duration))
        jobs.append(ops)
    
    # Flatten operations with job and op index
    operations = []  # (job_id, op_index, machine, duration)
    for job_id, ops in enumerate(jobs):
        for op_idx, (machine, dur) in enumerate(ops):
            operations.append((job_id, op_idx, machine, dur))
    
    n_ops = len(operations)
    
    # Precompute for each job: number of ops
    job_op_count = [len(ops) for ops in jobs]
    
    best = float('inf')
    
    # State: for each job, next op index to schedule; for each machine, next free time
    # We'll do DFS over operations order.
    
    # We'll use a list of remaining operations, and try all possible next operations
    # that are ready.
    
    # To speed up, we can use a priority queue approach, but for exact optimal we do DFS.
    
    # We'll store for each job the next op index, and for each machine the next free time.
    # We'll also store current time (max of machine free times and job ready times).
    
    # We'll do recursive search with memoization? Not needed for small size.
    
    # Let's implement DFS:
    
    job_next = [0] * j
    machine_free = [0] * m
    # We'll track current makespan as max(machine_free)
    
    def dfs(job_next, machine_free, current_max):
        nonlocal best
        # If all jobs done
        if all(job_next[i] == job_op_count[i] for i in range(j)):
            best = min(best, current_max)
            return
        # Prune
        if current_max >= best:
            return
        
        # Find all ready operations
        ready = []
        for job_id in range(j):
            if job_next[job_id] < job_op_count[job_id]:
                machine, dur = jobs[job_id][job_next[job_id]]
                # Earliest start = max(machine_free[machine], current_max? Actually job ready time is when previous op finished.
                # We need job ready time: that's when previous op finished. We can compute from machine_free? Not directly.
                # We'll track job_ready_time separately.
                # Let's add job_ready array.
                pass
        
        # Better: track job_ready_time
        # We'll modify DFS to include job_ready
    
    # Let's redo with job_ready array
    
    job_ready = [0] * j  # time when next op of job can start
    machine_free = [0] * m
    
    def dfs(job_ready, machine_free, current_max):
        nonlocal best
        if all(job_next[i] == job_op_count[i] for i in range(j)):
            best = min(best, current_max)
            return
        if current_max >= best:
            return
        
        # Try each job that has remaining ops and is ready
        for job_id in range(j):
            if job_next[job_id] < job_op_count[job_id]:
                machine, dur = jobs[job_id][job_next[job_id]]
                start_time = max(job_ready[job_id], machine_free[machine])
                # If we start now, new job_ready for this job = start_time + dur
                # new machine_free for this machine = start_time + dur
                # new current_max = max(current_max, start_time + dur)
                new_job_ready = job_ready[:]
                new_machine_free = machine_free[:]
                new_job_next = job_next[:]
                new_job_ready[job_id] = start_time + dur
                new_machine_free[machine] = start_time + dur
                new_job_next[job_id] += 1
                new_max = max(current_max, start_time + dur)
                dfs(new_job_ready, new_machine_free, new_max)
    
    dfs(job_ready, machine_free, 0)
    print(best)

if __name__ == "__main__":
    solve()