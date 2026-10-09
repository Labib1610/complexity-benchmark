import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    essential = set(map(int, input().split()))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t == 1:
        print(0)
        return
    
    # Root at any essential node
    root = next(iter(essential))
    
    parent = [-1] * n
    parent_edge_weight = [0] * n
    order = []
    stack = [root]
    parent[root] = root
    
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            parent_edge_weight[v] = w
            stack.append(v)
    
    essential_count = [0] * n
    for e in essential:
        essential_count[e] = 1
    
    total_cost = 0
    # Process in reverse order (post-order)
    for u in reversed(order):
        if u != root:
            if essential_count[u] > 0 and essential_count[u] < t:
                total_cost += parent_edge_weight[u]
            # propagate count to parent
            if u != root:
                essential_count[parent[u]] += essential_count[u]
    
    print(total_cost)

if __name__ == "__main__":
    solve()