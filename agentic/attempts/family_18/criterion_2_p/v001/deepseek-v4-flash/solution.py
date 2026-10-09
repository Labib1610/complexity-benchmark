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
    parent[0] = 0
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            stack.append(v)
    
    size = [1] * n
    min_cost = 0
    for u in reversed(order):
        if u != 0:
            min_cost += size[u]
        if parent[u] != u:
            size[parent[u]] += size[u]
    
    if min_cost > B:
        print("NO")
        return
    
    # Assign positions via DFS preorder
    pos = [0] * n
    cur = 1
    stack = [0]
    visited = [False] * n
    visited[0] = True
    while stack:
        u = stack.pop()
        pos[u] = cur
        cur += 1
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)
    
    print("YES")
    print(" ".join(str(pos[i]) for i in range(n)))

if __name__ == "__main__":
    solve()