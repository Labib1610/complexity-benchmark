import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 2:
        return

    k, t = data[0], data[1]
    triples = []
    column_rows = [0] * (3 * k)

    p = 2
    for row in range(t):
        f = data[p] - 1
        c = data[p + 1] - 1
        m = data[p + 2] - 1
        p += 3

        triples.append((f, c, m))
        bit = 1 << row
        column_rows[f] |= bit
        column_rows[k + c] |= bit
        column_rows[2 * k + m] |= bit

    if k == 0:
        print("YES")
        return
    if t < k:
        print("NO")
        return

    row_conflicts = [0] * t
    for i, (f, c, m) in enumerate(triples):
        row_conflicts[i] = (
            column_rows[f]
            | column_rows[k + c]
            | column_rows[2 * k + m]
        )

    all_rows = (1 << t) - 1
    all_columns = (1 << (3 * k)) - 1
    part_mask = (1 << k) - 1

    failed = set()
    answer = []
    memo_limit = 600000

    def has_perfect_matching(adj, left_mask, right_mask):
        left_vertices = []
        bits = left_mask
        while bits:
            b = bits & -bits
            u = b.bit_length() - 1
            if not (adj[u] & right_mask):
                return False
            left_vertices.append(u)
            bits ^= b

        left_vertices.sort(key=lambda u: (adj[u] & right_mask).bit_count())
        match_right = [-1] * k

        def augment(u, seen):
            candidates = adj[u] & right_mask & ~seen[0]
            while candidates:
                b = candidates & -candidates
                candidates ^= b
                v = b.bit_length() - 1
                seen[0] |= b
                old = match_right[v]
                if old == -1 or augment(old, seen):
                    match_right[v] = u
                    return True
            return False

        for u in left_vertices:
            if not augment(u, [0]):
                return False
        return True

    def pairwise_feasible(active, uncovered):
        rem_f = uncovered & part_mask
        rem_c = (uncovered >> k) & part_mask
        rem_m = (uncovered >> (2 * k)) & part_mask

        fc = [0] * k
        fm = [0] * k
        cm = [0] * k

        rows = active
        while rows:
            b = rows & -rows
            rows ^= b
            idx = b.bit_length() - 1
            f, c, m = triples[idx]
            fc[f] |= 1 << c
            fm[f] |= 1 << m
            cm[c] |= 1 << m

        return (
            has_perfect_matching(fc, rem_f, rem_c)
            and has_perfect_matching(fm, rem_f, rem_m)
            and has_perfect_matching(cm, rem_c, rem_m)
        )

    sys.setrecursionlimit(10000)

    def dfs(active, uncovered):
        if uncovered == 0:
            return True
        if uncovered in failed:
            return False

        cols = uncovered
        best_candidates = 0
        best_count = t + 1

        while cols:
            b = cols & -cols
            cols ^= b
            col = b.bit_length() - 1
            candidates = active & column_rows[col]
            count = candidates.bit_count()

            if count == 0:
                if len(failed) < memo_limit:
                    failed.add(uncovered)
                return False

            if count < best_count:
                best_count = count
                best_candidates = candidates
                if count == 1:
                    break

        if best_count > 1 and not pairwise_feasible(active, uncovered):
            if len(failed) < memo_limit:
                failed.add(uncovered)
            return False

        candidate_rows = []
        rows = best_candidates
        while rows:
            b = rows & -rows
            rows ^= b
            idx = b.bit_length() - 1
            score = (active & row_conflicts[idx]).bit_count()
            candidate_rows.append((score, idx))

        candidate_rows.sort()

        for _, idx in candidate_rows:
            f, c, m = triples[idx]
            removed_columns = (1 << f) | (1 << (k + c)) | (1 << (2 * k + m))
            new_uncovered = uncovered & ~removed_columns
            new_active = active & ~row_conflicts[idx]

            answer.append(idx)
            if dfs(new_active, new_uncovered):
                return True
            answer.pop()

        if len(failed) < memo_limit:
            failed.add(uncovered)
        return False

    if dfs(all_rows, all_columns):
        out = ["YES"]
        for idx in answer:
            f, c, m = triples[idx]
            out.append(f"{f + 1} {c + 1} {m + 1}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()