import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    critical = set(map(int, input().split()))
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Root at any critical node
    root = next(iter(critical))
    
    parent = [0]*(n+1)
    parent_edge_weight = [0]*(n+1)
    order = []
    stack = [root]
    parent[root] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            parent_edge_weight[v] = w
            stack.append(v)
    
    needed = [False]*(n+1)
    for c in critical:
        needed[c] = True
    
    # Process in reverse order (post-order)
    for u in reversed(order):
        if u == root:
            continue
        if needed[u]:
            needed[parent[u]] = True
    
    total_cost = 0
    for u in range(1, n+1):
        if u == root:
            continue
        if needed[u] and needed[parent[u]]:
            total_cost += parent_edge_weight[u]
    
    print(total_cost)

if __name__ == "__main__":
    solve()