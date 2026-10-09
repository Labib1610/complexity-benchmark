import sys
from collections import deque

def solve():
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    m = int(data[1])
    
    idx = 2
    projects = []
    
    for _ in range(j):
        o = int(data[idx])
        idx += 1
        phases = []
        for _ in range(o):
            facility = int(data[idx])
            duration = int(data[idx + 1])
            phases.append((facility, duration))
            idx += 2
        projects.append(phases)
    
    # Binary search on the answer
    def can_finish_by_cycle(limit):
        # For each facility, we'll simulate the schedule
        # We'll try to assign phases to facilities without exceeding the limit
        
        # This is a complex constraint satisfaction problem
        # We'll use a greedy approach with backtracking simulation
        
        # Let's model this as a scheduling problem with precedence constraints
        # We can use a timeline approach or constraint programming
        
        # Simpler approach: Try to build a valid schedule up to 'limit' cycles
        # For each cycle from 1 to limit, decide what phases can start
        
        # Let's track for each project:
        # - which phase it's currently at
        # - when that phase can start (depends on previous phase finish)
        
        # facility_end_times[f] = earliest time facility f is free
        facility_end_times = [0] * (m + 1)
        
        # project_phase_start[proj_idx] = earliest time project proj_idx can start its current phase
        project_phase_start = [0] * j
        
        # current_phase[proj_idx] = index of current phase for project proj_idx
        current_phase = [0] * j
        
        # Make a copy of projects data for simulation
        # We need to be able to "undo" choices, so let's do a greedy simulation
        
        # Actually, let's think differently:
        # At each time step, see what can start
        # But this might be too slow
        
        # Better: Event-driven simulation
        # Events are "phase starts" and "phase ends"
        
        # Even better for binary search: Given a limit, check if feasible
        # This is essentially a resource-constrained project scheduling problem
        
        # Simplified greedy check:
        # We'll simulate forward in time, tracking what can be scheduled
        
        # Reset state for this check
        facility_end_times = [0] * (m + 1)
        project_phase_start = [0] * j
        current_phase = [0] * j
        
        # Total number of phases
        total_phases = sum(len(proj) for proj in projects)
        completed_phases = 0
        
        # For simplicity in this constrained problem, let's do a greedy simulation
        # At each step, try to schedule any phase that can start now
        
        time = 0
        while completed_phases < total_phases and time <= limit:
            # Check if all projects are done
            if all(current_phase[p] == len(projects[p]) for p in range(j)):
                return True
                
            progress_made = False
            
            # Try to start phases at current time
            for proj_idx in range(j):
                if current_phase[proj_idx] >= len(projects[proj_idx]):
                    continue
                    
                # Can we start this phase?
                phase_facility, phase_duration = projects[proj_idx][current_phase[proj_idx]]
                
                # Phase can start only if:
                # 1. Previous phase of this project is finished
                # 2. Facility is free at this time
                
                earliest_start = project_phase_start[proj_idx]
                
                if time >= earliest_start:  # Project can start this phase
                    if time >= facility_end_times[phase_facility]:  # Facility is free
                        # Schedule this phase
                        facility_end_times[phase_facility] = time + phase_duration
                        project_phase_start[proj_idx] = time + phase_duration
                        current_phase[proj_idx] += 1
                        completed_phases += 1
                        progress_made = True
            
            # If no progress, advance time
            if not progress_made:
                # Find next event time
                next_event_time = limit + 1
                
                for proj_idx in range(j):
                    if current_phase[proj_idx] < len(projects[proj_idx]):
                        earliest_start = project_phase_start[proj_idx]
                        if earliest_start > time:
                            next_event_time = min(next_event_time, earliest_start)
                
                for f in range(1, m + 1):
                    if facility_end_times[f] > time:
                        next_event_time = min(next_event_time, facility_end_times[f])
                
                if next_event_time > limit:
                    break
                    
                time = next_event_time
            else:
                # Made progress, continue at same time in case more can be scheduled
                pass
        
        # Check if all projects are completed within limit
        return all(current_phase[p] == len(projects[p]) for p in range(j)) and time <= limit
    
    # Binary search on the minimum completion time
    left, right = 0, 50 * 1000  # Max possible time
    result = right
    
    while left <= right:
        mid = (left + right) // 2
        if can_finish_by_cycle(mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
            
    print(result)

solve()