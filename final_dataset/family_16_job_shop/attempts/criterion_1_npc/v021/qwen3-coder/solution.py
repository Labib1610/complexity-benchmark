from collections import defaultdict
import sys

def solve():
    j, m = map(int, input().split())
    
    potions = []
    for _ in range(j):
        line = list(map(int, input().split()))
        o = line[0]
        phases = []
        for i in range(o):
            focus = line[1 + 2*i]
            duration = line[2 + 2*i]
            phases.append((focus, duration))
        potions.append(phases)
    
    # We'll use backtracking with pruning
    # For each potion, we keep track of when it can start its next phase
    # For each focus, we keep track of when it becomes free
    
    # potion_times[i] is the earliest time potion i can start its next phase
    potion_times = [0] * j
    # focus_times[f] is the earliest time focus f becomes free (1-indexed)
    focus_times = [0] * (m + 1)
    
    def backtrack(potion_idx, phase_idx, potion_times, focus_times):
        # If we've processed all potions, return the maximum completion time
        if potion_idx == j:
            return max(potion_times)
        
        # If we've processed all phases of current potion, move to next potion
        if phase_idx == len(potions[potion_idx]):
            return backtrack(potion_idx + 1, 0, potion_times, focus_times)
        
        # Current phase details
        focus, duration = potions[potion_idx][phase_idx]
        
        # Earliest time this phase can start:
        # 1. When the potion is ready (previous phase done)
        # 2. When the focus is free
        start_time = max(potion_times[potion_idx], focus_times[focus])
        end_time = start_time + duration
        
        # Pruning: if current path already exceeds best known solution, stop
        # But we don't have a best yet, so we'll compute it
        
        # Make the choice
        new_potion_times = potion_times[:]
        new_focus_times = focus_times[:]
        new_potion_times[potion_idx] = end_time
        new_focus_times[focus] = end_time
        
        # Continue with next phase of same potion
        return backtrack(potion_idx, phase_idx + 1, new_potion_times, new_focus_times)
    
    # This approach is not correct because we're processing potions sequentially
    # We need to consider all possible orderings of phases
    
    # Let's try a different approach: generate all possible schedules
    # But that's too many. Let's use a more intelligent backtracking.
    
    # Better approach: at each step, choose which potion's next phase to schedule
    # We need to track for each potion, which phase is next
    
    # phase_idx[i] is the index of the next phase for potion i
    phase_idx = [0] * j
    # completion_times[i] is when potion i will be completed
    completion_times = [0] * j
    
    def backtrack_v2(phase_idx, completion_times, focus_times):
        # Check if all potions are done
        if all(phase_idx[i] == len(potions[i]) for i in range(j)):
            return max(completion_times) if completion_times else 0
        
        # Find all possible next phases
        best_time = float('inf')
        
        for i in range(j):
            # If potion i has more phases
            if phase_idx[i] < len(potions[i]):
                focus, duration = potions[i][phase_idx[i]]
                
                # When can this phase start?
                # 1. After the previous phase of this potion completes
                # 2. When the focus is free
                start_time = max(completion_times[i] if phase_idx[i] > 0 else 0, 
                                 focus_times[focus])
                end_time = start_time + duration
                
                # Make the move
                new_phase_idx = phase_idx[:]
                new_completion_times = completion_times[:]
                new_focus_times = focus_times[:]
                
                new_phase_idx[i] += 1
                new_completion_times[i] = end_time
                new_focus_times[focus] = end_time
                
                # Recurse
                time = backtrack_v2(new_phase_idx, new_completion_times, new_focus_times)
                best_time = min(best_time, time)
        
        return best_time
    
    result = backtrack_v2(phase_idx, completion_times, focus_times)
    print(result)

def solve_optimized():
    j, m = map(int, input().split())
    
    potions = []
    total_phases = 0
    for _ in range(j):
        line = list(map(int, input().split()))
        o = line[0]
        total_phases += o
        phases = []
        for i in range(o):
            focus = line[1 + 2*i]
            duration = line[2 + 2*i]
            phases.append((focus, duration))
        potions.append(phases)
    
    # State: for each potion, which phase we're at
    # For each focus, when it's free
    # Current time completion for each potion
    
    # We'll use DFS with memoization
    from functools import lru_cache
    
    # To make state hashable, we need to use tuples
    # But this might be too memory intensive
    
    def dfs(phase_positions, focus_free_times, potion_completion_times):
        # phase_positions: tuple of current phase index for each potion
        # focus_free_times: tuple of when each focus is free (1-indexed)
        # potion_completion_times: tuple of when each potion completed its last phase
        
        # If all potions are done
        if all(phase_positions[i] == len(potions[i]) for i in range(j)):
            return max(potion_completion_times) if potion_completion_times else 0
        
        result = float('inf')
        
        # Try scheduling next phase of each potion
        for i in range(j):
            if phase_positions[i] < len(potions[i]):
                focus, duration = potions[i][phase_positions[i]]
                
                # When can this start?
                start_time = max(
                    potion_completion_times[i] if phase_positions[i] > 0 else 0,
                    focus_free_times[focus-1]  # focus is 1-indexed, list is 0-indexed
                )
                end_time = start_time + duration
                
                # Update states
                new_positions = list(phase_positions)
                new_positions[i] += 1
                
                new_focus_times = list(focus_free_times)
                new_focus_times[focus-1] = end_time
                
                new_potion_times = list(potion_completion_times)
                new_potion_times[i] = end_time
                
                res = dfs(tuple(new_positions), tuple(new_focus_times), tuple(new_potion_times))
                result = min(result, res)
        
        return result
    
    # Initial states
    initial_positions = tuple(0 for _ in range(j))
    initial_focus_times = tuple(0 for _ in range(m))
    initial_potion_times = tuple(0 for _ in range(j))
    
    result = dfs(initial_positions, initial_focus_times, initial_potion_times)
    print(result)

# The above approach with full memoization might be too memory intensive
# Let's try without memoization but with better pruning

def solve_final():
    j, m = map(int, input().split())
    
    potions = []
    for _ in range(j):
        line = list(map(int, input().split()))
        o = line[0]
        phases = []
        for i in range(o):
            focus = line[1 + 2*i]
            duration = line[2 + 2*i]
            phases.append((focus, duration))
        potions.append(phases)
    
    # Global best
    best = [float('inf')]
    
    def dfs(phase_positions, focus_free_times, potion_completion_times):
        # Pruning
        current_max = max(potion_completion_times) if potion_completion_times else 0
        if current_max >= best[0]:
            return
        
        # If all potions are done
        if all(phase_positions[i] == len(potions[i]) for i in range(j)):
            best[0] = min(best[0], current_max)
            return
        
        # Try scheduling next phase of each potion
        for i in range(j):
            if phase_positions[i] < len(potions[i]):
                focus, duration = potions[i][phase_positions[i]]
                
                # When can this start?
                start_time = max(
                    potion_completion_times[i] if phase_positions[i] > 0 else 0,
                    focus_free_times[focus-1]  # focus is 1-indexed
                )
                end_time = start_time + duration
                
                # Update states
                phase_positions[i] += 1
                old_focus_time = focus_free_times[focus-1]
                focus_free_times[focus-1] = end_time
                old_potion_time = potion_completion_times[i]
                potion_completion_times[i] = end_time
                
                dfs(phase_positions, focus_free_times, potion_completion_times)
                
                # Backtrack
                phase_positions[i] -= 1
                focus_free_times[focus-1] = old_focus_time
                potion_completion_times[i] = old_potion_time
    
    # Initial states
    phase_positions = [0] * j
    focus_free_times = [0] * m
    potion_completion_times = [0] * j
    
    dfs(phase_positions, focus_free_times, potion_completion_times)
    print(best[0])

solve_final()