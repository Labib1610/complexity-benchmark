import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)

    # simple DFS ordering
    order = []
    visited = [False] * n

    def dfs(u):
        visited[u] = True
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                dfs(v)

    dfs(0)

    pos = [0] * n
    for idx, node in enumerate(order):
        pos[node] = idx + 1  # slots are 1-indexed

    total = 0
    for u in range(n):
        for v in adj[u]:
            if u < v:
                total += abs(pos[u] - pos[v])

    if total <= B:
        print("YES")
        print(' '.join(map(str, pos)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()