import sys
sys.setrecursionlimit(300000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); t = int(next(it))
    marked = [0] * (n + 1)
    for _ in range(t):
        marked[int(next(it))] = 1
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))

    total = 0
    visited = [False] * (n + 1)

    def dfs(u: int) -> int:
        nonlocal total
        visited[u] = True
        cnt = marked[u]
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