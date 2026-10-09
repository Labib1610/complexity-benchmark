from collections import deque

def solve():
    j, m = map(int, input().split())
    
    ships = []
    for _ in range(j):
        data = list(map(int, input().split()))
        p = data[0]
        steps = []
        for i in range(p):
            bay = data[1 + 2*i]
            duration = data[1 + 2*i + 1]
            steps.append((bay - 1, duration))  # Convert to 0-indexed bays
        ships.append(steps)
    
    # For each ship, we track which step it's on and when it can start that step
    ship_step_index = [0] * j
    ship_next_available_time = [0] * j
    
    # For each bay, we track when it becomes free (it's a queue of (end_time,))
    bay_end_times = [[] for _ in range(m)]
    
    # We simulate time progression
    current_time = 0
    total_steps = sum(len(ship) for ship in ships)
    completed_steps = 0
    
    # Precompute for each ship, for each of its steps, the earliest time it can start that step
    ship_step_start_times = [[0] for _ in range(j)]  # Step 0 can start at time 0 (before any step)
    
    while completed_steps < total_steps:
        # Determine for each ship what is the earliest time it can start its next step
        ship_can_start = []
        for ship_id in range(j):
            if ship_step_index[ship_id] < len(ships[ship_id]):
                # This ship has more steps
                step_idx = ship_step_index[ship_id]
                bay, duration = ships[ship_id][step_idx]
                
                # Earliest this ship can start this step is max of:
                # 1. When the previous step finishes (if any)
                # 2. When the required bay is free
                prev_finish_time = ship_step_start_times[ship_id][step_idx] 
                # Find the earliest time this bay is free
                bay_free_time = 0
                for end_time in bay_end_times[bay]:
                    if end_time > bay_free_time:
                        bay_free_time = end_time
                
                can_start_at = max(prev_finish_time, bay_free_time)
                ship_can_start.append((can_start_at, ship_id, bay, duration))
            else:
                ship_can_start.append((float('inf'), ship_id, -1, -1)) # No more steps
        
        # Find the ship that can start its step the earliest
        ship_can_start.sort()
        earliest_start_time, ship_id, bay, duration = ship_can_start[0]
        
        if earliest_start_time == float('inf'):
            break # No more steps for any ship
            
        # Advance time to when this step starts
        current_time = earliest_start_time
        
        # Execute this step
        end_time = current_time + duration
        bay_end_times[bay].append(end_time)
        
        # Record when this ship's step finishes
        step_idx = ship_step_index[ship_id]
        ship_step_start_times[ship_id].append(end_time) # This is when the next step can start
        
        # Move to next step for this ship
        ship_step_index[ship_id] += 1
        completed_steps += 1
        
        # Update current_time to reflect the progress
        current_time = end_time
    
    # The answer is the maximum time any ship finishes its last step
    max_finish_time = 0
    for times in ship_step_start_times:
        if times[-1] > max_finish_time:
            max_finish_time = times[-1]
            
    print(max_finish_time)

solve()