import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    essential = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # If only one essential, no edges needed
    if t == 1:
        print(0)
        return
    
    # Root at any essential node
    root = next(iter(essential))
    
    parent = [0] * (n + 1)
    parent_weight = [0] * (n + 1)
    order = []
    stack = [root]
    parent[root] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                parent_weight[v] = w
                stack.append(v)
    
    has_essential = [False] * (n + 1)
    for e in essential:
        has_essential[e] = True
    
    total = 0
    # Process in reverse order (post-order)
    for u in reversed(order):
        if u == root:
            continue
        if has_essential[u]:
            total += parent_weight[u]
            # propagate up
            p = parent[u]
            if p != -1:
                has_essential[p] = True
    
    print(total)

if __name__ == "__main__":
    solve()