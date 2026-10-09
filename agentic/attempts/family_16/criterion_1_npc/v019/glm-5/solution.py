import sys
from heapq import heappush, heappop

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    m = int(next(it))
    elixirs = []
    for _ in range(j):
        o = int(next(it))
        phases = []
        for _ in range(o):
            a = int(next(it))
            d = int(next(it))
            phases.append((a, d))
        elixirs.append(phases)

    # State: (time, elixir_phase_indices, apparatus_free_times)
    # elixir_phase_indices: tuple of next phase index for each elixir
    # apparatus_free_times: tuple of free time for each apparatus (1-indexed -> 0-indexed)
    
    initial_phases = tuple(0 for _ in range(j))
    initial_free = tuple(0 for _ in range(m))
    
    # Priority queue: (time, state)
    # state = (phases_tuple, free_tuple)
    pq = [(0, initial_phases, initial_free)]
    visited = {}
    visited[(initial_phases, initial_free)] = 0
    
    total_phases = [len(e) for e in elixirs]
    
    while pq:
        time, phases, free = heappop(pq)
        
        # Check if all elixirs are done
        if all(phases[i] >= total_phases[i] for i in range(j)):
            print(time)
            return
        
        # Skip if we've found a better time for this state
        if visited.get((phases, free), float('inf')) < time:
            continue
        
        # Try to schedule the next phase for each elixir that has remaining phases
        for i in range(j):
            if phases[i] < total_phases[i]:
                app, dur = elixirs[i][phases[i]]
                app_idx = app - 1  # 0-indexed
                
                # The phase can start at max(time, free[app_idx])
                start = max(time, free[app_idx])
                end = start + dur
                
                # Create new state
                new_phases = list(phases)
                new_phases[i] += 1
                new_phases = tuple(new_phases)
                
                new_free = list(free)
                new_free[app_idx] = end
                new_free = tuple(new_free)
                
                new_state = (new_phases, new_free)
                new_time = end
                
                if new_state not in visited or visited[new_state] > new_time:
                    visited[new_state] = new_time
                    heappush(pq, (new_time, new_phases, new_free))
    
    # Should never reach here if input is valid
    print(0)

solve()