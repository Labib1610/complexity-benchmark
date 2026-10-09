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

    color = [-1] * n               # -1 = uncoloured, else 0,1,2
    avail = [0b111] * n            # three bits set

    # order of vertices for tie‑breaking (higher degree first)
    degree = [bin(adj[i]).count('1') for i in range(n)]
    order = sorted(range(n), key=lambda x: -degree[x])

    # helper: count bits set (0..3)
    popcnt = lambda x: (x & 1) + ((x >> 1) & 1) + ((x >> 2) & 1)

    # recursive search
    changes = []   # stack of (vertex, old_avail)

    def dfs(coloured_cnt: int) -> bool:
        if coloured_cnt == n:
            return True

        # choose vertex with minimum remaining colours
        v = -1
        best = 4
        for u in order:
            if color[u] == -1:
                cnt = popcnt(avail[u])
                if cnt < best:
                    best = cnt
                    v = u
                    if cnt == 1:
                        break
        if v == -1:   # should not happen
            return False
        if best == 0:
            return False

        cur_avail = avail[v]
        # try each possible colour
        for c in range(3):
            if not (cur_avail >> c) & 1:
                continue
            # assign
            color[v] = c
            # record changes to neighbours
            changed = []
            mask = 1 << c
            nb = adj[v]
            while nb:
                u = (nb & -nb).bit_length() - 1
                nb &= nb - 1
                if color[u] == -1 and (avail[u] & mask):
                    old = avail[u]
                    new = old & ~mask
                    if new != old:
                        changed.append((u, old))
                        avail[u] = new
                        if new == 0:
                            # undo
                            for uu, oo in reversed(changed):
                                avail[uu] = oo
                            color[v] = -1
                            break
            else:
                # no conflict, recurse
                if dfs(coloured_cnt + 1):
                    return True
                # undo changes after recursion
                for uu, oo in reversed(changed):
                    avail[uu] = oo
            # undo assignment
            color[v] = -1
        return False

    possible = dfs(0)

    out = []
    if possible:
        out.append("YES")
        # convert 0/1/2 to 1/2/3
        out.append(' '.join(str(c + 1) for c in color))
    else:
        out.append("NO")
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()