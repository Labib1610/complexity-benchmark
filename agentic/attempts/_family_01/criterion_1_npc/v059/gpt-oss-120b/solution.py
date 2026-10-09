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

    # colour 0 = uncoloured, otherwise 1..3
    col = [0] * n
    # allowed[v]: bitmask 0b001 -> colour 1, 0b010 -> colour 2, 0b100 -> colour 3
    allowed = [0b111] * n

    # pre‑compute popcount for masks 0..7 (optional)
    popcnt = [bin(i).count('1') for i in range(8)]

    def dfs(coloured_cnt: int) -> bool:
        if coloured_cnt == n:
            return True

        # MRV: vertex with minimum number of still allowed colours
        v = -1
        best = 4  # larger than any possible count
        for i in range(n):
            if col[i] == 0:
                cnt = popcnt[allowed[i]]
                if cnt < best:
                    best = cnt
                    v = i
                    if cnt == 1:
                        break
        if v == -1:               # should not happen
            return True

        avail = allowed[v]
        # try colours 1,2,3 in order
        for c in (1, 2, 3):
            bit = 1 << (c - 1)
            if not (avail & bit):
                continue

            # assign colour
            col[v] = c
            changed = []          # (vertex, previous_allowed)
            contradiction = False

            for nb in adj[v]:
                if col[nb] == 0 and (allowed[nb] & bit):
                    prev = allowed[nb]
                    allowed[nb] = prev & ~bit
                    changed.append((nb, prev))
                    if allowed[nb] == 0:
                        contradiction = True
                        break

            if not contradiction:
                if dfs(coloured_cnt + 1):
                    return True

            # undo changes
            for nb, prev in changed:
                allowed[nb] = prev
            col[v] = 0

        return False

    possible = dfs(0)

    out = []
    if not possible:
        out.append("NO")
    else:
        out.append("YES")
        out.append(" ".join(str(col[i]) for i in range(n)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()