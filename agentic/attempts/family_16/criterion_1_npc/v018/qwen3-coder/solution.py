import sys
from collections import defaultdict

def solve():
    j, m = map(int, input().split())
    
    orders = []
    for _ in range(j):
        line = list(map(int, input().split()))
        o = line[0]
        phases = []
        for i in range(o):
            unit = line[1 + 2*i]
            duration = line[1 + 2*i + 1]
            phases.append((unit, duration))
        orders.append(phases)
    
    # For each fabrication unit, we track when it becomes free
    unit_free_time = [0] * (m + 1)  # 1-indexed
    
    # For each order, we track when it can start its next phase
    order_next_start = [0] * j
    
    # We simulate the process
    # Keep track of completed phases for each order
    completed_phases = [0] * j
    
    # Total number of phases
    total_phases = sum(len(order) for order in orders)
    finished_phases = 0
    
    while finished_phases < total_phases:
        # Find the next phase that can start
        best_order = -1
        best_phase = -1
        best_start_time = float('inf')
        
        for order_idx in range(j):
            if completed_phases[order_idx] < len(orders[order_idx]):
                phase_idx = completed_phases[order_idx]
                unit, duration = orders[order_idx][phase_idx]
                # This phase can start at max(order_next_start[order_idx], unit_free_time[unit])
                start_time = max(order_next_start[order_idx], unit_free_time[unit])
                if start_time < best_start_time:
                    best_start_time = start_time
                    best_order = order_idx
                    best_phase = phase_idx
        
        # Execute the best phase
        unit, duration = orders[best_order][best_phase]
        start_time = best_start_time
        end_time = start_time + duration
        
        # Update state
        unit_free_time[unit] = end_time
        order_next_start[best_order] = end_time
        completed_phases[best_order] += 1
        finished_phases += 1
    
    # The answer is the maximum time any unit is busy until
    result = max(unit_free_time)
    print(result)

solve()