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
    
    adj = [[] for _ in range(n+1)]
    indeg = [0]*(n+1)
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
        indeg[v] += 1
    
    # find root (indegree 0)
    root = 1
    for i in range(1, n+1):
        if indeg[i] == 0:
            root = i
            break
    
    parent = [0]*(n+1)
    order = []
    stack = [root]
    parent[root] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if v != parent[u]:
                parent[v] = u
                stack.append(v)
    
    # compute subtree sizes
    size = [1]*(n+1)
    for u in reversed(order):
        for v in adj[u]:
            if v != parent[u]:
                size[u] += size[v]
    
    # minimal total length
    min_len = 0
    for u in range(1, n+1):
        if parent[u] != -1:
            s = size[u]
            min_len += s * (n - s)
    
    if min_len > B:
        print("NO")
        return
    
    # assign positions in preorder
    pos = [0]*(n+1)
    cur = 1
    stack = [root]
    while stack:
        u = stack.pop()
        pos[u] = cur
        cur += 1
        # push children in reverse order to get natural order
        for v in reversed(adj[u]):
            if v != parent[u]:
                stack.append(v)
    
    print("YES")
    print(" ".join(str(pos[i]) for i in range(1, n+1)))

if __name__ == "__main__":
    solve()