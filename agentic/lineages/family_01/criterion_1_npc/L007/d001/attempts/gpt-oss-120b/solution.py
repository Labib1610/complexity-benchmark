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
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            continue
        adj[u].append(v)
        adj[v].append(u)

    # 0 = uncoloured, otherwise 1..3
    color = [0] * n
    # 3-bit mask, bit i -> colour i+1 allowed
    possible = [0b111] * n

    # depth‑first search, vertices processed in order 0..n-1
    def dfs(v: int) -> bool:
        if v == n:
            return True

        # colours still allowed by forward checking
        mask = possible[v]
        # forbid colours already used by coloured neighbours
        for nb in adj[v]:
            c = color[nb]
            if c:
                mask &= ~(1 << (c - 1))
        if mask == 0:
            return False

        for col in (1, 2, 3):
            bit = 1 << (col - 1)
            if not (mask & bit):
                continue

            # assign colour
            color[v] = col
            changed = []          # list of (vertex, old_mask)

            conflict = False
            for nb in adj[v]:
                if color[nb] == 0:
                    if possible[nb] & bit:
                        old = possible[nb]
                        new = old & ~bit
                        possible[nb] = new
                        changed.append((nb, old))
                        if new == 0:
                            conflict = True
                            break
            if not conflict:
                if dfs(v + 1):
                    return True

            # undo changes
            for nb, old in changed:
                possible[nb] = old
            color[v] = 0

        return False

    if dfs(0):
        out = ['YES', ' '.join(str(c) for c in color)]
    else:
        out = ['NO']
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()