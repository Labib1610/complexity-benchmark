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

    colour = [0] * n          # 0 = uncoloured, otherwise 1..3
    found = False

    def dfs(v: int) -> bool:
        """try to colour vertices v..n-1, return True on success"""
        if v == n:
            return True
        for col in (1, 2, 3):
            ok = True
            for nb in adj[v]:
                if nb < v and colour[nb] == col:
                    ok = False
                    break
            if not ok:
                continue
            colour[v] = col
            if dfs(v + 1):
                return True
            colour[v] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(map(str, colour)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()