import sys
sys.setrecursionlimit(100000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * n
    
    def dfs(u):
        for v in adj[u]:
            if color[v] == 0:
                color[v] = 4 - color[u]
                if not dfs(v):
                    return False
            elif color[v] == color[u]:
                return False
        return True
    
    for i in range(n):
        if color[i] == 0:
            color[i] = 1
            if not dfs(i):
                print("NO")
                return
    
    print("YES")
    print(' '.join(map(str, color)))

solve()