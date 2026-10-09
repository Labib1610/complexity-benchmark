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
    targets = set(int(next(it)) for _ in range(t))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))

    if t <= 1:
        print(0)
        return

    total = 0
    visited = [False] * (n + 1)

    def dfs(u: int) -> int:
        nonlocal total
        visited[u] = True
        cnt = 1 if u in targets else 0
        for v, w in adj[u]:
            if not visited[v]:
                sub = dfs(v)
                if 0 < sub < t:
                    total += w
                cnt += sub
        return cnt

    dfs(1)
    print(total)

if __name__ == "__main__":
    solve()