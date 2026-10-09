import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    priority = set(map(int, input().split()))
    
    adj = [[] for _ in range(n+1)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # DFS to count priority nodes in subtree and total cost
    parent = [0]*(n+1)
    parent_edge_cost = [0]*(n+1)
    order = []
    stack = [next(iter(priority))]
    parent[next(iter(priority))] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            parent_edge_cost[v] = w
            stack.append(v)
    
    subtree_priority_count = [0]*(n+1)
    for u in priority:
        subtree_priority_count[u] = 1
    
    total_cost = 0
    for u in reversed(order):
        if u == next(iter(priority)):
            continue
        if subtree_priority_count[u] > 0 and (t - subtree_priority_count[u]) > 0:
            total_cost += parent_edge_cost[u]
        p = parent[u]
        subtree_priority_count[p] += subtree_priority_count[u]
    
    print(total_cost)

if __name__ == "__main__":
    solve()