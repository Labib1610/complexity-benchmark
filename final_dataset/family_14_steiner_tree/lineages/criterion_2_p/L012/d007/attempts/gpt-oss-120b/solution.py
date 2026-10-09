import sys
sys.setrecursionlimit(1_000_000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))   # = n-1
    t = int(next(it))
    primary = [0] * (n + 1)
    for _ in range(t):
        primary[int(next(it))] = 1
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))

    total = t
    ans = 0

    def dfs(u: int, p: int) -> int:
        nonlocal ans
        cnt = primary[u]
        for v, w in adj[u]:
            if v == p:
                continue
            sub = dfs(v, u)
            # edge u-v separates sub and total-sub
            if sub > 0 and total - sub > 0:
                ans += w
            cnt += sub
        return cnt

    # root at 1 (any node)
    dfs(1, 0)
    print(ans)

if __name__ == "__main__":
    solve()