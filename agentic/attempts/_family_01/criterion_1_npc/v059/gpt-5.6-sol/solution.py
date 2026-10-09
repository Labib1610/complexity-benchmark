import sys
from collections import deque

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
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # Vertices of degree at most two can always be colored after the rest.
    active = (1 << n) - 1
    degree = [adj[v].bit_count() for v in range(n)]
    queue = deque(v for v in range(n) if degree[v] <= 2)
    removed = []

    while queue:
        v = queue.popleft()
        if not (active >> v) & 1 or degree[v] > 2:
            continue

        active ^= 1 << v
        removed.append(v)

        neighbors = adj[v] & active
        while neighbors:
            bit = neighbors & -neighbors
            neighbors ^= bit
            u = bit.bit_length() - 1
            degree[u] -= 1
            if degree[u] <= 2:
                queue.append(u)

    colors = [-1] * n

    # Find connected components of the remaining 3-core.
    components = []
    unseen = active
    while unseen:
        start_bit = unseen & -unseen
        comp_mask = 0
        frontier = start_bit
        unseen ^= start_bit

        while frontier:
            bit = frontier & -frontier
            frontier ^= bit
            v = bit.bit_length() - 1
            comp_mask |= bit

            nxt = adj[v] & unseen
            unseen ^= nxt
            frontier |= nxt

        components.append(comp_mask)

    def has_k4(comp_mask, vertices):
        for u in vertices:
            higher_u = adj[u] & comp_mask & ~((1 << (u + 1)) - 1)
            x = higher_u
            while x:
                vb = x & -x
                x ^= vb
                v = vb.bit_length() - 1
                common = adj[u] & adj[v] & comp_mask
                common &= ~((1 << (v + 1)) - 1)

                y = common
                while y:
                    wb = y & -y
                    y ^= wb
                    w = wb.bit_length() - 1
                    if adj[w] & common & ~((1 << (w + 1)) - 1):
                        return True
        return False

    def solve_component(comp_mask):
        vertices = []
        bits = comp_mask
        while bits:
            bit = bits & -bits
            bits ^= bit
            vertices.append(bit.bit_length() - 1)

        if has_k4(comp_mask, vertices):
            return False

        comp_degree = {
            v: (adj[v] & comp_mask).bit_count() for v in vertices
        }

        # Fix colors of a triangle, if one exists. Otherwise fix an edge.
        best_triangle = None
        best_triangle_score = -1
        best_edge = None
        best_edge_score = -1

        for u in vertices:
            neighbors = adj[u] & comp_mask
            while neighbors:
                vb = neighbors & -neighbors
                neighbors ^= vb
                v = vb.bit_length() - 1
                if u >= v:
                    continue

                edge_score = comp_degree[u] + comp_degree[v]
                if edge_score > best_edge_score:
                    best_edge_score = edge_score
                    best_edge = (u, v)

                common = adj[u] & adj[v] & comp_mask
                common &= ~((1 << (v + 1)) - 1)
                while common:
                    wb = common & -common
                    common ^= wb
                    w = wb.bit_length() - 1
                    score = comp_degree[u] + comp_degree[v] + comp_degree[w]
                    if score > best_triangle_score:
                        best_triangle_score = score
                        best_triangle = (u, v, w)

        if best_triangle is not None:
            presets = [
                (best_triangle[0], 0),
                (best_triangle[1], 1),
                (best_triangle[2], 2),
            ]
        elif best_edge is not None:
            presets = [(best_edge[0], 0), (best_edge[1], 1)]
        else:
            presets = [(vertices[0], 0)]

        used = [0] * n
        uncolored = comp_mask

        def assign(v, c):
            nonlocal uncolored
            bit_color = 1 << c
            colors[v] = c
            uncolored ^= 1 << v
            changes = []

            neighbors = adj[v] & uncolored & comp_mask
            while neighbors:
                bit = neighbors & -neighbors
                neighbors ^= bit
                u = bit.bit_length() - 1
                old = used[u]
                new = old | bit_color
                if old != new:
                    used[u] = new
                    changes.append((u, old))

            return v, changes

        def undo(entry):
            nonlocal uncolored
            v, changes = entry
            for u, old in reversed(changes):
                used[u] = old
            colors[v] = -1
            uncolored |= 1 << v

        for v, c in presets:
            if colors[v] != -1:
                if colors[v] != c:
                    return False
                continue
            if used[v] & (1 << c):
                return False
            assign(v, c)

        def search():
            forced_trail = []

            while True:
                if uncolored == 0:
                    return True

                forced_vertex = -1
                forced_color = -1
                best_vertex = -1
                best_available = 0
                best_key = (-1, -1, -1)

                scan = uncolored
                while scan:
                    bit = scan & -scan
                    scan ^= bit
                    v = bit.bit_length() - 1

                    available = 7 & ~used[v]
                    count = available.bit_count()

                    if count == 0:
                        for entry in reversed(forced_trail):
                            undo(entry)
                        return False

                    if count == 1:
                        forced_vertex = v
                        forced_color = (available & -available).bit_length() - 1
                        break

                    saturation = used[v].bit_count()
                    remaining_degree = (adj[v] & uncolored & comp_mask).bit_count()
                    key = (saturation, remaining_degree, comp_degree[v])

                    if key > best_key:
                        best_key = key
                        best_vertex = v
                        best_available = available

                if forced_vertex != -1:
                    forced_trail.append(assign(forced_vertex, forced_color))
                    continue

                v = best_vertex
                available = best_available

                while available:
                    color_bit = available & -available
                    available ^= color_bit
                    c = color_bit.bit_length() - 1

                    entry = assign(v, c)
                    if search():
                        return True
                    undo(entry)

                for entry in reversed(forced_trail):
                    undo(entry)
                return False

        return search()

    for component in components:
        if not solve_component(component):
            print("NO")
            return

    # Extend the coloring through the removed vertices in reverse order.
    for v in reversed(removed):
        forbidden = 0
        neighbors = adj[v]
        while neighbors:
            bit = neighbors & -neighbors
            neighbors ^= bit
            u = bit.bit_length() - 1
            if colors[u] != -1:
                forbidden |= 1 << colors[u]

        for c in range(3):
            if not (forbidden >> c) & 1:
                colors[v] = c
                break

    print("YES")
    print(*(c + 1 for c in colors))

if __name__ == "__main__":
    main()