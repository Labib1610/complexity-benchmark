import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 2:
        return

    k, t = data[0], data[1]
    ncols = 3 * k

    xs = [0] * t
    ys = [0] * t
    zs = [0] * t
    col_rows = [0] * ncols

    pos = 2
    for r in range(t):
        x = data[pos] - 1
        y = data[pos + 1] - 1
        z = data[pos + 2] - 1
        pos += 3

        xs[r] = x
        ys[r] = y
        zs[r] = z

        bit = 1 << r
        col_rows[x] |= bit
        col_rows[k + y] |= bit
        col_rows[2 * k + z] |= bit

    if t == 0:
        print("NO")
        return

    for bits in col_rows:
        if bits == 0:
            print("NO")
            return

    components = (xs, ys, zs)
    full_part = (1 << k) - 1
    all_uncovered = (1 << ncols) - 1
    all_active = (1 << t) - 1

    chosen = []
    dead = set()
    memo_limit = 500000

    def has_pair_matching(active, uncovered, left_part, right_part):
        left_mask = (uncovered >> (left_part * k)) & full_part
        right_mask = (uncovered >> (right_part * k)) & full_part

        if left_mask.bit_count() != right_mask.bit_count():
            return False

        left_values = []
        b = left_mask
        while b:
            lb = b & -b
            left_values.append(lb.bit_length() - 1)
            b -= lb

        if not left_values:
            return True

        left_comp = components[left_part]
        right_comp = components[right_part]
        adjs = [0] * k

        for u in left_values:
            rows = active & col_rows[left_part * k + u]
            adj = 0
            while rows:
                rb = rows & -rows
                r = rb.bit_length() - 1
                adj |= 1 << right_comp[r]
                rows -= rb
            adj &= right_mask
            if adj == 0:
                return False
            adjs[u] = adj

        left_values.sort(key=lambda u: adjs[u].bit_count())
        match_right = [-1] * k

        def augment(u, seen):
            available = adjs[u] & ~seen[0]
            while available:
                vb = available & -available
                available -= vb
                seen[0] |= vb
                v = vb.bit_length() - 1
                old = match_right[v]
                if old == -1 or augment(old, seen):
                    match_right[v] = u
                    return True
            return False

        for u in left_values:
            if not augment(u, [0]):
                return False
        return True

    sys.setrecursionlimit(10000)

    def search(active, uncovered, depth):
        if uncovered == 0:
            return True

        if uncovered in dead:
            return False

        best_col = -1
        best_count = t + 1
        degrees = [0] * ncols

        cols = uncovered
        while cols:
            cb = cols & -cols
            c = cb.bit_length() - 1
            cnt = (active & col_rows[c]).bit_count()
            degrees[c] = cnt

            if cnt == 0:
                if len(dead) < memo_limit:
                    dead.add(uncovered)
                return False

            if cnt < best_count:
                best_count = cnt
                best_col = c
                if cnt == 1:
                    break
            cols -= cb

        if depth % 3 == 0:
            if not has_pair_matching(active, uncovered, 0, 1):
                if len(dead) < memo_limit:
                    dead.add(uncovered)
                return False
            if not has_pair_matching(active, uncovered, 0, 2):
                if len(dead) < memo_limit:
                    dead.add(uncovered)
                return False
            if not has_pair_matching(active, uncovered, 1, 2):
                if len(dead) < memo_limit:
                    dead.add(uncovered)
                return False

        candidate_bits = active & col_rows[best_col]

        if best_count == 1:
            candidate_rows = [candidate_bits.bit_length() - 1]
        else:
            candidate_rows = []
            bits = candidate_bits
            while bits:
                rb = bits & -bits
                candidate_rows.append(rb.bit_length() - 1)
                bits -= rb

            def row_score(r):
                return (
                    degrees[xs[r]]
                    + degrees[k + ys[r]]
                    + degrees[2 * k + zs[r]]
                )

            candidate_rows.sort(key=row_score)

        for r in candidate_rows:
            c1 = xs[r]
            c2 = k + ys[r]
            c3 = 2 * k + zs[r]

            covered = (1 << c1) | (1 << c2) | (1 << c3)
            conflicting = col_rows[c1] | col_rows[c2] | col_rows[c3]

            chosen.append(r)
            if search(active & ~conflicting, uncovered & ~covered, depth + 1):
                return True
            chosen.pop()

        if len(dead) < memo_limit:
            dead.add(uncovered)
        return False

    if search(all_active, all_uncovered, 0):
        out = ["YES"]
        for r in chosen:
            out.append(f"{xs[r] + 1} {ys[r] + 1} {zs[r] + 1}")
        sys.stdout.write("\n".join(out))
    else:
        print("NO")

if __name__ == "__main__":
    main()