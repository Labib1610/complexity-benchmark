import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    rows_by_x = [[] for _ in range(k)]          # store (y, z, idx)
    triples = []
    for idx in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        triples.append((x, y, z))
        rows_by_x[x].append((y, z, idx))

    sys.setrecursionlimit(10000)

    from functools import lru_cache

    @lru_cache(maxsize=None)
    def dfs(used_x_mask: int, used_y_mask: int, used_z_mask: int):
        depth = used_x_mask.bit_count()
        if depth == k:
            return ()
        # choose an unused x with minimal viable candidates
        best_x = -1
        best_cands = None
        for x in range(k):
            if not (used_x_mask >> x) & 1:
                cand = []
                for y, z, idx in rows_by_x[x]:
                    if not (used_y_mask >> y) & 1 and not (used_z_mask >> z) & 1:
                        cand.append((y, z, idx))
                if not cand:
                    return None
                if best_cands is None or len(cand) < len(best_cands):
                    best_cands = cand
                    best_x = x
                    if len(best_cands) == 1:
                        break
        # try each candidate
        for y, z, idx in best_cands:
            res = dfs(used_x_mask | (1 << best_x),
                      used_y_mask | (1 << y),
                      used_z_mask | (1 << z))
            if res is not None:
                return ((best_x, y, z),) + res
        return None

    ans = dfs(0, 0, 0)
    out = []
    if ans is None:
        out.append("NO")
    else:
        out.append("YES")
        for x, y, z in ans:
            out.append(f"{x+1} {y+1} {z+1}")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()