import sys

sys.setrecursionlimit(1000000)

def solve() -> None:
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    k = next(it)
    t = next(it)

    triples = []                     # original triples, 1‑based for output
    by_op = [[] for _ in range(k)]   # per operator: (term, shift, idx)

    for idx in range(t):
        x = next(it) - 1
        y = next(it) - 1
        z = next(it) - 1
        triples.append((x + 1, y + 1, z + 1))   # keep 1‑based for printing
        by_op[x].append((y, z, idx))

    solution = []                    # indices of chosen triples

    # -------------------------------------------------------------
    def dfs(used_op: int, used_term: int, used_shift: int) -> bool:
        """return True if a perfect matching can be completed"""
        if len(solution) == k:
            return True

        best_op = -1
        best_opts = None
        best_len = 10 ** 9

        # choose the operator with the smallest number of still feasible triples
        for op in range(k):
            if (used_op >> op) & 1:
                continue
            opts = []
            for term, shift, idx in by_op[op]:
                if ((used_term >> term) & 1) == 0 and ((used_shift >> shift) & 1) == 0:
                    opts.append((term, shift, idx))
            if not opts:                     # dead end
                return False
            if len(opts) < best_len:
                best_len = len(opts)
                best_op = op
                best_opts = opts
                if best_len == 1:
                    break

        # try all possibilities for the selected operator
        for term, shift, idx in best_opts:
            solution.append(idx)
            if dfs(used_op | (1 << best_op),
                   used_term | (1 << term),
                   used_shift | (1 << shift)):
                return True
            solution.pop()
        return False
    # -------------------------------------------------------------

    possible = dfs(0, 0, 0)

    out_lines = []
    if possible:
        out_lines.append("YES")
        for idx in solution:
            x, y, z = triples[idx]
            out_lines.append(f"{x} {y} {z}")
    else:
        out_lines.append("NO")

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()