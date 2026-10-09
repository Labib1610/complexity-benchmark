import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    targets = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t <= 1:
        print(0)
        return
    
    # Root at any target
    root = next(iter(targets))
    
    parent = [0] * (n + 1)
    parent_edge_weight = [0] * (n + 1)
    visited = [False] * (n + 1)
    
    # DFS to build parent info
    stack = [root]
    visited[root] = True
    order = []
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                parent_edge_weight[v] = w
                stack.append(v)
    
    # Determine which edges are needed
    needed = [False] * (n + 1)
    for node in targets:
        needed[node] = True
    
    total = 0
    # Process in reverse order (post-order)
    for u in reversed(order):
        if u == root:
            continue
        if needed[u]:
            total += parent_edge_weight[u]
            needed[parent[u]] = True
    
    print(total)

if __name__ == "__main__":
    solve()