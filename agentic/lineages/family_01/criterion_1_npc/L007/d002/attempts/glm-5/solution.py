import sys
sys.setrecursionlimit(100000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [set() for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].add(v)
        adj[v].add(u)
    
    color = [0] * n
    
    def get_forbidden(u):
        forbidden = 0
        for v in adj[u]:
            if color[v] != 0:
                forbidden |= (1 << (color[v] - 1))
        return forbidden
    
    def dfs(u):
        if u == n:
            return True
        forbidden = get_forbidden(u)
        for c in range(1, 4):
            if not (forbidden & (1 << (c - 1))):
                color[u] = c
                if dfs(u + 1):
                    return True
                color[u] = 0
        return False
    
    if dfs(0):
        print("YES")
        print(' '.join(map(str, color)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()