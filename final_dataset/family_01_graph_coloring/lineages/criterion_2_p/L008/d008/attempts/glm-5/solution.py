import sys
from collections import deque

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr]); ptr += 1
    m = int(input[ptr]); ptr += 1
    
    adj = [[] for _ in range(n)]
    deg = [0] * n
    
    for _ in range(m):
        u = int(input[ptr]) - 1; ptr += 1
        v = int(input[ptr]) - 1; ptr += 1
        adj[u].append(v)
        adj[v].append(u)
        deg[u] += 1
        deg[v] += 1
    
    # Bipartite check: c[u] != c[v] for all edges
    color = [-1] * n
    q = deque()
    
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            q.append(i)
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
    
    # Check degree constraints: deg[u] must be even if color[u] == 0
    for u in range(n):
        if color[u] == 0 and deg[u] % 2 != 0:
            print("NO")
            return
    
    # Output lexicographically smallest: c[i] = 1 if color[i] == 0, else 2
    print("YES")
    print(' '.join(str(1 if color[i] == 0 else 2) for i in range(n)))

if __name__ == "__main__":
    sys.setrecursionlimit(300000)
    solve()