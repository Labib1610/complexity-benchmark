import sys
from heapq import heappush, heappop

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    j = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    orders = []
    for _ in range(j):
        o = int(data[idx]); idx += 1
        phases = []
        for _ in range(o):
            u = int(data[idx]); idx += 1
            d = int(data[idx]); idx += 1
            phases.append((u, d))
        orders.append(phases)
    
    # State: (time, order_index, phase_index, tuple of unit available times)
    # We process the earliest event first.
    start_state = (0, 0, 0, tuple([0] * (m + 1)))
    heap = [start_state]
    visited = {}
    
    total_phases = sum(len(o) for o in orders)
    
    while heap:
        time, oi, pi, units = heappop(heap)
        key = (oi, pi, units)
        if key in visited:
            continue
        visited[key] = time
        
        if oi == j:
            print(time)
            return
        
        order = orders[oi]
        if pi == len(order):
            # This order is done, move to next order
            new_state = (time, oi + 1, 0, units)
            heappush(heap, new_state)
        else:
            u, d = order[pi]
            # Can start when unit is free and previous phase of this order is done
            # Previous phase done time is tracked by 'time' (earliest this phase can start)
            start = max(time, units[u])
            end = start + d
            new_units = list(units)
            new_units[u] = end
            new_state = (end, oi, pi + 1, tuple(new_units))
            heappush(heap, new_state)
    
    # Should not reach here
    print(-1)

solve()