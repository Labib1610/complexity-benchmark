import sys

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

    # order vertices by decreasing degree
    order = sorted(range(n), key=lambda x: bin(adj[x]).count('1'), reverse=True)

    color = [-1] * n          # -1 = uncolored, otherwise 0,1,2

    sys.setrecursionlimit(10000)

    def dfs(pos: int) -> bool:
        if pos == n:
            return True
        v = order[pos]
        # compute which colours are forbidden by already coloured neighbours
        forb = 0
        neigh = adj[v]
        # iterate over neighbours that are already coloured
        while neigh:
            u = (neigh & -neigh).bit_length() - 1   # index of lowest set bit
            neigh &= neigh - 1
            cu = color[u]
            if cu != -1:
                forb |= 1 << cu
        for c in range(3):
            if not (forb >> c) & 1:
                color[v] = c
                if dfs(pos + 1):
                    return True
                color[v] = -1
        return False

    if dfs(0):
        out = ['YES', ' '.join(str(c + 1) for c in color)]
        sys.stdout.write('\n'.join(out))
    else:
        sys.stdout.write('NO')

if __name__ == "__main__":
    solve()