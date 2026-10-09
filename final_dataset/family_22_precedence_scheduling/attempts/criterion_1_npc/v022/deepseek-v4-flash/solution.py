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
    
    # Kahn's algorithm
    earliest = [1] * n
    heap = []
    for i in range(n):
        if indeg[i] == 0:
            heapq.heappush(heap, (1, i))
    
    assigned_day = [0] * n
    day_count = [0] * (T + 1)
    processed = 0
    
    while heap:
        day, u = heapq.heappop(heap)
        # Find the earliest day >= day with capacity
        d = day
        while d <= T and day_count[d] >= M:
            d += 1
        if d > T:
            print("NO")
            return
        assigned_day[u] = d
        day_count[d] += 1
        processed += 1
        
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                heapq.heappush(heap, (d + 1, v))
    
    if processed != n:
        print("NO")
        return
    
    print("YES")
    print(" ".join(str(assigned_day[i]) for i in range(n)))

if __name__ == "__main__":
    solve()