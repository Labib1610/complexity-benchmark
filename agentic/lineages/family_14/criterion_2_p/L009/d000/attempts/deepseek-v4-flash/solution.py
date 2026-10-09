import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    hubs = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # DFS to count hubs in subtree
    parent = [0] * (n + 1)
    weight = [0] * (n + 1)
    order = []
    stack = [1]
    parent[1] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                weight[v] = w
                stack.append(v)
    
    hub_count = [0] * (n + 1)
    for h in hubs:
        hub_count[h] = 1
    
    total_cost = 0
    for u in reversed(order):
        if u != 1:
            if hub_count[u] > 0 and hub_count[u] < t:
                total_cost += weight[u]
            if parent[u] != -1:
                hub_count[parent[u]] += hub_count[u]
    
    print(total_cost)

if __name__ == "__main__":
    solve()