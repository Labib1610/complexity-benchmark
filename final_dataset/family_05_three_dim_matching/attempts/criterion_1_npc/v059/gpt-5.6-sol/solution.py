import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    k, t = data[0], data[1]
    xs = [0] * t
    ys = [0] * t
    zs = [0] * t

    col_x = [0] * k
    col_y = [0] * k
    col_z = [0] * k

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
        col_x[x] |= bit
        col_y[y] |= bit
        col_z[z] |= bit

    if t == 0 or any(v == 0 for v in col_x) or any(v == 0 for v in col_y) or any(v == 0 for v in col_z):
        print("NO")
        return

    full_parts = (1 << k) - 1
    all_rows = (1 << t) - 1
    failed = set()
    memo_limit = 1_000_000
    answer = []

    sys.setrecursionlimit(10000)

    def has_perfect_matching(adj, left_mask, right_mask):
        left = []
        m = left_mask
        while m:
            b = m & -m
            i = b.bit_length() - 1
            available = adj[i] & right_mask
            if available == 0:
                return False
            left.append((available.bit_count(), i))
            m ^= b
        left.sort()

        matched = [-1] * k

        def augment(u, seen):
            choices = adj[u] & right_mask
            while choices:
                b = choices & -choices
                v = b.bit_length() - 1
                choices ^= b
                if seen[v]:
                    continue
                seen[v] = True
                old = matched[v]
                if old == -1 or augment(old, seen):
                    matched[v] = u
                    return True
            return False

        for _, u in left:
            if not augment(u, [False] * k):
                return False
        return True

    def projection_check(available, rem_x, rem_y, rem_z):
        adj_xy = [0] * k
        adj_xz = [0] * k
        adj_yz = [0] * k

        rows = available
        while rows:
            b = rows & -rows
            i = b.bit_length() - 1
            rows ^= b
            x, y, z = xs[i], ys[i], zs[i]
            adj_xy[x] |= 1 << y
            adj_xz[x] |= 1 << z
            adj_yz[y] |= 1 << z

        return (
            has_perfect_matching(adj_xy, rem_x, rem_y)
            and has_perfect_matching(adj_xz, rem_x, rem_z)
            and has_perfect_matching(adj_yz, rem_y, rem_z)
        )

    def search(used_x, used_y, used_z, available, depth):
        if used_x == full_parts:
            return True

        key = used_x | (used_y << k) | (used_z << (2 * k))
        if key in failed:
            return False

        rem_x = full_parts ^ used_x
        rem_y = full_parts ^ used_y
        rem_z = full_parts ^ used_z

        best_rows = 0
        best_count = t + 1

        count_x = [0] * k
        count_y = [0] * k
        count_z = [0] * k

        m = rem_x
        while m:
            b = m & -m
            i = b.bit_length() - 1
            m ^= b
            candidates = col_x[i] & available
            cnt = candidates.bit_count()
            if cnt == 0:
                if len(failed) < memo_limit:
                    failed.add(key)
                return False
            count_x[i] = cnt
            if cnt < best_count:
                best_count = cnt
                best_rows = candidates

        m = rem_y
        while m:
            b = m & -m
            i = b.bit_length() - 1
            m ^= b
            candidates = col_y[i] & available
            cnt = candidates.bit_count()
            if cnt == 0:
                if len(failed) < memo_limit:
                    failed.add(key)
                return False
            count_y[i] = cnt
            if cnt < best_count:
                best_count = cnt
                best_rows = candidates

        m = rem_z
        while m:
            b = m & -m
            i = b.bit_length() - 1
            m ^= b
            candidates = col_z[i] & available
            cnt = candidates.bit_count()
            if cnt == 0:
                if len(failed) < memo_limit:
                    failed.add(key)
                return False
            count_z[i] = cnt
            if cnt < best_count:
                best_count = cnt
                best_rows = candidates

        remaining = k - depth
        if best_count > 1 and remaining > 3 and depth % 3 == 0:
            if not projection_check(available, rem_x, rem_y, rem_z):
                if len(failed) < memo_limit:
                    failed.add(key)
                return False

        candidates = []
        rows = best_rows
        while rows:
            b = rows & -rows
            i = b.bit_length() - 1
            rows ^= b
            score = count_x[xs[i]] + count_y[ys[i]] + count_z[zs[i]]
            candidates.append((score, i))

        if len(candidates) > 1:
            candidates.sort()

        for _, row in candidates:
            x, y, z = xs[row], ys[row], zs[row]
            bx, by, bz = 1 << x, 1 << y, 1 << z

            if (used_x & bx) or (used_y & by) or (used_z & bz):
                continue

            next_available = available
            next_available &= ~col_x[x]
            next_available &= ~col_y[y]
            next_available &= ~col_z[z]

            answer.append(row)
            if search(
                used_x | bx,
                used_y | by,
                used_z | bz,
                next_available,
                depth + 1
            ):
                return True
            answer.pop()

        if len(failed) < memo_limit:
            failed.add(key)
        return False

    if search(0, 0, 0, all_rows, 0):
        out = ["YES"]
        out.extend(f"{xs[i] + 1} {ys[i] + 1} {zs[i] + 1}" for i in answer)
        sys.stdout.write("\n".join(out))
    else:
        print("NO")

if __name__ == "__main__":
    main()