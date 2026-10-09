import heapq
from collections import defaultdict

def solve():
    j, m = map(int, input().split())
    
    vessels = []
    for _ in range(j):
        line = list(map(int, input().split()))
        p = line[0]
        phases = []
        for i in range(p):
            facility = line[1 + 2*i]
            duration = line[1 + 2*i + 1]
            phases.append((facility, duration))
        vessels.append(phases)
    
    # For each vessel, track which phase it's on and when it can start that phase
    # For each facility, track when it becomes free
    
    # vessel_status[v] = (current_phase_index, earliest_start_time_for_current_phase)
    vessel_status = [(0, 0) for _ in range(j)]
    
    # facility_free_time[f] = time when facility f becomes free
    facility_free_time = [0] * (m + 1)  # 1-indexed
    
    # Event queue: (time, event_type, vessel_id)
    # event_type: 0 = vessel finishes a phase and can start next, 1 = facility becomes free
    events = []
    
    # Initialize: all vessels can start their first phase at time 0
    for v in range(j):
        if len(vessels[v]) > 0:
            heapq.heappush(events, (0, 0, v))
    
    completed_vessels = 0
    current_time = 0
    
    while completed_vessels < j:
        # Process all events at the current time
        while events and events[0][0] <= current_time:
            time, event_type, id = heapq.heappop(events)
            
            if event_type == 0:  # Vessel can start next phase
                v = id
                phase_idx, _ = vessel_status[v]
                if phase_idx >= len(vessels[v]):
                    completed_vessels += 1
                    continue
                
                facility, duration = vessels[v][phase_idx]
                start_time = max(current_time, facility_free_time[facility])
                finish_time = start_time + duration
                
                # Update when facility will be free
                facility_free_time[facility] = finish_time
                
                # Update vessel status
                vessel_status[v] = (phase_idx + 1, finish_time)
                
                # Schedule event for when vessel finishes this phase
                heapq.heappush(events, (finish_time, 0, v))
                
                current_time = max(current_time, start_time)
        
        # Advance time to next event
        if events:
            current_time = events[0][0]
        else:
            break
    
    print(current_time)

solve()