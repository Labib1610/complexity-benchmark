from itertools import permutations
import sys

def simulate(order, jobs):
    # jobs: list of list of (machine, duration)
    m = max(max(machine for machine, _ in job) for job in jobs) + 1
    machine_free = [0] * m
    job_finish = [0] * len(jobs)
    job_index = [0] * len(jobs)
    
    for job_id in order:
        for machine, dur in jobs[job_id]:
            start = max(machine_free[machine], job_finish[job_id])
            finish = start + dur
            machine_free[machine] = finish
            job_finish[job_id] = finish
    return max(job_finish)

def main():
    data = sys.stdin.read().strip().split()
    idx = 0
    j = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    jobs = []
    for _ in range(j):
        o = int(data[idx]); idx += 1
        job = []
        for _ in range(o):
            machine = int(data[idx]) - 1; idx += 1
            dur = int(data[idx]); idx += 1
            job.append((machine, dur))
        jobs.append(job)
    
    best = float('inf')
    for perm in permutations(range(j)):
        best = min(best, simulate(perm, jobs))
    print(best)

if __name__ == "__main__":
    main()