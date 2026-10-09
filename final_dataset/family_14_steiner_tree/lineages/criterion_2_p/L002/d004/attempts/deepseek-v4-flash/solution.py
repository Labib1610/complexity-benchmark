import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    targets = set(map(int, input().split()))
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # pick a root as any target
    root = next(iter(targets))
    
    parent = [0]*(n+1)
    parent_cost = [0]*(n+1)
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
            parent_cost[v] = w
            stack.append(v)
    
    has_target = [False]*(n+1)
    for x in targets:
        has_target[x] = True
    
    total_cost = 0
    # process in reverse order (post-order)
    for u in reversed(order):
        if u == root:
            continue
        if has_target[u]:
            total_cost += parent_cost[u]
            # propagate up
            p = parent[u]
            while p != -1 and not has_target[p]:
                has_target[p] = True
                p = parent[p]
    
    print(total_cost)

if __name__ == "__main__":
    solve()