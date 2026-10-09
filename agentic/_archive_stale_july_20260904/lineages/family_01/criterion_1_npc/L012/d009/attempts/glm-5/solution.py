import sys
sys.setrecursionlimit(10000)

def solve():
    data = sys.stdin.read().split()
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
    
    colors = [0] * n
    
    def is_valid(u, c):
        for v in adj[u]:
            if colors[v] == c:
                return False
        return True
    
    def dfs(u):
        if u == n:
            return True
        
        for c in range(1, 4):
            if is_valid(u, c):
                colors[u] = c
                if dfs(u + 1):
                    return True
                colors[u] = 0
        
        return False
    
    if dfs(0):
        print("YES")
        print(*(colors))
    else:
        print("NO")

if __name__ == "__main__":
    solve()