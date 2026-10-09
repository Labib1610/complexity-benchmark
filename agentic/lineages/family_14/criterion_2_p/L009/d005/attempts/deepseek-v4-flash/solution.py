import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    N, E, F = map(int, input().split())
    targets = set(map(int, input().split()))
    
    adj = [[] for _ in range(N)]
    edges = []
    for _ in range(E):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # DFS to count targets in subtree
    parent = [-1] * N
    order = [0]
    stack = [0]
    parent[0] = -2
    while stack:
        u = stack.pop()
        order.append(u)
        for v, _ in adj[u]:
            if parent[v] == -1:
                parent[v] = u
                stack.append(v)
    
    has_target = [False] * N
    for t in targets:
        has_target[t - 1] = True
    
    # Process in reverse order (post-order)
    total = 0
    for u in reversed(order):
        if u == 0:
            continue
        p = parent[u]
        # find weight of edge (u, p)
        w = None
        for v, wt in adj[u]:
            if v == p:
                w = wt
                break
        if has_target[u]:
            total += w
            has_target[p] = True
    
    print(total)

if __name__ == "__main__":
    solve()