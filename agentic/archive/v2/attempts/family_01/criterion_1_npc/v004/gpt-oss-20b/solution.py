import sys
sys.setrecursionlimit(10000)

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
        if v not in adj[u]:
            adj[u].append(v)
        if u not in adj[v]:
            adj[v].append(u)

    colors = [0] * n

    def dfs(i: int) -> bool:
        if i == n:
            return True
        forbidden = set()
        for nb in adj[i]:
            c = colors[nb]
            if c:
                forbidden.add(c)
        for c in (1, 2, 3):
            if c not in forbidden:
                colors[i] = c
                if dfs(i + 1):
                    return True
                colors[i] = 0
        return False

    if dfs(0):
        out_lines = ["YES", " ".join(map(str, colors))]
        sys.stdout.write("\n".join(out_lines))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()