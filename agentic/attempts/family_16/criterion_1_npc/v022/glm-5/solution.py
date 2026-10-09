import sys
from collections import deque

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    m = int(next(it))
    
    subroutines = []
    total_gates = 0
    for _ in range(j):
        o = int(next(it))
        gates = []
        for _ in range(o):
            core = int(next(it)) - 1  # 0-indexed
            duration = int(next(it))
            gates.append((core, duration))
        subroutines.append(gates)
        total_gates += o
    
    # State: tuple of indices (one per subroutine) representing current position in each
    # We also need to track when each core becomes free
    # Use BFS/Dijkstra with priority queue
    
    # Initial state: all at position 0, all cores free at time 0
    start_state = tuple(0 for _ in range(j))
    
    # Priority queue: (current_time, state, core_free_times)
    # core_free_times is a tuple of m integers
    import heapq
    pq = []
    initial_core_free = tuple(0 for _ in range(m))
    heapq.heappush(pq, (0, start_state, initial_core_free))
    
    visited = {}  # state -> min time to reach this state
    
    while pq:
        time, state, core_free = heapq.heappop(pq)
        
        # Check if all subroutines are complete
        all_done = True
        for idx in range(j):
            if state[idx] < len(subroutines[idx]):
                all_done = False
                break
        if all_done:
            print(time)
            return
        
        # Skip if we've seen this state with better or equal time
        state_key = (state, core_free)
        if state_key in visited and visited[state_key] <= time:
            continue
        visited[state_key] = time
        
        # Try to advance each subroutine by one gate
        for idx in range(j):
            pos = state[idx]
            if pos >= len(subroutines[idx]):
                continue
            
            core, duration = subroutines[idx][pos]
            
            # Gate can start when: 1) previous gate in this subroutine is done (time)
            #                     2) the core is free (core_free[core])
            start_time = max(time, core_free[core])
            end_time = start_time + duration
            
            # Create new state
            new_state = list(state)
            new_state[idx] = pos + 1
            new_state = tuple(new_state)
            
            new_core_free = list(core_free)
            new_core_free[core] = end_time
            new_core_free = tuple(new_core_free)
            
            # The time for this new state is end_time (when this gate finishes)
            # But other subroutines might still be at their previous times
            # Actually, the "time" in our state represents when each subroutine's last completed gate finished
            # So for the advanced subroutine, it's end_time; for others, it's their current time
            
            new_time = list(state)
            new_time[idx] = end_time
            # Wait, we need to track per-subroutine completion times
            
            # Let me reconsider: the state should track position, and we track time separately
            # Actually, the time in the priority queue is the max of all subroutine completion times
            # But we need to track individual completion times for dependency
            
            # Let's use a different approach: track completion time for each subroutine
            # State: (positions, completion_times_per_subroutine, core_free_times)
            # But that's too many dimensions
            
            # Alternative: the "time" in PQ is when we're making a decision
            # Each subroutine has a "ready time" which is when its last gate finished
            # This ready time is stored implicitly: if a subroutine is at position p,
            # its ready time is the time when gate p-1 finished
            
            # Let me restructure: store per-subroutine ready times in the state
            pass
    
    # Let me restart with a cleaner approach
    # State: (positions for each subroutine, ready_time for each subroutine, core_free times)
    # But this is too large
    
    # Better: use the fact that total gates <= 50
    # State: positions for each subroutine (at most 51^j states, but j <= 10, so this is huge)
    # Actually, total gates <= 50, so sum of positions <= 50
    # This is a classic job shop scheduling problem
    
    # Let's use a different representation
    # State: tuple of positions
    # For each state, we compute the minimum time to reach it
    # The time to reach a state depends on scheduling decisions
    
    # Actually, let's track: for each state (positions), what's the earliest time
    # each subroutine can start its next gate?
    
    # We need to track: for each subroutine, when its last gate finished
    # And for each core, when it becomes free
    
    # Let me use a cleaner Dijkstra approach
    # State: (positions, subroutine_finish_times, core_free_times)
    # But we can optimize: subroutine_finish_times can be derived from the path
    # 
    # Actually, let's just track positions and core_free_times
    # The subroutine_finish_time for subroutine i is the time when gate at position state[i]-1 finished
    # We need to track this explicitly
    
    # New approach: track (positions, finish_times, core_free)
    # finish_times[i] = when subroutine i's last completed gate finished (0 if no gates completed)
    
    # Initial: positions = (0,0,...), finish_times = (0,0,...), core_free = (0,0,...)
    
    pq = []
    start_positions = tuple(0 for _ in range(j))
    start_finish_times = tuple(0 for _ in range(j))
    start_core_free = tuple(0 for _ in range(m))
    heapq.heappush(pq, (0, start_positions, start_finish_times, start_core_free))
    
    visited = {}  # (positions, core_free) -> min max_finish_time
    
    while pq:
        max_time, positions, finish_times, core_free = heapq.heappop(pq)
        
        # Check if done
        done = True
        for idx in range(j):
            if positions[idx] < len(subroutines[idx]):
                done = False
                break
        if done:
            print(max_time)
            return
        
        # Skip if visited with better time
        state_key = (positions, core_free)
        if state_key in visited and visited[state_key] <= max_time:
            continue
        visited[state_key] = max_time
        
        # Try advancing each subroutine
        for idx in range(j):
            pos = positions[idx]
            if pos >= len(subroutines[idx]):
                continue
            
            core, duration = subroutines[idx][pos]
            
            # Start time is max of: when this subroutine finished last gate, when core is free
            start_time = max(finish_times[idx], core_free[core])
            end_time = start_time + duration
            
            new_positions = list(positions)
            new_positions[idx] = pos + 1
            new_positions = tuple(new_positions)
            
            new_finish_times = list(finish_times)
            new_finish_times[idx] = end_time
            new_finish_times = tuple(new_finish_times)
            
            new_core_free = list(core_free)
            new_core_free[core] = end_time
            new_core_free = tuple(new_core_free)
            
            new_max_time = max(max_time, end_time)
            
            heapq.heappush(pq, (new_max_time, new_positions, new_finish_times, new_core_free))

solve()