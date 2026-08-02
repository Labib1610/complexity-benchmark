import sys
sys.setrecursionlimit(10000)

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

    colors = [0] * n  # 0 means unassigned

    def dfs(idx: int) -> bool:
        if idx == n:
            return True
        for c in (1, 2, 3):
            ok = True
            for nb in adj[idx]:
                if colors[nb] == c:
                    ok = False
                    break
            if ok:
                colors[idx] = c
                if dfs(idx + 1):
                    return True
                colors[idx] = 0
        return False

    if dfs(0):
        out_lines = ["YES", " ".join(map(str, colors))]
        sys.stdout.write("\n".join(out_lines))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()