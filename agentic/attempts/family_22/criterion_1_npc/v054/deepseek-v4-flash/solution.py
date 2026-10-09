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
    
    # earliest possible cycle for each node
    earliest = [1] * n
    # count of steps per cycle
    cycle_count = {}
    
    # min-heap: (earliest_cycle, node)
    heap = []
    for i in range(n):
        if indeg[i] == 0:
            heapq.heappush(heap, (1, i))
    
    assigned = [0] * n
    processed = 0
    
    while heap:
        cyc, u = heapq.heappop(heap)
        # find actual cycle: must be >= cyc and capacity < M
        while cycle_count.get(cyc, 0) >= M:
            cyc += 1
        if cyc > T:
            print("NO")
            return
        assigned[u] = cyc
        cycle_count[cyc] = cycle_count.get(cyc, 0) + 1
        processed += 1
        
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                # earliest cycle for v is at least assigned[u] + 1
                heapq.heappush(heap, (assigned[u] + 1, v))
    
    if processed != n:
        print("NO")
        return
    
    print("YES")
    print(" ".join(str(x) for x in assigned))

if __name__ == "__main__":
    solve()