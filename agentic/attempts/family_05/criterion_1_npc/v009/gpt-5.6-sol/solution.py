import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    k, t = data[0], data[1]
    xs = [0] * t
    ys = [0] * t
    zs = [0] * t
    column_rows = [0] * (3 * k)

    p = 2
    for i in range(t):
        x = data[p] - 1
        y = data[p + 1] - 1
        z = data[p + 2] - 1
        p += 3

        xs[i] = x
        ys[i] = y
        zs[i] = z

        bit = 1 << i
        column_rows[x] |= bit
        column_rows[k + y] |= bit
        column_rows[2 * k + z] |= bit

    if t == 0:
        print("NO")
        return

    for rows in column_rows:
        if rows == 0:
            print("NO")
            return

    conflicts = [0] * t
    for i in range(t):
        conflicts[i] = (
            column_rows[xs[i]]
            | column_rows[k + ys[i]]
            | column_rows[2 * k + zs[i]]
        )

    full = (1 << k) - 1
    all_active = (1 << t) - 1
    failed = set()
    answer = []
    sys.setrecursionlimit(100000)

    def can_match(adj, left_mask, right_mask):
        if left_mask.bit_count() != right_mask.bit_count():
            return False

        left = []
        bits = left_mask
        while bits:
            b = bits & -bits
            u = b.bit_length() - 1
            choices = adj[u] & right_mask
            if choices == 0:
                return False
            left.append((choices.bit_count(), u))
            bits ^= b

        left.sort()
        match_right = [-1] * k
        seen = [0] * k
        stamp = 0

        def augment(u):
            choices = adj[u] & right_mask
            while choices:
                b = choices & -choices
                v = b.bit_length() - 1
                choices ^= b
                if seen[v] == stamp:
                    continue
                seen[v] = stamp
                previous = match_right[v]
                if previous == -1 or augment(previous):
                    match_right[v] = u
                    return True
            return False

        for _, u in left:
            stamp += 1
            if not augment(u):
                return False
        return True

    def search(mx, my, mz, active):
        if mx == full:
            return True

        state = mx | (my << k) | (mz << (2 * k))
        if state in failed:
            return False

        best_rows = 0
        best_count = t + 1

        missing = full ^ mx
        while missing:
            b = missing & -missing
            x = b.bit_length() - 1
            rows = active & column_rows[x]
            count = rows.bit_count()
            if count == 0:
                if len(failed) < 1_000_000:
                    failed.add(state)
                return False
            if count < best_count:
                best_count = count
                best_rows = rows
                if count == 1:
                    break
            missing ^= b

        if best_count != 1:
            missing = full ^ my
            while missing:
                b = missing & -missing
                y = b.bit_length() - 1
                rows = active & column_rows[k + y]
                count = rows.bit_count()
                if count == 0:
                    if len(failed) < 1_000_000:
                        failed.add(state)
                    return False
                if count < best_count:
                    best_count = count
                    best_rows = rows
                    if count == 1:
                        break
                missing ^= b

        if best_count != 1:
            missing = full ^ mz
            while missing:
                b = missing & -missing
                z = b.bit_length() - 1
                rows = active & column_rows[2 * k + z]
                count = rows.bit_count()
                if count == 0:
                    if len(failed) < 1_000_000:
                        failed.add(state)
                    return False
                if count < best_count:
                    best_count = count
                    best_rows = rows
                    if count == 1:
                        break
                missing ^= b

        adj_xy = [0] * k
        adj_xz = [0] * k
        adj_yz = [0] * k

        rows = active
        while rows:
            b = rows & -rows
            i = b.bit_length() - 1
            rows ^= b
            x = xs[i]
            y = ys[i]
            z = zs[i]
            adj_xy[x] |= 1 << y
            adj_xz[x] |= 1 << z
            adj_yz[y] |= 1 << z

        rem_x = full ^ mx
        rem_y = full ^ my
        rem_z = full ^ mz

        if (
            not can_match(adj_xy, rem_x, rem_y)
            or not can_match(adj_xz, rem_x, rem_z)
            or not can_match(adj_yz, rem_y, rem_z)
        ):
            if len(failed) < 1_000_000:
                failed.add(state)
            return False

        candidates = []
        rows = best_rows
        while rows:
            b = rows & -rows
            candidates.append(b.bit_length() - 1)
            rows ^= b

        if len(candidates) <= 48:
            candidates.sort(key=lambda r: (active & conflicts[r]).bit_count())

        for r in candidates:
            x = xs[r]
            y = ys[r]
            z = zs[r]

            answer.append(r)
            if search(
                mx | (1 << x),
                my | (1 << y),
                mz | (1 << z),
                active & ~conflicts[r]
            ):
                return True
            answer.pop()

        if len(failed) < 1_000_000:
            failed.add(state)
        return False

    if search(0, 0, 0, all_active):
        out = ["YES"]
        for r in answer:
            out.append(f"{xs[r] + 1} {ys[r] + 1} {zs[r] + 1}")
        sys.stdout.write("\n".join(out))
    else:
        print("NO")

if __name__ == "__main__":
    main()