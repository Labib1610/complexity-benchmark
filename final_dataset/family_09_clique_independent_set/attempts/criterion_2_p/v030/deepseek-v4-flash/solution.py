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
    side0 = []
    side1 = []
    
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            side0.append(i)
            q = deque([i])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        if color[v] == 0:
                            side0.append(v)
                        else:
                            side1.append(v)
                        q.append(v)
    
    if len(side0) >= len(side1):
        big = side0
    else:
        big = side1
    
    if k > len(big):
        print("NO")
    else:
        print("YES")
        print(" ".join(str(x+1) for x in big[:k]))

if __name__ == "__main__":
    solve()