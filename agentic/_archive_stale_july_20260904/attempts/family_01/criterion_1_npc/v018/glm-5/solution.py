import sys

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
    
    assignment = [0] * n
    
    def is_valid(u, color):
        for v in adj[u]:
            if assignment[v] == color:
                return False
        return True
    
    def dfs(u):
        for color in range(1, 4):
            if is_valid(u, color):
                assignment[u] = color
                if dfs(u + 1):
                    return True
                assignment[u] = 0
        return False
    
    if dfs(0):
        print("YES")
        print(*(assignment))
    else:
        print("NO")

if __name__ == '__main__':
    solve()