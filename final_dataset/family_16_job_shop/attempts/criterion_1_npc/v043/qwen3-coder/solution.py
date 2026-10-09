import heapq
from collections import defaultdict, deque

def solve():
    j, m = map(int, input().split())
    
    # clerk_finish_times tracks when each clerk will be free
    clerk_finish_times = [0] * (m + 1)  # 1-indexed
    
    # For each dossier, we'll track when it finishes each step
    # We process dossiers in order, but steps within them are sequential
    
    # We model this as an event-based simulation
    # Events: (time, event_type, dossier_id, step_idx)
    # event_type: 'start' or 'finish'
    
    # But a simpler way is to process each dossier step-by-step,
    # tracking when each step can start based on:
    # 1. Previous step of same dossier finished
    # 2. Required clerk is free
    
    # For each dossier, we store when it finishes each step
    dossier_step_finish = [[] for _ in range(j)]
    
    # Also store the step info
    dossiers = []
    
    for i in range(j):
        line = list(map(int, input().split()))
        o = line[0]
        steps = []
        for k in range(o):
            clerk = line[1 + 2*k]
            duration = line[1 + 2*k + 1]
            steps.append((clerk, duration))
        dossiers.append(steps)
    
    # For each dossier, track when it finishes its previous step
    dossier_prev_finish = [0] * j
    
    # Process all steps in chronological order of when they can start
    # This is a greedy approach: whenever a clerk is free and a dossier's 
    # previous step is done, start the next step
    
    # Let's track for each dossier, which step it's on
    dossier_step_index = [0] * j
    
    # When a dossier completes a step, we update:
    # - dossier_step_finish[dossier_id].append(finish_time)
    # - dossier_prev_finish[dossier_id] = finish_time
    # - dossier_step_index[dossier_id] += 1
    
    # We continue until all dossiers have completed all their steps
    
    total_steps_completed = 0
    total_steps_all = sum(len(d) for d in dossiers)
    
    while total_steps_completed < total_steps_all:
        # Find the earliest possible step to start
        min_start_time = float('inf')
        next_dossier = -1
        next_step_idx = -1
        next_clerk = -1
        next_duration = -1
        
        for i in range(j):
            if dossier_step_index[i] < len(dossiers[i]):
                # This dossier has more steps
                step_idx = dossier_step_index[i]
                clerk, duration = dossiers[i][step_idx]
                
                # This step can start at max(prev_step_finish, clerk_free_time)
                prev_finish = dossier_prev_finish[i]
                clerk_free = clerk_finish_times[clerk]
                start_time = max(prev_finish, clerk_free)
                
                if start_time < min_start_time:
                    min_start_time = start_time
                    next_dossier = i
                    next_step_idx = step_idx
                    next_clerk = clerk
                    next_duration = duration
        
        # Execute this step
        start_time = min_start_time
        finish_time = start_time + next_duration
        
        # Update state
        dossier_step_finish[next_dossier].append(finish_time)
        dossier_prev_finish[next_dossier] = finish_time
        dossier_step_index[next_dossier] += 1
        clerk_finish_times[next_clerk] = finish_time
        total_steps_completed += 1
    
    # The answer is the maximum finish time among all dossiers
    result = 0
    for finish_list in dossier_step_finish:
        if finish_list:
            result = max(result, finish_list[-1])
            
    print(result)

solve()