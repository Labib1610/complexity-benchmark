import sys
import heapq

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    m = int(next(it))
    
    compositions = []
    for _ in range(j):
        o = int(next(it))
        segments = []
        for _ in range(o):
            inst = int(next(it))
            dur = int(next(it))
            segments.append((inst, dur))
        compositions.append(segments)
    
    # State: (current_segment_index for each composition)
    # We track the earliest finish time for each composition at current segment
    # and the earliest available time for each instrument
    
    # Priority queue: (time, composition_finish_times tuple, instrument_available_times tuple, segment_indices tuple)
    # But this is too expensive. Instead, use Dijkstra-like approach.
    
    # State: tuple of (finish_time[i] for each i, segment_idx[i] for each i, instrument_available[m])
    # Too many dimensions. Let's think differently.
    
    # For each composition i, we track:
    # - segment_idx[i]: which segment we're on
    # - finish_time[i]: when composition i finishes its current segment
    
    # For each instrument k, we track:
    # - available[k]: when instrument k becomes available
    
    # Initial state
    init_finish = tuple(0 for _ in range(j))
    init_seg_idx = tuple(0 for _ in range(j))
    init_instrument = tuple(0 for _ in range(m))
    
    # Priority queue: (max_finish_time, finish_times, seg_indices, instrument_times)
    # We want to minimize the max finish time when all segments are done
    
    visited = {}
    pq = []
    heapq.heappush(pq, (0, init_finish, init_seg_idx, init_instrument))
    
    while pq:
        max_finish, finish_times, seg_indices, instrument_times = heapq.heappop(pq)
        
        # Check if all compositions are done
        all_done = True
        for i in range(j):
            if seg_indices[i] < len(compositions[i]):
                all_done = False
                break
        if all_done:
            print(max_finish)
            return
        
        state = (finish_times, seg_indices, instrument_times)
        if state in visited:
            continue
        visited[state] = True
        
        # Try to advance each composition
        for comp_idx in range(j):
            seg_idx = seg_indices[comp_idx]
            if seg_idx >= len(compositions[comp_idx]):
                continue  # This composition is done
            
            inst, dur = compositions[comp_idx][seg_idx]
            
            # This segment can start at max(finish_times[comp_idx], instrument_times[inst-1])
            start_time = max(finish_times[comp_idx], instrument_times[inst-1])
            end_time = start_time + dur
            
            # Create new state
            new_finish = list(finish_times)
            new_finish[comp_idx] = end_time
            
            new_seg_idx = list(seg_indices)
            new_seg_idx[comp_idx] += 1
            
            new_instrument = list(instrument_times)
            new_instrument[inst-1] = end_time
            
            new_finish_tuple = tuple(new_finish)
            new_seg_idx_tuple = tuple(new_seg_idx)
            new_instrument_tuple = tuple(new_instrument)
            
            new_max_finish = max(max_finish, end_time)
            
            new_state = (new_finish_tuple, new_seg_idx_tuple, new_instrument_tuple)
            if new_state not in visited:
                heapq.heappush(pq, (new_max_finish, new_finish_tuple, new_seg_idx_tuple, new_instrument_tuple))

solve()