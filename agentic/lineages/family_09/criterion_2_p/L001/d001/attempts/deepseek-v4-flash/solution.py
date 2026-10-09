import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    color = [-1] * (n+1)
    camp_sizes = [0, 0]  # camp 0 and camp 1
    
    for i in range(1, n+1):
        if color[i] == -1:
            # BFS to color component
            q = deque([i])
            color[i] = 0
            camp_sizes[0] += 1
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        camp_sizes[color[v]] += 1
                        q.append(v)
                    elif color[v] == color[u]:
                        # Should not happen due to bipartite guarantee
                        pass
    
    if camp_sizes[0] >= k:
        group = [str(u) for u in range(1, n+1) if color[u] == 0][:k]
        print("YES")
        print(" ".join(group))
    elif camp_sizes[1] >= k:
        group = [str(u) for u in range(1, n+1) if color[u] == 1][:k]
        print("YES")
        print(" ".join(group))
    else:
        print("NO")

if __name__ == "__main__":
    solve()