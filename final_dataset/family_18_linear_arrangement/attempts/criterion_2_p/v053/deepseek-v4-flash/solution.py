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
            if parent[v] == -1:
                parent[v] = u
                stack.append(v)
    
    size = [1] * n
    for u in reversed(order):
        for v in adj[u]:
            if parent[v] == u:
                size[u] += size[v]
    
    min_total = 0
    for u in range(1, n):
        s = size[u]
        min_total += min(s, n - s)
    
    if min_total > B:
        print("NO")
        return
    
    # Assign positions via DFS preorder
    pos = [0] * n
    idx = 1
    stack = [0]
    visited = [False] * n
    visited[0] = True
    while stack:
        u = stack.pop()
        pos[u] = idx
        idx += 1
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)
    
    print("YES")
    print(" ".join(str(x) for x in pos))

if __name__ == "__main__":
    solve()