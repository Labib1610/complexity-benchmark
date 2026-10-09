import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    targets = set(map(int, input().split()))
    
    adj = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # Root at any target
    root = next(iter(targets))
    
    parent = [-1] * n
    parent_edge_cost = [0] * n
    order = [root]
    for node in order:
        for nei, w in adj[node]:
            if nei == parent[node]:
                continue
            parent[nei] = node
            parent_edge_cost[nei] = w
            order.append(nei)
    
    target_count = [0] * n
    for node in range(n):
        if node in targets:
            target_count[node] = 1
    
    total_cost = 0
    # Process in reverse order (post-order)
    for node in reversed(order):
        if node == root:
            continue
        p = parent[node]
        target_count[p] += target_count[node]
        if target_count[node] > 0 and target_count[node] < t:
            total_cost += parent_edge_cost[node]
    
    print(total_cost)

if __name__ == "__main__":
    solve()