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

    # 0,1,2 are colours; mask 1<<c
    allowed = [0b111] * n
    assigned = [-1] * n

    # ------------------------------------------------------------
    def dfs(coloured_cnt: int) -> bool:
        if coloured_cnt == n:
            return True

        # MRV: vertex with fewest allowed colours
        v = -1
        best = 4
        for i in range(n):
            if assigned[i] == -1:
                cnt = allowed[i].bit_count()
                if cnt < best:
                    best = cnt
                    v = i
                    if cnt == 1:
                        break
        if v == -1:          # should not happen
            return True
        if best == 0:
            return False

        mask = allowed[v]
        for c in range(3):
            if not (mask & (1 << c)):
                continue
            # conflict with already coloured neighbours?
            conflict = False
            for nb in adj[v]:
                if assigned[nb] == c:
                    conflict = True
                    break
            if conflict:
                continue

            # assign colour c to v
            assigned[v] = c
            old_allowed_v = allowed[v]
            allowed[v] = 1 << c
            changes = []
            fail = False

            for nb in adj[v]:
                if assigned[nb] == -1:
                    if allowed[nb] & (1 << c):
                        old = allowed[nb]
                        allowed[nb] &= ~(1 << c)
                        changes.append((nb, old))
                        if allowed[nb] == 0:
                            fail = True
                            break

            if not fail:
                if dfs(coloured_cnt + 1):
                    return True

            # backtrack
            for nb, old in changes:
                allowed[nb] = old
            allowed[v] = old_allowed_v
            assigned[v] = -1

        return False
    # ------------------------------------------------------------

    possible = dfs(0)

    if not possible:
        print("NO")
    else:
        print("YES")
        # convert 0,1,2 -> 1,2,3
        out = [str(c + 1) for c in assigned]
        print(" ".join(out))


if __name__ == "__main__":
    solve()