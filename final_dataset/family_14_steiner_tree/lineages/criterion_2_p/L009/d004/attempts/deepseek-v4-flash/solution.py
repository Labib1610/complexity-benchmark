import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    N, E, F = map(int, input().split())
    critical = set(map(int, input().split()))
    
    adj = [[] for _ in range(N+1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if F <= 1:
        print(0)
        return
    
    # Root at any critical node
    root = next(iter(critical))
    
    parent = [0]*(N+1)
    parent_edge = [0]*(N+1)
    depth = [0]*(N+1)
    stack = [(root, 0, 0)]
    order = []
    while stack:
        u, p, w = stack.pop()
        parent[u] = p
        parent_edge[u] = w
        depth[u] = depth[p] + 1 if p != 0 else 0
        order.append(u)
        for v, wgt in adj[u]:
            if v != p:
                stack.append((v, u, wgt))
    
    # Mark nodes that are critical or have critical descendants
    is_needed = [False]*(N+1)
    for c in critical:
        is_needed[c] = True
    
    # Process in reverse order (post-order)
    for u in reversed(order):
        if u == root:
            continue
        p = parent[u]
        if is_needed[u]:
            is_needed[p] = True
    
    # Sum weights of edges where child is needed
    total = 0
    for u in range(1, N+1):
        if u != root and is_needed[u]:
            total += parent_edge[u]
    
    print(total)

if __name__ == "__main__":
    solve()