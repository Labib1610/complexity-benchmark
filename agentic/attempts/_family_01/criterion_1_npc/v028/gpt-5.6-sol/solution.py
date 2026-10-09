import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    adj = [0] * n
    p = 2
    for _ in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # Find connected components.
    components = []
    unseen = (1 << n) - 1
    while unseen:
        start_bit = unseen & -unseen
        unseen ^= start_bit
        stack = [start_bit.bit_length() - 1]
        comp = []

        while stack:
            v = stack.pop()
            comp.append(v)
            candidates = adj[v] & unseen
            while candidates:
                b = candidates & -candidates
                candidates ^= b
                unseen ^= b
                stack.append(b.bit_length() - 1)

        components.append(comp)

    answer = [-1] * n
    domains = [7] * n
    colors = [-1] * n

    def solve_component(vertices):
        comp_mask = 0
        for v in vertices:
            comp_mask |= 1 << v

        # Bipartite components need only two colors.
        side = [-1] * n
        bipartite = True
        for start in vertices:
            if side[start] != -1:
                continue
            side[start] = 0
            queue = [start]
            head = 0
            while head < len(queue) and bipartite:
                v = queue[head]
                head += 1
                nb = adj[v] & comp_mask
                while nb:
                    b = nb & -nb
                    nb ^= b
                    u = b.bit_length() - 1
                    if side[u] == -1:
                        side[u] = side[v] ^ 1
                        queue.append(u)
                    elif side[u] == side[v]:
                        bipartite = False
                        break
            if not bipartite:
                break

        if bipartite:
            for v in vertices:
                answer[v] = side[v]
            return True

        for v in vertices:
            colors[v] = -1
            domains[v] = 7

        trail = []

        def undo(checkpoint):
            while len(trail) > checkpoint:
                v, old = trail.pop()
                if old == -1:
                    colors[v] = -1
                else:
                    domains[v] = old

        def assign(first_v, first_bit):
            queue = [(first_v, first_bit)]
            head = 0

            while head < len(queue):
                v, bit = queue[head]
                head += 1

                if colors[v] != -1:
                    if (1 << colors[v]) != bit:
                        return False
                    continue

                if not (domains[v] & bit):
                    return False

                c = bit.bit_length() - 1
                trail.append((v, -1))
                colors[v] = c

                nb = adj[v] & comp_mask
                while nb:
                    b = nb & -nb
                    nb ^= b
                    u = b.bit_length() - 1

                    if colors[u] != -1:
                        if colors[u] == c:
                            return False
                        continue

                    old = domains[u]
                    if old & bit:
                        new = old & ~bit
                        trail.append((u, old))
                        domains[u] = new

                        if new == 0:
                            return False
                        if new & (new - 1) == 0:
                            queue.append((u, new))

            return True

        sys.setrecursionlimit(10000)

        def search():
            chosen = -1
            best_size = 4
            best_degree = -1
            best_uncolored_degree = -1

            for v in vertices:
                if colors[v] != -1:
                    continue

                size = domains[v].bit_count()
                uncolored_degree = 0
                nb = adj[v] & comp_mask
                while nb:
                    b = nb & -nb
                    nb ^= b
                    u = b.bit_length() - 1
                    if colors[u] == -1:
                        uncolored_degree += 1

                degree = (adj[v] & comp_mask).bit_count()
                if (size < best_size or
                    (size == best_size and degree > best_degree) or
                    (size == best_size and degree == best_degree and
                     uncolored_degree > best_uncolored_degree)):
                    chosen = v
                    best_size = size
                    best_degree = degree
                    best_uncolored_degree = uncolored_degree

            if chosen == -1:
                return True

            options = []
            bits = domains[chosen]
            while bits:
                bit = bits & -bits
                bits ^= bit
                impact = 0
                nb = adj[chosen] & comp_mask
                while nb:
                    b = nb & -nb
                    nb ^= b
                    u = b.bit_length() - 1
                    if colors[u] == -1 and (domains[u] & bit):
                        impact += 1
                options.append((impact, bit))
            options.sort()

            for _, bit in options:
                checkpoint = len(trail)
                if assign(chosen, bit) and search():
                    return True
                undo(checkpoint)

            return False

        root = max(vertices, key=lambda x: (adj[x] & comp_mask).bit_count())
        root_neighbors = adj[root] & comp_mask

        if not assign(root, 1):
            return False

        if root_neighbors:
            neighbor_vertices = []
            bits = root_neighbors
            while bits:
                b = bits & -bits
                bits ^= b
                neighbor_vertices.append(b.bit_length() - 1)
            second = max(
                neighbor_vertices,
                key=lambda x: (adj[x] & comp_mask).bit_count()
            )
            if not assign(second, 2):
                return False

        if not search():
            return False

        for v in vertices:
            answer[v] = colors[v]
        return True

    for component in components:
        if not solve_component(component):
            print("NO")
            return

    print("YES")
    print(*[c + 1 for c in answer])

if __name__ == "__main__":
    main()