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
        if u == v:
            continue
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    colors = [0] * n
    color_mask = [0, 0, 0, 0]  # index 1..3

    sys.setrecursionlimit(10000)

    def dfs(pos: int) -> bool:
        if pos == n:
            return True
        for c in (1, 2, 3):
            if (adj[pos] & color_mask[c]) == 0:
                colors[pos] = c
                color_mask[c] |= 1 << pos
                if dfs(pos + 1):
                    return True
                color_mask[c] ^= 1 << pos
                colors[pos] = 0
        return False

    if dfs(0):
        out = ['YES', '\n', ' '.join(str(colors[i]) for i in range(n))]
        sys.stdout.write(''.join(out))
    else:
        sys.stdout.write('NO')

if __name__ == "__main__":
    solve()