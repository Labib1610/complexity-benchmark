import sys

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
    
    assignment = [0] * n
    
    def is_safe(node, color):
        for neighbor in adj[node]:
            if assignment[neighbor] == color:
                return False
        return True
    
    def dfs(node):
        if node == n:
            return True
        
        for color in [1, 2, 3]:
            if is_safe(node, color):
                assignment[node] = color
                if dfs(node + 1):
                    return True
                assignment[node] = 0
        
        return False
    
    if dfs(0):
        print("YES")
        print(" ".join(map(str, assignment)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()