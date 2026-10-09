import sys
from functools import lru_cache

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    m = int(next(it))
    
    orders = []
    for _ in range(j):
        o = int(next(it))
        phases = []
        for _ in range(o):
            unit = int(next(it)) - 1  # 0-indexed
            dur = int(next(it))
            phases.append((unit, dur))
        orders.append(phases)
    
    # Flatten all phases with order index and phase index
    all_phases = []
    for oi, order in enumerate(orders):
        for pi, (unit, dur) in enumerate(order):
            all_phases.append((oi, pi, unit, dur))
    
    n = len(all_phases)
    
    # Precompute successors in same order
    next_phase = {}
    for oi, order in enumerate(orders):
        for pi in range(len(order) - 1):
            next_phase[(oi, pi)] = (oi, pi + 1)
    
    # Precompute which phases use which unit
    unit_phases = [[] for _ in range(m)]
    for idx, (oi, pi, unit, dur) in enumerate(all_phases):
        unit_phases[unit].append(idx)
    
    # We'll do DFS with pruning: assign start times to phases in order of index
    # But we need to respect constraints.
    
    # Better: use a priority queue to simulate possible schedules (like branch and bound)
    # But since j <= 10, m <= 10, total phases <= 50, we can do a backtracking search
    # over start times, trying to minimize makespan.
    
    # We'll use a simple approach: binary search on makespan and check feasibility
    # using a constraint satisfaction search.
    
    total_duration = sum(dur for _, _, _, dur in all_phases)
    low = 0
    high = total_duration  # upper bound: run all sequentially
    
    # Feasibility check for a given makespan T
    def feasible(T):
        # We'll try to assign start times to all phases.
        # Use backtracking with ordering: choose phase with smallest possible start time.
        start_times = [None] * n
        # For each order, track last finish time
        order_finish = [0] * j
        # For each unit, track intervals of busy time
        unit_busy = [[] for _ in range(m)]  # list of (start, end)
        
        # Precompute phase index mapping
        phase_index = {}
        for idx, (oi, pi, unit, dur) in enumerate(all_phases):
            phase_index[(oi, pi)] = idx
        
        # Recursive assignment
        def backtrack(count):
            if count == n:
                return True
            # Choose next phase to assign: pick one with smallest possible start time
            best_idx = -1
            best_start = T + 1
            for idx, (oi, pi, unit, dur) in enumerate(all_phases):
                if start_times[idx] is not None:
                    continue
                # Earliest start: after previous phase in same order
                if pi == 0:
                    earliest = 0
                else:
                    prev_idx = phase_index[(oi, pi - 1)]
                    earliest = start_times[prev_idx] + orders[oi][pi - 1][1]
                # Also must be after last busy time on that unit
                for s, e in unit_busy[unit]:
                    if e > earliest:
                        earliest = e
                if earliest + dur > T:
                    continue
                if earliest < best_start:
                    best_start = earliest
                    best_idx = idx
            if best_idx == -1:
                return False
            # Try assigning best_idx at best_start
            oi, pi, unit, dur = all_phases[best_idx]
            start_times[best_idx] = best_start
            end = best_start + dur
            # Insert busy interval
            unit_busy[unit].append((best_start, end))
            unit_busy[unit].sort()
            if backtrack(count + 1):
                return True
            # Undo
            start_times[best_idx] = None
            unit_busy[unit].remove((best_start, end))
            return False
        
        return backtrack(0)
    
    # Binary search
    while low < high:
        mid = (low + high) // 2
        if feasible(mid):
            high = mid
        else:
            low = mid + 1
    print(low)

if __name__ == "__main__":
    solve()