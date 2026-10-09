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

    # 0 = uncoloured, 1..3 = colour
    col = [0] * n
    # mask of possible colours, bit 0->1, bit1->2, bit2->3
    mask = [0b111] * n

    # pre‑compute popcount for masks 0..7 (optional)
    popcnt = [bin(i).count('1') for i in range(8)]

    def dfs(coloured_cnt: int) -> bool:
        if coloured_cnt == n:
            return True

        # choose vertex with minimum remaining colours
        v = -1
        best = 4
        for i in range(n):
            if col[i] == 0:
                cnt = popcnt[mask[i]]
                if cnt < best:
                    best = cnt
                    v = i
                    if cnt == 1:
                        break
        if best == 0:          # dead end
            return False

        cur_mask = mask[v]
        # try colours 1,2,3 that are still possible
        for c in (1, 2, 3):
            if not (cur_mask & (1 << (c - 1))):
                continue

            # assign colour c to v
            col[v] = c
            changed = []          # list of (vertex, old_mask)
            ok = True

            for nb in adj[v]:
                if col[nb] == 0:
                    if mask[nb] & (1 << (c - 1)):
                        old = mask[nb]
                        new = old & ~(1 << (c - 1))
                        if new != old:
                            changed.append((nb, old))
                            mask[nb] = new
                            if new == 0:
                                ok = False
                                break
                elif col[nb] == c:
                    ok = False
                    break

            if ok and dfs(coloured_cnt + 1):
                return True

            # backtrack: restore masks and colour
            for u, old in reversed(changed):
                mask[u] = old
            col[v] = 0

        return False

    possible = dfs(0)

    out = sys.stdout
    if not possible:
        out.write("NO\n")
    else:
        out.write("YES\n")
        out.write(' '.join(str(col[i]) for i in range(n)) + "\n")

if __name__ == "__main__":
    solve()