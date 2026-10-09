import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    idx = 0
    j = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    T = int(input_data[idx]); idx += 1

    jobs = []
    for _ in range(j):
        o = int(input_data[idx]); idx += 1
        ops = []
        for _ in range(o):
            machine = int(input_data[idx]); idx += 1
            duration = int(input_data[idx]); idx += 1
            ops.append((machine - 1, duration))
        jobs.append(ops)

    # machine availability times
    machine_available = [0] * m
    # job next start times
    job_next_start = [0] * j
    # schedule storage
    schedule = [[None] * len(jobs[i]) for i in range(j)]

    # backtracking
    def backtrack(job_idx, op_idx):
        if job_idx == j:
            return True
        if op_idx == len(jobs[job_idx]):
            return backtrack(job_idx + 1, 0)
        
        machine, duration = jobs[job_idx][op_idx]
        start_time = max(job_next_start[job_idx], machine_available[machine])
        if start_time + duration > T:
            return False
        
        # try to place
        original_machine_avail = machine_available[machine]
        original_job_next = job_next_start[job_idx]
        
        schedule[job_idx][op_idx] = start_time
        machine_available[machine] = start_time + duration
        job_next_start[job_idx] = start_time + duration
        
        if backtrack(job_idx, op_idx + 1):
            return True
        
        # backtrack
        machine_available[machine] = original_machine_avail
        job_next_start[job_idx] = original_job_next
        schedule[job_idx][op_idx] = None
        return False

    if backtrack(0, 0):
        print("YES")
        for job in schedule:
            print(" ".join(str(t) for t in job))
    else:
        print("NO")

if __name__ == "__main__":
    solve()