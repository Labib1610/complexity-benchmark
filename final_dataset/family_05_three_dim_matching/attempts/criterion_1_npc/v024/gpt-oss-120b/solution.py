import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    rows_by_d = [[] for _ in range(k)]          # 0‑based
    triples = []                                 # (d,f,m) for output
    for idx in range(t):
        d = int(next(it)) - 1
        f = int(next(it)) - 1
        m = int(next(it)) - 1
        rows_by_d[d].append((f, m, idx))
        triples.append((d + 1, f + 1, m + 1))

    full_mask = (1 << k) - 1

    used_d = 0
    used_f = 0
    used_m = 0
    solution = []

    # pre‑compute for fast counting
    def count_candidates(d, used_f, used_m):
        cnt = 0
        for f, m, _ in rows_by_d[d]:
            if not (used_f >> f) & 1 and not (used_m >> m) & 1:
                cnt += 1
        return cnt

    def search() -> bool:
        nonlocal used_d, used_f, used_m
        if used_d == full_mask:          # all demographics taken
            return True

        # choose the unused demographic with fewest candidates
        best_d = -1
        best_cnt = 10**9
        for d in range(k):
            if (used_d >> d) & 1:
                continue
            cnt = count_candidates(d, used_f, used_m)
            if cnt == 0:
                return False
            if cnt < best_cnt:
                best_cnt = cnt
                best_d = d
                if cnt == 1:
                    break

        d = best_d
        for f, m, idx in rows_by_d[d]:
            if (used_f >> f) & 1 or (used_m >> m) & 1:
                continue
            # take this triple
            used_d |= 1 << d
            used_f |= 1 << f
            used_m |= 1 << m
            solution.append(idx)

            if search():
                return True

            # backtrack
            solution.pop()
            used_d ^= 1 << d
            used_f ^= 1 << f
            used_m ^= 1 << m

        return False

    if search():
        out = ["YES"]
        for idx in solution:
            out.append("{} {} {}".format(*triples[idx]))
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()