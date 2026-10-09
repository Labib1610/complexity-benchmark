import sys
from heapq import heappush, heappop

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    j = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    jobs = []
    for _ in range(j):
        o = int(data[idx]); idx += 1
        steps = []
        for _ in range(o):
            s = int(data[idx]); idx += 1
            d = int(data[idx]); idx += 1
            steps.append((s, d))
        jobs.append(steps)
    
    # State: (time, job_index, step_index, station_free_times tuple)
    # Use list for station_free_times for mutability, but tuple for heap key
    # We'll store station_free_times as a tuple in the state
    
    initial_stations = tuple([0] * (m + 1))  # index 1..m
    # job progress: tuple of step indices for each job
    initial_progress = tuple([0] * j)
    
    # State: (current_time, station_free_times, job_progress)
    # We want to minimize completion time
    
    # Use Dijkstra-like approach
    # State key: (station_free_times, job_progress)
    # Value: minimum time to reach this state
    
    import heapq
    
    start_state = (0, initial_stations, initial_progress)
    heap = [start_state]
    visited = {}
    visited[(initial_stations, initial_progress)] = 0
    
    best = float('inf')
    
    while heap:
        time, stations, progress = heappop(heap)
        
        if time >= best:
            continue
            
        key = (stations, progress)
        if visited.get(key, float('inf')) < time:
            continue
        
        # Check if all jobs complete
        all_done = True
        for ji in range(j):
            if progress[ji] < len(jobs[ji]):
                all_done = False
                break
        if all_done:
            best = min(best, time)
            continue
        
        # Find all jobs that can make a move (next step's station is free at current time)
        # A job can move if: progress[ji] < len(jobs[ji]) and stations[station] <= time
        # But we also need to handle the case where no job can move right now -> advance time
        
        can_move = False
        for ji in range(j):
            if progress[ji] < len(jobs[ji]):
                station, duration = jobs[ji][progress[ji]]
                if stations[station] <= time:
                    can_move = True
                    # Execute this step
                    new_stations = list(stations)
                    new_stations[station] = time + duration
                    new_stations = tuple(new_stations)
                    new_progress = list(progress)
                    new_progress[ji] += 1
                    new_progress = tuple(new_progress)
                    new_time = time  # time doesn't advance, we just scheduled a step
                    new_key = (new_stations, new_progress)
                    if new_key not in visited or visited[new_key] > new_time:
                        visited[new_key] = new_time
                        heappush(heap, (new_time, new_stations, new_progress))
        
        if not can_move:
            # Advance time to the next station free time
            min_free = float('inf')
            for ji in range(j):
                if progress[ji] < len(jobs[ji]):
                    station, _ = jobs[ji][progress[ji]]
                    if stations[station] > time:
                        min_free = min(min_free, stations[station])
            if min_free < float('inf'):
                new_key = (stations, progress)
                if new_key not in visited or visited[new_key] > min_free:
                    visited[new_key] = min_free
                    heappush(heap, (min_free, stations, progress))
    
    print(best)

solve()