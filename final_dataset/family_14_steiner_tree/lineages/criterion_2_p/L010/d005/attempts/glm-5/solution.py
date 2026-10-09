import sys
sys.setrecursionlimit(1 << 25)

def solve():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    terminals = [int(next(it)) for _ in range(t)]
    is_terminal = [False] * (n + 1)
    for x in terminals:
        is_terminal[x] = True
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # DFS to compute subtree info
    parent = [0] * (n + 1)
    parent_edge_weight = [0] * (n + 1)
    order = []
    stack = [(1, 0, 0)]  # (node, parent, weight)
    
    while stack:
        u, p, w = stack.pop()
        parent[u] = p
        parent_edge_weight[u] = w
        order.append(u)
        for v, weight in adj[u]:
            if v != p:
                stack.append((v, u, weight))
    
    # Process in reverse order (bottom-up)
    has_terminal = [False] * (n + 1)
    for x in terminals:
        has_terminal[x] = True
    
    total_cost = 0
    
    for u in reversed(order):
        if u == 1:
            continue
        p = parent[u]
        w = parent_edge_weight[u]
        if has_terminal[u]:
            total_cost += w
            has_terminal[p] = True
    
    print(total_cost)

if __name__ == "__main__":
    solve()