import sys
import random
from collections import deque

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    
    edges = []
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
    
    def cost(perm):
        pos = [0]*n
        for i, p in enumerate(perm):
            pos[p] = i
        total = 0
        for u, v in edges:
            total += abs(pos[u] - pos[v])
            if total > B:
                return total
        return total
    
    # Try natural order
    perm = list(range(n))
    if cost(perm) <= B:
        print("YES")
        print(" ".join(str(x+1) for x in perm))
        return
    
    # Try degree-based: place high degree near center
    deg = [len(adj[i]) for i in range(n)]
    order = sorted(range(n), key=lambda x: -deg[x])
    perm = [0]*n
    left = 0
    right = n-1
    # Place high degree nodes in middle
    for node in order:
        if left <= right:
            if left <= n-1-right:
                perm[left] = node
                left += 1
            else:
                perm[right] = node
                right -= 1
    if cost(perm) <= B:
        print("YES")
        print(" ".join(str(x+1) for x in perm))
        return
    
    # Try BFS from highest degree node
    start = max(range(n), key=lambda x: deg[x])
    visited = [False]*n
    q = deque([start])
    visited[start] = True
    bfs_order = []
    while q:
        u = q.popleft()
        bfs_order.append(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
    # Add any unvisited (shouldn't happen if connected, but just in case)
    for i in range(n):
        if not visited[i]:
            bfs_order.append(i)
    perm = bfs_order
    if cost(perm) <= B:
        print("YES")
        print(" ".join(str(x+1) for x in perm))
        return
    
    # Try random permutations (limited attempts)
    random.seed(0)
    for _ in range(200):
        perm = list(range(n))
        random.shuffle(perm)
        if cost(perm) <= B:
            print("YES")
            print(" ".join(str(x+1) for x in perm))
            return
    
    print("NO")

if __name__ == "__main__":
    solve()