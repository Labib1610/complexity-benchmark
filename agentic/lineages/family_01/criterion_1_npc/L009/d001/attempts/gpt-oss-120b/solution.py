import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # adjacency lists
    neigh = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        neigh[u].append(v)
        neigh[v].append(u)

    # 0 = uncoloured, otherwise 1..3
    col = [0] * n
    # bitmask of allowed colours, bit 0 -> colour 1, etc.
    allow = [0b111] * n   # all three colours possible initially

    # depth‑first search with forward checking
    def dfs(idx: int) -> bool:
        if idx == n:
            return True

        cur_allowed = allow[idx]
        for colour in (1, 2, 3):
            mask = 1 << (colour - 1)
            if not (cur_allowed & mask):
                continue

            # assign colour
            col[idx] = colour
            changes = []          # (vertex, previous_mask)
            ok = True

            for u in neigh[idx]:
                if col[u] != 0:
                    continue
                old = allow[u]
                new = old & ~mask
                if new != old:
                    changes.append((u, old))
                    allow[u] = new
                    if new == 0:
                        ok = False
                        break

            if ok and dfs(idx + 1):
                return True

            # backtrack
            for u, old in reversed(changes):
                allow[u] = old
            col[idx] = 0

        return False

    if dfs(0):
        out = ['YES', ' '.join(str(c) for c in col)]
    else:
        out = ['NO']
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()