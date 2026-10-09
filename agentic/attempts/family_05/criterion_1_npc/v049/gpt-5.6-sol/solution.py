import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    k, t = data[0], data[1]
    xs = [0] * t
    ys = [0] * t
    zs = [0] * t
    incidence = [[] for _ in range(3 * k)]

    p = 2
    for i in range(t):
        x = data[p] - 1
        y = data[p + 1] - 1
        z = data[p + 2] - 1
        p += 3
        xs[i], ys[i], zs[i] = x, y, z
        incidence[x].append(i)
        incidence[k + y].append(i)
        incidence[2 * k + z].append(i)

    if t < k:
        print("NO")
        return

    full = (1 << k) - 1
    failed = set()
    answer = []
    nodes = 0
    memo_limit = 700000

    def compatible(e, mx, my, mz):
        return ((mx >> xs[e]) & 1) and ((my >> ys[e]) & 1) and ((mz >> zs[e]) & 1)

    def has_perfect_matching(left_mask, right_mask, adj):
        left = []
        m = left_mask
        while m:
            b = m & -m
            u = b.bit_length() - 1
            available = adj[u] & right_mask
            if not available:
                return False
            left.append((available.bit_count(), u))
            m ^= b
        left.sort()

        match = [-1] * k

        def augment(u, seen):
            choices = adj[u] & right_mask & ~seen
            while choices:
                b = choices & -choices
                choices ^= b
                v = b.bit_length() - 1
                seen2 = seen | b
                if match[v] == -1 or augment(match[v], seen2):
                    match[v] = u
                    return True
            return False

        for _, u in left:
            if not augment(u, 0):
                return False
        return True

    def strong_check(mx, my, mz):
        target = mx | (my << k) | (mz << (2 * k))
        basis = [0] * (3 * k)

        adj_xy = [0] * k
        adj_xz = [0] * k
        adj_yz = [0] * k

        parent = list(range(3 * k))

        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a

        def union(a, b):
            a = find(a)
            b = find(b)
            if a != b:
                parent[b] = a

        feasible_count = 0
        for e in range(t):
            x = xs[e]
            y = ys[e]
            z = zs[e]
            if not ((mx >> x) & 1 and (my >> y) & 1 and (mz >> z) & 1):
                continue

            feasible_count += 1
            adj_xy[x] |= 1 << y
            adj_xz[x] |= 1 << z
            adj_yz[y] |= 1 << z

            a = x
            b = k + y
            c = 2 * k + z
            union(a, b)
            union(a, c)

            v = (1 << a) | (1 << b) | (1 << c)
            while v:
                q = v.bit_length() - 1
                if basis[q]:
                    v ^= basis[q]
                else:
                    basis[q] = v
                    break

        if feasible_count < mx.bit_count():
            return False

        v = target
        while v:
            q = v.bit_length() - 1
            if not basis[q]:
                return False
            v ^= basis[q]

        component_counts = {}
        for category, mask in enumerate((mx, my, mz)):
            m = mask
            offset = category * k
            while m:
                b = m & -m
                i = b.bit_length() - 1
                root = find(offset + i)
                counts = component_counts.get(root)
                if counts is None:
                    counts = [0, 0, 0]
                    component_counts[root] = counts
                counts[category] += 1
                m ^= b

        for counts in component_counts.values():
            if counts[0] != counts[1] or counts[0] != counts[2]:
                return False

        if not has_perfect_matching(mx, my, adj_xy):
            return False
        if not has_perfect_matching(mx, mz, adj_xz):
            return False
        if not has_perfect_matching(my, mz, adj_yz):
            return False

        return True

    def dfs(mx, my, mz, depth):
        nonlocal nodes
        if mx == 0:
            return True

        key = mx | (my << k) | (mz << (2 * k))
        if key in failed:
            return False

        nodes += 1
        counts = [0] * (3 * k)
        best_col = -1
        best_count = t + 1

        masks = (mx, my, mz)
        for category in range(3):
            m = masks[category]
            offset = category * k
            while m:
                b = m & -m
                i = b.bit_length() - 1
                col = offset + i
                count = 0
                for e in incidence[col]:
                    if compatible(e, mx, my, mz):
                        count += 1
                counts[col] = count
                if count < best_count:
                    best_count = count
                    best_col = col
                    if count == 0:
                        if len(failed) < memo_limit:
                            failed.add(key)
                        return False
                m ^= b

        if depth == 0 or (best_count >= 3 and depth % 3 == 0):
            if not strong_check(mx, my, mz):
                if len(failed) < memo_limit:
                    failed.add(key)
                return False

        candidates = []
        for e in incidence[best_col]:
            if compatible(e, mx, my, mz):
                score = counts[xs[e]] + counts[k + ys[e]] + counts[2 * k + zs[e]]
                candidates.append((score, e))
        candidates.sort()

        for _, e in candidates:
            x = xs[e]
            y = ys[e]
            z = zs[e]
            answer.append(e)
            if dfs(mx ^ (1 << x), my ^ (1 << y), mz ^ (1 << z), depth + 1):
                return True
            answer.pop()

        if len(failed) < memo_limit:
            failed.add(key)
        return False

    if dfs(full, full, full, 0):
        out = ["YES"]
        for e in answer:
            out.append(f"{xs[e] + 1} {ys[e] + 1} {zs[e] + 1}")
        sys.stdout.write("\n".join(out))
    else:
        print("NO")

if __name__ == "__main__":
    main()