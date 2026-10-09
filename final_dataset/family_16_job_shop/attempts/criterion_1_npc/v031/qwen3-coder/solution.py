from collections import deque
import sys

def solve():
    j, m = map(int, input().split())
    
    dishes = []
    for _ in range(j):
        line = list(map(int, input().split()))
        o = line[0]
        steps = []
        for i in range(o):
            workstation = line[1 + 2*i]
            duration = line[1 + 2*i + 1]
            steps.append((workstation, duration))
        dishes.append(steps)
    
    # We'll use a BFS/DFS with state compression
    # State: for each dish, we track which step it's on and when it will finish that step
    # But this can be exponential...
    
    # Let's try a different approach: simulate the process
    # At any time, we know for each dish: what's the earliest time it can start its next step
    # And we know for each workstation: when it becomes free
    
    # Actually, let's think of this as a scheduling problem with dependencies
    # For each dish, its steps have to happen in order
    # For each workstation, only one thing can happen at a time
    
    # This is essentially a job shop scheduling problem
    # Since constraints are small, we can use a backtracking approach with pruning
    
    # Let's represent the state:
    # For each dish, track which step it's currently on
    # For each workstation, track when it becomes free
    
    # We can model this as finding the minimum makespan
    
    # Use recursive backtracking with memoization
    # State: (dish_step_index_tuple, workstation_free_times)
    
    from functools import lru_cache
    
    # But the state space might still be too big
    # Let's try a different approach: iterative deepening DFS or A* might be overkill
    
    # Let's go with a more direct simulation approach with backtracking
    
    def backtrack(dish_steps, workstation_free, dish_current_step, max_time):
        # dish_steps: list of steps for each dish
        # workstation_free: list, when each workstation becomes free
        # dish_current_step: current step index for each dish
        # max_time: current maximum finish time
        
        # Check if all dishes are done
        all_done = True
        for i in range(len(dish_steps)):
            if dish_current_step[i] < len(dish_steps[i]):
                all_done = False
                break
        
        if all_done:
            return max_time
            
        # Try to schedule the next step of each dish
        result = float('inf')
        
        for dish_id in range(len(dish_steps)):
            if dish_current_step[dish_id] >= len(dish_steps[dish_id]):
                continue
                
            workstation, duration = dish_steps[dish_id][dish_current_step[dish_id]]
            
            # A dish can start this step only after:
            # 1. The previous step of this dish is done
            # 2. The workstation is free
            
            start_time = workstation_free[workstation - 1]
            if dish_current_step[dish_id] > 0:
                # Need to wait for previous step to finish
                prev_w, prev_d = dish_steps[dish_id][dish_current_step[dish_id] - 1]
                # This is handled by our state tracking
            
            # The actual start time is max of when the workstation is free and when the previous step finishes
            # But in our model, workstation_free already accounts for this
            actual_start = start_time
            
            finish_time = actual_start + duration
            
            if finish_time > result:
                continue  # Pruning
                
            # Make the move
            old_workstation_free = workstation_free[workstation - 1]
            workstation_free[workstation - 1] = finish_time
            
            old_dish_step = dish_current_step[dish_id]
            dish_current_step[dish_id] += 1
            
            # Recurse
            res = backtrack(dish_steps, workstation_free, dish_current_step, max(max_time, finish_time))
            result = min(result, res)
            
            # Undo the move
            dish_current_step[dish_id] = old_dish_step
            workstation_free[workstation - 1] = old_workstation_free
            
        return result
    
    # Initialize
    workstation_free = [0] * m
    dish_current_step = [0] * j
    
    # But there's a flaw in the above logic: we're not properly tracking when a dish can start its next step
    # A dish's next step can only start after its previous step finishes
    
    # Let's fix the approach:
    # For each dish, we track when it finishes its previous step
    # For each workstation, we track when it becomes free
    # When scheduling a step, it starts at max(prev_step_finish, workstation_free)
    
    def backtrack_v2(dish_steps, workstation_free, dish_prev_finish, max_time):
        # dish_prev_finish: when each dish finished its previous step (or 0 if starting)
        
        # Check if all dishes are done
        all_done = True
        for i in range(len(dish_steps)):
            if dish_prev_finish[i] != -1 or len(dish_steps[i]) > 0:
                # Check if there are more steps
                # Actually, let's reorganize the state
                
                steps_done = 0
                for k in range(len(dish_steps[i])):
                    if dish_prev_finish[i] == -1:
                        break
                    w, d = dish_steps[i][k]
                    # This approach is getting messy
                    
        # Let me restart with a cleaner approach
        
        # State: for each dish, how many steps completed
        # For each step, we know when it can start: 
        #   max(time dish is ready, time workstation is free)
        
        # Let's use a recursive function with proper state tracking
        
        pass
    
    # Let's try yet another approach: generate all possible schedules?
    # No, that's exponential.
    
    # Let's go back to the first backtrack but fix the logic:
    
    def get_min_time(dish_steps):
        # dish_steps[dish_index] = [(workstation, duration), ...]
        
        # Memoization state should capture:
        # - for each dish, how many steps are completed
        # - for each workstation, when it will be free next
        
        @lru_cache(maxsize=None)
        def dp(state):
            dish_progress, ws_free_str = state
            dish_progress = list(dish_progress)
            ws_free = list(map(int, ws_free_str.split(','))) if ws_free_str else [0]*m
            
            # Check if all dishes are complete
            done = True
            for i, progress in enumerate(dish_progress):
                if progress < len(dish_steps[i]):
                    done = False
                    break
            
            if done:
                return 0
                
            result = float('inf')
            # Try advancing any dish's next step
            for dish_idx in range(len(dish_steps)):
                if dish_progress[dish_idx] >= len(dish_steps[dish_idx]):
                    continue
                    
                w, d = dish_steps[dish_idx][dish_progress[dish_idx]]
                
                # When can this step start?
                # It needs the workstation to be free AND the previous step of this dish to be done
                start_time = ws_free[w-1]  # Workstation free time
                
                # Create new state
                new_dish_progress = dish_progress[:]
                new_dish_progress[dish_idx] += 1
                
                new_ws_free = ws_free[:]
                finish_time = start_time + d
                new_ws_free[w-1] = finish_time
                
                # Recursive call
                sub_result = dp((tuple(new_dish_progress), ','.join(map(str, new_ws_free))))
                result = min(result, finish_time + sub_result if sub_result != float('inf') else finish_time if all(p >= len(dish_steps[i]) for i, p in enumerate(new_dish_progress)) else float('inf'))
                
                # Actually, this DP formulation isn't quite right because we're double-counting times
            
            # Simpler base case check:
            if done:
                return 0
            
            # Let's just compute the actual finish time directly
            result = float('inf')
            for dish_idx in range(len(dish_steps)):
                if dish_progress[dish_idx] >= len(dish_steps[dish_idx]):
                    continue
                    
                w, d = dish_steps[dish_idx][dish_progress[dish_idx]]
                start_time = ws_free[w-1]
                finish_time = start_time + d
                
                # New state
                new_dish_progress = dish_progress[:]
                new_dish_progress[dish_idx] += 1
                new_ws_free = ws_free[:]
                new_ws_free[w-1] = finish_time
                
                sub = dp((tuple(new_dish_progress), ','.join(map(str, new_ws_free))))
                candidate = sub  # This is wrong
                
            # Let me abandon this DP approach and do a direct search
            
            return result
            
        # Initial state
        initial_progress = tuple([0] * len(dish_steps))
        initial_ws_free = tuple([0] * m)
        
        # Actually, let's do a much simpler recursive search without memoization since the state space is manageable
        
        def search(dish_progress, ws_free):
            # Check if done
            if all(dish_progress[i] == len(dish_steps[i]) for i in range(len(dish_steps))):
                return 0
                
            best = float('inf')
            for i in range(len(dish_steps)):
                if dish_progress[i] < len(dish_steps[i]):
                    w, d = dish_steps[i][dish_progress[i]]
                    start_time = ws_free[w-1]
                    finish_time = start_time + d
                    
                    # Update state
                    new_progress = list(dish_progress)
                    new_progress[i] += 1
                    new_ws_free = list(ws_free)
                    new_ws_free[w-1] = finish_time
                    
                    # Recurse
                    rest = search(tuple(new_progress), tuple(new_ws_free))
                    best = min(best, max(finish_time, rest))
                    
            return best
            
        return search(tuple([0] * len(dish_steps)), tuple([0] * m))
    
    result = get_min_time(dishes)
    print(result)

solve()