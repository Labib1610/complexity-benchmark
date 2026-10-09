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
    
    # Min-heap of available tasks (by index for deterministic order)
    heap = []
    for i in range(n):
        if indeg[i] == 0:
            heapq.heappush(heap, i)
    
    week_assignment = [0] * n
    assigned_count = 0
    
    for week in range(1, T + 1):
        if assigned_count == n:
            break
        if not heap:
            print("NO")
            return
        
        # Take up to M tasks this week
        take = []
        for _ in range(min(M, len(heap))):
            u = heapq.heappop(heap)
            take.append(u)
            week_assignment[u] = week
            assigned_count += 1
        
        # After assigning, reduce indegrees
        for u in take:
            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    heapq.heappush(heap, v)
    
    if assigned_count != n:
        print("NO")
        return
    
    print("YES")
    print(" ".join(str(week_assignment[i]) for i in range(n)))

if __name__ == "__main__":
    solve()