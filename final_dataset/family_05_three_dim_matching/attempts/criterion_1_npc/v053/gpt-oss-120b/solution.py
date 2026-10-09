import sys

sys.setrecursionlimit(1000000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    triples = [[] for _ in range(k)]          # per frequency x (0‑based)
    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        triples[x].append((y, z, (x + 1, y + 1, z + 1)))   # keep original for output

    # quick impossibility test: every frequency must have at least one triple
    for lst in triples:
        if not lst:
            print("NO")
            return

    used_y = 0          # bit i set  -> voltage (i+1) already taken
    used_z = 0
    assigned = []       # list of original triples
    free_x = set(range(k))

    # -------------------------------------------------------------
    def dfs() -> bool:
        nonlocal used_y, used_z

        if not free_x:                     # all frequencies assigned
            return True

        # choose frequency with minimum remaining options
        best_x = None
        best_opts = None

        for x in free_x:
            opts = []
            for y, z, orig in triples[x]:
                if (used_y >> y) & 1:
                    continue
                if (used_z >> z) & 1:
                    continue
                opts.append((y, z, orig))
            cnt = len(opts)
            if cnt == 0:
                return False                # dead end
            if best_opts is None or cnt < len(best_opts):
                best_opts = opts
                best_x = x
                if cnt == 1:                # cannot be better
                    break

        # branch on the chosen frequency
        free_x.remove(best_x)
        for y, z, orig in best_opts:
            used_y |= (1 << y)
            used_z |= (1 << z)
            assigned.append(orig)

            if dfs():
                return True

            # backtrack
            assigned.pop()
            used_y ^= (1 << y)
            used_z ^= (1 << z)

        free_x.add(best_x)
        return False
    # -------------------------------------------------------------

    if dfs():
        print("YES")
        out_lines = ["{} {} {}".format(*tr) for tr in assigned]
        sys.stdout.write("\n".join(out_lines))
    else:
        print("NO")


if __name__ == "__main__":
    solve()