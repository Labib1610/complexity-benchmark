import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    k, t = data[0], data[1]
    triples = []
    col_rows = [0] * (3 * k)

    p = 2
    for i in range(t):
        x = data[p] - 1
        y = data[p + 1] - 1
        z = data[p + 2] - 1
        p += 3
        triples.append((x, y, z))
        bit = 1 << i
        col_rows[x] |= bit
        col_rows[k + y] |= bit
        col_rows[2 * k + z] |= bit

    if t == 0:
        print("NO")
        return

    for rows in col_rows:
        if rows == 0:
            print("NO")
            return

    all_active = (1 << t) - 1
    all_columns = (1 << (3 * k)) - 1

    conflicts = [0] * t
    for i, (x, y, z) in enumerate(triples):
        conflicts[i] = col_rows[x] | col_rows[k + y] | col_rows[2 * k + z]

    xy = [[0] * k for _ in range(k)]
    xz = [[0] * k for _ in range(k)]
    yz = [[0] * k for _ in range(k)]

    for a in range(k):
        ra = col_rows[a]
        for b in range(k):
            xy[a][b] = ra & col_rows[k + b]
            xz[a][b] = ra & col_rows[2 * k + b]

    for a in range(k):
        ra = col_rows[k + a]
        for b in range(k):
            yz[a][b] = ra & col_rows[2 * k + b]

    def available_indices(covered, offset):
        mask = ((covered >> offset) & ((1 << k) - 1))
        result = []
        free = ((1 << k) - 1) ^ mask
        while free:
            bit = free & -free
            result.append(bit.bit_length() - 1)
            free ^= bit
        return result

    def projection_has_matching(active, left, right, matrix):
        adjacency = []
        for a in left:
            neighbors = 0
            row = matrix[a]
            for b in right:
                if active & row[b]:
                    neighbors |= 1 << b
            if neighbors == 0:
                return False
            adjacency.append((neighbors.bit_count(), a, neighbors))

        adjacency.sort()
        match = [-1] * k

        def augment(a, neighbors, seen):
            bits = neighbors
            while bits:
                bit = bits & -bits
                bits ^= bit
                b = bit.bit_length() - 1
                if seen[b]:
                    continue
                seen[b] = True
                old = match[b]
                if old == -1:
                    match[b] = a
                    return True
                old_neighbors = adj_by_left[old]
                if augment(old, old_neighbors, seen):
                    match[b] = a
                    return True
            return False

        adj_by_left = {}
        for _, a, neighbors in adjacency:
            adj_by_left[a] = neighbors

        for _, a, neighbors in adjacency:
            if not augment(a, neighbors, [False] * k):
                return False
        return True

    def projections_feasible(active, covered):
        xs = available_indices(covered, 0)
        ys = available_indices(covered, k)
        zs = available_indices(covered, 2 * k)

        if not projection_has_matching(active, xs, ys, xy):
            return False
        if not projection_has_matching(active, xs, zs, xz):
            return False
        if not projection_has_matching(active, ys, zs, yz):
            return False
        return True

    failed = set()
    cache_limit = 500000
    path = []

    sys.setrecursionlimit(10000)

    def dfs(active, covered, depth):
        if depth == k:
            return True

        if covered in failed:
            return False

        uncovered = all_columns ^ covered
        best_options = 0
        best_count = t + 1

        bits = uncovered
        while bits:
            bit = bits & -bits
            bits ^= bit
            c = bit.bit_length() - 1
            options = active & col_rows[c]
            count = options.bit_count()
            if count == 0:
                if len(failed) < cache_limit:
                    failed.add(covered)
                return False
            if count < best_count:
                best_count = count
                best_options = options
                if count == 1:
                    break

        if best_count > 1 and not projections_feasible(active, covered):
            if len(failed) < cache_limit:
                failed.add(covered)
            return False

        candidates = []
        bits = best_options
        while bits:
            bit = bits & -bits
            bits ^= bit
            candidates.append(bit.bit_length() - 1)

        if 1 < len(candidates) <= 24:
            candidates.sort(key=lambda r: (active & conflicts[r]).bit_count())

        for r in candidates:
            x, y, z = triples[r]
            new_covered = covered | (1 << x) | (1 << (k + y)) | (1 << (2 * k + z))
            new_active = active & ~conflicts[r]

            path.append(r)
            if dfs(new_active, new_covered, depth + 1):
                return True
            path.pop()

        if len(failed) < cache_limit:
            failed.add(covered)
        return False

    if dfs(all_active, 0, 0):
        out = ["YES"]
        for r in path:
            x, y, z = triples[r]
            out.append(f"{x + 1} {y + 1} {z + 1}")
        sys.stdout.write("\n".join(out))
    else:
        print("NO")

if __name__ == "__main__":
    solve()