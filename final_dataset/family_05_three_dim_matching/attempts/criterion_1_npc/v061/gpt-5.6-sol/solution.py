import sys

sys.setrecursionlimit(1000000)

def in_span_gf2(row_vectors, target):
    basis = {}
    for v in row_vectors:
        while v:
            p = v.bit_length() - 1
            b = basis.get(p)
            if b is None:
                basis[p] = v
                break
            v ^= b

    v = target
    while v:
        p = v.bit_length() - 1
        b = basis.get(p)
        if b is None:
            return False
        v ^= b
    return True


def in_span_gf3(row_vectors, target, n):
    mask = (1 << n) - 1
    basis_lo = [0] * n
    basis_hi = [0] * n

    def add3(al, ah, bl, bh):
        a0 = mask ^ (al | ah)
        b0 = mask ^ (bl | bh)
        nl = (a0 & bl) | (al & b0) | (ah & bh)
        nh = (a0 & bh) | (ah & b0) | (al & bl)
        return nl, nh

    for vec in row_vectors:
        lo, hi = vec, 0
        while lo | hi:
            union = lo | hi
            lb = union & -union
            p = lb.bit_length() - 1

            if basis_lo[p] == 0 and basis_hi[p] == 0:
                if hi & lb:
                    lo, hi = hi, lo
                basis_lo[p] = lo
                basis_hi[p] = hi
                break

            if lo & lb:
                lo, hi = add3(lo, hi, basis_hi[p], basis_lo[p])
            else:
                lo, hi = add3(lo, hi, basis_lo[p], basis_hi[p])

    lo, hi = target, 0
    while lo | hi:
        union = lo | hi
        lb = union & -union
        p = lb.bit_length() - 1
        if basis_lo[p] == 0 and basis_hi[p] == 0:
            return False
        if lo & lb:
            lo, hi = add3(lo, hi, basis_hi[p], basis_lo[p])
        else:
            lo, hi = add3(lo, hi, basis_lo[p], basis_hi[p])
    return True


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    k, t = data[0], data[1]
    rows = []
    incidence = []

    pos = 2
    for _ in range(t):
        x = data[pos] - 1
        y = data[pos + 1] - 1
        z = data[pos + 2] - 1
        pos += 3
        rows.append((x, y, z))
        incidence.append((1 << x) | (1 << (k + y)) | (1 << (2 * k + z)))

    if t < k:
        print("NO")
        return

    ncols = 3 * k
    target = (1 << ncols) - 1

    if not in_span_gf2(incidence, target):
        print("NO")
        return
    if not in_span_gf3(incidence, target, ncols):
        print("NO")
        return

    col_rows = [0] * ncols
    for i, (x, y, z) in enumerate(rows):
        bit = 1 << i
        col_rows[x] |= bit
        col_rows[k + y] |= bit
        col_rows[2 * k + z] |= bit

    for c in range(ncols):
        if col_rows[c] == 0:
            print("NO")
            return

    conflicts = [0] * t
    for i, (x, y, z) in enumerate(rows):
        conflicts[i] = col_rows[x] | col_rows[k + y] | col_rows[2 * k + z]

    all_rows = (1 << t) - 1
    full = (1 << k) - 1
    answer = []
    failed = set()
    FAILED_LIMIT = 350000

    groups = [
        col_rows[0:k],
        col_rows[k:2 * k],
        col_rows[2 * k:3 * k]
    ]

    def projection_matching(available, used_a, used_b, ga, gb):
        aa = full ^ used_a
        bb = full ^ used_b
        adjacency = [0] * k

        am = aa
        while am:
            abit = am & -am
            a = abit.bit_length() - 1
            possible_rows = available & groups[ga][a]
            adj = 0
            bm = bb
            while bm:
                bbit = bm & -bm
                b = bbit.bit_length() - 1
                if possible_rows & groups[gb][b]:
                    adj |= bbit
                bm ^= bbit
            if adj == 0:
                return False
            adjacency[a] = adj
            am ^= abit

        match = [-1] * k

        def augment(a, seen):
            options = adjacency[a] & ~seen[0]
            while options:
                bit = options & -options
                options ^= bit
                b = bit.bit_length() - 1
                seen[0] |= bit
                old = match[b]
                if old == -1 or augment(old, seen):
                    match[b] = a
                    return True
            return False

        am = aa
        while am:
            abit = am & -am
            a = abit.bit_length() - 1
            if not augment(a, [0]):
                return False
            am ^= abit
        return True

    def local_gf2_check(available, used_x, used_y, used_z):
        remaining_target = (
            (full ^ used_x)
            | ((full ^ used_y) << k)
            | ((full ^ used_z) << (2 * k))
        )

        basis = {}
        a = available
        while a:
            bit = a & -a
            idx = bit.bit_length() - 1
            v = incidence[idx]
            while v:
                p = v.bit_length() - 1
                b = basis.get(p)
                if b is None:
                    basis[p] = v
                    break
                v ^= b
            a ^= bit

        v = remaining_target
        while v:
            p = v.bit_length() - 1
            b = basis.get(p)
            if b is None:
                return False
            v ^= b
        return True

    def dfs(available, used_x, used_y, used_z, depth):
        if depth == k:
            return True

        state = (used_x, used_y, used_z)
        if state in failed:
            return False

        min_count = t + 1
        chosen_column = -1

        ux = full ^ used_x
        while ux:
            bit = ux & -ux
            c = bit.bit_length() - 1
            cnt = (available & col_rows[c]).bit_count()
            if cnt == 0:
                if len(failed) < FAILED_LIMIT:
                    failed.add(state)
                return False
            if cnt < min_count:
                min_count = cnt
                chosen_column = c
                if cnt == 1:
                    break
            ux ^= bit

        if min_count != 1:
            uy = full ^ used_y
            while uy:
                bit = uy & -uy
                j = bit.bit_length() - 1
                c = k + j
                cnt = (available & col_rows[c]).bit_count()
                if cnt == 0:
                    if len(failed) < FAILED_LIMIT:
                        failed.add(state)
                    return False
                if cnt < min_count:
                    min_count = cnt
                    chosen_column = c
                    if cnt == 1:
                        break
                uy ^= bit

        if min_count != 1:
            uz = full ^ used_z
            while uz:
                bit = uz & -uz
                j = bit.bit_length() - 1
                c = 2 * k + j
                cnt = (available & col_rows[c]).bit_count()
                if cnt == 0:
                    if len(failed) < FAILED_LIMIT:
                        failed.add(state)
                    return False
                if cnt < min_count:
                    min_count = cnt
                    chosen_column = c
                    if cnt == 1:
                        break
                uz ^= bit

        if depth % 2 == 0:
            if not projection_matching(available, used_x, used_y, 0, 1):
                if len(failed) < FAILED_LIMIT:
                    failed.add(state)
                return False
            if not projection_matching(available, used_x, used_z, 0, 2):
                if len(failed) < FAILED_LIMIT:
                    failed.add(state)
                return False
            if not projection_matching(available, used_y, used_z, 1, 2):
                if len(failed) < FAILED_LIMIT:
                    failed.add(state)
                return False

        available_count = available.bit_count()
        if depth > 0 and depth % 4 == 0 and available_count <= 2000:
            if not local_gf2_check(available, used_x, used_y, used_z):
                if len(failed) < FAILED_LIMIT:
                    failed.add(state)
                return False

        candidates_mask = available & col_rows[chosen_column]
        candidates = []
        while candidates_mask:
            bit = candidates_mask & -candidates_mask
            candidates.append(bit.bit_length() - 1)
            candidates_mask ^= bit

        if 1 < len(candidates) <= 64:
            candidates.sort(key=lambda r: (available & conflicts[r]).bit_count())

        for r in candidates:
            x, y, z = rows[r]
            bx, by, bz = 1 << x, 1 << y, 1 << z
            new_available = available & ~conflicts[r]

            answer.append(r)
            if dfs(
                new_available,
                used_x | bx,
                used_y | by,
                used_z | bz,
                depth + 1
            ):
                return True
            answer.pop()

        if len(failed) < FAILED_LIMIT:
            failed.add(state)
        return False

    if dfs(all_rows, 0, 0, 0, 0):
        out = ["YES"]
        for r in answer:
            x, y, z = rows[r]
            out.append(f"{x + 1} {y + 1} {z + 1}")
        print("\n".join(out))
    else:
        print("NO")


if __name__ == "__main__":
    main()