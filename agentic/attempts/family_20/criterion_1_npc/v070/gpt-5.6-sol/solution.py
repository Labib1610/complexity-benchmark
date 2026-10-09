import sys
from itertools import permutations

sys.setrecursionlimit(10000)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 2:
        return

    n, m = data[0], data[1]
    if len(data) != 2 + 2 * m:
        print("NO")
        return

    edges = []
    incident = [[] for _ in range(n)]

    pos = 2
    for eid in range(m):
        u = data[pos] - 1
        v = data[pos + 1] - 1
        pos += 2
        if not (0 <= u < n and 0 <= v < n) or u == v:
            print("NO")
            return
        edges.append((u, v))
        incident[u].append(eid)
        incident[v].append(eid)

    if any(len(incident[v]) != 3 for v in range(n)):
        print("NO")
        return

    # Find connected components and reject bridges.
    tin = [-1] * n
    low = [0] * n
    timer = 0
    components = []
    has_bridge = False

    def dfs_bridge(v, parent_edge, vertices, component_edges):
        nonlocal timer, has_bridge
        tin[v] = low[v] = timer
        timer += 1
        vertices.append(v)

        for eid in incident[v]:
            u, w = edges[eid]
            to = w if u == v else u

            if eid == parent_edge:
                continue

            if tin[to] != -1:
                low[v] = min(low[v], tin[to])
            else:
                component_edges.append(eid)
                dfs_bridge(to, eid, vertices, component_edges)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    has_bridge = True

    for start in range(n):
        if tin[start] == -1:
            vertices = []
            tree_edges = []
            dfs_bridge(start, -1, vertices, tree_edges)

            edge_set = set()
            for v in vertices:
                edge_set.update(incident[v])
            components.append((vertices, list(edge_set)))

    if has_bridge:
        print("NO")
        return

    domains = [7] * m
    trail = []
    perms = list(permutations((1, 2, 4)))

    def rollback(mark):
        while len(trail) > mark:
            eid, old = trail.pop()
            domains[eid] = old

    def restrict(eid, new_mask, queue, in_queue):
        old = domains[eid]
        new_mask &= old
        if new_mask == old:
            return new_mask != 0
        trail.append((eid, old))
        domains[eid] = new_mask
        if new_mask == 0:
            return False

        u, v = edges[eid]
        if not in_queue[u]:
            in_queue[u] = True
            queue.append(u)
        if not in_queue[v]:
            in_queue[v] = True
            queue.append(v)
        return True

    def propagate(initial_vertices):
        queue = []
        in_queue = [False] * n

        for v in initial_vertices:
            if not in_queue[v]:
                in_queue[v] = True
                queue.append(v)

        head = 0
        while head < len(queue):
            v = queue[head]
            head += 1
            in_queue[v] = False

            e0, e1, e2 = incident[v]
            d0, d1, d2 = domains[e0], domains[e1], domains[e2]

            a0 = a1 = a2 = 0
            found = False
            for p0, p1, p2 in perms:
                if (d0 & p0) and (d1 & p1) and (d2 & p2):
                    found = True
                    a0 |= p0
                    a1 |= p1
                    a2 |= p2

            if not found:
                return False

            if not restrict(e0, a0, queue, in_queue):
                return False
            if not restrict(e1, a1, queue, in_queue):
                return False
            if not restrict(e2, a2, queue, in_queue):
                return False

        return True

    def solve_component(vertices, component_edges):
        root_mark = len(trail)
        root = vertices[0]
        queue_vertices = set()

        for eid, color_bit in zip(incident[root], (1, 2, 4)):
            old = domains[eid]
            if not (old & color_bit):
                rollback(root_mark)
                return False
            if old != color_bit:
                trail.append((eid, old))
                domains[eid] = color_bit
                u, v = edges[eid]
                queue_vertices.add(u)
                queue_vertices.add(v)

        if not propagate(queue_vertices):
            rollback(root_mark)
            return False

        def search():
            chosen = -1
            chosen_size = 4
            chosen_score = -1

            for eid in component_edges:
                mask = domains[eid]
                size = mask.bit_count()
                if size <= 1:
                    continue

                u, v = edges[eid]
                score = 0
                for other in incident[u]:
                    if other != eid:
                        score += 3 - domains[other].bit_count()
                for other in incident[v]:
                    if other != eid:
                        score += 3 - domains[other].bit_count()

                if size < chosen_size or (size == chosen_size and score > chosen_score):
                    chosen = eid
                    chosen_size = size
                    chosen_score = score

            if chosen == -1:
                return True

            mask = domains[chosen]
            values = []
            bit = 1
            while bit <= 4:
                if mask & bit:
                    u, v = edges[chosen]
                    value_score = 0
                    for other in incident[u]:
                        if other != chosen:
                            value_score += (domains[other] & ~bit).bit_count()
                    for other in incident[v]:
                        if other != chosen:
                            value_score += (domains[other] & ~bit).bit_count()
                    values.append((-value_score, bit))
                bit <<= 1
            values.sort()

            for _, color_bit in values:
                mark = len(trail)
                old = domains[chosen]
                trail.append((chosen, old))
                domains[chosen] = color_bit

                u, v = edges[chosen]
                if propagate((u, v)) and search():
                    return True

                rollback(mark)

            return False

        if search():
            return True

        rollback(root_mark)
        return False

    for vertices, component_edges in components:
        if not solve_component(vertices, component_edges):
            print("NO")
            return

    answer = []
    for mask in domains:
        if mask == 1:
            answer.append("1")
        elif mask == 2:
            answer.append("2")
        elif mask == 4:
            answer.append("3")
        else:
            print("NO")
            return

    print("YES")
    print(" ".join(answer))

if __name__ == "__main__":
    main()