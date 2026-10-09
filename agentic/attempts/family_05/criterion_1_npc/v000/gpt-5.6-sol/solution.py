import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 2:
        return

    k, t = data[0], data[1]
    if t < k:
        print("NO")
        return

    xs = [0] * t
    ys = [0] * t
    zs = [0] * t
    incidence = [0] * (3 * k)

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
        incidence[x] |= bit
        incidence[k + y] |= bit
        incidence[2 * k + z] |= bit

    parent = list(range(3 * k))
    size = [1] * (3 * k)

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a, b):
        a = find(a)
        b = find(b)
        if a == b:
            return
        if size[a] < size[b]:
            a, b = b, a
        parent[b] = a
        size[a] += size[b]

    for i in range(t):
        a = xs[i]
        b = k + ys[i]
        c = 2 * k + zs[i]
        union(a, b)
        union(a, c)

    components = {}
    for v in range(3 * k):
        r = find(v)
        components.setdefault(r, []).append(v)

    component_data = []
    for vertices in components.values():
        cx = cy = cz = 0
        uncovered = 0
        available = 0
        for v in vertices:
            uncovered |= 1 << v
            available |= incidence[v]
            if v < k:
                cx += 1
            elif v < 2 * k:
                cy += 1
            else:
                cz += 1

        if cx != cy or cx != cz or cx == 0:
            print("NO")
            return

        for v in vertices:
            if incidence[v] == 0:
                print("NO")
                return

        component_data.append((len(vertices), uncovered, available))

    component_data.sort()

    vertex_mask = [0] * t
    conflict = [0] * t
    for i in range(t):
        a = xs[i]
        b = k + ys[i]
        c = 2 * k + zs[i]
        vertex_mask[i] = (1 << a) | (1 << b) | (1 << c)
        conflict[i] = incidence[a] | incidence[b] | incidence[c]

    def projected_match_check(available, uncovered):
        nxy = [0] * k
        nxz = [0] * k
        nyz = [0] * k

        bits = available
        while bits:
            low = bits & -bits
            i = low.bit_length() - 1
            bits ^= low
            x, y, z = xs[i], ys[i], zs[i]
            nxy[x] |= 1 << y
            nxz[x] |= 1 << z
            nyz[y] |= 1 << z

        x_left = [i for i in range(k) if uncovered & (1 << i)]
        y_left = [i for i in range(k) if uncovered & (1 << (k + i))]

        def can_match(left, neighbors):
            owner = [-1] * k

            def augment(u, seen):
                choices = neighbors[u] & ~seen
                while choices:
                    low = choices & -choices
                    choices ^= low
                    v = low.bit_length() - 1
                    old = owner[v]
                    if old == -1 or augment(old, seen | low):
                        owner[v] = u
                        return True
                return False

            left = sorted(left, key=lambda u: neighbors[u].bit_count())
            for u in left:
                if neighbors[u] == 0 or not augment(u, 0):
                    return False
            return True

        return (
            can_match(x_left, nxy)
            and can_match(x_left, nxz)
            and can_match(y_left, nyz)
        )

    answer = []

    for _, initial_uncovered, initial_available in component_data:
        if not projected_match_check(initial_available, initial_uncovered):
            print("NO")
            return

        failed = set()
        memo_limit = 700000

        def dfs(uncovered, available):
            if uncovered == 0:
                return []

            if uncovered in failed:
                return None

            scan = uncovered
            best_options = 0
            best_count = t + 1

            while scan:
                low = scan & -scan
                v = low.bit_length() - 1
                scan ^= low

                options = incidence[v] & available
                count = options.bit_count()
                if count == 0:
                    if len(failed) < memo_limit:
                        failed.add(uncovered)
                    return None
                if count < best_count:
                    best_count = count
                    best_options = options
                    if count == 1:
                        break

            candidates = []
            bits = best_options
            while bits:
                low = bits & -bits
                i = low.bit_length() - 1
                bits ^= low
                candidates.append(i)

            if 1 < len(candidates) <= 100:
                candidates.sort(
                    key=lambda i: (available & conflict[i]).bit_count()
                )

            for i in candidates:
                result = dfs(
                    uncovered & ~vertex_mask[i],
                    available & ~conflict[i]
                )
                if result is not None:
                    result.append(i)
                    return result

            if len(failed) < memo_limit:
                failed.add(uncovered)
            return None

        part = dfs(initial_uncovered, initial_available)
        if part is None:
            print("NO")
            return
        answer.extend(part)

    if len(answer) != k:
        print("NO")
        return

    out = ["YES"]
    for i in answer:
        out.append(f"{xs[i] + 1} {ys[i] + 1} {zs[i] + 1}")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()