import sys
sys.setrecursionlimit(1 << 25)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    # BFS to get order
    order = []
    visited = [False] * (n + 1)
    q = [1]
    visited[1] = True
    while q:
        u = q.pop(0)
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
    
    # Calculate total cable length for this assignment
    pos = [0] * (n + 1)
    for i, u in enumerate(order):
        pos[u] = i + 1
    
    total = 0
    for u in range(1, n + 1):
        for v in adj[u]:
            if u < v:
                total += abs(pos[u] - pos[v])
    
    if total <= B:
        print("YES")
        print(' '.join(map(str, pos[1:])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()