import sys
import heapq

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    m = int(next(it))
    
    projects = []
    total_steps = 0
    for _ in range(j):
        o = int(next(it))
        steps = []
        for _ in range(o):
            ws = int(next(it)) - 1
            dur = int(next(it))
            steps.append((ws, dur))
        projects.append(steps)
        total_steps += o
    
    # State: (time, project_next_step_indices, workstation_free_times)
    # project_next_step_indices: tuple of integers, index of next step for each project
    # workstation_free_times: tuple of integers, time when each workstation becomes free
    
    initial_indices = tuple(0 for _ in range(j))
    initial_wstimes = tuple(0 for _ in range(m))
    
    # Priority queue: (current_time, indices, wstimes)
    pq = [(0, initial_indices, initial_wstimes)]
    visited = set()
    visited.add((initial_indices, initial_wstimes))
    
    result = float('inf')
    
    while pq:
        time, indices, wstimes = heapq.heappop(pq)
        
        if time >= result:
            continue
        
        # Check if all projects are done
        all_done = True
        for i in range(j):
            if indices[i] < len(projects[i]):
                all_done = False
                break
        
        if all_done:
            result = time
            continue
        
        # Try to schedule each project's next step
        for proj_id in range(j):
            step_idx = indices[proj_id]
            if step_idx >= len(projects[proj_id]):
                continue
            
            ws, dur = projects[proj_id][step_idx]
            
            # Step can start when:
            # 1. Previous step of same project is done (time)
            # 2. Workstation is free (wstimes[ws])
            start_time = max(time, wstimes[ws])
            end_time = start_time + dur
            
            new_indices = list(indices)
            new_indices[proj_id] = step_idx + 1
            new_indices = tuple(new_indices)
            
            new_wstimes = list(wstimes)
            new_wstimes[ws] = end_time
            new_wstimes = tuple(new_wstimes)
            
            state = (new_indices, new_wstimes)
            if state not in visited:
                visited.add(state)
                heapq.heappush(pq, (end_time, new_indices, new_wstimes))
    
    print(result)

if __name__ == "__main__":
    solve()