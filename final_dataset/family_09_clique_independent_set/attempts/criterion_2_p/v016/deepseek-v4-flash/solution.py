import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [-1] * n
    size = [0, 0]
    
    for i in range(n):
        if color[i] == -1:
            # BFS
            q = deque([i])
            color[i] = 0
            size[0] += 1
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        size[color[v]] += 1
                        q.append(v)
    
    # choose the partition with size >= k
    if max(size) < k:
        print("NO")
        return
    
    chosen_color = 0 if size[0] >= k else 1
    res = [str(i+1) for i in range(n) if color[i] == chosen_color][:k]
    print("YES")
    print(" ".join(res))

if __name__ == "__main__":
    solve()