import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    offices = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # DFS to count offices in subtree
    parent = [0] * (n + 1)
    parent_edge_cost = [0] * (n + 1)
    order = []
    stack = [1]
    parent[1] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                parent_edge_cost[v] = w
                stack.append(v)
    
    office_count = [0] * (n + 1)
    for o in offices:
        office_count[o] = 1
    
    total_cost = 0
    for u in reversed(order):
        if u == 1:
            continue
        p = parent[u]
        office_count[p] += office_count[u]
        if office_count[u] > 0 and office_count[u] < t:
            total_cost += parent_edge_cost[u]
    
    print(total_cost)

if __name__ == "__main__":
    solve()