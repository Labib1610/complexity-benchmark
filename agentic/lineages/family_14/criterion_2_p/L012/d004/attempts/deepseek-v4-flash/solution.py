import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    targets = set(map(int, input().split()))
    
    adj = [[] for _ in range(n+1)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # DFS to count targets in subtree
    parent = [0]*(n+1)
    parent_edge_weight = [0]*(n+1)
    order = []
    stack = [1]
    parent[1] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                parent_edge_weight[v] = w
                stack.append(v)
    
    target_count = [0]*(n+1)
    for node in targets:
        target_count[node] = 1
    
    total_cost = 0
    for u in reversed(order):
        if u != 1:
            if target_count[u] > 0 and (t - target_count[u]) > 0:
                total_cost += parent_edge_weight[u]
            if parent[u] != -1:
                target_count[parent[u]] += target_count[u]
    
    print(total_cost)

if __name__ == "__main__":
    solve()