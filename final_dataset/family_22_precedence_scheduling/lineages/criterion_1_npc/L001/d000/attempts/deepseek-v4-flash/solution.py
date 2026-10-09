import sys
import heapq

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    M = int(next(it))
    T = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    indeg = [0] * n
    
    for _ in range(m):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        adj[a].append(b)
        indeg[b] += 1
    
    # min-heap of (earliest_possible_time, node)
    # We'll assign times greedily
    time_assigned = [0] * n
    # Initialize with indegree 0 nodes
    heap = []
    for i in range(n):
        if indeg[i] == 0:
            heapq.heappush(heap, (1, i))
    
    assigned_count = 0
    # Track how many assigned to each time slot
    slot_count = [0] * (T + 1)
    
    while heap:
        t, u = heapq.heappop(heap)
        # If this time slot is full, push to next available
        while t <= T and slot_count[t] >= M:
            t += 1
        if t > T:
            print("NO")
            return
        time_assigned[u] = t
        slot_count[t] += 1
        assigned_count += 1
        
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                # Earliest possible time for v is t+1
                heapq.heappush(heap, (t + 1, v))
    
    if assigned_count != n:
        print("NO")
        return
    
    print("YES")
    print(" ".join(str(x) for x in time_assigned))

if __name__ == "__main__":
    solve()