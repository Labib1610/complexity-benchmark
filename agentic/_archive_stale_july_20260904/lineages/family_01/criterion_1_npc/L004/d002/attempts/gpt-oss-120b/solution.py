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
        if u == v:
            continue
        adj[u].append(v)
        adj[v].append(u)

    colour = [0] * n          # 0 = uncoloured, else 1..3

    def dfs(v: int) -> bool:
        if v == n:
            return True
        used = 0
        for nb in adj[v]:
            c = colour[nb]
            if c:
                used |= 1 << (c - 1)
        for col in (1, 2, 3):
            if not (used & (1 << (col - 1))):
                colour[v] = col
                if dfs(v + 1):
                    return True
                colour[v] = 0
        return False

    if dfs(0):
        out = ['YES', ' '.join(str(c) for c in colour)]
    else:
        out = ['NO']
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()