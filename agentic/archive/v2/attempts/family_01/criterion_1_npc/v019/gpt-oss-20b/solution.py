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

    color = [0] * n  # 0 unassigned, 1..3 assigned

    def dfs(v: int) -> bool:
        if v == n:
            return True
        for c in (1, 2, 3):
            conflict = False
            for nb in adj[v]:
                if color[nb] == c:
                    conflict = True
                    break
            if not conflict:
                color[v] = c
                if dfs(v + 1):
                    return True
                color[v] = 0
        return False

    if dfs(0):
        out_lines = ["YES", " ".join(map(str, color))]
        sys.stdout.write("\n".join(out_lines))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()