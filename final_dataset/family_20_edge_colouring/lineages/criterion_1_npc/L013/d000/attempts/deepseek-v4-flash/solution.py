import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    edges = []
    for i in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # Check bipartiteness
    color = [-1] * n
    for start in range(n):
        if color[start] == -1:
            color[start] = 0
            q = deque([start])
            while q:
                u = q.popleft()
                for v, _ in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        q.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
    
    # Edge coloring
    edge_color = [0] * m
    for u in range(n):
        used = [False] * 4
        for v, idx in adj[u]:
            if edge_color[idx] != 0:
                used[edge_color[idx]] = True
        # Assign colors to uncolored edges
        for v, idx in adj[u]:
            if edge_color[idx] == 0:
                for c in range(1, 4):
                    if not used[c]:
                        edge_color[idx] = c
                        used[c] = True
                        break
    
    print("YES")
    print(" ".join(map(str, edge_color)))

if __name__ == "__main__":
    solve()