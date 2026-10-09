import sys
import heapq

def solve():
    input_data = sys.stdin.read().strip().split()
    it = iter(input_data)
    j = int(next(it))
    m = int(next(it))
    
    queries = []
    for _ in range(j):
        o = int(next(it))
        steps = []
        for _ in range(o):
            r = int(next(it)) - 1
            d = int(next(it))
            steps.append((r, d))
        queries.append(steps)
    
    # State: (time, tuple of next step indices, tuple of resource availability)
    # We'll use Dijkstra-like search to minimize finish time.
    
    start_state = (0, tuple([0]*j), tuple([0]*m))
    # priority queue: (current_time, next_step_indices, resource_avail)
    pq = []
    heapq.heappush(pq, start_state)
    
    visited = set()
    
    while pq:
        time, pos, avail = heapq.heappop(pq)
        if pos in visited:
            continue
        visited.add(pos)
        
        # Check if all queries done
        if all(p == len(queries[i]) for i, p in enumerate(pos)):
            print(time)
            return
        
        # Try to schedule next step of each query
        for qi in range(j):
            pi = pos[qi]
            if pi < len(queries[qi]):
                r, d = queries[qi][pi]
                start_time = max(time, avail[r])
                finish_time = start_time + d
                new_pos = list(pos)
                new_pos[qi] += 1
                new_avail = list(avail)
                new_avail[r] = finish_time
                new_state = (finish_time, tuple(new_pos), tuple(new_avail))
                heapq.heappush(pq, new_state)
    
    # Should never reach here
    print(-1)

if __name__ == "__main__":
    solve()