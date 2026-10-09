from collections import defaultdict
import heapq

def solve():
    j, m = map(int, input().split())
    
    potions = []
    for _ in range(j):
        line = list(map(int, input().split()))
        o = line[0]
        phases = []
        for i in range(o):
            focus = line[1 + 2*i]
            duration = line[1 + 2*i + 1]
            phases.append((focus, duration))
        potions.append(phases)
    
    # We'll use a backtracking approach with pruning
    # For each potion, we keep track of which phase we're on
    # For each focus, we keep track of when it becomes free
    
    # Let's try a different approach - since constraints are small,
    # we can model this as a state space search
    
    # State: (time, potion_phases, focus_free_time)
    # potion_phases[i] = which phase potion i is currently on (or -1 if done)
    # focus_free_time[i] = when focus i becomes free
    
    # Initial state
    num_phases = [len(potion) for potion in potions]
    initial_potion_phases = [0 if num_phases[i] > 0 else -1 for i in range(j)]
    initial_focus_free_time = [0] * (m + 1)  # 1-indexed
    
    # We'll use a priority queue for best-first search
    pq = [(0, tuple(initial_potion_phases), tuple(initial_focus_free_time))]
    visited = set()
    
    while pq:
        time, potion_phases, focus_free_time = heapq.heappop(pq)
        state_key = (potion_phases, focus_free_time)
        
        if state_key in visited:
            continue
        visited.add(state_key)
        
        # Check if all potions are done
        if all(phase == -1 for phase in potion_phases):
            print(time)
            return
        
        # For each potion, see if we can start its current phase
        for i in range(j):
            phase_idx = potion_phases[i]
            if phase_idx == -1 or phase_idx >= num_phases[i]:
                continue  # Potion is done or invalid
            
            focus, duration = potions[i][phase_idx]
            
            # When can this phase start?
            start_time = max(time, focus_free_time[focus])
            end_time = start_time + duration
            
            # Create new state
            new_potion_phases = list(potion_phases)
            new_potion_phases[i] = phase_idx + 1
            if new_potion_phases[i] >= num_phases[i]):
                new_potion_phases[i] = -1
                
            new_focus_free_time = list(focus_free_time)
            new_focus_free_time[focus] = end_time
            
            heapq.heappush(pq, (end_time, tuple(new_potion_phases), tuple(new_focus_free_time)))

solve()