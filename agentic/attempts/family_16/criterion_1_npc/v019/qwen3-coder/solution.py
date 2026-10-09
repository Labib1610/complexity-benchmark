from collections import deque
import sys

def solve():
    j, m = map(int, input().split())
    
    elixirs = []
    for _ in range(j):
        line = list(map(int, input().split()))
        o = line[0]
        phases = []
        for i in range(1, len(line), 2):
            apparatus = line[i]
            duration = line[i+1]
            phases.append((apparatus, duration))
        elixirs.append(phases)
    
    # We'll use a backtracking approach with pruning
    # State: for each elixir, we track which phase it's on and when it started that phase
    # For each apparatus, we track when it becomes free
    
    # apparatus_end_time[i] = time when apparatus i becomes free (1-indexed)
    apparatus_end_time = [0] * (m + 1)
    
    def backtrack(elixir_phases, elixir_idx, phase_idx, elixir_start_times, current_max_time):
        # elixir_phases: list of phase lists for each elixir
        # elixir_idx: current elixir we're considering
        # phase_idx: current phase within that elixir
        # elixir_start_times: for each elixir, start time of its current phase
        # current_max_time: current maximum completion time
        
        # Base case: if we've processed all phases of all elixirs
        if elixir_idx >= len(elixir_phases):
            return current_max_time
            
        # If this elixir has no more phases, move to the next elixir
        if phase_idx >= len(elixir_phases[elixir_idx]):
            return backtrack(elixir_phases, elixir_idx + 1, 0, elixir_start_times, current_max_time)
        
        # Pruning: if current max time already exceeds our best known solution, return
        # (We'd need to pass best_known_time to do this effectively)
        
        # Get the current phase details
        apparatus, duration = elixir_phases[elixir_idx][phase_idx]
        
        # Calculate earliest time this phase can start:
        # 1. After the previous phase of the same elixir finishes
        phase_start_time = 0
        if phase_idx > 0:
            prev_app, prev_dur = elixir_phases[elixir_idx][phase_idx - 1]
            phase_start_time = elixir_start_times[elixir_idx] + prev_dur
            
        # 2. After the apparatus becomes free
        apparatus_free_time = apparatus_end_time[apparatus]
        
        # The actual start time is the maximum of these
        actual_start_time = max(phase_start_time, apparatus_free_time)
        finish_time = actual_start_time + duration
        
        # Update state
        old_apparatus_end = apparatus_end_time[apparatus]
        old_elixir_start = elixir_start_times[elixir_idx]
        old_current_max = current_max_time
        
        apparatus_end_time[apparatus] = finish_time
        elixir_start_times[elixir_idx] = actual_start_time
        new_max_time = max(current_max_time, finish_time)
        
        # Recurse
        result = backtrack(elixir_phases, elixir_idx, phase_idx + 1, elixir_start_times, new_max_time)
        
        # Backtrack state
        apparatus_end_time[apparatus] = old_apparatus_end
        elixir_start_times[elixir_idx] = old_elixir_start
        
        return result
    
    # Try all permutations of processing order of elixirs
    # But that's too much; let's think differently
    
    # Actually, let's model this as a scheduling problem
    # We can try all possible orders of starting the elixirs
    
    from itertools import permutations
    
    def simulate_order(order):
        # apparatus_end_time[i] = time when apparatus i becomes free (1-indexed)
        app_end = [0] * (m + 1)
        # elixir_completion[i] = completion time of elixir i
        elixir_completion = [0] * len(elixirs)
        
        # For tracking when each elixir starts its current phase
        elixir_phase_start = [0] * len(elixirs)
        
        # Process elixirs in the given order
        for elixir_id in order:
            phases = elixirs[elixir_id]
            time = 0  # Start time for the first phase of this elixir
            
            for phase_idx, (apparatus, duration) in enumerate(phases):
                # This phase can start after:
                # 1. Previous phase of same elixir finishes
                # 2. Apparatus becomes free
                
                if phase_idx > 0:
                    time = elixir_phase_start[elixir_id] 
                
                # Apparatus might not be free yet
                start_time = max(time, app_end[apparatus])
                end_time = start_time + duration
                
                # Update apparatus availability
                app_end[apparatus] = end_time
                elixir_phase_start[elixir_id] = end_time
                time = end_time
                
            elixir_completion[elixir_id] = time
            
        return max(elixir_completion)
    
    # Try all permutations of elixir processing order
    min_time = float('inf')
    for perm in permutations(range(len(elixirs))):
        time = simulate_order(perm)
        min_time = min(min_time, time)
        
    print(min_time)

solve()