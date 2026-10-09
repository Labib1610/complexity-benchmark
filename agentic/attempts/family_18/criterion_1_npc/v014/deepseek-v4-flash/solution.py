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
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # BFS/DFS layout
    pos = [-1] * n
    pos[0] = 0
    next_slot = 1
    queue = deque([0])
    visited = [False] * n
    visited[0] = True
    
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                pos[v] = next_slot
                next_slot += 1
                queue.append(v)
    
    # Assign remaining unvisited nodes (if graph disconnected)
    for i in range(n):
        if pos[i] == -1:
            pos[i] = next_slot
            next_slot += 1
    
    # Compute total wire length
    total = 0
    for u in range(n):
        for v in adj[u]:
            if u < v:
                total += abs(pos[u] - pos[v])
    
    if total <= B:
        print("YES")
        print(" ".join(str(p + 1) for p in pos))
    else:
        print("NO")

if __name__ == "__main__":
    solve()