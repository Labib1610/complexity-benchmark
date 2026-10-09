import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    targets = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # DFS to mark which nodes are needed
    needed = [False] * (n + 1)
    for x in targets:
        needed[x] = True
    
    parent = [0] * (n + 1)
    parent_w = [0] * (n + 1)
    order = []
    stack = [1]
    parent[1] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                parent_w[v] = w
                stack.append(v)
    
    # Post-order: propagate needed status
    for u in reversed(order):
        for v, w in adj[u]:
            if v != parent[u]:
                if needed[v]:
                    needed[u] = True
    
    # Sum weights of edges where both endpoints are needed
    total = 0
    for u in range(2, n + 1):
        if needed[u] and needed[parent[u]]:
            total += parent_w[u]
    
    print(total)

if __name__ == "__main__":
    solve()