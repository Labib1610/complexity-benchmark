import sys

sys.setrecursionlimit(1_000_000)


def contains_k4(adj):
    n = len(adj)
    for u in range(n):
        vs = adj[u] & ~((1 << (u + 1)) - 1)
        while vs:
            vb = vs & -vs
            vs ^= vb
            v = vb.bit_length() - 1
            common = adj[u] & adj[v] & ~((1 << (v + 1)) - 1)
            ws = common
            while ws:
                wb = ws & -ws
                ws ^= wb
                w = wb.bit_length() - 1
                if adj[w] & common & ~((1 << (w + 1)) - 1):
                    return True
    return False


def solve_component(adj):
    n = len(adj)
    full = (1 << n) - 1

    if contains_k4(adj):
        return None

    comp_adj = [
        full & ~(adj[v] | (1 << v))
        for v in range(n)
    ]

    def bipartite(rem):
        side0 = 0
        side1 = 0
        unseen = rem
        queue = 0

        while unseen:
            start = unseen & -unseen
            unseen ^= start
            side0 |= start
            queue |= start

            while queue:
                bit = queue & -queue
                queue ^= bit
                v = bit.bit_length() - 1
                neighbors = adj[v] & rem

                if side0 & bit:
                    if neighbors & side0:
                        return None
                    new_vertices = neighbors & unseen
                    unseen ^= new_vertices
                    side1 |= new_vertices
                else:
                    if neighbors & side1:
                        return None
                    new_vertices = neighbors & unseen
                    unseen ^= new_vertices
                    side0 |= new_vertices

                queue |= new_vertices

        return side0, side1

    initial_bipartition = bipartite(full)
    if initial_bipartition is not None:
        a, b = initial_bipartition
        colors = [0] * n
        for i in range(n):
            colors[i] = 2 if (a >> i) & 1 else 3
        return colors

    answer = None

    def search(chosen, candidates, excluded):
        nonlocal answer

        if candidates == 0:
            if excluded != 0:
                return False

            remainder = full ^ chosen
            partition = bipartite(remainder)
            if partition is None:
                return False

            a, b = partition
            colors = [1] * n
            for i in range(n):
                bit = 1 << i
                if a & bit:
                    colors[i] = 2
                elif b & bit:
                    colors[i] = 3
            answer = colors
            return True

        union = candidates | excluded
        pivot = -1
        best_count = -1
        temp = union
        while temp:
            bit = temp & -temp
            temp ^= bit
            u = bit.bit_length() - 1
            count = (candidates & comp_adj[u]).bit_count()
            if count > best_count:
                best_count = count
                pivot = u

        branch_vertices = candidates & ~comp_adj[pivot]

        while branch_vertices:
            bit = branch_vertices & -branch_vertices
            branch_vertices ^= bit
            v = bit.bit_length() - 1

            if search(
                chosen | bit,
                candidates & comp_adj[v],
                excluded & comp_adj[v]
            ):
                return True

            candidates ^= bit
            excluded |= bit

        return False

    search(0, full, 0)
    return answer


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    graph = [0] * n

    pos = 2
    for _ in range(m):
        u = data[pos] - 1
        v = data[pos + 1] - 1
        pos += 2
        if u == v:
            print("NO")
            return
        graph[u] |= 1 << v
        graph[v] |= 1 << u

    colors = [0] * n
    unvisited = (1 << n) - 1

    while unvisited:
        start = unvisited & -unvisited
        component_mask = 0
        frontier = start
        unvisited ^= start

        while frontier:
            bit = frontier & -frontier
            frontier ^= bit
            v = bit.bit_length() - 1
            component_mask |= bit

            new_vertices = graph[v] & unvisited
            unvisited ^= new_vertices
            frontier |= new_vertices

        vertices = []
        temp = component_mask
        while temp:
            bit = temp & -temp
            temp ^= bit
            vertices.append(bit.bit_length() - 1)

        index = {v: i for i, v in enumerate(vertices)}
        local_adj = [0] * len(vertices)

        for i, v in enumerate(vertices):
            neighbors = graph[v] & component_mask
            while neighbors:
                bit = neighbors & -neighbors
                neighbors ^= bit
                local_adj[i] |= 1 << index[bit.bit_length() - 1]

        local_colors = solve_component(local_adj)
        if local_colors is None:
            print("NO")
            return

        for i, v in enumerate(vertices):
            colors[v] = local_colors[i]

    print("YES")
    print(*colors)


if __name__ == "__main__":
    main()