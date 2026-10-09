import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))          # equals n-1, not used separately
    t = int(next(it))
    crit = [int(next(it)) for _ in range(t)]
    is_crit = [0] * (n + 1)
    for v in crit:
        is_crit[v] = 1

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))

    total = 0
    sys.setrecursionlimit(1 << 25)

    def dfs(v: int, p: int) -> int:
        nonlocal total
        cnt = is_crit[v]
        for to, w in adj[v]:
            if to == p:
                continue
            sub = dfs(to, v)
            if 0 < sub < t:
                total += w
            cnt += sub
        return cnt

    dfs(1, 0)
    print(total)

if __name__ == "__main__":
    solve()