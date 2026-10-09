from collections import deque
import heapq

def solve():
    j, m = map(int, input().split())
    
    # Read subroutines
    subroutines = []
    for _ in range(j):
        line = list(map(int, input().split()))
        o = line[0]
        gates = []
        for i in range(o):
            core = line[1 + 2*i]
            duration = line[1 + 2*i + 1]
            gates.append((core, duration))
        subroutines.append(gates)
    
    # BFS with priority queue (Dijkstra-like) to find minimum time
    # State: (time, positions, core_end_times)
    # positions[i] = index of next gate to execute in subroutine i
    # core_end_times[c] = time when core c becomes free
    
    # Initial state
    initial_positions = tuple(0 for _ in range(j))
    initial_core_times = tuple(0 for _ in range(m + 1))  # 1-indexed cores
    
    # Priority queue: (time, positions, core_end_times)
    pq = [(0, initial_positions, initial_core_times)]
    visited = set()
    
    while pq:
        time, positions, core_times = heapq.heappop(pq)
        
        # Check if all subroutines are done
        if all(positions[i] == len(subroutines[i]) for i in range(j)):
            print(time)
            return
        
        state = (positions, core_times)
        if state in visited:
            continue
        visited.add(state)
        
        # Try to schedule next gate from each subroutine
        for i in range(j):
            if positions[i] < len(subroutines[i]):
                core, duration = subroutines[i][positions[i]]
                
                # Earliest time this gate can start is max(current_time, core_free_time)
                start_time = max(time, core_times[core])
                end_time = start_time + duration
                
                # Create new state
                new_positions = list(positions)
                new_positions[i] += 1
                new_positions_tuple = tuple(new_positions)
                
                new_core_times = list(core_times)
                new_core_times[core] = end_time
                new_core_times_tuple = tuple(new_core_times)
                
                heapq.heappush(pq, (end_time, new_positions_tuple, new_core_times_tuple))

solve()