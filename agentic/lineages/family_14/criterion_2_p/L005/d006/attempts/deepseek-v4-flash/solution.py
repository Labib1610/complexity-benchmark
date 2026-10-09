import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    primaries = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # If only one primary, no cost needed
    if t == 1:
        print(0)
        return
    
    # Root at first primary
    root = next(iter(primaries))
    parent = [0] * (n + 1)
    parent_edge_cost = [0] * (n + 1)
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
                parent_edge_cost[v] = w
                stack.append(v)
    
    # Count how many primary sensors in each subtree
    primary_count = [0] * (n + 1)
    for p in primaries:
        primary_count[p] = 1
    
    total_cost = 0
    # Process in reverse order (post-order)
    for u in reversed(order):
        if u == root:
            continue
        if primary_count[u] > 0:
            total_cost += parent_edge_cost[u]
            primary_count[parent[u]] += primary_count[u]
    
    print(total_cost)

if __name__ == "__main__":
    solve()