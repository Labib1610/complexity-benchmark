import sys

sys.setrecursionlimit(1000000)


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 2:
        return

    n, m = data[0], data[1]
    adj = [[] for _ in range(n)]
    edges = []

    p = 2
    for eid in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        edges.append((u, v))
        adj[u].append(eid)
        adj[v].append(eid)

    if m * 2 != 3 * n or any(len(adj[v]) != 3 for v in range(n)):
        print("NO")
        return

    # A cubic graph containing a bridge cannot be 3-edge-colored.
    tin = [-1] * n
    low = [0] * n
    timer = 0
    has_bridge = False

    def dfs_bridge(v, parent_edge):
        nonlocal timer, has_bridge
        tin[v] = low[v] = timer
        timer += 1

        for eid in adj[v]:
            if eid == parent_edge:
                continue
            a, b = edges[eid]
            to = b if a == v else a

            if tin[to] == -1:
                dfs_bridge(to, eid)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    has_bridge = True
            else:
                low[v] = min(low[v], tin[to])

    for start in range(n):
        if tin[start] == -1:
            dfs_bridge(start, -1)

    if has_bridge:
        print("NO")
        return

    # Domain masks: colors 1, 2, 3 correspond to bits 1, 2, 4.
    domains = [7] * m
    popcount = [0, 1, 1, 2, 1, 2, 2, 3]
    trail = []

    def rollback(mark):
        while len(trail) > mark:
            eid, old = trail.pop()
            domains[eid] = old

    def set_domain(eid, new_mask, queue):
        old = domains[eid]
        new_mask &= old
        if new_mask == old:
            return True
        if new_mask == 0:
            return False
        trail.append((eid, old))
        domains[eid] = new_mask
        u, v = edges[eid]
        queue.append(u)
        queue.append(v)
        return True

    def propagate(queue):
        head = 0

        while head < len(queue):
            v = queue[head]
            head += 1

            e0, e1, e2 = adj[v]
            es = (e0, e1, e2)
            ds = (domains[e0], domains[e1], domains[e2])

            if ds[0] == 0 or ds[1] == 0 or ds[2] == 0:
                return False

            # Hall conditions for three all-different variables.
            if (ds[0] | ds[1] | ds[2]) != 7:
                return False

            if popcount[ds[0] | ds[1]] < 2:
                return False
            if popcount[ds[0] | ds[2]] < 2:
                return False
            if popcount[ds[1] | ds[2]] < 2:
                return False

            singles = 0
            seen_single = 0
            for d in ds:
                if popcount[d] == 1:
                    if seen_single & d:
                        return False
                    seen_single |= d
                    singles |= d

            if singles:
                for i in range(3):
                    if popcount[ds[i]] > 1:
                        if not set_domain(es[i], domains[es[i]] & ~singles, queue):
                            return False

            union01 = ds[0] | ds[1]
            if popcount[union01] == 2:
                if not set_domain(e2, domains[e2] & ~union01, queue):
                    return False

            union02 = ds[0] | ds[2]
            if popcount[union02] == 2:
                if not set_domain(e1, domains[e1] & ~union02, queue):
                    return False

            union12 = ds[1] | ds[2]
            if popcount[union12] == 2:
                if not set_domain(e0, domains[e0] & ~union12, queue):
                    return False

        return True

    visited = [False] * n

    for start in range(n):
        if visited[start]:
            continue

        component_vertices = []
        component_edges = []
        edge_seen = set()
        stack = [start]
        visited[start] = True

        while stack:
            v = stack.pop()
            component_vertices.append(v)
            for eid in adj[v]:
                if eid not in edge_seen:
                    edge_seen.add(eid)
                    component_edges.append(eid)
                a, b = edges[eid]
                to = b if a == v else a
                if not visited[to]:
                    visited[to] = True
                    stack.append(to)

        # Fix the color permutation symmetry at one vertex.
        root = component_vertices[0]
        root_edges = adj[root]
        initial_mark = len(trail)
        q = []

        ok = True
        for eid, color_mask in zip(root_edges, (1, 2, 4)):
            if not set_domain(eid, color_mask, q):
                ok = False
                break

        if ok:
            ok = propagate(q)

        if not ok:
            rollback(initial_mark)
            print("NO")
            return

        def search():
            chosen = -1
            best_size = 4

            for eid in component_edges:
                size = popcount[domains[eid]]
                if 1 < size < best_size:
                    best_size = size
                    chosen = eid
                    if size == 2:
                        break

            if chosen == -1:
                return True

            mask = domains[chosen]
            while mask:
                bit = mask & -mask
                mask -= bit
                mark = len(trail)
                queue = []

                if set_domain(chosen, bit, queue) and propagate(queue):
                    if search():
                        return True

                rollback(mark)

            return False

        if not search():
            rollback(initial_mark)
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