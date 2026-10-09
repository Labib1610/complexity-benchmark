import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    terminals = set(map(int, input().split()))
    
    adj = [[] for _ in range(n+1)]
    total_weight = 0
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        total_weight += w

    deg = [len(adj[i]) for i in range(n+1)]
    removed = [False]*(n+1)
    q = deque()
    for i in range(1, n+1):
        if deg[i] == 1 and i not in terminals:
            q.append(i)
    
    removed_weight = 0
    while q:
        node = q.popleft()
        if removed[node]:
            continue
        removed[node] = True
        # This node was not a terminal, so it can be removed
        for nb, w in adj[node]:
            if not removed[nb]:
                removed_weight += w
                deg[nb] -= 1
                if deg[nb] == 1 and nb not in terminals:
                    q.append(nb)
    
    print(total_weight - removed_weight)

if __name__ == "__main__":
    solve()