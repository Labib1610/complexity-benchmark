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

    colour = [-1] * n               # -1 = uncoloured, else 0/1/2
    col_mask = [0, 0, 0]            # bits of vertices with each colour
    coloured_mask = 0               # union of the three masks

    # choose vertex with most already coloured neighbours
    def choose_vertex() -> int:
        best = -1
        best_deg = -1
        for v in range(n):
            if colour[v] == -1:
                deg = (adj[v] & coloured_mask).bit_count()
                if deg > best_deg:
                    best_deg = deg
                    best = v
        return best

    def dfs(coloured_cnt: int) -> bool:
        nonlocal coloured_mask
        if coloured_cnt == n:
            return True
        v = choose_vertex()
        # compute which colours are forbidden by already coloured neighbours
        forbidden = 0
        for c in range(3):
            if adj[v] & col_mask[c]:
                forbidden |= 1 << c
        for c in range(3):
            if (forbidden >> c) & 1:
                continue
            # assign colour c
            colour[v] = c
            col_mask[c] |= 1 << v
            coloured_mask |= 1 << v
            if dfs(coloured_cnt + 1):
                return True
            # backtrack
            colour[v] = -1
            col_mask[c] ^= 1 << v
            coloured_mask ^= 1 << v
        return False

    possible = dfs(0)
    out = []
    if possible:
        out.append("YES")
        # convert 0/1/2 to 1/2/3
        out.append(' '.join(str(c + 1) for c in colour))
    else:
        out.append("NO")
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()