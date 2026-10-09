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
        if u == v:
            print("NO")
            return
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    degree = [x.bit_count() for x in adj]
    color = [-1] * n
    forbidden_count = [[0, 0, 0] for _ in range(n)]

    # Find connected components.
    components = []
    unseen = (1 << n) - 1
    while unseen:
        start_bit = unseen & -unseen
        start = start_bit.bit_length() - 1
        unseen ^= start_bit
        component = []
        stack = [start]

        while stack:
            v = stack.pop()
            component.append(v)
            candidates = adj[v] & unseen
            while candidates:
                bit = candidates & -candidates
                candidates ^= bit
                unseen ^= bit
                stack.append(bit.bit_length() - 1)

        components.append(component)

    def bipartite_assignment(vertices):
        vertex_set = 0
        for v in vertices:
            vertex_set |= 1 << v

        side = [-1] * n
        for start in vertices:
            if side[start] != -1:
                continue
            side[start] = 0
            queue = deque([start])

            while queue:
                v = queue.popleft()
                neighbors = adj[v] & vertex_set
                while neighbors:
                    bit = neighbors & -neighbors
                    neighbors ^= bit
                    u = bit.bit_length() - 1
                    if side[u] == -1:
                        side[u] = side[v] ^ 1
                        queue.append(u)
                    elif side[u] == side[v]:
                        return None

        return side

    def solve_component(vertices):
        if len(vertices) == 1:
            color[vertices[0]] = 0
            return True

        bipartite = bipartite_assignment(vertices)
        if bipartite is not None:
            for v in vertices:
                color[v] = bipartite[v]
            return True

        vertex_mask = 0
        for v in vertices:
            vertex_mask |= 1 << v

        def assign(v, c):
            if color[v] != -1 or forbidden_count[v][c] != 0:
                return False
            color[v] = c
            neighbors = adj[v] & vertex_mask
            while neighbors:
                bit = neighbors & -neighbors
                neighbors ^= bit
                u = bit.bit_length() - 1
                forbidden_count[u][c] += 1
            return True

        def unassign(v, c):
            neighbors = adj[v] & vertex_mask
            while neighbors:
                bit = neighbors & -neighbors
                neighbors ^= bit
                u = bit.bit_length() - 1
                forbidden_count[u][c] -= 1
            color[v] = -1

        # Prefer fixing a high-degree triangle to all three colors.
        best_triangle = None
        best_score = -1
        for i, u in enumerate(vertices):
            later_u = adj[u] & vertex_mask
            for v in vertices[i + 1:]:
                if not (later_u >> v) & 1:
                    continue
                common = adj[u] & adj[v] & vertex_mask
                while common:
                    bit = common & -common
                    common ^= bit
                    w = bit.bit_length() - 1
                    if w <= v:
                        continue
                    score = degree[u] + degree[v] + degree[w]
                    if score > best_score:
                        best_score = score
                        best_triangle = (u, v, w)

        initial = []
        if best_triangle is not None:
            initial = [
                (best_triangle[0], 0),
                (best_triangle[1], 1),
                (best_triangle[2], 2),
            ]
        else:
            best_edge = None
            best_score = -1
            for u in vertices:
                neighbors = adj[u] & vertex_mask
                while neighbors:
                    bit = neighbors & -neighbors
                    neighbors ^= bit
                    v = bit.bit_length() - 1
                    if u < v:
                        score = degree[u] + degree[v]
                        if score > best_score:
                            best_score = score
                            best_edge = (u, v)
            initial = [(best_edge[0], 0), (best_edge[1], 1)]

        for v, c in initial:
            if not assign(v, c):
                return False

        def has_odd_two_domain_cycle(domains):
            for target_domain in (3, 5, 6):
                candidates = 0
                for v in vertices:
                    if color[v] == -1 and domains[v] == target_domain:
                        candidates |= 1 << v

                parity = {}
                remaining = candidates
                while remaining:
                    bit = remaining & -remaining
                    start = bit.bit_length() - 1
                    remaining ^= bit
                    parity[start] = 0
                    queue = [start]

                    while queue:
                        v = queue.pop()
                        neighbors = adj[v] & candidates
                        while neighbors:
                            nb = neighbors & -neighbors
                            neighbors ^= nb
                            u = nb.bit_length() - 1
                            if u not in parity:
                                parity[u] = parity[v] ^ 1
                                remaining &= ~nb
                                queue.append(u)
                            elif parity[u] == parity[v]:
                                return True
            return False

        def dfs():
            forced = []

            while True:
                forced_vertex = -1
                forced_color = -1
                domains = {}
                contradiction = False

                for v in vertices:
                    if color[v] != -1:
                        continue
                    domain = 0
                    for c in range(3):
                        if forbidden_count[v][c] == 0:
                            domain |= 1 << c
                    if domain == 0:
                        contradiction = True
                        break
                    domains[v] = domain
                    if domain & (domain - 1) == 0:
                        forced_vertex = v
                        forced_color = domain.bit_length() - 1
                        break

                if contradiction:
                    for v, c in reversed(forced):
                        unassign(v, c)
                    return False

                if forced_vertex == -1:
                    break

                assign(forced_vertex, forced_color)
                forced.append((forced_vertex, forced_color))

            domains = {}
            best_vertex = -1
            best_key = None

            for v in vertices:
                if color[v] != -1:
                    continue

                domain = 0
                for c in range(3):
                    if forbidden_count[v][c] == 0:
                        domain |= 1 << c
                domains[v] = domain

                uncolored_neighbors = 0
                neighbors = adj[v] & vertex_mask
                while neighbors:
                    bit = neighbors & -neighbors
                    neighbors ^= bit
                    u = bit.bit_length() - 1
                    if color[u] == -1:
                        uncolored_neighbors += 1

                key = (-domain.bit_count(), uncolored_neighbors, degree[v])
                if best_key is None or key > best_key:
                    best_key = key
                    best_vertex = v

            if best_vertex == -1:
                return True

            if has_odd_two_domain_cycle(domains):
                for v, c in reversed(forced):
                    unassign(v, c)
                return False

            choices = []
            domain = domains[best_vertex]
            for c in range(3):
                if domain & (1 << c):
                    impact = 0
                    neighbors = adj[best_vertex] & vertex_mask
                    while neighbors:
                        bit = neighbors & -neighbors
                        neighbors ^= bit
                        u = bit.bit_length() - 1
                        if color[u] == -1 and forbidden_count[u][c] == 0:
                            impact += 1
                    choices.append((impact, c))

            choices.sort()

            for _, c in choices:
                assign(best_vertex, c)
                if dfs():
                    return True
                unassign(best_vertex, c)

            for v, c in reversed(forced):
                unassign(v, c)
            return False

        if dfs():
            return True

        for v, c in reversed(initial):
            if color[v] == c:
                unassign(v, c)
        return False

    for component in components:
        if not solve_component(component):
            print("NO")
            return

    print("YES")
    print(*(c + 1 for c in color))

if __name__ == "__main__":
    main()