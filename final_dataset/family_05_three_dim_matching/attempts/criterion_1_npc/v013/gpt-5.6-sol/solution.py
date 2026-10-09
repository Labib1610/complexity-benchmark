import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 2:
        return

    k, t = data[0], data[1]
    rows = []
    row_vectors = []
    column_rows = [0] * (3 * k)

    pair_xy = [0] * (k * k)
    pair_xz = [0] * (k * k)
    pair_yz = [0] * (k * k)

    pos = 2
    for r in range(t):
        x = data[pos] - 1
        y = data[pos + 1] - 1
        z = data[pos + 2] - 1
        pos += 3

        rows.append((x, y, z))
        vec = (1 << x) | (1 << (k + y)) | (1 << (2 * k + z))
        row_vectors.append(vec)

        bit = 1 << r
        column_rows[x] |= bit
        column_rows[k + y] |= bit
        column_rows[2 * k + z] |= bit

        pair_xy[x * k + y] |= bit
        pair_xz[x * k + z] |= bit
        pair_yz[y * k + z] |= bit

    if k == 0:
        print("YES")
        return
    if t == 0:
        print("NO")
        return

    all_columns = (1 << (3 * k)) - 1
    full_resource_mask = (1 << k) - 1
    all_active = (1 << t) - 1

    conflicts = [0] * t
    for r, (x, y, z) in enumerate(rows):
        conflicts[r] = (
            column_rows[x]
            | column_rows[k + y]
            | column_rows[2 * k + z]
        )

    def parity_consistent(active, target):
        basis = [0] * (3 * k)
        a = active

        while a:
            lb = a & -a
            r = lb.bit_length() - 1
            a ^= lb

            v = row_vectors[r]
            while v:
                p = v.bit_length() - 1
                b = basis[p]
                if b:
                    v ^= b
                else:
                    basis[p] = v
                    if (target >> p) & 1:
                        target ^= v
                        if target == 0:
                            return True
                    break

        return target == 0

    def projection_has_matching(active, left_mask, right_mask, pair_rows):
        adjacency = []
        lm = left_mask

        while lm:
            lb = lm & -lm
            u = lb.bit_length() - 1
            lm ^= lb

            neighbors = 0
            rm = right_mask
            while rm:
                rb = rm & -rm
                v = rb.bit_length() - 1
                rm ^= rb
                if pair_rows[u * k + v] & active:
                    neighbors |= rb

            if neighbors == 0:
                return False
            adjacency.append((neighbors.bit_count(), u, neighbors))

        adjacency.sort()
        match_right = [-1] * k

        def augment(u, seen):
            choices = adj_by_left[u] & right_mask & ~seen
            while choices:
                vb = choices & -choices
                choices ^= vb
                v = vb.bit_length() - 1
                previous = match_right[v]
                if previous == -1 or augment(previous, seen | vb):
                    match_right[v] = u
                    return True
            return False

        adj_by_left = [0] * k
        for _, u, neighbors in adjacency:
            adj_by_left[u] = neighbors

        for _, u, _ in adjacency:
            if not augment(u, 0):
                return False
        return True

    failed = set()
    memo_limit = 500_000
    chosen = []

    sys.setrecursionlimit(10000)

    def search(active, covered, depth):
        if depth == k:
            return covered == all_columns

        if covered in failed:
            return False

        uncovered = all_columns ^ covered

        minimum_count = t + 1
        branch_rows = 0

        cols = uncovered
        while cols:
            cb = cols & -cols
            c = cb.bit_length() - 1
            cols ^= cb

            candidates = column_rows[c] & active
            count = candidates.bit_count()
            if count == 0:
                if len(failed) < memo_limit:
                    failed.add(covered)
                return False
            if count < minimum_count:
                minimum_count = count
                branch_rows = candidates
                if count == 1:
                    break

        if not parity_consistent(active, uncovered):
            if len(failed) < memo_limit:
                failed.add(covered)
            return False

        mx = covered & full_resource_mask
        my = (covered >> k) & full_resource_mask
        mz = (covered >> (2 * k)) & full_resource_mask

        rx = full_resource_mask ^ mx
        ry = full_resource_mask ^ my
        rz = full_resource_mask ^ mz

        if not projection_has_matching(active, rx, ry, pair_xy):
            if len(failed) < memo_limit:
                failed.add(covered)
            return False
        if not projection_has_matching(active, rx, rz, pair_xz):
            if len(failed) < memo_limit:
                failed.add(covered)
            return False
        if not projection_has_matching(active, ry, rz, pair_yz):
            if len(failed) < memo_limit:
                failed.add(covered)
            return False

        candidates = []
        b = branch_rows
        while b:
            rb = b & -b
            r = rb.bit_length() - 1
            b ^= rb
            score = (conflicts[r] & active).bit_count()
            tie = (r * 2654435761) & 0xFFFFFFFF
            candidates.append((score, tie, r))

        candidates.sort()

        for _, _, r in candidates:
            chosen.append(r)
            if search(
                active & ~conflicts[r],
                covered | row_vectors[r],
                depth + 1
            ):
                return True
            chosen.pop()

        if len(failed) < memo_limit:
            failed.add(covered)
        return False

    if search(all_active, 0, 0):
        out = ["YES"]
        for r in chosen:
            x, y, z = rows[r]
            out.append(f"{x + 1} {y + 1} {z + 1}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    main()