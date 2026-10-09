import sys

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
    
    def is_safe(u, c):
        for v in adj[u]:
            if color[v] == c:
                return False
        return True
    
    def backtrack(u):
        if u == n:
            return True
        for c in range(1, 4):
            if is_safe(u, c):
                color[u] = c
                if backtrack(u + 1):
                    return True
                color[u] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(' '.join(map(str, color)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()