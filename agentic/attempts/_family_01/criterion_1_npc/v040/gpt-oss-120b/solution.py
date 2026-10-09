import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * n          # bit mask of neighbours
    degree = [0] * n

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            continue
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        degree[u] += 1
        degree[v] += 1

    colour = [0] * n       # 0 = uncoloured, else 1..3

    # ---------- DSATUR vertex selection ----------
    def select_vertex() -> int:
        best = -1
        best_sat = -1
        best_deg = -1
        for v in range(n):
            if colour[v]:
                continue
            # compute saturation: different colours among coloured neighbours
            mask = adj[v]
            sat_mask = 0
            while mask:
                u = (mask & -mask).bit_length() - 1
                c = colour[u]
                if c:
                    sat_mask |= 1 << (c - 1)
                mask &= mask - 1
            sat = sat_mask.bit_count()
            deg = degree[v]
            if sat > best_sat or (sat == best_sat and deg > best_deg):
                best_sat = sat
                best_deg = deg
                best = v
        return best

    # ---------- depth‑first search ----------
    def dfs(coloured_cnt: int) -> bool:
        if coloured_cnt == n:
            return True
        v = select_vertex()
        # colours already used by coloured neighbours
        forbidden = 0
        mask = adj[v]
        while mask:
            u = (mask & -mask).bit_length() - 1
            c = colour[u]
            if c:
                forbidden |= 1 << (c - 1)
            mask &= mask - 1
        for col in (1, 2, 3):
            if not (forbidden & (1 << (col - 1))):
                colour[v] = col
                if dfs(coloured_cnt + 1):
                    return True
                colour[v] = 0
        return False

    possible = dfs(0)

    out = []
    if possible:
        out.append("YES")
        out.append(" ".join(str(c) for c in colour))
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()