import sys
from itertools import permutations

def solve():
    data = sys.stdin.read().strip().split()
    idx = 0
    j = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    
    steps = []
    for _ in range(j):
        p = int(data[idx]); idx += 1
        ship_steps = []
        for _ in range(p):
            bay = int(data[idx]); idx += 1
            dur = int(data[idx]); idx += 1
            ship_steps.append((bay, dur))
        steps.append(ship_steps)
    
    # State: for each ship, which step index it's on
    # We'll simulate time and try all possible next steps
    # Use recursion with memoization on (time, ship_states)
    
    from functools import lru_cache
    
    # ship_states: tuple of current step index for each ship
    # bay_free_time: when each bay becomes free
    @lru_cache(None)
    def dfs(ship_states, bay_free):
        # ship_states: tuple of ints
        # bay_free: tuple of ints (free time for each bay)
        
        # Check if all ships done
        if all(ship_states[i] == len(steps[i]) for i in range(j)):
            return 0
        
        current_time = max(0, min(bay_free) if bay_free else 0)
        # Actually we need to consider the earliest possible next event
        # We'll just try all possible next steps from current state
        
        best = float('inf')
        
        for i in range(j):
            if ship_states[i] < len(steps[i]):
                bay, dur = steps[i][ship_states[i]]
                start_time = max(current_time, bay_free[bay-1])
                # If we schedule this step now
                new_ship_states = list(ship_states)
                new_ship_states[i] += 1
                new_bay_free = list(bay_free)
                new_bay_free[bay-1] = start_time + dur
                
                # The time for this step is start_time + dur
                # But we need to pass the time when this step finishes
                # We'll pass the max of all bay_free times as current time
                next_time = max(new_bay_free)
                # Actually we need to pass the state after this step
                # The recursion will handle time implicitly
                # We'll pass the new bay_free and ship_states
                # But we need to know the time spent so far
                # So we'll add the duration from start_time to finish
                # Better: pass current_time as parameter
                # Let's restructure: dfs(current_time, ship_states, bay_free)
                pass
        
        # Restructure with current_time parameter
        return best
    
    # Let's do a proper simulation with recursion including current_time
    from functools import lru_cache
    
    @lru_cache(None)
    def dfs(time, ship_states, bay_free):
        # ship_states: tuple of ints
        # bay_free: tuple of ints
        if all(ship_states[i] == len(steps[i]) for i in range(j)):
            return time
        
        best = float('inf')
        for i in range(j):
            if ship_states[i] < len(steps[i]):
                bay, dur = steps[i][ship_states[i]]
                start_time = max(time, bay_free[bay-1])
                new_ship_states = list(ship_states)
                new_ship_states[i] += 1
                new_bay_free = list(bay_free)
                new_bay_free[bay-1] = start_time + dur
                best = min(best, dfs(start_time + dur, tuple(new_ship_states), tuple(new_bay_free)))
        return best
    
    initial_ship_states = tuple([0]*j)
    initial_bay_free = tuple([0]*m)
    result = dfs(0, initial_ship_states, initial_bay_free)
    print(result)

if __name__ == "__main__":
    solve()