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

    # 0 = uncoloured, 1..3 = colour
    color = [0] * n
    # 3-bit mask, bit 0 -> colour 1, bit 1 -> colour 2, bit 2 -> colour 3
    allowed = [0b111] * n

    # pre‑compute popcount for 0..7 (optional)
    popcnt = [bin(i).count('1') for i in range(8)]

    def dfs(coloured: int) -> bool:
        if coloured == n:
            return True

        # MRV: vertex with smallest number of allowed colours
        v = -1
        best = 4
        for i in range(n):
            if color[i] == 0:
                cnt = popcnt[allowed[i]]
                if cnt < best:
                    best = cnt
                    v = i
                    if cnt == 1:
                        break
        if best == 0:          # no colour possible
            return False

        mask = allowed[v]
        # try colours 1,2,3
        for c in (1, 2, 3):
            bit = 1 << (c - 1)
            if mask & bit:
                # assign
                color[v] = c
                changed = []          # neighbours whose mask we modify
                neigh = adj[v]
                while neigh:
                    lsb = neigh & -neigh
                    u = (lsb.bit_length() - 1)
                    if color[u] == 0 and (allowed[u] & bit):
                        allowed[u] &= ~bit
                        changed.append(u)
                    neigh ^= lsb
                if dfs(coloured + 1):
                    return True
                # undo
                for u in changed:
                    allowed[u] |= bit
                color[v] = 0
        return False

    if dfs(0):
        out = ['YES', ' '.join(str(c) for c in color)]
    else:
        out = ['NO']
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()