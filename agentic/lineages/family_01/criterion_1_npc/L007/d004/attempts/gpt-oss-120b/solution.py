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
        adj[u].append(v)
        adj[v].append(u)

    colors = [0] * n
    found = False

    def dfs(v: int) -> bool:
        nonlocal found
        if v == n:
            return True
        for c in (1, 2, 3):
            ok = True
            for nb in adj[v]:
                if nb < v and colors[nb] == c:
                    ok = False
                    break
            if not ok:
                continue
            colors[v] = c
            if dfs(v + 1):
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