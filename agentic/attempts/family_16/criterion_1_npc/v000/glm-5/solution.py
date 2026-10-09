import sys
import heapq

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
    
    # State: (time, job_completion_state, machine_availability_state)
    # job_completion_state: tuple of (operation_index) for each job
    # machine_availability_state: tuple of (available_time) for each machine
    
    init_job_state = tuple(0 for _ in range(j))
    init_machine_state = tuple(0 for _ in range(m))
    
    # Priority queue: (current_time, job_state, machine_state)
    pq = [(0, init_job_state, init_machine_state)]
    visited = set()
    visited.add((init_job_state, init_machine_state))
    
    while pq:
        time, job_state, machine_state = heapq.heappop(pq)
        
        # Check if all jobs are complete
        all_done = True
        for i in range(j):
            if job_state[i] < len(jobs[i]):
                all_done = False
                break
        if all_done:
            print(time)
            return
        
        # Try to schedule the next operation for each job
        for i in range(j):
            op_idx = job_state[i]
            if op_idx < len(jobs[i]):
                machine, duration = jobs[i][op_idx]
                
                # Earliest start time for this operation
                # Must wait for previous operation of same job to finish
                # (which is captured by 'time' in the current state)
                # and for the machine to be available
                start_time = max(time, machine_state[machine])
                end_time = start_time + duration
                
                # Create new states
                new_job_state = list(job_state)
                new_job_state[i] = op_idx + 1
                new_job_state = tuple(new_job_state)
                
                new_machine_state = list(machine_state)
                new_machine_state[machine] = end_time
                new_machine_state = tuple(new_machine_state)
                
                state_key = (new_job_state, new_machine_state)
                if state_key not in visited:
                    visited.add(state_key)
                    heapq.heappush(pq, (end_time, new_job_state, new_machine_state))

if __name__ == "__main__":
    solve()