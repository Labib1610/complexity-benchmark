import sys

sys.setrecursionlimit(1000000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    triples_by_source = [[] for _ in range(k)]  # store (y, z)
    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it))
        z = int(next(it))
        triples_by_source[x].append((y, z))

    # quick impossibility check: each source must have at least one triple
    for lst in triples_by_source:
        if not lst:
            print("NO")
            return

    usedS = 0
    usedT = 0
    usedD = 0
    path = []

    # memoization of dead states could help, but not necessary for k<=22
    def dfs() -> bool:
        nonlocal usedS, usedT, usedD
        if len(path) == k:
            return True

        # choose the unassigned source with fewest viable options
        best_s = -1
        best_opts = None
        for s in range(k):
            if not (usedS >> s) & 1:
                opts = []
                for y, z in triples_by_source[s]:
                    if not (usedT >> (y - 1)) & 1 and not (usedD >> (z - 1)) & 1:
                        opts.append((y, z))
                if not opts:   # dead end
                    return False
                if best_s == -1 or len(opts) < len(best_opts):
                    best_s = s
                    best_opts = opts
                    if len(best_opts) == 1:
                        break

        # mark source as used
        usedS |= 1 << best_s
        for y, z in best_opts:
            if (usedT >> (y - 1)) & 1 or (usedD >> (z - 1)) & 1:
                continue
            # choose this triple
            path.append((best_s + 1, y, z))
            usedT |= 1 << (y - 1)
            usedD |= 1 << (z - 1)

            if dfs():
                return True

            # backtrack
            path.pop()
            usedT &= ~(1 << (y - 1))
            usedD &= ~(1 << (z - 1))

        # unmark source
        usedS &= ~(1 << best_s)
        return False

    if dfs():
        print("YES")
        out = "\n".join(f"{x} {y} {z}" for x, y, z in path)
        sys.stdout.write(out + ("\n" if out else ""))
    else:
        print("NO")


if __name__ == "__main__":
    solve()