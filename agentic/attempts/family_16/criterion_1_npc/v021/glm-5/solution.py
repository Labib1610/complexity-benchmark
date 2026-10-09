import sys
import heapq

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    m = int(next(it))
    
    potions = []
    for _ in range(j):
        o = int(next(it))
        phases = []
        for _ in range(o):
            focus = int(next(it))
            duration = int(next(it))
            phases.append((focus - 1, duration))  # 0-indexed focus
        potions.append(phases)
    
    # State: (time, potion_idx, phase_idx for each potion, focus_available_time for each focus)
    # We use a priority queue for Dijkstra-like search
    
    # Initial state: all potions at phase 0, all foci available at time 0
    # State representation: (current_time, phase_indices tuple, focus_available tuple)
    
    # For efficiency, we track:
    # - phase_idx[i]: current phase index for potion i (0 to len(potions[i]))
    # - focus_time[f]: earliest time focus f becomes available
    
    # Initial state
    init_phases = tuple(0 for _ in range(j))
    init_focus_time = tuple(0 for _ in range(m))
    
    # Priority queue: (time, phases, focus_times)
    # Use a visited set to avoid revisiting states
    visited = {}
    pq = [(0, init_phases, init_focus_time)]
    visited[(init_phases, init_focus_time)] = 0
    
    result = float('inf')
    
    while pq:
        time, phases, focus_times = heapq.heappop(pq)
        
        # Skip if we've found a better path to this state
        if visited.get((phases, focus_times), float('inf')) < time:
            continue
        
        # Check if all potions are complete
        all_done = True
        for i in range(j):
            if phases[i] < len(potions[i]):
                all_done = False
                break
        
        if all_done:
            result = min(result, time)
            continue
        
        # Try to advance each potion that can be advanced
        for potion_idx in range(j):
            phase_idx = phases[potion_idx]
            if phase_idx >= len(potions[potion_idx]):
                continue  # This potion is done
            
            focus, duration = potions[potion_idx][phase_idx]
            
            # Calculate when this phase can start
            # It can start after:
            # 1. Current time (we're at this state at this time)
            # 2. The focus becomes available
            start_time = max(time, focus_times[focus])
            end_time = start_time + duration
            
            # Create new state
            new_phases = list(phases)
            new_phases[potion_idx] = phase_idx + 1
            new_phases = tuple(new_phases)
            
            new_focus_times = list(focus_times)
            new_focus_times[focus] = end_time
            new_focus_times = tuple(new_focus_times)
            
            # The new "current time" is the minimum of:
            # - end_time (if we just finished this phase)
            # - Other times that might be relevant
            # Actually, for correctness, we need to track when we can make the next decision
            # The state time should be the earliest time at which we can make a new decision
            # This is the minimum of all focus_times and the current time
            # But since we're using a priority queue, we can just use the end_time as the new time
            # and let the focus_times track when each focus is available
            
            new_time = end_time
            
            state_key = (new_phases, new_focus_times)
            if state_key not in visited or visited[state_key] > new_time:
                visited[state_key] = new_time
                heapq.heappush(pq, (new_time, new_phases, new_focus_times))
    
    print(result)

solve()