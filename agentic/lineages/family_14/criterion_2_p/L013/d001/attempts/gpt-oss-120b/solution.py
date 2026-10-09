import sys
sys.setrecursionlimit(300000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))  # = n-1
    t = int(next(it))
    targets = set(int(next(it)) for _ in range(t))
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

    total_targets = t
    ans = 0

    def dfs(u: int, p: int) -> int:
        nonlocal ans
        cnt = 1 if u in targets else 0
        for v, w in adj[u]:
            if v == p:
                continue
            sub = dfs(v, u)
            # edge (u,v) is needed if sub>0 and sub<total_targets
            if 0 < sub < total_targets:
                ans += w
            cnt += sub
        return cnt

    dfs(1, 0)
    print(ans)

if __name__ == "__main__":
    solve()