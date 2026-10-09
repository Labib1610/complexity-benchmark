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

    col = [0] * n                     # 0 = uncoloured, else 1..3

    # forward checking: are all still uncoloured vertices still feasible?
    def future_ok(idx: int) -> bool:
        # vertices > idx are still uncoloured
        for v in range(idx + 1, n):
            forbidden = 0
            for nb in adj[v]:
                c = col[nb]
                if c:
                    forbidden |= 1 << (c - 1)
            if forbidden == 0b111:   # all three colours blocked
                return False
        return True

    def dfs(idx: int) -> bool:
        if idx == n:
            return True
        # colours already used by coloured neighbours
        forbidden = 0
        for nb in adj[idx]:
            c = col[nb]
            if c:
                forbidden |= 1 << (c - 1)

        for colour in (1, 2, 3):
            if not (forbidden & (1 << (colour - 1))):
                col[idx] = colour
                if future_ok(idx) and dfs(idx + 1):
                    return True
                col[idx] = 0
        return False

    if dfs(0):
        out = ['YES', ' '.join(str(c) for c in col)]
    else:
        out = ['NO']
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()