import sys

sys.setrecursionlimit(1_000_000)


def solve_component(vertices, global_adj):
    k = len(vertices)
    index = {v: i for i, v in enumerate(vertices)}
    adj = [0] * k

    for i, v in enumerate(vertices):
        bits = global_adj[v]
        mask = 0
        while bits:
            b = bits & -bits
            u = b.bit_length() - 1
            if u in index:
                mask |= 1 << index[u]
            bits ^= b
        adj[i] = mask

    full = (1 << k) - 1
    degrees = [x.bit_count() for x in adj]

    # Find any 3-coloring using DSATUR. This also proves impossibility.
    colors = [-1] * k

    def dsatur(colored_count, max_used):
        if colored_count == k:
            return True

        chosen = -1
        chosen_sat = -1
        chosen_deg = -1
        chosen_forbidden = 0

        for v in range(k):
            if colors[v] != -1:
                continue
            forbidden = 0
            nb = adj[v]
            while nb:
                b = nb & -nb
                u = b.bit_length() - 1
                c = colors[u]
                if c != -1:
                    forbidden |= 1 << c
                nb ^= b

            sat = forbidden.bit_count()
            if sat > chosen_sat or (sat == chosen_sat and degrees[v] > chosen_deg):
                chosen = v
                chosen_sat = sat
                chosen_deg = degrees[v]
                chosen_forbidden = forbidden

        limit = min(2, max_used + 1)
        for c in range(limit + 1):
            if chosen_forbidden & (1 << c):
                continue
            colors[chosen] = c
            if dsatur(colored_count + 1, max(max_used, c)):
                return True
            colors[chosen] = -1
        return False

    if not dsatur(0, -1):
        return None

    def bipartite_after_removing(independent_set):
        rem = full ^ independent_set
        colored = 0
        side_a = 0

        while colored != rem:
            remaining = rem & ~colored
            root_bit = remaining & -remaining
            side_a |= root_bit
            colored |= root_bit
            queue = root_bit

            while queue:
                vb = queue & -queue
                queue ^= vb
                v = vb.bit_length() - 1
                nb = adj[v] & rem

                if side_a & vb:
                    if nb & side_a:
                        return None
                    new = nb & ~colored
                else:
                    side_b = colored & ~side_a
                    if nb & side_b:
                        return None
                    new = nb & ~colored
                    side_a &= ~new

                colored |= new
                queue |= new

        return side_a

    def make_tuple(independent_set, side_a):
        return tuple(
            1 if (independent_set >> i) & 1
            else 2 if (side_a >> i) & 1
            else 3
            for i in range(k)
        )

    best = None
    best_i = 0

    # Seed the upper bound from all color classes of the found coloring.
    for c in range(3):
        independent_set = 0
        for i in range(k):
            if colors[i] == c:
                independent_set |= 1 << i
        side_a = bipartite_after_removing(independent_set)
        if side_a is not None:
            candidate = make_tuple(independent_set, side_a)
            if best is None or candidate < best:
                best = candidate
                best_i = independent_set

    # Enumerate maximal independent sets as maximal cliques in the complement.
    comp = [full ^ adj[i] ^ (1 << i) for i in range(k)]

    def bron_kerbosch(r, p, x):
        nonlocal best, best_i

        if best is not None:
            possible = r | p
            diff = possible ^ best_i
            if diff == 0:
                return
            first = diff & -diff
            if best_i & first:
                return

        if p == 0:
            if x == 0:
                side_a = bipartite_after_removing(r)
                if side_a is not None:
                    candidate = make_tuple(r, side_a)
                    if best is None or candidate < best:
                        best = candidate
                        best_i = r
            return

        union = p | x
        pivot = -1
        pivot_score = -1
        temp = union
        while temp:
            b = temp & -temp
            u = b.bit_length() - 1
            score = (p & comp[u]).bit_count()
            if score > pivot_score:
                pivot_score = score
                pivot = u
            temp ^= b

        candidates = p if pivot == -1 else p & ~comp[pivot]
        while candidates:
            vb = candidates & -candidates
            candidates ^= vb
            v = vb.bit_length() - 1

            bron_kerbosch(r | vb, p & comp[v], x & comp[v])

            p ^= vb
            x |= vb

    bron_kerbosch(0, full, 0)
    return best


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    adj = [0] * n
    pos = 2

    for _ in range(m):
        u = data[pos] - 1
        v = data[pos + 1] - 1
        pos += 2
        if u != v:
            adj[u] |= 1 << v
            adj[v] |= 1 << u

    unseen = (1 << n) - 1
    components = []

    while unseen:
        root = unseen & -unseen
        unseen ^= root
        stack = root
        component_mask = 0

        while stack:
            vb = stack & -stack
            stack ^= vb
            v = vb.bit_length() - 1
            component_mask |= vb

            new = adj[v] & unseen
            unseen ^= new
            stack |= new

        vertices = []
        bits = component_mask
        while bits:
            b = bits & -bits
            vertices.append(b.bit_length() - 1)
            bits ^= b
        components.append(vertices)

    answer = [0] * n

    for vertices in components:
        result = solve_component(vertices, adj)
        if result is None:
            print("NO")
            return
        for i, v in enumerate(vertices):
            answer[v] = result[i]

    print("YES")
    print(*answer)


if __name__ == "__main__":
    main()