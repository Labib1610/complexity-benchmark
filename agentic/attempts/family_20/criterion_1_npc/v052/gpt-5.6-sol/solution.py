import sys

sys.setrecursionlimit(10000)

PERMS = (
    (1, 2, 4), (1, 4, 2),
    (2, 1, 4), (2, 4, 1),
    (4, 1, 2), (4, 2, 1)
)


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 2:
        return

    n, m = data[0], data[1]
    edges = []
    adj = [[] for _ in range(n)]

    pos = 2
    for eid in range(m):
        u = data[pos] - 1
        v = data[pos + 1] - 1
        pos += 2
        edges.append((u, v))
        adj[u].append(eid)
        adj[v].append(eid)

    if any(len(adj[v]) != 3 for v in range(n)):
        print("NO")
        return

    # A cubic graph with a bridge cannot have a proper 3-edge-coloring.
    tin = [-1] * n
    low = [0] * n
    timer = 0
    has_bridge = False

    def find_bridges(v, parent_edge):
        nonlocal timer, has_bridge
        tin[v] = low[v] = timer
        timer += 1

        for eid in adj[v]:
            if eid == parent_edge:
                continue
            a, b = edges[eid]
            to = b if a == v else a
            if tin[to] == -1:
                find_bridges(to, eid)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    has_bridge = True
            else:
                low[v] = min(low[v], tin[to])

    for start in range(n):
        if tin[start] == -1:
            find_bridges(start, -1)

    if has_bridge:
        print("NO")
        return

    components = []
    seen = [False] * n

    for start in range(n):
        if seen[start]:
            continue
        stack = [start]
        seen[start] = True
        vertices = []
        edge_set = set()

        while stack:
            v = stack.pop()
            vertices.append(v)
            for eid in adj[v]:
                edge_set.add(eid)
                a, b = edges[eid]
                to = b if a == v else a
                if not seen[to]:
                    seen[to] = True
                    stack.append(to)

        components.append((vertices, list(edge_set)))

    domains = [7] * m
    trail = []

    def narrow(eid, new_domain, queue):
        old = domains[eid]
        new_domain &= old
        if new_domain == old:
            return new_domain != 0
        if new_domain == 0:
            return False
        trail.append((eid, old))
        domains[eid] = new_domain
        u, v = edges[eid]
        queue.append(u)
        queue.append(v)
        return True

    def propagate(initial_queue):
        queue = initial_queue
        head = 0

        while head < len(queue):
            v = queue[head]
            head += 1

            e0, e1, e2 = adj[v]
            d0, d1, d2 = domains[e0], domains[e1], domains[e2]

            s0 = s1 = s2 = 0
            found = False

            for p0, p1, p2 in PERMS:
                if (d0 & p0) and (d1 & p1) and (d2 & p2):
                    found = True
                    s0 |= p0
                    s1 |= p1
                    s2 |= p2

            if not found:
                return False

            if s0 != d0 and not narrow(e0, s0, queue):
                return False
            if s1 != d1 and not narrow(e1, s1, queue):
                return False
            if s2 != d2 and not narrow(e2, s2, queue):
                return False

        return True

    def options_for_vertex(v):
        e0, e1, e2 = adj[v]
        d0, d1, d2 = domains[e0], domains[e1], domains[e2]
        result = []
        for p in PERMS:
            if (d0 & p[0]) and (d1 & p[1]) and (d2 & p[2]):
                result.append(p)
        return result

    def solve_component(vertices, component_edges):
        root = vertices[0]
        root_edges = adj[root]
        marker = len(trail)
        queue = []

        for eid, color in zip(root_edges, (1, 2, 4)):
            if not narrow(eid, color, queue):
                while len(trail) > marker:
                    e, old = trail.pop()
                    domains[e] = old
                return False

        if not propagate(queue):
            while len(trail) > marker:
                e, old = trail.pop()
                domains[e] = old
            return False

        def dfs():
            best_v = -1
            best_options = None
            best_count = 7
            best_score = -1

            for v in vertices:
                opts = options_for_vertex(v)
                count = len(opts)

                if count == 0:
                    return False
                if count == 1:
                    continue

                score = 0
                for eid in adj[v]:
                    score += 3 - domains[eid].bit_count()
                    a, b = edges[eid]
                    to = b if a == v else a
                    for ne in adj[to]:
                        score += 3 - domains[ne].bit_count()

                if count < best_count or (count == best_count and score > best_score):
                    best_count = count
                    best_score = score
                    best_v = v
                    best_options = opts

            if best_v == -1:
                return True

            incident = adj[best_v]

            for option in best_options:
                branch_marker = len(trail)
                queue = []
                valid = True

                for i in range(3):
                    if not narrow(incident[i], option[i], queue):
                        valid = False
                        break

                if valid and propagate(queue) and dfs():
                    return True

                while len(trail) > branch_marker:
                    eid, old = trail.pop()
                    domains[eid] = old

            return False

        if dfs():
            return True

        while len(trail) > marker:
            eid, old = trail.pop()
            domains[eid] = old
        return False

    for vertices, component_edges in components:
        if not solve_component(vertices, component_edges):
            print("NO")
            return

    answer = []
    for d in domains:
        if d == 1:
            answer.append("1")
        elif d == 2:
            answer.append("2")
        elif d == 4:
            answer.append("3")
        else:
            print("NO")
            return

    print("YES")
    print(" ".join(answer))


if __name__ == "__main__":
    main()