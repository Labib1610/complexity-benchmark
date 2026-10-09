import sys

sys.setrecursionlimit(1000000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    triples = []                     # (s,m,z,original_index)
    by_spec = [[] for _ in range(k)]

    for idx in range(t):
        s = int(next(it)) - 1
        m = int(next(it)) - 1
        z = int(next(it)) - 1
        triples.append((s, m, z, idx))
        by_spec[s].append((m, z, idx))

    full_mask = (1 << k) - 1
    chosen = []                      # stores indices of selected rows (reverse order)

    # memoisation could be added, but not needed for given limits
    def dfs(free_spec: int, free_mach: int, free_time: int) -> bool:
        if free_spec == 0:
            return True

        # choose specialist with fewest usable rows
        best_s = -1
        best_opts = None

        spec = free_spec
        while spec:
            s = (spec & -spec).bit_length() - 1
            spec ^= 1 << s
            opts = []
            for m, z, idx in by_spec[s]:
                if (free_mach >> m) & 1 and (free_time >> z) & 1:
                    opts.append((m, z, idx))
            if not opts:
                return False
            if best_opts is None or len(opts) < len(best_opts):
                best_opts = opts
                best_s = s
                if len(best_opts) == 1:
                    break

        # try each option
        for m, z, idx in best_opts:
            if dfs(free_spec ^ (1 << best_s),
                   free_mach ^ (1 << m),
                   free_time ^ (1 << z)):
                chosen.append(idx)
                return True
        return False

    if dfs(full_mask, full_mask, full_mask):
        out = ["YES"]
        # reverse to original order of selection (any order is fine)
        for idx in reversed(chosen):
            s, m, z, _ = triples[idx]
            out.append(f"{s+1} {m+1} {z+1}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()