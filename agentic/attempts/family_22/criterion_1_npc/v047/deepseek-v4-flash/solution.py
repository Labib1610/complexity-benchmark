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
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        indeg[v] += 1
    
    # Kahn's algorithm with day assignment
    heap = []
    for i in range(n):
        if indeg[i] == 0:
            heapq.heappush(heap, (1, i))  # (day, node)
    
    day_count = [0] * (T + 1)
    assigned = [0] * n
    processed = 0
    
    while heap:
        day, u = heapq.heappop(heap)
        if day > T:
            print("NO")
            return
        if day_count[day] >= M:
            # try next day
            day += 1
            if day > T:
                print("NO")
                return
        assigned[u] = day
        day_count[day] += 1
        processed += 1
        
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                heapq.heappush(heap, (day + 1, v))
    
    if processed != n:
        print("NO")
        return
    
    # Check capacity constraint for all days
    for d in range(1, T + 1):
        if day_count[d] > M:
            print("NO")
            return
    
    print("YES")
    print(" ".join(str(assigned[i]) for i in range(n)))

if __name__ == "__main__":
    solve()