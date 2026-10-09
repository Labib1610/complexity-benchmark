import sys
from collections import deque

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    m = int(next(it))
    
    sequences = []
    for _ in range(j):
        o = int(next(it))
        seq = []
        for _ in range(o):
            emitter = int(next(it)) - 1
            duration = int(next(it))
            seq.append((emitter, duration))
        sequences.append(seq)
    
    # State: (phase_index for each sequence)
    # We use BFS/DP to find minimum time to reach the final state
    # Since total phases <= 50 and j <= 10, state space is manageable
    
    # For each state, we track the earliest time to reach it
    # We also need to track when each emitter becomes free
    
    # Let's use a different approach: simulate time steps
    # But durations can be up to 1000, so we need a smarter approach
    
    # Use event-driven simulation with priority queue
    # State: (current_time, phase_indices, emitter_free_times)
    # But this might have too many states
    
    # Alternative: DP with state being phase indices
    # For each state, we compute the minimum time to reach it
    # When transitioning, we need to account for emitter availability
    
    from functools import lru_cache
    
    # Get total phases for each sequence
    seq_lens = [len(seq) for seq in sequences]
    final_state = tuple(seq_lens)
    
    # For each sequence, compute prefix sums of durations
    # This helps us know the minimum time needed for a sequence up to a certain phase
    # But we need to account for emitter conflicts
    
    # Let's use BFS with state being (phase_indices)
    # For each state, we track the earliest finish time for each emitter
    
    # Actually, let's think differently:
    # We can model this as finding the shortest path in a state graph
    # State: (phase_indices for all sequences)
    # Transition: advance one or more sequences to their next phase
    # Cost: time needed for the transition
    
    # But we need to track emitter availability, which depends on history
    
    # Better approach: use DP where state includes phase indices
    # and we compute the minimum time to reach each state
    # When transitioning, we compute the earliest time we can start the next phase
    
    # Let's use memoization with state being phase indices
    # We'll compute the minimum time to complete all phases
    
    # Actually, let's use a different formulation:
    # For each sequence, track the current phase index
    # For each emitter, track when it becomes free
    # We use BFS/priority queue to find minimum time
    
    import heapq
    
    # State: (time, phase_indices_tuple, emitter_free_times_tuple)
    # Start: (0, (0, 0, ...), (0, 0, ...))
    
    start_phases = tuple(0 for _ in range(j))
    start_emitters = tuple(0 for _ in range(m))
    
    # Use priority queue for Dijkstra-like algorithm
    # State: (time, phase_indices, emitter_free_times)
    # We want to find minimum time to reach final state
    
    # To reduce state space, we can note that emitter_free_times can be derived
    # from the history of phases executed. But this is complex.
    
    # Let's try a simpler approach: BFS with pruning
    
    # visited: set of (phase_indices, emitter_free_times)
    visited = set()
    pq = []
    heapq.heappush(pq, (0, start_phases, start_emitters))
    
    while pq:
        time, phases, emitters = heapq.heappop(pq)
        
        if phases == final_state:
            print(time)
            return
        
        state = (phases, emitters)
        if state in visited:
            continue
        visited.add(state)
        
        # Try to advance each sequence
        for seq_idx in range(j):
            phase_idx = phases[seq_idx]
            if phase_idx >= seq_lens[seq_idx]:
                continue
            
            emitter, duration = sequences[seq_idx][phase_idx]
            
            # This phase can start at max(time, emitters[emitter])
            start_time = max(time, emitters[emitter])
            end_time = start_time + duration
            
            # Create new state
            new_phases = list(phases)
            new_phases[seq_idx] = phase_idx + 1
            new_phases = tuple(new_phases)
            
            new_emitters = list(emitters)
            new_emitters[emitter] = end_time
            new_emitters = tuple(new_emitters)
            
            new_state = (new_phases, new_emitters)
            if new_state not in visited:
                heapq.heappush(pq, (end_time, new_phases, new_emitters))
    
    # Should not reach here
    print(-1)

solve()