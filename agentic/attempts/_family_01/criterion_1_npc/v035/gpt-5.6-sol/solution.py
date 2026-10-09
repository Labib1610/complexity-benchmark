import sys

def solve_component(vertices, global_adj):
    vertices.sort(key=lambda v: (global_adj[v].bit_count(), v), reverse=True)
    k = len(vertices)
    full = (1 << k) - 1
    index = {v: i for i, v in enumerate(vertices)}

    adj = [0] * k
    for i, v in enumerate(vertices):
        mask = global_adj[v]
        local = 0
        while mask:
            bit = mask & -mask
            w = bit.bit_length() - 1
            j = index.get(w)
            if j is not None:
                local |= 1 << j
            mask ^= bit
        adj[i] = local

    # A K4 makes a 3-coloring impossible.
    for u in range(k):
        vs = adj[u] & ~((1 << (u + 1)) - 1)
        while vs:
            vb = vs & -vs
            v = vb.bit_length() - 1
            common = adj[u] & adj[v]
            test = common
            while test:
                wb = test & -test
                w = wb.bit_length() - 1
                if adj[w] & common:
                    return None
                test ^= wb
            vs ^= vb

    def bipartite(remain):
        todo = remain
        side_a = 0
        side_b = 0

        while todo:
            start = todo & -todo
            todo ^= start
            side_a |= start
            queue = start

            while queue:
                vb = queue & -queue
                queue ^= vb
                v = vb.bit_length() - 1
                neighbors = adj[v] & remain

                if vb & side_a:
                    if neighbors & side_a:
                        return None
                    new_vertices = neighbors & todo
                    side_b |= new_vertices
                else:
                    if neighbors & side_b:
                        return None
                    new_vertices = neighbors & todo
                    side_a |= new_vertices

                todo ^= new_vertices
                queue |= new_vertices

        return side_a, side_b

    initial = bipartite(full)
    if initial is not None:
        a, b = initial
        result = [0] * k
        for i in range(k):
            bit = 1 << i
            result[i] = 2 if a & bit else 3
        return result

    # Maximal independent sets in the original graph are maximal cliques
    # in its complement.
    comp_adj = [full & ~(adj[i] | (1 << i)) for i in range(k)]
    answer = None

    def bron_kerbosch(chosen, possible, excluded):
        nonlocal answer

        if possible == 0:
            if excluded == 0:
                remaining = full ^ chosen
                parts = bipartite(remaining)
                if parts is not None:
                    answer = (chosen, parts[0], parts[1])
                    return True
            return False

        union = possible | excluded
        pivot = -1
        best_score = -1
        temp = union
        while temp:
            ub = temp & -temp
            u = ub.bit_length() - 1
            score = (possible & comp_adj[u]).bit_count()
            if score > best_score:
                best_score = score
                pivot = u
                if score == possible.bit_count():
                    break
            temp ^= ub

        candidates = possible if pivot < 0 else possible & ~comp_adj[pivot]

        while candidates:
            vb = candidates & -candidates
            v = vb.bit_length() - 1

            if bron_kerbosch(
                chosen | vb,
                possible & comp_adj[v],
                excluded & comp_adj[v]
            ):
                return True

            possible ^= vb
            excluded |= vb
            candidates ^= vb

        return False

    if not bron_kerbosch(0, full, 0):
        return None

    chosen, side_a, side_b = answer
    result = [0] * k
    for i in range(k):
        bit = 1 << i
        if chosen & bit:
            result[i] = 1
        elif side_a & bit:
            result[i] = 2
        else:
            result[i] = 3
    return result


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
        if u != v:
            adj[u] |= 1 << v
            adj[v] |= 1 << u

    colors = [0] * n
    unseen = (1 << n) - 1

    while unseen:
        start = unseen & -unseen
        unseen ^= start
        component_mask = start
        frontier = start

        while frontier:
            vb = frontier & -frontier
            frontier ^= vb
            v = vb.bit_length() - 1
            new_vertices = adj[v] & unseen
            unseen ^= new_vertices
            component_mask |= new_vertices
            frontier |= new_vertices

        vertices = []
        temp = component_mask
        while temp:
            vb = temp & -temp
            vertices.append(vb.bit_length() - 1)
            temp ^= vb

        component_colors = solve_component(vertices, adj)
        if component_colors is None:
            print("NO")
            return

        for i, v in enumerate(vertices):
            colors[v] = component_colors[i]

    print("YES")
    print(*colors)


if __name__ == "__main__":
    main()