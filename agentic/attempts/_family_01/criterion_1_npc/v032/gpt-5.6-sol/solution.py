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

    answer = [0] * n

    def bipartite(component):
        side0 = 0
        side1 = 0
        unseen = component

        while unseen:
            start_bit = unseen & -unseen
            unseen ^= start_bit
            side0 |= start_bit
            queue = start_bit

            while queue:
                bit = queue & -queue
                queue ^= bit
                v = bit.bit_length() - 1

                if side0 & bit:
                    same, other = side0, side1
                else:
                    same, other = side1, side0

                neighbors = adj[v] & component
                if neighbors & same:
                    return None

                new_vertices = neighbors & unseen
                if new_vertices:
                    unseen ^= new_vertices
                    if side0 & bit:
                        side1 |= new_vertices
                    else:
                        side0 |= new_vertices
                    queue |= new_vertices

        return side0, side1

    def solve_component(component):
        bi = bipartite(component)
        if bi is not None:
            return bi[0], bi[1], 0

        vertices = []
        temp = component
        while temp:
            bit = temp & -temp
            temp ^= bit
            vertices.append(bit.bit_length() - 1)

        best_triangle = None
        best_score = -1

        for u in vertices:
            higher = adj[u] & component & ~((1 << (u + 1)) - 1)
            while higher:
                vb = higher & -higher
                higher ^= vb
                v = vb.bit_length() - 1
                common = adj[u] & adj[v] & component & ~((1 << (v + 1)) - 1)
                while common:
                    wb = common & -common
                    common ^= wb
                    w = wb.bit_length() - 1
                    score = (
                        (adj[u] & component).bit_count()
                        + (adj[v] & component).bit_count()
                        + (adj[w] & component).bit_count()
                    )
                    if score > best_score:
                        best_score = score
                        best_triangle = (u, v, w)

        if best_triangle is not None:
            a, b, c = best_triangle
            initial = (1 << a, 1 << b, 1 << c)
        else:
            best_edge = None
            best_score = -1
            for u in vertices:
                neighbors = adj[u] & component & ~((1 << (u + 1)) - 1)
                while neighbors:
                    vb = neighbors & -neighbors
                    neighbors ^= vb
                    v = vb.bit_length() - 1
                    score = (
                        (adj[u] & component).bit_count()
                        + (adj[v] & component).bit_count()
                    )
                    if score > best_score:
                        best_score = score
                        best_edge = (u, v)

            if best_edge is None:
                return component, 0, 0

            a, b = best_edge
            initial = (1 << a, 1 << b, 0)

        failed = set()
        memo_limit = 350000

        def dfs(c0, c1, c2):
            colored = c0 | c1 | c2
            uncolored = component ^ colored
            if not uncolored:
                return c0, c1, c2

            key = (c0, c1, c2)
            if key in failed:
                return None

            chosen = -1
            chosen_forbidden = 0
            best_sat = -1
            best_degree = -1

            scan = uncolored
            while scan:
                bit = scan & -scan
                scan ^= bit
                v = bit.bit_length() - 1

                forbidden = 0
                av = adj[v]
                if av & c0:
                    forbidden |= 1
                if av & c1:
                    forbidden |= 2
                if av & c2:
                    forbidden |= 4

                sat = forbidden.bit_count()
                if sat == 3:
                    if len(failed) < memo_limit:
                        failed.add(key)
                    return None

                degree = (av & uncolored).bit_count()
                if sat > best_sat or (sat == best_sat and degree > best_degree):
                    best_sat = sat
                    best_degree = degree
                    chosen = v
                    chosen_forbidden = forbidden

            bit = 1 << chosen
            options = []

            for color, mask in enumerate((c0, c1, c2)):
                if chosen_forbidden & (1 << color):
                    continue

                impact = 0
                neighbors = adj[chosen] & uncolored
                while neighbors:
                    nb = neighbors & -neighbors
                    neighbors ^= nb
                    u = nb.bit_length() - 1
                    if not (adj[u] & mask):
                        impact += 1
                options.append((impact, color))

            options.sort()

            for _, color in options:
                if color == 0:
                    result = dfs(c0 | bit, c1, c2)
                elif color == 1:
                    result = dfs(c0, c1 | bit, c2)
                else:
                    result = dfs(c0, c1, c2 | bit)

                if result is not None:
                    return result

            if len(failed) < memo_limit:
                failed.add(key)
            return None

        return dfs(*initial)

    unseen = (1 << n) - 1

    while unseen:
        start = unseen & -unseen
        unseen ^= start
        component = start
        frontier = start

        while frontier:
            bit = frontier & -frontier
            frontier ^= bit
            v = bit.bit_length() - 1
            new_vertices = adj[v] & unseen
            if new_vertices:
                unseen ^= new_vertices
                component |= new_vertices
                frontier |= new_vertices

        coloring = solve_component(component)
        if coloring is None:
            print("NO")
            return

        for color, mask in enumerate(coloring, 1):
            current = mask
            while current:
                bit = current & -current
                current ^= bit
                answer[bit.bit_length() - 1] = color

    print("YES")
    print(*answer)

if __name__ == "__main__":
    main()