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
    
    adj = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)
    
    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)
        indeg[b] += 1
    
    # earliest day each node can be scheduled
    earliest = [1] * (n + 1)
    # min-heap: (earliest_day, node)
    heap = []
    for i in range(1, n + 1):
        if indeg[i] == 0:
            heapq.heappush(heap, (earliest[i], i))
    
    day_count = [0] * (T + 1)
    result = [0] * (n + 1)
    scheduled = 0
    
    while heap:
        day, u = heapq.heappop(heap)
        # find the actual day to place u
        d = day
        while d <= T and day_count[d] >= M:
            d += 1
        if d > T:
            print("NO")
            return
        result[u] = d
        day_count[d] += 1
        scheduled += 1
        
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                earliest[v] = max(earliest[v], d + 1)
                heapq.heappush(heap, (earliest[v], v))
    
    if scheduled != n:
        print("NO")
        return
    
    print("YES")
    print(" ".join(str(result[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()