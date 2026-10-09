import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    priority = set(map(int, input().split()))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # If only one priority vertex, cost is 0
    if t == 1:
        print(0)
        return
    
    # Root at first priority vertex
    root = next(iter(priority))
    parent = [-1] * n
    parent_edge_weight = [0] * n
    order = []
    stack = [root]
    parent[root] = root
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if parent[v] == -1:
                parent[v] = u
                parent_edge_weight[v] = w
                stack.append(v)
    
    has_priority = [False] * n
    for p in priority:
        has_priority[p] = True
    
    total_cost = 0
    # Process in reverse order (post-order)
    for u in reversed(order):
        if u == root:
            continue
        if has_priority[u]:
            total_cost += parent_edge_weight[u]
            # propagate up
            p = parent[u]
            has_priority[p] = True
        else:
            # check if any child had priority
            # we already propagated, so if has_priority[u] is True, it means subtree has priority
            if has_priority[u]:
                total_cost += parent_edge_weight[u]
                p = parent[u]
                has_priority[p] = True
    
    print(total_cost)

if __name__ == "__main__":
    solve()