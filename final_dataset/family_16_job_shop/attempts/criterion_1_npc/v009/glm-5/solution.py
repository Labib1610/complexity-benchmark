import sys
from collections import deque

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
    
    # State: (job_idx, op_idx for each job)
    # Represented as tuple of op indices
    start_state = tuple(0 for _ in range(j))
    
    # Priority queue: (time, state)
    import heapq
    pq = []
    heapq.heappush(pq, (0, start_state))
    
    # Visited states with minimum time to reach
    dist = {start_state: 0}
    
    while pq:
        time, state = heapq.heappop(pq)
        if dist.get(state, float('inf')) < time:
            continue
        
        # Check if all jobs completed
        all_done = True
        for i in range(j):
            if state[i] < len(jobs[i]):
                all_done = False
                break
        if all_done:
            print(time)
            return
        
        # Find operations that can start now
        # An operation can start if it's the next operation for its job
        # and the machine is free at 'time'
        
        # First, identify all available operations
        available = []
        for i in range(j):
            op_idx = state[i]
            if op_idx < len(jobs[i]):
                machine, duration = jobs[i][op_idx]
                available.append((i, op_idx, machine, duration))
        
        # Try all subsets of non-conflicting operations
        n = len(available)
        # Generate all valid subsets (no two operations use the same machine)
        # Using bitmask enumeration
        for mask in range(1, 1 << n):
            machines_used = set()
            valid = True
            for i in range(n):
                if mask & (1 << i):
                    machine = available[i][2]
                    if machine in machines_used:
                        valid = False
                        break
                    machines_used.add(machine)
            if not valid:
                continue
            
            # This subset is valid, execute all operations in parallel
            new_state = list(state)
            max_duration = 0
            for i in range(n):
                if mask & (1 << i):
                    job_idx, op_idx, machine, duration = available[i]
                    new_state[job_idx] = op_idx + 1
                    max_duration = max(max_duration, duration)
            
            new_state = tuple(new_state)
            new_time = time + max_duration
            
            if new_time < dist.get(new_state, float('inf')):
                dist[new_state] = new_time
                heapq.heappush(pq, (new_time, new_state))
    
    # Should not reach here if input is valid
    print(-1)

solve()