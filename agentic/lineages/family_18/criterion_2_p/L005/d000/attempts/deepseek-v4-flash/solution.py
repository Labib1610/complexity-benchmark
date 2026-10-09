import sys
sys.setrecursionlimit(300000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    parent = [-1] * n
    order = []
    stack = [0]
    parent[0] = -2
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            stack.append(v)
    
    size = [1] * n
    for u in reversed(order):
        for v in adj[u]:
            if v == parent[u]:
                continue
            size[u] += size[v]
    
    total = 0
    for u in range(1, n):
        s = size[u]
        total += s * (n - s)
    
    if total > B:
        print("NO")
        return
    
    pos = [0] * n
    cur = 1
    def dfs(u):
        nonlocal cur
        pos[u] = cur
        cur += 1
        for v in adj[u]:
            if v == parent[u]:
                continue
            dfs(v)
    
    dfs(0)
    
    print("YES")
    print(" ".join(str(pos[i]) for i in range(n)))

if __name__ == "__main__":
    solve()