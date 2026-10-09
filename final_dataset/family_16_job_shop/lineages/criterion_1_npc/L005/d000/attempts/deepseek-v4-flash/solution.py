import sys
import heapq

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    m = int(next(it))
    
    petitions = []
    for _ in range(j):
        o = int(next(it))
        steps = []
        for _ in range(o):
            mag = int(next(it)) - 1
            hrs = int(next(it))
            steps.append((mag, hrs))
        petitions.append(steps)
    
    # For each petition, track next step index
    next_step = [0] * j
    # For each magistrate, track when they become free
    mag_free = [0] * m
    # For each petition, track when it becomes available for next step
    pet_free = [0] * j
    
    # Min-heap of events: (time, petition_index)
    # We'll push initial availability of each petition at time 0
    heap = []
    for p in range(j):
        heapq.heappush(heap, (0, p))
    
    max_time = 0
    
    while heap:
        t, p = heapq.heappop(heap)
        if next_step[p] >= len(petitions[p]):
            continue
        mag, hrs = petitions[p][next_step[p]]
        # Start time is max(petition free, magistrate free)
        start = max(t, mag_free[mag])
        finish = start + hrs
        # Update magistrate free time
        mag_free[mag] = finish
        # Update petition free time
        pet_free[p] = finish
        # Move to next step
        next_step[p] += 1
        max_time = max(max_time, finish)
        if next_step[p] < len(petitions[p]):
            heapq.heappush(heap, (finish, p))
    
    print(max_time)

if __name__ == "__main__":
    solve()