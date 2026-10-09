import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 2:
        return

    k, t = data[0], data[1]
    full = (1 << k) - 1
    triples = []
    incident = [[[] for _ in range(k)] for _ in range(3)]

    pos = 2
    for i in range(t):
        x = data[pos] - 1
        y = data[pos + 1] - 1
        z = data[pos + 2] - 1
        pos += 3

        bx = 1 << x
        by = 1 << y
        bz = 1 << z
        column = bx | (by << k) | (bz << (2 * k))
        triples.append((x, y, z, bx, by, bz, column))
        incident[0][x].append(i)
        incident[1][y].append(i)
        incident[2][z].append(i)

    if t < k:
        print("NO")
        return

    def has_perfect_matching(adj, left_mask):
        vertices = []
        m = left_mask
        while m:
            bit = m & -m
            u = bit.bit_length() - 1
            if adj[u] == 0:
                return False
            vertices.append(u)
            m ^= bit

        vertices.sort(key=lambda u: adj[u].bit_count())
        match_right = [-1] * k

        def augment(u, seen):
            choices = adj[u] & ~seen[0]
            while choices:
                bit = choices & -choices
                choices ^= bit
                seen[0] |= bit
                v = bit.bit_length() - 1
                other = match_right[v]
                if other == -1 or augment(other, seen):
                    match_right[v] = u
                    return True
            return False

        for u in vertices:
            seen = [0]
            if not augment(u, seen):
                return False
        return True

    failed = set()
    selected = []
    answer = None
    memo_limit = 1_200_000
    total_resources = 3 * k

    sys.setrecursionlimit(10000)

    def dfs(mx, my, mz, depth):
        nonlocal answer

        if depth == k:
            answer = selected.copy()
            return True

        key = mx | (my << k) | (mz << (2 * k))
        if key in failed:
            return False

        ax = full ^ mx
        ay = full ^ my
        az = full ^ mz

        degree = [0] * total_resources
        adj_xy = [0] * k
        adj_xz = [0] * k
        adj_yz = [0] * k
        basis = [0] * total_resources

        for x, y, z, bx, by, bz, column in triples:
            if (mx & bx) or (my & by) or (mz & bz):
                continue

            degree[x] += 1
            degree[k + y] += 1
            degree[2 * k + z] += 1

            adj_xy[x] |= by
            adj_xz[x] |= bz
            adj_yz[y] |= bz

            v = column
            while v:
                p = v.bit_length() - 1
                b = basis[p]
                if b:
                    v ^= b
                else:
                    basis[p] = v
                    break

        best_resource = -1
        best_degree = t + 1

        m = ax
        while m:
            bit = m & -m
            u = bit.bit_length() - 1
            d = degree[u]
            if d == 0:
                if len(failed) < memo_limit:
                    failed.add(key)
                return False
            if d < best_degree:
                best_degree = d
                best_resource = u
            m ^= bit

        m = ay
        while m:
            bit = m & -m
            u = bit.bit_length() - 1
            idx = k + u
            d = degree[idx]
            if d == 0:
                if len(failed) < memo_limit:
                    failed.add(key)
                return False
            if d < best_degree:
                best_degree = d
                best_resource = idx
            m ^= bit

        m = az
        while m:
            bit = m & -m
            u = bit.bit_length() - 1
            idx = 2 * k + u
            d = degree[idx]
            if d == 0:
                if len(failed) < memo_limit:
                    failed.add(key)
                return False
            if d < best_degree:
                best_degree = d
                best_resource = idx
            m ^= bit

        target = ax | (ay << k) | (az << (2 * k))
        v = target
        while v:
            p = v.bit_length() - 1
            b = basis[p]
            if not b:
                if len(failed) < memo_limit:
                    failed.add(key)
                return False
            v ^= b

        if not has_perfect_matching(adj_xy, ax):
            if len(failed) < memo_limit:
                failed.add(key)
            return False
        if not has_perfect_matching(adj_xz, ax):
            if len(failed) < memo_limit:
                failed.add(key)
            return False
        if not has_perfect_matching(adj_yz, ay):
            if len(failed) < memo_limit:
                failed.add(key)
            return False

        if best_resource < k:
            dim = 0
            resource = best_resource
        elif best_resource < 2 * k:
            dim = 1
            resource = best_resource - k
        else:
            dim = 2
            resource = best_resource - 2 * k

        candidates = []
        for idx in incident[dim][resource]:
            x, y, z, bx, by, bz, _ = triples[idx]
            if (mx & bx) or (my & by) or (mz & bz):
                continue
            score = degree[x] + degree[k + y] + degree[2 * k + z]
            candidates.append((score, idx))

        candidates.sort()

        for _, idx in candidates:
            x, y, z, bx, by, bz, _ = triples[idx]
            selected.append(idx)
            if dfs(mx | bx, my | by, mz | bz, depth + 1):
                return True
            selected.pop()

        if len(failed) < memo_limit:
            failed.add(key)
        return False

    if not dfs(0, 0, 0, 0):
        print("NO")
        return

    out = ["YES"]
    for idx in answer:
        x, y, z = triples[idx][0], triples[idx][1], triples[idx][2]
        out.append(f"{x + 1} {y + 1} {z + 1}")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()