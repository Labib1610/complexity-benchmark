import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(data[idx]) - 1; idx += 1
        v = int(data[idx]) - 1; idx += 1
        adj[u].append(v)
        adj[v].append(u)
    
    colors = [0] * n
    
    def backtrack(node):
        if node == n:
            return True
        for color in [1, 2, 3]:
            valid = True
            for neighbor in adj[node]:
                if colors[neighbor] == color:
                    valid = False
                    break
            if valid:
                colors[node] = color
                if backtrack(node + 1):
                    return True
                colors[node] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, colors)))
    else:
        print("NO")

solve()