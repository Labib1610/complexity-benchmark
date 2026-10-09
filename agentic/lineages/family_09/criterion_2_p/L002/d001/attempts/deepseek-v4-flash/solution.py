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
    color_count = [0, 0]
    
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            color_count[0] += 1
            q = deque([i])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        color_count[color[v]] += 1
                        q.append(v)
    
    if color_count[0] >= k:
        chosen = [i+1 for i in range(n) if color[i] == 0][:k]
    elif color_count[1] >= k:
        chosen = [i+1 for i in range(n) if color[i] == 1][:k]
    else:
        print("NO")
        return
    
    print("YES")
    print(" ".join(map(str, chosen)))

if __name__ == "__main__":
    solve()