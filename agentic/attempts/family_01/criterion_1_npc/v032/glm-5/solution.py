import sys
sys.setrecursionlimit(10000)

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
    
    def dfs(u, c):
        color[u] = c
        for v in adj[u]:
            if color[v] == 0:
                if not dfs(v, 3 - c):
                    return False
            elif color[v] == c:
                return False
        return True
    
    for i in range(n):
        if color[i] == 0:
            if not dfs(i, 1):
                print("NO")
                return
    
    result = []
    for i in range(n):
        result.append(str(color[i]))
    print("YES")
    print(" ".join(result))

solve()