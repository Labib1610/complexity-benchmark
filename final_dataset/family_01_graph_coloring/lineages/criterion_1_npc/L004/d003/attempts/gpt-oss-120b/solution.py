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
    deg = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            continue
        adj[u].append(v)
        adj[v].append(u)
        deg[u] += 1
        deg[v] += 1

    color = [0] * n          # 0 = uncoloured, else 1..3
    forbid = [0] * n         # bitmask of forbidden colours

    # -----------------------------------------------------------------
    def dfs(coloured_cnt: int) -> bool:
        if coloured_cnt == n:
            return True

        # choose vertex with maximal saturation, tie by degree
        best_v = -1
        best_sat = -1
        best_deg = -1
        for v in range(n):
            if color[v] == 0:
                sat = (forbid[v] & 1) + ((forbid[v] >> 1) & 1) + ((forbid[v] >> 2) & 1)
                d = deg[v]
                if sat > best_sat or (sat == best_sat and d > best_deg):
                    best_sat = sat
                    best_deg = d
                    best_v = v
        v = best_v

        # try every allowed colour
        for c in range(1, 4):
            mask = 1 << (c - 1)
            if forbid[v] & mask:
                continue

            # assign colour
            color[v] = c
            changed = []          # neighbours whose forbid mask really changed
            for u in adj[v]:
                if color[u] == 0 and not (forbid[u] & mask):
                    forbid[u] |= mask
                    changed.append(u)

            # early failure detection
            dead = False
            for u in adj[v]:
                if color[u] == 0 and forbid[u] == 7:
                    dead = True
                    break

            if not dead and dfs(coloured_cnt + 1):
                return True

            # undo
            for u in changed:
                forbid[u] &= ~mask
            color[v] = 0

        return False
    # -----------------------------------------------------------------

    possible = dfs(0)

    out = []
    if possible:
        out.append("YES")
        out.append(" ".join(str(c) for c in color))
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()