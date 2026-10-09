import sys
sys.setrecursionlimit(1 << 25)

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); t = int(next(it))
    required = [0] * (n + 1)
    for _ in range(t):
        required[int(next(it))] = 1

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))

    cnt = [0] * (n + 1)
    ans = 0

    def dfs(u, p):
        nonlocal ans
        c = required[u]
        for v, w in adj[u]:
            if v == p:
                continue
            sub = dfs(v, u)
            if 0 < sub < t:
                ans += w
            c += sub
        cnt[u] = c
        return c

    dfs(1, 0)
    print(ans)

if __name__ == "__main__":
    main()