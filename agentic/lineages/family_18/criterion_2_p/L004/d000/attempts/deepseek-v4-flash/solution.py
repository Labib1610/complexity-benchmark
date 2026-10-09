import sys
sys.setrecursionlimit(300000)

def solve():
    n, m, B = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))

    parent = [-1] * n
    order = []
    stack = [0]
    parent[0] = 0
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            stack.append(v)

    size = [1] * n
    for u in reversed(order):
        for v in adj[u]:
            if v == parent[u]:
                continue
            size[u] += size[v]

    min_cost = 0
    for u, v in edges:
        if parent[u] == v:
            min_cost += min(size[u], n - size[u])
        else:
            min_cost += min(size[v], n - size[v])

    if min_cost > B:
        print("NO")
        return

    # Build a valid ordering: DFS preorder
    pos = [0] * n
    order2 = []
    stack = [0]
    visited = [False] * n
    visited[0] = True
    while stack:
        u = stack.pop()
        order2.append(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)

    for i, node in enumerate(order2):
        pos[node] = i + 1

    print("YES")
    print(" ".join(map(str, pos)))

if __name__ == "__main__":
    solve()