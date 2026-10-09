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

    col = [-1] * n               # -1 = uncoloured, else 0..2
    sat = [0] * n                # bitmask of neighbour colours
    deg = [adj[i].bit_count() for i in range(n)]

    sys.setrecursionlimit(10000)

    def dfs(coloured_cnt: int) -> bool:
        if coloured_cnt == n:
            return True

        # select vertex with maximal saturation, tie by degree
        best = -1
        best_sat = -1
        best_deg = -1
        for v in range(n):
            if col[v] != -1:
                continue
            s = sat[v].bit_count()
            if s > best_sat or (s == best_sat and deg[v] > best_deg):
                best = v
                best_sat = s
                best_deg = deg[v]

        v = best
        forbidden = sat[v]
        for colour in range(3):
            if forbidden & (1 << colour):
                continue
            # assign colour
            col[v] = colour
            changed = []
            nb = adj[v]
            while nb:
                lsb = nb & -nb
                u = (lsb.bit_length() - 1)
                nb ^= lsb
                if col[u] == -1:
                    if not (sat[u] & (1 << colour)):
                        sat[u] |= (1 << colour)
                        changed.append(u)
            if dfs(coloured_cnt + 1):
                return True
            # undo
            for u in changed:
                # recompute sat[u] from neighbours
                mask = 0
                nb2 = adj[u]
                while nb2:
                    lsb2 = nb2 & -nb2
                    w = (lsb2.bit_length() - 1)
                    nb2 ^= lsb2
                    if col[w] != -1:
                        mask |= 1 << col[w]
                sat[u] = mask
            col[v] = -1
        return False

    if dfs(0):
        out = ['YES', ' '.join(str(c + 1) for c in col)]
    else:
        out = ['NO']
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()