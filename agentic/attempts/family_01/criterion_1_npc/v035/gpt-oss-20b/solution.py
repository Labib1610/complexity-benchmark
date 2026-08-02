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
        if u != v:
            adj[u].add(v)
            adj[v].add(u)

    colors = [-1] * n  # 1,2,3

    def dfs(idx: int) -> bool:
        if idx == n:
            return True
        for c in (1, 2, 3):
            conflict = False
            for nb in adj[idx]:
                if colors[nb] == c:
                    conflict = True
                    break
            if conflict:
                continue
            colors[idx] = c
            if dfs(idx + 1):
                return True
            colors[idx] = -1
        return False

    if dfs(0):
        out = ["YES", " ".join(str(colors[i]) for i in range(n))]
    else:
        out = ["NO"]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()