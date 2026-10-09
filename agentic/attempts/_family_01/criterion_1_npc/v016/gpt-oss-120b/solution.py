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

    # order vertices by decreasing degree
    order = sorted(range(n), key=lambda x: -adj[x].bit_count())

    color = [-1] * n

    def dfs(pos: int) -> bool:
        if pos == n:
            return True
        v = order[pos]
        # collect colours used by already coloured neighbours
        forbidden = 0
        nb = adj[v]
        while nb:
            u = (nb & -nb).bit_length() - 1
            nb &= nb - 1
            cu = color[u]
            if cu != -1:
                forbidden |= 1 << cu
        for c in range(3):
            if not (forbidden >> c) & 1:
                color[v] = c
                if dfs(pos + 1):
                    return True
                color[v] = -1
        return False

    if dfs(0):
        out = ['YES']
        out.append(' '.join(str(c + 1) for c in color))
        sys.stdout.write('\n'.join(out))
    else:
        sys.stdout.write('NO')

if __name__ == "__main__":
    solve()