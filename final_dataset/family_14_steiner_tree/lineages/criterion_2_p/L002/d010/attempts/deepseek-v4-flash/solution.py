import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    critical = set(map(int, input().split()))
    
    adj = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # DFS to mark which nodes have critical in their subtree
    parent = [-1] * n
    order = []
    stack = [0]
    parent[0] = 0
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            stack.append(v)
    
    has_critical = [False] * n
    for c in critical:
        has_critical[c] = True
    
    for u in reversed(order):
        for v, w in adj[u]:
            if v == parent[u]:
                continue
            if has_critical[v]:
                has_critical[u] = True
    
    # Sum edges where both sides have critical
    total = 0
    for u, v, w in edges:
        if has_critical[u] and has_critical[v]:
            total += w
    
    print(total)

if __name__ == "__main__":
    solve()