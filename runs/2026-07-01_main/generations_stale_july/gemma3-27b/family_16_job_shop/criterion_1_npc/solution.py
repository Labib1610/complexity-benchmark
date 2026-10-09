def solve():
    j, m = map(int, input().split())
    jobs = []
    for _ in range(j):
        o, *ops = map(int, input().split())
        job_ops = []
        for i in range(0, len(ops), 2):
            job_ops.append((ops[i], ops[i+1]))
        jobs.append(job_ops)

    import itertools
    
    best_finish_time = float('inf')
    
    for perm in itertools.permutations(range(j)):
        machine_times = [0] * m
        job_finish_times = [0] * j
        
        for job_index in perm:
            job = jobs[job_index]
            current_time = 0
            for machine, duration in job:
                start_time = max(current_time, machine_times[machine-1])
                current_time = start_time + duration
                machine_times[machine-1] = current_time
            job_finish_times[job_index] = current_time
        
        best_finish_time = min(best_finish_time, max(job_finish_times))
        
    print(best_finish_time)

solve()