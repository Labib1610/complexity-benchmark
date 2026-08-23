import sys

def solve() -> None:
    sys.setrecursionlimit(1000000)
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

    def dfs(idx: int) -> bool:
        nonlocal found
        if idx == n:
            found = True
            return True
        for c in (1, 2, 3):
            ok = True
            for nb in adj[idx]:
                if nb < idx and colors[nb] == c:
                    ok = False
                    break
            if ok:
                colors[idx] = c
                if dfs(idx + 1):
                    return True
                colors[idx] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(map(str, colors)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()