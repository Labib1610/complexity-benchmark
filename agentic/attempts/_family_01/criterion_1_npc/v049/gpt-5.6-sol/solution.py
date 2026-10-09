import sys
from collections import deque

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
        if u == v:
            print("NO")
            return
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # A K4 immediately makes the graph non-3-colorable.
    for u in range(n):
        neighbors = adj[u]
        bits = neighbors
        while bits:
            vb = bits & -bits
            bits ^= vb
            v = vb.bit_length() - 1
            if v <= u:
                continue
            common = neighbors & adj[v]
            check = common
            while check:
                xb = check & -check
                check ^= xb
                x = xb.bit_length() - 1
                if adj[x] & (common ^ xb):
                    print("NO")
                    return

    # Remove vertices of degree at most two. Any coloring of the remaining
    # 3-core can be greedily extended in reverse removal order.
    active = [True] * n
    degree = [adj[v].bit_count() for v in range(n)]
    queue = deque(v for v in range(n) if degree[v] <= 2)
    removed = []

    while queue:
        v = queue.popleft()
        if not active[v] or degree[v] > 2:
            continue
        active[v] = False
        removed.append(v)

        bits = adj[v]
        while bits:
            ub = bits & -bits
            bits ^= ub
            u = ub.bit_length() - 1
            if active[u]:
                degree[u] -= 1
                if degree[u] == 2:
                    queue.append(u)

    colors = [0] * n
    seen = [False] * n

    def solve_component(vertices):
        k = len(vertices)
        index = {v: i for i, v in enumerate(vertices)}
        local_adj = [0] * k

        for i, v in enumerate(vertices):
            bits = adj[v]
            mask = 0
            while bits:
                ub = bits & -bits
                bits ^= ub
                u = ub.bit_length() - 1
                j = index.get(u)
                if j is not None:
                    mask |= 1 << j
            local_adj[i] = mask

        all_mask = (1 << k) - 1

        def bipartite(rem):
            unseen = rem
            side_a = 0
            side_b = 0

            while unseen:
                seed = unseen & -unseen
                unseen ^= seed
                side_a |= seed
                frontier = seed
                side = 0

                while frontier:
                    neighbors = 0
                    bits = frontier
                    while bits:
                        vb = bits & -bits
                        bits ^= vb
                        v = vb.bit_length() - 1
                        neighbors |= local_adj[v]

                    neighbors &= rem
                    if side == 0:
                        if neighbors & side_a:
                            return None
                        new_vertices = neighbors & unseen
                        side_b |= new_vertices
                    else:
                        if neighbors & side_b:
                            return None
                        new_vertices = neighbors & unseen
                        side_a |= new_vertices

                    unseen &= ~new_vertices
                    frontier = new_vertices
                    side ^= 1

            return side_a, side_b

        initial = bipartite(all_mask)
        if initial is not None:
            a, b = initial
            for i, v in enumerate(vertices):
                colors[v] = 1 if (a >> i) & 1 else 2
            return True

        # Maximal independent sets of the original graph are maximal cliques
        # in its complement.
        complement = [
            all_mask ^ (1 << i) ^ local_adj[i]
            for i in range(k)
        ]

        answer = None

        def bron_kerbosch(r, candidates, excluded):
            nonlocal answer

            if candidates == 0:
                if excluded == 0:
                    result = bipartite(all_mask ^ r)
                    if result is not None:
                        answer = (r, result[0], result[1])
                        return True
                return False

            union = candidates | excluded
            pivot = -1
            best = -1
            bits = union
            while bits:
                ub = bits & -bits
                bits ^= ub
                u = ub.bit_length() - 1
                score = (candidates & complement[u]).bit_count()
                if score > best:
                    best = score
                    pivot = u

            if pivot == -1:
                branches = candidates
            else:
                branches = candidates & ~complement[pivot] & all_mask

            while branches:
                vb = branches & -branches
                branches ^= vb
                v = vb.bit_length() - 1

                if bron_kerbosch(
                    r | vb,
                    candidates & complement[v],
                    excluded & complement[v]
                ):
                    return True

                candidates ^= vb
                excluded |= vb

            return False

        if not bron_kerbosch(0, all_mask, 0):
            return False

        independent, a, b = answer
        for i, v in enumerate(vertices):
            bit = 1 << i
            if independent & bit:
                colors[v] = 3
            elif a & bit:
                colors[v] = 1
            else:
                colors[v] = 2
        return True

    # Solve each connected component of the remaining core.
    for start in range(n):
        if not active[start] or seen[start]:
            continue

        component = []
        stack = [start]
        seen[start] = True

        while stack:
            v = stack.pop()
            component.append(v)
            bits = adj[v]
            while bits:
                ub = bits & -bits
                bits ^= ub
                u = ub.bit_length() - 1
                if active[u] and not seen[u]:
                    seen[u] = True
                    stack.append(u)

        if not solve_component(component):
            print("NO")
            return

    # Extend the coloring through removed vertices.
    for v in reversed(removed):
        used = 0
        bits = adj[v]
        while bits:
            ub = bits & -bits
            bits ^= ub
            u = ub.bit_length() - 1
            if colors[u]:
                used |= 1 << colors[u]

        for c in (1, 2, 3):
            if not (used & (1 << c)):
                colors[v] = c
                break

        if colors[v] == 0:
            print("NO")
            return

    print("YES")
    print(*colors)

if __name__ == "__main__":
    main()