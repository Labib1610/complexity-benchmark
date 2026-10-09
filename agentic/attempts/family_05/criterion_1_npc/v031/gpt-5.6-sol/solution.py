import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 2:
        return

    k, t = data[0], data[1]
    ncols = 3 * k
    rows = []
    incidence = [0] * ncols
    pair_xy = [0] * (k * k)
    pair_xz = [0] * (k * k)
    pair_yz = [0] * (k * k)

    p = 2
    for r in range(t):
        x = data[p] - 1
        y = data[p + 1] - 1
        z = data[p + 2] - 1
        p += 3

        rows.append((x, y, z))
        bit = 1 << r
        incidence[x] |= bit
        incidence[k + y] |= bit
        incidence[2 * k + z] |= bit
        pair_xy[x * k + y] |= bit
        pair_xz[x * k + z] |= bit
        pair_yz[y * k + z] |= bit

    if t == 0 or any(mask == 0 for mask in incidence):
        print("NO")
        return

    conflicts = [0] * t
    row_used_bits = [0] * t
    for r, (x, y, z) in enumerate(rows):
        conflicts[r] = incidence[x] | incidence[k + y] | incidence[2 * k + z]
        row_used_bits[r] = (1 << x) | (1 << (k + y)) | (1 << (2 * k + z))

    full_k = (1 << k) - 1
    full_cols = (1 << ncols) - 1
    all_rows = (1 << t) - 1

    def has_perfect_matching(pair_rows, left_mask, right_mask, available):
        left_vertices = []
        lm = left_mask

        while lm:
            lb = lm & -lm
            i = lb.bit_length() - 1
            lm ^= lb

            adjacency = 0
            rm = right_mask
            base = i * k
            while rm:
                rb = rm & -rm
                j = rb.bit_length() - 1
                rm ^= rb
                if pair_rows[base + j] & available:
                    adjacency |= rb

            if adjacency == 0:
                return False
            left_vertices.append((adjacency.bit_count(), i, adjacency))

        left_vertices.sort()
        match = [-1] * k
        seen = [0] * k
        token = 0
        adjacency_by_left = [0] * k
        for _, i, adjacency in left_vertices:
            adjacency_by_left[i] = adjacency

        sys.setrecursionlimit(1000000)

        def augment(i, mark):
            bits = adjacency_by_left[i]
            while bits:
                rb = bits & -bits
                bits ^= rb
                j = rb.bit_length() - 1
                if seen[j] == mark:
                    continue
                seen[j] = mark
                previous = match[j]
                if previous == -1 or augment(previous, mark):
                    match[j] = i
                    return True
            return False

        for _, i, _ in left_vertices:
            token += 1
            if not augment(i, token):
                return False
        return True

    chosen = []
    failed = set()
    memo_limit = 1_000_000

    sys.setrecursionlimit(1000000)

    def remember_failure(state):
        if len(failed) < memo_limit:
            failed.add(state)

    def dfs(used, available, depth):
        if used == full_cols:
            return True
        if used in failed:
            return False

        remaining_cols = full_cols ^ used
        scan = remaining_cols
        minimum_count = t + 1
        candidate_rows = 0

        while scan:
            cb = scan & -scan
            scan ^= cb
            c = cb.bit_length() - 1
            candidates = incidence[c] & available
            count = candidates.bit_count()
            if count == 0:
                remember_failure(used)
                return False
            if count < minimum_count:
                minimum_count = count
                candidate_rows = candidates
                if count == 1:
                    break

        remaining = k - depth

        if minimum_count > 1 and remaining >= 3:
            used_x = used & full_k
            used_y = (used >> k) & full_k
            used_z = (used >> (2 * k)) & full_k
            rem_x = full_k ^ used_x
            rem_y = full_k ^ used_y
            rem_z = full_k ^ used_z

            if not has_perfect_matching(pair_xy, rem_x, rem_y, available):
                remember_failure(used)
                return False
            if not has_perfect_matching(pair_xz, rem_x, rem_z, available):
                remember_failure(used)
                return False
            if not has_perfect_matching(pair_yz, rem_y, rem_z, available):
                remember_failure(used)
                return False

        ordered = []

        if 1 < minimum_count <= 24:
            bits = candidate_rows
            while bits:
                rb = bits & -bits
                bits ^= rb
                r = rb.bit_length() - 1
                new_used = used | row_used_bits[r]
                new_available = available & ~conflicts[r]

                cols = full_cols ^ new_used
                min_after = t + 1
                valid = True
                while cols:
                    cb = cols & -cols
                    cols ^= cb
                    c = cb.bit_length() - 1
                    count = (incidence[c] & new_available).bit_count()
                    if count == 0:
                        valid = False
                        break
                    if count < min_after:
                        min_after = count

                if valid:
                    ordered.append((min_after, r, new_used, new_available))

            ordered.sort(reverse=True)
            iterable = ((r, nu, na) for _, r, nu, na in ordered)
        else:
            raw = []
            bits = candidate_rows
            while bits:
                rb = bits & -bits
                bits ^= rb
                r = rb.bit_length() - 1
                raw.append((
                    r,
                    used | row_used_bits[r],
                    available & ~conflicts[r]
                ))
            iterable = iter(raw)

        for r, new_used, new_available in iterable:
            chosen.append(r)
            if dfs(new_used, new_available, depth + 1):
                return True
            chosen.pop()

        remember_failure(used)
        return False

    if not dfs(0, all_rows, 0):
        print("NO")
        return

    output = ["YES"]
    for r in chosen:
        x, y, z = rows[r]
        output.append(f"{x + 1} {y + 1} {z + 1}")
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()