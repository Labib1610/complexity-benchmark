import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, B = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)

    # Compute minimal possible sum of edge lengths
    parent = [-1] * n
    order = []
    stack = [0]
    parent[0] = 0
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if parent[v] == -1:
                parent[v] = u
                stack.append(v)

    size = [1] * n
    min_sum = 0
    for u in reversed(order):
        for v in adj[u]:
            if v != parent[u]:
                size[u] += size[v]
    for u in range(1, n):
        min_sum += min(size[u], n - size[u])

    if min_sum > B:
        print("NO")
        return

    # Produce a DFS ordering
    pos = [0] * n
    visited = [False] * n
    res = []
    def dfs(u):
        visited[u] = True
        res.append(u)
        for v in adj[u]:
            if not visited[v]:
                dfs(v)
    dfs(0)

    for i, u in enumerate(res, start=1):
        pos[u] = i

    print("YES")
    print(" ".join(str(pos[i]) for i in range(n)))

if __name__ == "__main__":
    solve()