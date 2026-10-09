import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    adj_mask = [0] * n
    adj = [[] for _ in range(n)]
    impossible = False

    p = 2
    for _ in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        if u == v:
            impossible = True
        elif not ((adj_mask[u] >> v) & 1):
            adj_mask[u] |= 1 << v
            adj_mask[v] |= 1 << u
            adj[u].append(v)
            adj[v].append(u)

    if impossible:
        print("NO")
        return

    degree = [len(x) for x in adj]
    colors = [-1] * n
    sat_mask = [0] * n

    # Find connected components.
    components = []
    unseen = (1 << n) - 1
    while unseen:
        start_bit = unseen & -unseen
        unseen ^= start_bit
        start = start_bit.bit_length() - 1
        stack = [start]
        comp = []
        comp_mask = 0

        while stack:
            v = stack.pop()
            comp.append(v)
            comp_mask |= 1 << v
            candidates = adj_mask[v] & unseen
            while candidates:
                bit = candidates & -candidates
                candidates ^= bit
                unseen ^= bit
                stack.append(bit.bit_length() - 1)

        components.append((comp, comp_mask))

    components.sort(
        key=lambda item: (sum(degree[v] for v in item[0]), len(item[0])),
        reverse=True
    )

    sys.setrecursionlimit(10000)

    def solve_component(comp, comp_mask):
        # Bipartite components need only two colors.
        side = {}
        bipartite = True
        for start in comp:
            if start in side:
                continue
            side[start] = 0
            queue = [start]
            qhead = 0
            while qhead < len(queue) and bipartite:
                v = queue[qhead]
                qhead += 1
                for u in adj[v]:
                    if u not in side:
                        side[u] = side[v] ^ 1
                        queue.append(u)
                    elif side[u] == side[v]:
                        bipartite = False
                        break
            if not bipartite:
                break

        if bipartite:
            for v in comp:
                colors[v] = side[v]
            return True

        uncolored = comp_mask

        def permanent_assign(v, c):
            nonlocal uncolored
            colors[v] = c
            uncolored ^= 1 << v
            bit = 1 << c
            neighbors = adj_mask[v] & uncolored
            while neighbors:
                b = neighbors & -neighbors
                neighbors ^= b
                u = b.bit_length() - 1
                sat_mask[u] |= bit
                if sat_mask[u] == 7:
                    return False
            return True

        # If there is a triangle, its three colors can be fixed by symmetry.
        best_triangle = None
        best_score = -1
        for i in comp:
            js = adj_mask[i] & comp_mask & ~((1 << (i + 1)) - 1)
            while js:
                bj = js & -js
                js ^= bj
                j = bj.bit_length() - 1
                ks = adj_mask[i] & adj_mask[j] & comp_mask
                ks &= ~((1 << (j + 1)) - 1)
                while ks:
                    bk = ks & -ks
                    ks ^= bk
                    k = bk.bit_length() - 1
                    score = degree[i] + degree[j] + degree[k]
                    if score > best_score:
                        best_score = score
                        best_triangle = (i, j, k)

        max_color = -1
        if best_triangle is not None:
            for c, v in enumerate(best_triangle):
                if not permanent_assign(v, c):
                    return False
            max_color = 2

        def dfs(remaining, max_used):
            if remaining == 0:
                return True

            best_v = -1
            best_key = (-1, -1, -1)

            bits = remaining
            while bits:
                b = bits & -bits
                bits ^= b
                v = b.bit_length() - 1
                sm = sat_mask[v]
                if sm == 7:
                    return False
                key = (
                    sm.bit_count(),
                    (adj_mask[v] & remaining).bit_count(),
                    degree[v]
                )
                if key > best_key:
                    best_key = key
                    best_v = v

            available = (~sat_mask[best_v]) & 7
            allowed_count = min(3, max_used + 2)
            available &= (1 << allowed_count) - 1
            if available == 0:
                return False

            candidates = []
            cm = available
            neighbor_bits = adj_mask[best_v] & remaining
            while cm:
                cb = cm & -cm
                cm ^= cb
                c = cb.bit_length() - 1
                impact = 0
                ns = neighbor_bits
                while ns:
                    nb = ns & -ns
                    ns ^= nb
                    u = nb.bit_length() - 1
                    if not (sat_mask[u] & cb):
                        impact += 1
                candidates.append((impact, c))

            candidates.sort()
            new_remaining = remaining ^ (1 << best_v)

            for _, c in candidates:
                color_bit = 1 << c
                colors[best_v] = c
                changed = []
                failed = False

                ns = adj_mask[best_v] & new_remaining
                while ns:
                    nb = ns & -ns
                    ns ^= nb
                    u = nb.bit_length() - 1
                    old = sat_mask[u]
                    new = old | color_bit
                    if new != old:
                        changed.append((u, old))
                        sat_mask[u] = new
                        if new == 7:
                            failed = True
                            break

                if not failed and dfs(new_remaining, max(max_used, c)):
                    return True

                for u, old in reversed(changed):
                    sat_mask[u] = old
                colors[best_v] = -1

            return False

        return dfs(uncolored, max_color)

    for comp, comp_mask in components:
        if not solve_component(comp, comp_mask):
            print("NO")
            return

    print("YES")
    print(*[c + 1 for c in colors])

if __name__ == "__main__":
    main()