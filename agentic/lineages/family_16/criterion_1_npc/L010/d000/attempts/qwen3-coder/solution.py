from collections import deque
import sys

def solve():
    j, m = map(int, input().split())
    
    projects = []
    total_phases = 0
    for _ in range(j):
        line = list(map(int, input().split()))
        o = line[0]
        phases = []
        for i in range(o):
            facility = line[1 + 2*i]
            duration = line[1 + 2*i + 1]
            phases.append((facility, duration))
        projects.append(phases)
        total_phases += o
    
    # Binary search on the answer
    def can_finish_by_cycle(limit):
        # For each facility, we'll simulate which phases can be scheduled
        # We use a greedy approach: for each project, try to schedule its next phase
        # as early as possible given the constraints.
        
        # Keep track of when each facility is free
        facility_end_time = [0] * (m + 1)
        
        # For each project, keep track of which phase we're on and when it can start
        project_phase_idx = [0] * j
        project_earliest_start = [0] * j
        
        # Keep a list of projects that have unscheduled phases
        active_projects = set(range(j))
        
        while active_projects:
            # Find the project that can make progress earliest
            min_start_time = float('inf')
            next_project = -1
            
            for proj in active_projects:
                phase_idx = project_phase_idx[proj]
                if phase_idx >= len(projects[proj]):
                    active_projects.discard(proj)
                    continue
                
                facility, duration = projects[proj][phase_idx]
                # This phase can start at max(project_earliest_start[proj], facility_end_time[facility])
                start_time = max(project_earliest_start[proj], facility_end_time[facility])
                finish_time = start_time + duration
                
                if finish_time > limit:
                    return False
                
                if start_time < min_start_time:
                    min_start_time = start_time
                    next_project = proj
            
            if next_project == -1:
                break
                
            # Schedule the phase for next_project
            phase_idx = project_phase_idx[next_project]
            facility, duration = projects[next_project][phase_idx]
            start_time = max(project_earliest_start[next_project], facility_end_time[facility])
            finish_time = start_time + duration
            
            if finish_time > limit:
                return False
                
            facility_end_time[facility] = finish_time
            project_phase_idx[next_project] += 1
            
            # The next phase of this project can start at earliest at finish_time
            if project_phase_idx[next_project] < len(projects[next_project]):
                project_earliest_start[next_project] = finish_time
            else:
                active_projects.discard(next_project)
        
        return True
    
    # Binary search for the minimum cycle
    left, right = 0, 50 * 1000  # Max possible is 50 phases * 1000 duration
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        if can_finish_by_cycle(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    print(answer)

solve()