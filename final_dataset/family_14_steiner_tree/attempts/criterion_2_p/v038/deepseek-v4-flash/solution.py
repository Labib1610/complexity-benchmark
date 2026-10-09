import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    priority = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # DFS to mark which nodes have priority in their subtree
    has_priority = [False] * (n + 1)
    parent = [0] * (n + 1)
    parent_edge_weight = [0] * (n + 1)
    
    stack = [(1, 0)]
    order = []
    while stack:
        u, p = stack.pop()
        parent[u] = p
        order.append(u)
        for v, w in adj[u]:
            if v != p:
                parent_edge_weight[v] = w
                stack.append((v, u))
    
    # Process in reverse order
    for u in reversed(order):
        if u in priority:
            has_priority[u] = True
        for v, w in adj[u]:
            if v != parent[u] and has_priority[v]:
                has_priority[u] = True
    
    # Sum edges where both sides have priority
    total = 0
    for u in range(1, n + 1):
        if u == 1:
            continue
        if has_priority[u] and has_priority[parent[u]]:
            total += parent_edge_weight[u]
    
    print(total)

if __name__ == "__main__":
    solve()