import sys
import heapq

def solve():
    input_data = sys.stdin.read().strip().split()
    idx = 0
    j = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    potions = []
    for _ in range(j):
        o = int(input_data[idx]); idx += 1
        phases = []
        for _ in range(o):
            focus = int(input_data[idx]); idx += 1
            dur = int(input_data[idx]); idx += 1
            phases.append((focus, dur))
        potions.append(phases)
    
    # Each potion has a current phase index
    phase_idx = [0] * j
    # Time when each potion is free to start next phase
    potion_free = [0] * j
    # Time when each focus is free
    focus_free = [0] * (m + 1)
    
    # Min-heap: (start_time, potion_id, phase_index)
    heap = []
    # Initialize with first phase of each potion
    for p in range(j):
        focus, dur = potions[p][0]
        heapq.heappush(heap, (0, p, 0))
    
    max_time = 0
    
    while heap:
        start, p, ph = heapq.heappop(heap)
        focus, dur = potions[p][ph]
        # Start time must be max(potion_free[p], focus_free[focus], start)
        actual_start = max(start, potion_free[p], focus_free[focus])
        finish = actual_start + dur
        max_time = max(max_time, finish)
        # Update resources
        potion_free[p] = finish
        focus_free[focus] = finish
        # Schedule next phase of this potion if any
        if ph + 1 < len(potions[p]):
            heapq.heappush(heap, (finish, p, ph + 1))
    
    print(max_time)

if __name__ == "__main__":
    solve()