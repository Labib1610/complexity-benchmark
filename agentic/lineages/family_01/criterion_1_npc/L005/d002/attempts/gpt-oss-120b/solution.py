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

    degree = [len(adj[i]) for i in range(n)]
    # initial masks: 0b111 = 7, all three colours possible
    mask = [7] * n
    colour = [0] * n  # 0 = uncoloured, else 1/2/3

    # pre‑order for tie‑break (higher degree first)
    order = sorted(range(n), key=lambda x: -degree[x])

    # helper: popcount of 3‑bit mask
    popcnt = lambda x: (x & 1) + ((x >> 1) & 1) + ((x >> 2) & 1)

    def dfs(coloured_cnt: int) -> bool:
        if coloured_cnt == n:
            return True

        # MRV selection
        v = -1
        best = 4
        best_deg = -1
        for u in range(n):
            if colour[u] != 0:
                continue
            d = popcnt(mask[u])
            if d < best or (d == best and degree[u] > best_deg):
                best = d
                v = u
                best_deg = degree[u]
        if best == 0:
            return False

        saved = []  # list of (vertex, old_mask)

        for c in (1, 2, 3):
            bit = 1 << (c - 1)
            if not (mask[v] & bit):
                continue
            colour[v] = c
            ok = True
            # forward checking
            for nb in adj[v]:
                if colour[nb] != 0:
                    continue
                if mask[nb] & bit:
                    saved.append((nb, mask[nb]))
                    mask[nb] &= ~bit
                    if mask[nb] == 0:
                        ok = False
                        break
            if ok and dfs(coloured_cnt + 1):
                return True
            # undo
            for u, old in reversed(saved):
                mask[u] = old
            saved.clear()
            colour[v] = 0
        return False

    if dfs(0):
        out = ['YES', ' '.join(str(colour[i]) for i in range(n))]
        sys.stdout.write('\n'.join(out))
    else:
        sys.stdout.write('NO')

if __name__ == "__main__":
    solve()