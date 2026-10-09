import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * n          # bitmask of neighbours
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    col = [0] * n          # 0 = uncoloured, else 1..3
    avail = [0b111] * n    # three bits, all colours possible

    # helper: find first vertex with col==0
    def next_uncoloured(start):
        for i in range(start, n):
            if col[i] == 0:
                return i
        return n

    # depth‑first search
    def dfs(pos):
        v = next_uncoloured(pos)
        if v == n:                     # all coloured
            return True

        mask = avail[v]
        for colour in (1, 2, 3):
            bit = 1 << (colour - 1)
            if not (mask & bit):
                continue

            # assign
            col[v] = colour
            changed = []               # neighbours that lose this colour
            neigh_mask = adj[v]
            while neigh_mask:
                u = (neigh_mask & -neigh_mask).bit_length() - 1
                neigh_mask &= neigh_mask - 1
                if col[u] == 0 and (avail[u] & bit):
                    avail[u] &= ~bit
                    changed.append(u)
                    if avail[u] == 0:   # dead end
                        break
            else:
                # no dead end, recurse
                if dfs(v + 1):
                    return True

            # undo
            for u in changed:
                avail[u] |= bit
            col[v] = 0

        return False

    possible = dfs(0)

    out = []
    if not possible:
        out.append("NO")
    else:
        out.append("YES")
        out.append(" ".join(str(c) for c in col))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()