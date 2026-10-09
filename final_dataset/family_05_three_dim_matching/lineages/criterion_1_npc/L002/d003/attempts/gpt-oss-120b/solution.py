import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    triples = []                     # (u,v,w,original_index)
    by_u = [[] for _ in range(k)]
    by_v = [[] for _ in range(k)]
    by_w = [[] for _ in range(k)]

    for idx in range(t):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it)) - 1
        triples.append((u, v, w, idx))
        by_u[u].append(idx)
        by_v[v].append(idx)
        by_w[w].append(idx)

    # quick impossibility test: each dimension must have at least k triples covering it
    if any(len(lst) < k for lst in (by_u, by_v, by_w)):
        print("NO")
        return

    # recursion
    full_mask = (1 << k) - 1

    def search(used_u, used_v, used_w, chosen):
        if len(chosen) == k:
            return chosen

        # heuristic: pick uncovered value with fewest usable triples
        best_candidates = None
        best_dim = None
        best_val = None

        # helper to evaluate a dimension
        def evaluate(dim_list, used_mask, other1_mask, other2_mask, dim):
            nonlocal best_candidates, best_dim, best_val
            for val, lst in enumerate(dim_list):
                if (used_mask >> val) & 1:
                    continue
                cand = []
                for ti in lst:
                    u, v, w, _ = triples[ti]
                    if ((used_u >> u) & 1) or ((used_v >> v) & 1) or ((used_w >> w) & 1):
                        continue
                    cand.append(ti)
                if not cand:
                    return False  # dead end
                if best_candidates is None or len(cand) < len(best_candidates):
                    best_candidates = cand
                    best_dim = dim
                    best_val = val
            return True

        # try each dimension
        if not evaluate(by_u, used_u, used_v, used_w, 'u'):
            return None
        if not evaluate(by_v, used_v, used_u, used_w, 'v'):
            return None
        if not evaluate(by_w, used_w, used_u, used_v, 'w'):
            return None

        # now branch on the selected candidates
        for ti in best_candidates:
            u, v, w, _ = triples[ti]
            # set bits
            if ((used_u >> u) & 1) or ((used_v >> v) & 1) or ((used_w >> w) & 1):
                continue
            res = search(used_u | (1 << u), used_v | (1 << v), used_w | (1 << w), chosen + [ti])
            if res is not None:
                return res
        return None

    ans = search(0, 0, 0, [])
    if ans is None:
        print("NO")
    else:
        print("YES")
        out = []
        for ti in ans:
            u, v, w, _ = triples[ti]
            out.append(f"{u+1} {v+1} {w+1}")
        sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()