import sys
from collections import defaultdict

def solve():
    j, m = map(int, input().split())
    
    compositions = []
    for _ in range(j):
        line = list(map(int, input().split()))
        o = line[0]
        segments = []
        for i in range(o):
            instrument = line[1 + 2*i]
            duration = line[1 + 2*i + 1]
            segments.append((instrument, duration))
        compositions.append(segments)
    
    # Binary search on the answer
    def can_finish_in_time(limit):
        # For each instrument, we have a list of time intervals when it's busy
        # We'll use backtracking with pruning to check if we can schedule everything
        
        # Try all possible orderings of compositions using recursive backtracking
        def backtrack(comp_idx, instrument_end_times):
            if comp_idx == j:
                return True
                
            # Try to schedule composition comp_idx
            comp = compositions[comp_idx]
            
            # Generate all valid start times for this composition
            def try_schedule_segment(seg_idx, current_time, inst_end_times):
                if seg_idx == len(comp):
                    # Successfully scheduled this composition
                    return backtrack(comp_idx + 1, inst_end_times)
                
                instrument, duration = comp[seg_idx]
                start_time = max(current_time, inst_end_times[instrument])
                end_time = start_time + duration
                
                if end_time > limit:
                    return False
                    
                # Update instrument end time
                new_inst_end_times = inst_end_times.copy()
                new_inst_end_times[instrument] = end_time
                
                # Recurse to next segment
                return try_schedule_segment(seg_idx + 1, end_time, new_inst_end_times)
            
            # Start scheduling this composition from time 0
            return try_schedule_segment(0, 0, instrument_end_times)
        
        initial_times = defaultdict(int)
        return backtrack(0, initial_times)
    
    # Binary search for the minimum time
    left, right = 0, 50000  # Upper bound: 50 segments * 1000 max duration
    result = right
    
    while left <= right:
        mid = (left + right) // 2
        if can_finish_in_time(mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    
    print(result)

solve()