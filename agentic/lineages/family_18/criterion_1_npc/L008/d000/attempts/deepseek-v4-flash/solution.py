import sys
from heapq import heappush, heappop

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    placed = [False] * n
    pos = [0] * n
    order = []
    
    # Start with vertex 0
    placed[0] = True
    pos[0] = 0
    order.append(0)
    
    # For each next position, pick the unplaced vertex with minimal cost increase
    for idx in range(1, n):
        best_vertex = -1
        best_cost = float('inf')
        for v in range(n):
            if not placed[v]:
                cost = 0
                for u in adj[v]:
                    if placed[u]:
                        cost += abs(idx - pos[u])
                if cost < best_cost:
                    best_cost = cost
                    best_vertex = v
        placed[best_vertex] = True
        pos[best_vertex] = idx
        order.append(best_vertex)
    
    # Compute total cost
    total_cost = 0
    for u in range(n):
        for v in adj[u]:
            if u < v:
                total_cost += abs(pos[u] - pos[v])
    
    if total_cost <= B:
        print("YES")
        # Output phase for each step (1-indexed)
        phase = [0] * n
        for i, v in enumerate(order):
            phase[v] = i + 1
        print(" ".join(str(phase[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()