import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    color = [0] * n          # 0 = uncoloured, else 1..3
    solution = None

    # forward checking: return False if some uncoloured vertex has no colour left
    def forward_ok() -> bool:
        for v in range(n):
            if color[v] != 0:
                continue
            forbidden = 0
            nb = adj[v]
            while nb:
                u = (nb & -nb).bit_length() - 1
                nb &= nb - 1
                c = color[u]
                if c:
                    forbidden |= 1 << (c - 1)
            if forbidden == 0b111:   # all three colours forbidden
                return False
        return True

    def dfs(v: int) -> bool:
        nonlocal solution
        if v == n:
            solution = color.copy()
            return True
        # try colours 1,2,3
        neigh = adj[v]
        used = 0
        nb = neigh
        while nb:
            u = (nb & -nb).bit_length() - 1
            nb &= nb - 1
            c = color[u]
            if c:
                used |= 1 << (c - 1)
        for c in (1, 2, 3):
            if used & (1 << (c - 1)):
                continue
            color[v] = c
            if forward_ok():
                if dfs(v + 1):
                    return True
            color[v] = 0
        return False

    if dfs(0):
        out = ["YES", " ".join(str(x) for x in solution)]
    else:
        out = ["NO"]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()