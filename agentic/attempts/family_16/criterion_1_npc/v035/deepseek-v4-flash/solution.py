import sys

def main():
    data = sys.stdin.read().strip().split()
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
            ops.append((machine, duration))
        jobs.append(ops)
    
    # For each job, track next operation index
    job_step = [0] * j
    # For each machine, track when it becomes free
    machine_free = [0] * (m + 1)  # 1-indexed machines
    # For each job, track when it can start its next op
    job_ready = [0] * j
    
    completed = 0
    time = 0
    
    while completed < j:
        # Find the earliest time when some job can proceed
        next_time = float('inf')
        for i in range(j):
            if job_step[i] < len(jobs[i]):
                machine, dur = jobs[i][job_step[i]]
                start_time = max(job_ready[i], machine_free[machine])
                next_time = min(next_time, start_time)
        
        time = next_time
        
        # Process all jobs that can start at this time
        for i in range(j):
            if job_step[i] < len(jobs[i]):
                machine, dur = jobs[i][job_step[i]]
                start_time = max(job_ready[i], machine_free[machine])
                if start_time == time:
                    # Schedule this operation
                    finish_time = time + dur
                    machine_free[machine] = finish_time
                    job_ready[i] = finish_time
                    job_step[i] += 1
                    if job_step[i] == len(jobs[i]):
                        completed += 1
    
    # The answer is the maximum finish time among all jobs
    print(max(job_ready))

if __name__ == "__main__":
    main()