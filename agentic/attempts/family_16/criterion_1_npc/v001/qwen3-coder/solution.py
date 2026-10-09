import sys
from collections import deque

def solve():
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    j = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    
    projects = []
    for _ in range(j):
        o = int(data[idx])
        idx += 1
        steps = []
        for _ in range(o):
            workstation = int(data[idx])
            idx += 1
            duration = int(data[idx])
            idx += 1
            steps.append((workstation, duration))
        projects.append(steps)
    
    # We'll use backtracking with pruning
    # For each project, we need to track when each step can start
    # State: for each project, what step index it's on, and when it can start that step
    # For each workstation, track when it becomes free
    
    # This is a complex scheduling problem - we can model it as a state space search
    
    # Let's try a different approach: simulate the process
    # We'll keep track of:
    # - For each project, which step it's currently on
    # - For each workstation, when it will be free
    # - For each project, when its current step can start (depends on previous step finish time)
    
    # Initialize
    workstation_free_time = [0] * (m + 1)  # 1-indexed
    project_step_start_time = [0] * j     # When each project can start its current step
    project_current_step = [0] * j         # Current step index for each project
    project_finish_time = [0] * j          # When each project finishes completely
    
    # Precompute step dependencies: when each step can start based on previous step
    project_step_ready_time = [0] * j      # For current step of each project
    
    # We'll simulate the process in chronological order
    # At each time, check which steps can start and assign them to workstations
    
    # Better approach: Use a priority queue simulation
    import heapq
    
    # Event queue: (time, event_type, project_id, step_id)
    # event_type: 0 = step ready to start, 1 = step finished
    events = []
    
    # Initially, all projects can start their first step at time 0
    for p in range(j):
        if projects[p]:  # If project has steps
            heapq.heappush(events, (0, 0, p, 0))  # time=0, start_step, project_p, step_0
    
    workstation_free = [0] * (m + 1)  # When each workstation is free
    project_step_finish = [[0] * len(projects[p]) for p in range(j)]  # When each step finishes
    
    while events:
        time, event_type, p, s = heapq.heappop(events)
        
        if event_type == 0:  # Step is ready to start
            workstation, duration = projects[p][s]
            # Check if workstation is free
            if workstation_free[workstation] <= time:
                # Start the step now
                start_time = time
                finish_time = start_time + duration
                workstation_free[workstation] = finish_time
                project_step_finish[p][s] = finish_time
                
                # Schedule finish event
                heapq.heappush(events, (finish_time, 1, p, s))
                
                # If there's a next step, schedule it to be ready
                if s + 1 < len(projects[p]):
                    # Next step can start when this one finishes
                    heapq.heappush(events, (finish_time, 0, p, s + 1))
                else:
                    # Project finished
                    project_finish_time[p] = finish_time
            else:
                # Workstation busy, wait until it's free
                # Re-schedule this event for when workstation is free
                heapq.heappush(events, (workstation_free[workstation], 0, p, s))
        # event_type == 1 means step finished, but we handle that implicitly above
    
    print(max(project_finish_time))

def solve_optimized():
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    j = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    
    projects = []
    for _ in range(j):
        o = int(data[idx])
        idx += 1
        steps = []
        for _ in range(o):
            workstation = int(data[idx])
            idx += 1
            duration = int(data[idx])
            idx += 1
            steps.append((workstation, duration))
        projects.append(steps)
    
    # Use backtracking with memoization
    # State: (project_positions, workstation_end_times)
    from functools import lru_cache
    
    # But state space might be too large. Let's think differently.
    
    # Simulation approach with priority queue
    import heapq
    
    # For each workstation, when it will be free
    workstation_end = [0] * (m + 1)
    
    # For each project, track completion of steps
    # project_step_end[p][s] = when step s of project p ends
    project_step_end = [ [0] * len(proj) for proj in projects ]
    
    # Events: (time, type, project, step)
    # type: 0 = step can start, 1 = step ends
    heap = []
    
    # Initially, all projects can start step 0 at time 0
    for p in range(j):
        if projects[p]:
            heapq.heappush(heap, (0, 0, p, 0))
    
    max_time = 0
    
    while heap:
        time, typ, p, s = heapq.heappop(heap)
        max_time = max(max_time, time)
        
        if typ == 0:  # Step can start
            ws, dur = projects[p][s]
            # When can this step actually start?
            start_time = max(time, workstation_end[ws])
            end_time = start_time + dur
            
            workstation_end[ws] = end_time
            project_step_end[p][s] = end_time
            
            # Add finish event
            heapq.heappush(heap, (end_time, 1, p, s))
            
            # If there's a next step, it can start when this one finishes
            if s + 1 < len(projects[p]):
                heapq.heappush(heap, (end_time, 0, p, s + 1))
        # typ == 1: step finished, nothing more to do explicitly
        
    print(max(workstation_end))

# The above simulation has issues. Let me re-think.

def solve_correct():
    import sys
    import heapq
    
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    j = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    
    projects = []
    for _ in range(j):
        o = int(data[idx])
        idx += 1
        steps = []
        for _ in range(o):
            workstation = int(data[idx])
            idx += 1
            duration = int(data[idx])
            idx += 1
            steps.append((workstation - 1, duration))  # Convert to 0-indexed
        projects.append(steps)
    
    # Simulation
    # workstation_end[i] = when workstation i becomes free
    workstation_end = [0] * m
    
    # project_step_end[p][s] = when step s of project p ends
    project_step_end = []
    for proj in projects:
        project_step_end.append([0] * len(proj))
    
    # Priority queue of events: (time, event_type, project_id, step_id)
    # event_type: 0 = step ready to start, 1 = step finished
    pq = []
    
    # Initially, step 0 of each project is ready at time 0
    for p in range(j):
        if projects[p]:
            heapq.heappush(pq, (0, 0, p, 0))
    
    while pq:
        time, event_type, p, s = heapq.heappop(pq)
        
        if event_type == 0:  # Step ready to start
            workstation, duration = projects[p][s]
            
            # Step can start at max(current time, when workstation is free)
            start_time = max(time, workstation_end[workstation])
            end_time = start_time + duration
            
            # Update workstation and step end times
            workstation_end[workstation] = end_time
            project_step_end[p][s] = end_time
            
            # Schedule step finish event
            heapq.heappush(pq, (end_time, 1, p, s))
            
            # If there's a next step in this project, it becomes ready when this step finishes
            if s + 1 < len(projects[p]):
                heapq.heappush(pq, (end_time, 0, p, s + 1))
            # No else clause needed - project completion is tracked by max of all workstation_end times
    
    # The answer is when all workstations are free (i.e., all work is done)
    print(max(workstation_end))

solve_correct()