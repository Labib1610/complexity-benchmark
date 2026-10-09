import sys
import heapq

def solve():
    input_data = sys.stdin.read().strip().split()
    it = iter(input_data)
    j = int(next(it))
    m = int(next(it))
    
    jobs = []
    for _ in range(j):
        o = int(next(it))
        gates = []
        for _ in range(o):
            core = int(next(it)) - 1
            dur = int(next(it))
            gates.append((core, dur))
        jobs.append(gates)
    
    # DP: state = tuple of completed gates per job
    # We'll store (time, state, core_free_times)
    # But core_free_times can be derived from state? Not directly.
    # So we store (time, state, core_free_times_tuple)
    
    start_state = tuple([0]*j)
    core_free = tuple([0]*m)
    
    # Priority queue: (time, state, core_free_times)
    pq = [(0, start_state, core_free)]
    visited = {}
    visited[(start_state, core_free)] = 0
    
    total_gates = sum(len(g) for g in jobs)
    
    while pq:
        time, state, core_free = heapq.heappop(pq)
        if visited.get((state, core_free), float('inf')) < time:
            continue
        
        # Check if all done
        if sum(state) == total_gates:
            print(time)
            return
        
        # Try to start next gate of each job
        for job_idx in range(j):
            if state[job_idx] < len(jobs[job_idx]):
                core, dur = jobs[job_idx][state[job_idx]]
                # Check if previous gate in this job is done (it is, by state)
                # Check if core is free
                if core_free[core] <= time:
                    # Start this gate
                    new_state = list(state)
                    new_state[job_idx] += 1
                    new_state = tuple(new_state)
                    
                    new_core_free = list(core_free)
                    new_core_free[core] = time + dur
                    new_core_free = tuple(new_core_free)
                    
                    new_time = time + dur
                    
                    if new_time < visited.get((new_state, new_core_free), float('inf')):
                        visited[(new_state, new_core_free)] = new_time
                        heapq.heappush(pq, (new_time, new_state, new_core_free))
    
    # Should not reach here
    print(-1)

if __name__ == "__main__":
    solve()