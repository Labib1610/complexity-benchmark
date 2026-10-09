import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * n                     # bitmask of neighbours
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    col = [0] * n                     # 0 = uncoloured, else 1..3
    mask = [0, 0, 0, 0]               # mask[c] = vertices coloured c

    # ------------------------------------------------------------
    # existence test: can the current partial colouring be completed?
    def exists() -> bool:
        # find uncoloured vertex with fewest possible colours
        best_v = -1
        best_opts = 0
        min_cnt = 4                     # more than max possible (3)
        for v in range(n):
            if col[v]:
                continue
            opts = 0
            for c in (1, 2, 3):
                if (adj[v] & mask[c]) == 0:
                    opts |= 1 << c
            cnt = opts.bit_count()
            if cnt == 0:
                return False
            if cnt < min_cnt:
                min_cnt = cnt
                best_v = v
                best_opts = opts
                if cnt == 1:
                    break
        if best_v == -1:                # all coloured
            return True

        # try colours in natural order 1,2,3
        for c in (1, 2, 3):
            if best_opts & (1 << c):
                col[best_v] = c
                mask[c] |= 1 << best_v
                if exists():
                    # undo before returning, we only need existence
                    col[best_v] = 0
                    mask[c] &= ~(1 << best_v)
                    return True
                col[best_v] = 0
                mask[c] &= ~(1 << best_v)
        return False
    # ------------------------------------------------------------

    # build lexicographically smallest assignment
    for i in range(n):
        placed = False
        for c in (1, 2, 3):
            if (adj[i] & mask[c]) != 0:          # conflict with already fixed neighbours
                continue
            col[i] = c
            mask[c] |= 1 << i
            if exists():
                placed = True
                break
            # not feasible, revert
            col[i] = 0
            mask[c] &= ~(1 << i)
        if not placed:
            print("NO")
            return

    # all vertices coloured
    print("YES")
    print(' '.join(str(col[i]) for i in range(n)))

if __name__ == "__main__":
    solve()