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

    # bit 0 -> colour 1, bit 1 -> colour 2, bit 2 -> colour 3
    ALL = 0b111
    allowed = [ALL] * n
    col = [-1] * n          # -1 = uncoloured, otherwise 0,1,2

    # ------------------------------------------------------------
    def dfs() -> bool:
        # find uncoloured vertex with fewest allowed colours
        v = -1
        min_cnt = 4
        for i in range(n):
            if col[i] == -1:
                cnt = allowed[i].bit_count()
                if cnt == 0:
                    return False          # dead end
                if cnt < min_cnt:
                    min_cnt = cnt
                    v = i
                    if cnt == 1:
                        break
        if v == -1:                     # all coloured
            return True

        mask = allowed[v]
        # try colours in order 0,1,2
        for c in range(3):
            bit = 1 << c
            if mask & bit:
                # assign colour c to v
                col[v] = c
                saved_allowed_v = allowed[v]
                allowed[v] = bit          # keep only this colour for v

                changed = []              # neighbours from which we removed the bit
                for nb in adj[v]:
                    if col[nb] == -1 and (allowed[nb] & bit):
                        allowed[nb] &= ~bit
                        changed.append(nb)

                if dfs():
                    return True

                # undo
                allowed[v] = saved_allowed_v
                for nb in changed:
                    allowed[nb] |= bit
                col[v] = -1
        return False
    # ------------------------------------------------------------

    possible = dfs()
    out = []
    if possible:
        out.append("YES")
        out.append(" ".join(str(col[i] + 1) for i in range(n)))
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()