import sys
sys.setrecursionlimit(1_000_000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))  # = n-1
    t = int(next(it))
    target = set()
    for _ in range(t):
        target.add(int(next(it)))
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))

    if t <= 1:
        print(0)
        return

    total = t
    visited = [False] * (n + 1)
    ans = 0

    def dfs(u: int) -> int:
        nonlocal ans
        visited[u] = True
        cnt = 1 if u in target else 0
        for v, w in adj[u]:
            if not visited[v]:
                sub = dfs(v)
                if sub > 0 and sub < total:
                    ans += w
                cnt += sub
        return cnt

    dfs(1)
    print(ans)

if __name__ == "__main__":
    solve()