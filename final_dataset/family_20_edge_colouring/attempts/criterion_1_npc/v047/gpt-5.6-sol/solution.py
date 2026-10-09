import sys
sys.setrecursionlimit(10000)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 2:
        return

    n, m = data[0], data[1]
    if n % 2 or m != 3 * n // 2 or len(data) != 2 + 2 * m:
        print("NO")
        return

    edges = []
    adj = [[] for _ in range(n)]
    incident = [[] for _ in range(n)]

    pos = 2
    valid = True
    for eid in range(m):
        u = data[pos] - 1
        v = data[pos + 1] - 1
        pos += 2
        if not (0 <= u < v < n):
            valid = False
            continue
        edges.append((u, v))
        adj[u].append((v, eid))
        adj[v].append((u, eid))
        incident[u].append(eid)
        incident[v].append(eid)

    if not valid or len(edges) != m or any(len(x) != 3 for x in incident):
        print("NO")
        return

    # A cubic graph with a bridge cannot be 3-edge-colored.
    tin = [-1] * n
    low = [0] * n
    timer = 0
    has_bridge = False
    components = []

    def dfs_bridge(v, parent_edge, comp):
        nonlocal timer, has_bridge
        tin[v] = low[v] = timer
        timer += 1
        comp.append(v)

        for to, eid in adj[v]:
            if eid == parent_edge:
                continue
            if tin[to] != -1:
                low[v] = min(low[v], tin[to])
            else:
                dfs_bridge(to, eid, comp)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    has_bridge = True

    for start in range(n):
        if tin[start] == -1:
            comp = []
            dfs_bridge(start, -1, comp)
            components.append(comp)

    if has_bridge:
        print("NO")
        return

    # Bit masks for colors 1, 2, 3.
    domains = [7] * m
    permutations = (
        (1, 2, 4), (1, 4, 2),
        (2, 1, 4), (2, 4, 1),
        (4, 1, 2), (4, 2, 1)
    )

    def solve_component(vertices):
        trail = []

        def set_domain(eid, new_domain, queue):
            old = domains[eid]
            if old == new_domain:
                return True
            if new_domain == 0:
                return False
            trail.append((eid, old))
            domains[eid] = new_domain
            u, v = edges[eid]
            queue.append(u)
            queue.append(v)
            return True

        def rollback(mark):
            while len(trail) > mark:
                eid, old = trail.pop()
                domains[eid] = old

        def propagate(queue):
            qpos = 0
            while qpos < len(queue):
                v = queue[qpos]
                qpos += 1

                e0, e1, e2 = incident[v]
                d0, d1, d2 = domains[e0], domains[e1], domains[e2]

                s0 = s1 = s2 = 0
                found = False
                for a, b, c in permutations:
                    if (d0 & a) and (d1 & b) and (d2 & c):
                        found = True
                        s0 |= a
                        s1 |= b
                        s2 |= c

                if not found:
                    return False

                nd = d0 & s0
                if nd != d0 and not set_domain(e0, nd, queue):
                    return False
                nd = d1 & s1
                if nd != d1 and not set_domain(e1, nd, queue):
                    return False
                nd = d2 & s2
                if nd != d2 and not set_domain(e2, nd, queue):
                    return False

            return True

        def search(queue):
            if not propagate(queue):
                return False

            best_options = None
            best_edges = None
            best_key = (7, 100)

            for v in vertices:
                e0, e1, e2 = incident[v]
                d0, d1, d2 = domains[e0], domains[e1], domains[e2]

                if (d0 & (d0 - 1) == 0 and
                    d1 & (d1 - 1) == 0 and
                    d2 & (d2 - 1) == 0):
                    continue

                options = []
                for p in permutations:
                    if (d0 & p[0]) and (d1 & p[1]) and (d2 & p[2]):
                        options.append(p)

                if not options:
                    return False

                key = (len(options),
                       d0.bit_count() + d1.bit_count() + d2.bit_count())
                if key < best_key:
                    best_key = key
                    best_options = options
                    best_edges = (e0, e1, e2)
                    if key[0] == 2 and key[1] <= 5:
                        break

            if best_options is None:
                return True

            e0, e1, e2 = best_edges
            for p in best_options:
                mark = len(trail)
                next_queue = []
                ok = (
                    set_domain(e0, p[0], next_queue) and
                    set_domain(e1, p[1], next_queue) and
                    set_domain(e2, p[2], next_queue)
                )
                if ok and search(next_queue):
                    return True
                rollback(mark)

            return False

        # Remove the global color-permutation symmetry.
        root = vertices[0]
        root_edges = incident[root]
        initial_queue = []
        for eid, color in zip(root_edges, (1, 2, 4)):
            if not set_domain(eid, color, initial_queue):
                return False

        return search(initial_queue)

    for component in components:
        if not solve_component(component):
            print("NO")
            return

    if any(mask == 0 or mask & (mask - 1) for mask in domains):
        print("NO")
        return

    answer = [mask.bit_length() for mask in domains]
    print("YES")
    print(*answer)

if __name__ == "__main__":
    main()