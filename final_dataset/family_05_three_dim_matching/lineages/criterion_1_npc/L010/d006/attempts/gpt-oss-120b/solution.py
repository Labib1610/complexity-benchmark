import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    triples = []
    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        triples.append((a, b, c))

    if k == 1:
        if t >= 1:
            print("YES")
            a, b, c = triples[0]
            print(a + 1, b + 1, c + 1)
        else:
            print("NO")
        return

    # quick impossibility check
    if t < k:
        print("NO")
        return

    # column numbering:
    # 0..k-1               -> first component (A)
    # k..2k-1              -> second component (B)
    # 2k..3k-1             -> third component (C)
    ncols = 3 * k
    rows = []                     # list of (colA, colB, colC)
    col_rows = [[] for _ in range(ncols)]

    for idx, (a, b, c) in enumerate(triples):
        ca = a
        cb = k + b
        cc = 2 * k + c
        rows.append((ca, cb, cc))
        col_rows[ca].append(idx)
        col_rows[cb].append(idx)
        col_rows[cc].append(idx)

    # initial sets
    all_rows = set(range(len(rows)))
    uncovered = set(range(ncols))

    # ---------- recursive exact cover ----------
    def search(selected, remaining, uncovered_cols):
        if not uncovered_cols:          # all columns covered
            return selected

        # choose column with the fewest remaining rows (heuristic)
        best_col = None
        best_cnt = None
        for col in uncovered_cols:
            cnt = 0
            for r in col_rows[col]:
                if r in remaining:
                    cnt += 1
            if cnt == 0:                # dead end
                return None
            if best_cnt is None or cnt < best_cnt:
                best_cnt = cnt
                best_col = col
                if cnt == 1:
                    break

        # try every row that covers the chosen column
        for r in col_rows[best_col]:
            if r not in remaining:
                continue
            ca, cb, cc = rows[r]
            # rows that intersect any of the three columns
            to_remove = set()
            for col in (ca, cb, cc):
                for rr in col_rows[col]:
                    if rr in remaining:
                        to_remove.add(rr)

            new_remaining = remaining - to_remove
            new_uncovered = uncovered_cols - {ca, cb, cc}
            res = search(selected + [r], new_remaining, new_uncovered)
            if res is not None:
                return res
        return None

    solution = search([], all_rows, uncovered)

    if solution is None:
        print("NO")
    else:
        print("YES")
        out = []
        for r in solution:
            a, b, c = triples[r]
            out.append(f"{a+1} {b+1} {c+1}")
        sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()