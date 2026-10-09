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
    
    # pick any target as root
    root = next(iter(targets))
    
    parent = [0]*(n+1)
    weight = [0]*(n+1)
    order = []
    stack = [root]
    parent[root] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                weight[v] = w
                stack.append(v)
    
    has_target = [False]*(n+1)
    for v in targets:
        has_target[v] = True
    
    total_cost = 0
    # process in reverse order (post-order)
    for u in reversed(order):
        if u == root:
            continue
        if has_target[u]:
            total_cost += weight[u]
            # propagate up
            p = parent[u]
            if p != -1:
                has_target[p] = True
    
    print(total_cost)

if __name__ == "__main__":
    solve()