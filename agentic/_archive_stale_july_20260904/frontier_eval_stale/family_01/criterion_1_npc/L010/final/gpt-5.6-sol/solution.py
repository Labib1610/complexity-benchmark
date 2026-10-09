import sys

sys.setrecursionlimit(1_000_000)


def is_three_colorable(adj):
    n = len(adj)
    if n <= 3:
        return True

    colors = [-1] * n
    saturation = [0] * n
    degrees = [x.bit_count() for x in adj]

    first = max(range(n), key=lambda v: degrees[v])
    colors[first] = 0

    changed = []
    bits = adj[first]
    while bits:
        b = bits & -bits
        bits -= b
        v = b.bit_length() - 1
        saturation[v] = 1
        changed.append(v)

    def dfs(remaining, used_colors):
        if remaining == 0:
            return True

        best = -1
        best_sat = -1
        best_deg = -1

        bits = remaining
        while bits:
            b = bits & -bits
            bits -= b
            v = b.bit_length() - 1
            sat = saturation[v].bit_count()
            deg = (adj[v] & remaining).bit_count()
            if sat > best_sat or (sat == best_sat and deg > best_deg):
                best = v
                best_sat = sat
                best_deg = deg

        forbidden = saturation[best]
        limit = min(3, used_colors + 1)

        for c in range(limit):
            cb = 1 << c
            if forbidden & cb:
                continue

            colors[best] = c
            updates = []
            conflict = False
            neighbors = adj[best] & (remaining ^ (1 << best))

            while neighbors:
                b = neighbors & -neighbors
                neighbors -= b
                u = b.bit_length() - 1
                old = saturation[u]
                new = old | cb
                if new != old:
                    saturation[u] = new
                    updates.append((u, old))
                    if new == 7:
                        conflict = True
                        break

            if not conflict:
                new_used = used_colors + (c == used_colors)
                if dfs(remaining ^ (1 << best), new_used):
                    return True

            for u, old in reversed(updates):
                saturation[u] = old
            colors[best] = -1

        return False

    all_mask = (1 << n) - 1
    return dfs(all_mask ^ (1 << first), 1)


def lexicographically_smallest_component(adj):
    n = len(adj)
    all_mask = (1 << n) - 1
    closed = [adj[i] | (1 << i) for i in range(n)]
    suffix = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix[i] = suffix[i + 1] | (1 << i)

    result = None

    def bipartite_coloring(independent):
        rem = all_mask ^ independent
        side0 = 0
        side1 = 0
        unseen = rem

        while unseen:
            start = unseen & -unseen
            side0 |= start
            stack = start

            while stack:
                vb = stack & -stack
                stack -= vb
                v = vb.bit_length() - 1
                neighbors = adj[v] & rem

                if side0 & vb:
                    if neighbors & side0:
                        return None
                    new = neighbors & ~(side0 | side1)
                    side1 |= new
                else:
                    if neighbors & side1:
                        return None
                    new = neighbors & ~(side0 | side1)
                    side0 |= new

                stack |= new

            unseen = rem & ~(side0 | side1)

        coloring = [1] * n
        bits = side0
        while bits:
            b = bits & -bits
            bits -= b
            coloring[b.bit_length() - 1] = 2

        bits = side1
        while bits:
            b = bits & -bits
            bits -= b
            coloring[b.bit_length() - 1] = 3

        return coloring

    def viable(undominated, available):
        bits = undominated
        while bits:
            b = bits & -bits
            bits -= b
            u = b.bit_length() - 1
            if not (adj[u] & available):
                return False
        return True

    def dfs(i, independent, blocked, undominated):
        nonlocal result

        while i < n and (blocked & (1 << i)):
            i += 1

        if i == n:
            if undominated == 0:
                coloring = bipartite_coloring(independent)
                if coloring is not None:
                    result = coloring
                    return True
            return False

        bit = 1 << i

        # Prefer putting vertex i into color 1.
        new_independent = independent | bit
        new_blocked = blocked | closed[i]
        new_undominated = undominated & ~adj[i]
        available = suffix[i + 1] & ~new_blocked

        if viable(new_undominated, available):
            if dfs(i + 1, new_independent, new_blocked, new_undominated):
                return True

        # Otherwise exclude it; it must later be dominated for maximality.
        new_undominated = undominated | bit
        available = suffix[i + 1] & ~blocked

        if viable(new_undominated, available):
            if dfs(i + 1, independent, blocked, new_undominated):
                return True

        return False

    dfs(0, 0, 0, 0)
    return result


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    graph = [0] * n
    invalid = False

    pos = 2
    for _ in range(m):
        u = data[pos] - 1
        v = data[pos + 1] - 1
        pos += 2
        if u == v:
            invalid = True
        else:
            graph[u] |= 1 << v
            graph[v] |= 1 << u

    if invalid:
        print("NO")
        return

    answer = [0] * n
    unseen = (1 << n) - 1

    while unseen:
        start = unseen & -unseen
        component_mask = 0
        frontier = start

        while frontier:
            component_mask |= frontier
            neighbors = 0
            bits = frontier
            while bits:
                b = bits & -bits
                bits -= b
                v = b.bit_length() - 1
                neighbors |= graph[v]
            frontier = neighbors & unseen & ~component_mask

        unseen &= ~component_mask

        vertices = []
        bits = component_mask
        while bits:
            b = bits & -bits
            bits -= b
            vertices.append(b.bit_length() - 1)

        k = len(vertices)
        index = {v: i for i, v in enumerate(vertices)}
        local_adj = [0] * k

        for i, v in enumerate(vertices):
            neighbors = graph[v] & component_mask
            mask = 0
            while neighbors:
                b = neighbors & -neighbors
                neighbors -= b
                mask |= 1 << index[b.bit_length() - 1]
            local_adj[i] = mask

        if not is_three_colorable(local_adj):
            print("NO")
            return

        coloring = lexicographically_smallest_component(local_adj)
        if coloring is None:
            print("NO")
            return

        for i, v in enumerate(vertices):
            answer[v] = coloring[i]

    print("YES")
    print(*answer)


if __name__ == "__main__":
    main()