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
        adj[u].append(v)
        adj[v].append(u)

    # 0 = uncoloured, 1..3 = colour
    col = [0] * n
    # domain masks, bit 0 -> colour 1, bit 1 -> colour 2, bit 2 -> colour 3
    dom = [0b111] * n

    # depth‑first search with forward checking
    def dfs() -> bool:
        # find first uncoloured vertex (lexicographic order)
        v = -1
        for i in range(n):
            if col[i] == 0:
                v = i
                break
        if v == -1:          # all coloured
            return True

        mask = dom[v]
        for c in (1, 2, 3):
            bit = 1 << (c - 1)
            if not (mask & bit):
                continue

            # assign colour c to v
            col[v] = c
            changed = []          # (vertex, previous_mask)
            conflict = False

            for u in adj[v]:
                if col[u] == 0 and (dom[u] & bit):
                    prev = dom[u]
                    dom[u] &= ~bit
                    changed.append((u, prev))
                    if dom[u] == 0:
                        conflict = True
                        break

            if not conflict:
                if dfs():
                    return True

            # undo changes
            for u, prev in reversed(changed):
                dom[u] = prev
            col[v] = 0

        return False

    if dfs():
        out = ['YES', ' '.join(str(c) for c in col)]
    else:
        out = ['NO']
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()