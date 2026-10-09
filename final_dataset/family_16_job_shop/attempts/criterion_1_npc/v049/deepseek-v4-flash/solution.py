import sys
from collections import deque

def solve():
    data = sys.stdin.read().strip().split()
    idx = 0
    j = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    
    jobs = []
    for _ in range(j):
        o = int(data[idx]); idx += 1
        steps = []
        for _ in range(o):
            station = int(data[idx]); idx += 1
            duration = int(data[idx]); idx += 1
            steps.append((station, duration))
        jobs.append(steps)
    
    # For each job, track current step index
    job_step = [0] * j
    # For each job, track when it becomes available (after previous step finishes)
    job_available = [0] * j
    # For each station, track when it becomes free
    station_free = [0] * (m + 1)  # 1-indexed
    
    time = 0
    completed = 0
    total_steps = sum(len(job) for job in jobs)
    
    while completed < total_steps:
        # Try to start any available step
        started = False
        for job_id in range(j):
            if job_step[job_id] < len(jobs[job_id]):
                station, dur = jobs[job_id][job_step[job_id]]
                if job_available[job_id] <= time and station_free[station] <= time:
                    # Start this step
                    finish_time = time + dur
                    station_free[station] = finish_time
                    job_available[job_id] = finish_time
                    job_step[job_id] += 1
                    completed += 1
                    started = True
        if not started:
            # Advance time to next event
            next_time = min(
                [station_free[s] for s in range(1, m+1) if station_free[s] > time] +
                [job_available[job] for job in range(j) if job_available[job] > time]
            )
            time = next_time
        else:
            # If we started something, keep time same to try more in same time slot
            pass
    
    # The final time is when all jobs are done
    print(max(job_available))

if __name__ == "__main__":
    solve()