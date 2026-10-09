import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    color = [-1] * (n + 1)
    camps = [[], []]
    
    for i in range(1, n + 1):
        if color[i] == -1:
            color[i] = 0
            camps[0].append(i)
            q = deque([i])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        camps[color[v]].append(v)
                        q.append(v)
    
    # pick the larger camp
    if len(camps[0]) >= len(camps[1]):
        big = camps[0]
    else:
        big = camps[1]
    
    if len(big) < k:
        print("NO")
        return
    
    print("YES")
    print(" ".join(map(str, big[:k])))

if __name__ == "__main__":
    solve()