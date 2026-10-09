import sys

sys.setrecursionlimit(1_000_000)


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    k, t = data[0], data[1]
    column_count = 3 * k

    incidence = [0] * column_count
    pair_xy = [0] * (k * k)
    pair_xz = [0] * (k * k)
    pair_yz = [0] * (k * k)

    xs = [0] * t
    ys = [0] * t
    zs = [0] * t
    covers = [0] * t

    p = 2
    for e in range(t):
        x = data[p] - 1
        y = data[p + 1] - 1
        z = data[p + 2] - 1
        p += 3

        xs[e] = x
        ys[e] = y
        zs[e] = z

        cx = x
        cy = k + y
        cz = 2 * k + z
        cover = (1 << cx) | (1 << cy) | (1 << cz)
        covers[e] = cover

        bit = 1 << e
        incidence[cx] |= bit
        incidence[cy] |= bit
        incidence[cz] |= bit

        pair_xy[x * k + y] |= bit
        pair_xz[x * k + z] |= bit
        pair_yz[y * k + z] |= bit

    del data

    if t == 0:
        print("NO")
        return

    for mask in incidence:
        if mask == 0:
            print("NO")
            return

    conflicts = [
        incidence[xs[e]] | incidence[k + ys[e]] | incidence[2 * k + zs[e]]
        for e in range(t)
    ]

    all_edges = (1 << t) - 1
    all_columns = (1 << column_count) - 1

    def bipartite_ok(active, left_remaining, right_remaining, pair_masks):
        left_vertices = []
        m = left_remaining
        while m:
            b = m & -m
            left_vertices.append(b.bit_length() - 1)
            m ^= b

        right_vertices = []
        m = right_remaining
        while m:
            b = m & -m
            right_vertices.append(b.bit_length() - 1)
            m ^= b

        adjacency = []
        for a in left_vertices:
            row = 0
            base = a * k
            for b in right_vertices:
                if active & pair_masks[base + b]:
                    row |= 1 << b
            if row == 0:
                return False
            adjacency.append(row)

        order = sorted(range(len(left_vertices)),
                       key=lambda i: adjacency[i].bit_count())
        match = [-1] * k

        def augment(i, seen):
            choices = adjacency[i] & ~seen
            while choices:
                bit = choices & -choices
                choices ^= bit
                b = bit.bit_length() - 1
                previous = match[b]
                if previous == -1 or augment(previous, seen | bit):
                    match[b] = i
                    return True
            return False

        for i in order:
            if not augment(i, 0):
                return False
        return True

    def projections_ok(active, uncovered):
        base_mask = (1 << k) - 1
        rem_x = uncovered & base_mask
        rem_y = (uncovered >> k) & base_mask
        rem_z = (uncovered >> (2 * k)) & base_mask

        return (
            bipartite_ok(active, rem_x, rem_y, pair_xy)
            and bipartite_ok(active, rem_x, rem_z, pair_xz)
            and bipartite_ok(active, rem_y, rem_z, pair_yz)
        )

    failed = set()
    memo_limit = 800_000
    answer = []

    def search(active, uncovered, depth):
        if uncovered == 0:
            return True
        if uncovered in failed:
            return False

        remaining_columns = uncovered
        chosen_candidates = 0
        minimum = t + 1

        while remaining_columns:
            col_bit = remaining_columns & -remaining_columns
            remaining_columns ^= col_bit
            col = col_bit.bit_length() - 1
            candidates = active & incidence[col]
            count = candidates.bit_count()

            if count == 0:
                if len(failed) < memo_limit:
                    failed.add(uncovered)
                return False

            if count < minimum:
                minimum = count
                chosen_candidates = candidates
                if count == 1:
                    break

        if depth % 4 == 0 and not projections_ok(active, uncovered):
            if len(failed) < memo_limit:
                failed.add(uncovered)
            return False

        if minimum <= 20 and minimum > 1:
            candidate_ids = []
            m = chosen_candidates
            while m:
                bit = m & -m
                m ^= bit
                e = bit.bit_length() - 1
                candidate_ids.append(e)
            candidate_ids.sort(key=lambda e: (active & conflicts[e]).bit_count())

            for e in candidate_ids:
                answer.append(e)
                if search(active & ~conflicts[e],
                          uncovered ^ covers[e],
                          depth + 1):
                    return True
                answer.pop()
        else:
            m = chosen_candidates
            while m:
                bit = m & -m
                m ^= bit
                e = bit.bit_length() - 1

                answer.append(e)
                if search(active & ~conflicts[e],
                          uncovered ^ covers[e],
                          depth + 1):
                    return True
                answer.pop()

        if len(failed) < memo_limit:
            failed.add(uncovered)
        return False

    if not projections_ok(all_edges, all_columns):
        print("NO")
        return

    if search(all_edges, all_columns, 0):
        out = ["YES"]
        out.extend(
            f"{xs[e] + 1} {ys[e] + 1} {zs[e] + 1}"
            for e in answer
        )
        sys.stdout.write("\n".join(out))
    else:
        print("NO")


if __name__ == "__main__":
    main()