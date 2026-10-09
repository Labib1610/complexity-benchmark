import sys
sys.setrecursionlimit(1000000)

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
    
    assignment = [0] * n
    
    def is_valid(v, color):
        for nb in adj[v]:
            if assignment[nb] == color:
                return False
        return True
    
    def dfs(v):
        if v == n:
            return True
        for color in [1, 2, 3]:
            if is_valid(v, color):
                assignment[v] = color
                if dfs(v + 1):
                    return True
                assignment[v] = 0
        return False
    
    if dfs(0):
        print("YES")
        print(' '.join(map(str, assignment)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()