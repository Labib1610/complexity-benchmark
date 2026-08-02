import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)

    colors = [0] * n  # 0 uncolored, 1..3 colors

    sys.setrecursionlimit(1000000)

    def dfs(pos: int) -> bool:
        if pos == n:
            return True
        v = pos
        used = [False] * 4
        for u in adj[v]:
            c = colors[u]
            if c:
                used[c] = True
        for c in (1, 2, 3):
            if not used[c]:
                colors[v] = c
                if dfs(pos + 1):
                    return True
                colors[v] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(map(str, colors)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()