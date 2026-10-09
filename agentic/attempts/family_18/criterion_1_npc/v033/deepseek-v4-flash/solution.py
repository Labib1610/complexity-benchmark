import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    
    adj = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    best_perm = None
    best_cost = float('inf')
    
    # Try BFS ordering from each vertex as start
    for start in range(n):
        order = []
        visited = [False] * n
        q = deque([start])
        visited[start] = True
        while q:
            u = q.popleft()
            order.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        # If graph is disconnected, add remaining vertices
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                order.append(i)
        
        pos = [0] * n
        for idx, node in enumerate(order):
            pos[node] = idx + 1
        
        cost = 0
        for u, v in edges:
            cost += abs(pos[u] - pos[v])
            if cost > B:
                break
        if cost < best_cost:
            best_cost = cost
            best_perm = pos[:]
    
    if best_cost <= B:
        print("YES")
        print(" ".join(str(x) for x in best_perm))
    else:
        print("NO")

if __name__ == "__main__":
    solve()