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

    order = sorted(range(n), key=lambda x: -len(adj[x]))
    color = [0] * n
    used = [False] * n  # not needed

    def dfs(pos: int) -> bool:
        if pos == n:
            return True
        v = order[pos]
        # try colors 1..3
        for c in (1, 2, 3):
            ok = True
            for nb in adj[v]:
                if color[nb] == c:
                    ok = False
                    break
            if not ok:
                continue
            color[v] = c
            if dfs(pos + 1):
                return True
            color[v] = 0
        return False

    if dfs(0):
        print("YES")
        # output in original order
        print(' '.join(str(color[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()