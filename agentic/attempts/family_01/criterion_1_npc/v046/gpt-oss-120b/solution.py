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

    order = sorted(range(n), key=lambda x: -len(adj[x]))
    color = [0] * n

    sys.setrecursionlimit(10000)

    def dfs(idx: int) -> bool:
        if idx == n:
            return True
        v = order[idx]
        # try colors 1..3
        for c in (1, 2, 3):
            conflict = False
            for nb in adj[v]:
                if color[nb] == c:
                    conflict = True
                    break
            if not conflict:
                color[v] = c
                if dfs(idx + 1):
                    return True
                color[v] = 0
        return False

    if dfs(0):
        out = "YES\n" + " ".join(str(color[i]) for i in range(n))
        sys.stdout.write(out)
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()