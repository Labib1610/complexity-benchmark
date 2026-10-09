import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    critical = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    parent = [0] * (n + 1)
    parent_edge_cost = [0] * (n + 1)
    order = [1]
    parent[1] = -1
    for node in order:
        for nei, w in adj[node]:
            if nei == parent[node]:
                continue
            parent[nei] = node
            parent_edge_cost[nei] = w
            order.append(nei)
    
    has_critical = [False] * (n + 1)
    for node in range(1, n + 1):
        if node in critical:
            has_critical[node] = True
    
    total_cost = 0
    for node in reversed(order):
        if node == 1:
            continue
        if has_critical[node]:
            total_cost += parent_edge_cost[node]
            has_critical[parent[node]] = True
    
    print(total_cost)

if __name__ == "__main__":
    solve()