import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [set() for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].add(v)
        adj[v].add(u)

    colors = [0] * n
    sys.setrecursionlimit(10000)

    def dfs(idx: int) -> bool:
        if idx == n:
            return True
        for col in (1, 2, 3):
            ok = True
            for nb in adj[idx]:
                if nb < idx and colors[nb] == col:
                    ok = False
                    break
            if not ok:
                continue
            colors[idx] = col
            if dfs(idx + 1):
                return True
            colors[idx] = 0
        return False

    if dfs(0):
        out = ["YES", " ".join(map(str, colors))]
    else:
        out = ["NO"]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()