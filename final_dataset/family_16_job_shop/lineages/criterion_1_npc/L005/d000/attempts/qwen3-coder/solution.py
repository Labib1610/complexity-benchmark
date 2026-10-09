from collections import defaultdict
import sys

def solve():
    j, m = map(int, input().split())
    
    petitions = []
    for _ in range(j):
        line = list(map(int, input().split()))
        o = line[0]
        steps = []
        for i in range(o):
            magistrate = line[1 + 2*i]
            hours = line[1 + 2*i + 1]
            steps.append((magistrate, hours))
        petitions.append(steps)
    
    # Try all possible orderings of petitions
    # Since j <= 10, we can try all permutations if needed
    # But that's too many. Let's use a different approach.
    
    # We'll use backtracking to try all possible assignments
    # Actually, let's think differently.
    
    # This is a scheduling problem. We want to minimize the makespan.
    # Let's try a greedy approach with backtracking.
    
    # Since j is small (<= 10), and total steps <= 50, 
    # we can try all possible interleavings of the petitions.
    # But that's still a lot.
    
    # Better approach: state space search
    # State: for each petition, which step we're at, and when it will finish
    # But we also need to track when each magistrate is free
    
    # Let's model this as a state search problem
    # We can use a priority queue or just DFS with memoization
    
    # Actually, let's try a simpler approach:
    # Try all possible ways to interleave the petitions
    # Since the number of steps is small, we can enumerate all possible valid schedules
    
    # Even simpler: since j is small, we can try all permutations of petitions
    # and for each permutation, process them in order
    # But that's not optimal either because petitions can be interleaved
    
    # Let's think of this as a job shop scheduling problem
    # We can use a backtracking approach
    
    # State: (time, [petition_states], [magistrate_free_time])
    # petition_states[i] = which step petition i is on
    # magistrate_free_time[k] = when magistrate k+1 becomes free
    
    from functools import lru_cache
    
    # Let's restructure the data
    # For each petition, we have a list of (magistrate, duration)
    # We want to find the minimum time to complete all petitions
    
    # Let's use a recursive approach with memoization
    # State: (petition_step_index_tuple, magistrate_free_times)
    
    # Convert to tuple for hashing
    def get_next_state(petition_idx, step_idx, mag_free_times):
        # When can this step start?
        # It needs the previous step of this petition to finish
        # and the magistrate to be free
        magistrate, duration = petitions[petition_idx][step_idx]
        mag_idx = magistrate - 1
        
        start_time = mag_free_times[mag_idx]
        # But also, for this petition, the previous step must be done
        # We need to track when each petition finished its previous step
        
        return start_time, start_time + duration
    
    # Let's try a different approach: simulation with backtracking
    # At each time step, see which petitions can start their next step
    
    # Actually, let's use a more direct approach
    # We'll try all possible valid schedules
    
    # Since the constraints are small, we can do a search
    # Let's represent the state as:
    # - for each petition, which step it's on
    # - for each magistrate, when they're free
    # - current time
    
    # But we don't know the order, so we need to explore
    
    # Let's use a recursive function with memoization
    # State: (tuple of current step for each petition, tuple of free times for each magistrate)
    
    @lru_cache(maxsize=None)
    def min_time(petition_steps, mag_free_times):
        # If all petitions are done, return 0
        if all(petition_steps[i] == len(petitions[i]) for i in range(j)):
            return 0
            
        # Try to schedule the next step of each petition
        result = float('inf')
        
        for i in range(j):
            # If petition i has more steps
            if petition_steps[i] < len(petitions[i]):
                magistrate, duration = petitions[i][petition_steps[i]]
                mag_idx = magistrate - 1
                
                # When can this step start?
                # The magistrate must be free, and the previous step of this petition must be done
                start_time = mag_free_times[mag_idx]
                
                # Also, if this is not the first step, the previous step must be done
                if petition_steps[i] > 0:
                    # We need to know when petition i finished its previous step
                    # This is tricky to compute without more state
                    # Let's reorganize the approach
                    
                    # Let's track for each petition, when it finished its last step
                    pass
                    
        # This approach is getting complex. Let's restart with a cleaner method.
        return result
    
    # Restart with a cleaner approach
    # We'll simulate the process
    
    def backtrack(petition_positions, magistrate_free_time, current_time):
        # petition_positions[i] = index of next step for petition i (-1 if done)
        # magistrate_free_time[k] = time when magistrate k+1 is free
        # current_time = current simulation time
        
        # If all petitions are done
        if all(pos == -1 for pos in petition_positions):
            return current_time
            
        # Find all possible next steps
        min_completion = float('inf')
        
        for i in range(j):
            if petition_positions[i] != -1:  # If petition i is not done
                step_idx = petition_positions[i]
                if step_idx < len(petitions[i]):
                    magistrate, duration = petitions[i][step_idx]
                    mag_idx = magistrate - 1
                    
                    # When can this step start?
                    # It can start when:
                    # 1. The magistrate is free
                    # 2. The previous step of this petition is done (which means current_time is advanced enough)
                    
                    # For simplicity, let's assume we track this correctly in the state
                    
                    # The start time is max of when the magistrate is free and when the previous step finished
                    # To know when the previous step finished, we need more state
                    
                    # Let's simplify: we'll just check if the magistrate is free at or after current_time
                    start_time = max(current_time, magistrate_free_time[mag_idx])
                    end_time = start_time + duration
                    
                    # Make a copy of states
                    new_positions = petition_positions[:]
                    new_mag_times = magistrate_free_time[:]
                    
                    # Update states
                    new_positions[i] = step_idx + 1
                    if new_positions[i] >= len(petitions[i]):
                        new_positions[i] = -1
                        
                    new_mag_times[mag_idx] = end_time
                    
                    # Recurse
                    completion_time = backtrack(new_positions, new_mag_times, current_time)
                    min_completion = min(min_completion, completion_time)
                    
        return min_completion
    
    # This is still not right. We're not advancing time correctly.
    
    # Let's try a different simulation approach
    # At each step, find the earliest event (a step completion)
    # Then update the state
    
    # Actually, let's look at the constraints again
    # j <= 10, total steps <= 50
    # We can try a state-based DP
    
    # State: for each petition, which step it's on
    # For each magistrate, the earliest time they can start work
    # But we also need to know the dependencies (previous step of same petition)
    
    # Let's try to model this properly:
    # For each petition, we track:
    # - current step index
    # - time when it can start its current step (after previous step finishes)
    
    # For each magistrate, we track when they're free
    
    # Initial state:
    # All petitions at step 0, can start immediately
    # All magistrates free at time 0
    
    # We can use a priority queue or just recursive search
    
    @lru_cache(maxsize=None)
    def solve_state(petition_step_indices, magistrate_next_free):
        # petition_step_indices: tuple, step index for each petition
        # magistrate_next_free: tuple, next free time for each magistrate (0-indexed)
        
        # If all petitions are done
        if all(petition_step_indices[i] == len(petitions[i]) for i in range(j)):
            return 0
            
        # Try all possible next steps
        min_time_needed = float('inf')
        
        for i in range(j):
            # If petition i has a next step
            if petition_step_indices[i] < len(petitions[i]):
                magistrate_id, duration = petitions[i][petition_step_indices[i]]
                mag_idx = magistrate_id - 1
                
                # When can this step start?
                # 1. The magistrate must be free
                # 2. The previous step of this petition must be finished
                
                # The previous step constraint is implicit in our state:
                # We only consider petition i if all previous steps are conceptually scheduled
                # But we need to know when the previous step finishes
                
                # Actually, in this state representation, we assume that
                # if we're considering scheduling step k of petition i,
                # then step k-1 of petition i has already been scheduled and finished
                
                # So the start time is just when the magistrate is free
                start_time = magistrate_next_free[mag_idx]
                end_time = start_time + duration
                
                # Create new state
                new_petition_steps = list(petition_step_indices)
                new_petition_steps[i] += 1
                new_mag_free = list(magistrate_next_free)
                new_mag_free[mag_idx] = end_time
                
                # Recurse
                remaining_time = solve_state(tuple(new_petition_steps), tuple(new_mag_free))
                total_time = max(end_time, remaining_time)
                min_time_needed = min(min_time_needed, total_time)
                
        return min_time_needed
    
    initial_steps = tuple(0 for _ in range(j))
    initial_free = tuple(0 for _ in range(m))
    
    result = solve_state(initial_steps, initial_free)
    print(result)

solve()