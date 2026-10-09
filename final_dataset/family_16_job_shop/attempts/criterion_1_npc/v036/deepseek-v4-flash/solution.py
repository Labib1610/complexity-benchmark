import sys
import heapq

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    j = int(next(it))
    m = int(next(it))
    
    vessels = []
    for _ in range(j):
        p = int(next(it))
        phases = []
        for _ in range(p):
            fac = int(next(it)) - 1
            dur = int(next(it))
            phases.append((fac, dur))
        vessels.append(phases)
    
    # Each vessel: current phase index
    phase_idx = [0] * j
    # Machine availability time
    machine_free = [0] * m
    # Current time for each vessel (when it finished its last phase)
    vessel_time = [0] * j
    
    # Min-heap: (time, vessel_id)
    heap = []
    for v in range(j):
        if phase_idx[v] < len(vessels[v]):
            fac, dur = vessels[v][0]
            heapq.heappush(heap, (0, v))
    
    max_time = 0
    
    while heap:
        t, v = heapq.heappop(heap)
        if phase_idx[v] >= len(vessels[v]):
            continue
        fac, dur = vessels[v][phase_idx[v]]
        start_time = max(t, vessel_time[v], machine_free[fac])
        finish_time = start_time + dur
        machine_free[fac] = finish_time
        vessel_time[v] = finish_time
        max_time = max(max_time, finish_time)
        phase_idx[v] += 1
        if phase_idx[v] < len(vessels[v]):
            heapq.heappush(heap, (vessel_time[v], v))
    
    print(max_time)

if __name__ == "__main__":
    solve()