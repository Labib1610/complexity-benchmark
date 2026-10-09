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

    # possible colours mask, bits 0..2 correspond to colours 1..3
    poss = [0b111] * n
    col = [0] * n                     # 0 = uncoloured, else 1..3
    popcnt = [0, 1, 1, 2, 1, 2, 2, 3]  # for numbers 0..7

    # choose vertex with Minimum Remaining Values (fewest possible colours)
    def select_vertex() -> int:
        best = -1
        best_cnt = 4
        for v in range(n):
            if col[v] == 0:
                cnt = popcnt[poss[v]]
                if cnt < best_cnt:
                    best_cnt = cnt
                    best = v
                    if cnt == 1:
                        break
        return best

    def dfs() -> bool:
        # all coloured?
        if all(col[v] != 0 for v in range(n)):
            return True

        v = select_vertex()
        mask = poss[v]
        # try colours 1,2,3
        for colour in (1, 2, 3):
            bit = 1 << (colour - 1)
            if mask & bit == 0:
                continue

            # assign colour
            col[v] = colour
            changed = []          # (neighbor, old_mask)
            ok = True

            for nb in adj[v]:
                if col[nb] == 0 and (poss[nb] & bit):
                    new_mask = poss[nb] & ~bit
                    if new_mask != poss[nb]:
                        changed.append((nb, poss[nb]))
                        poss[nb] = new_mask
                        if new_mask == 0:
                            ok = False
                            break

            if ok and dfs():
                return True

            # revert changes
            for nb, old in reversed(changed):
                poss[nb] = old
            col[v] = 0

        return False

    if dfs():
        out = ["YES", " ".join(str(c) for c in col)]
    else:
        out = ["NO"]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()