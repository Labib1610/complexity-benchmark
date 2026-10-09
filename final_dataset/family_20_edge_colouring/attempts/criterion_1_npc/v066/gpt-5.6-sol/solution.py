import sys
from collections import deque

sys.setrecursionlimit(10000)


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
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

    if any(len(adj[v]) != 3 for v in range(n)):
        print("NO")
        return

    # A cubic graph with a bridge cannot be 3-edge-colored.
    tin = [-1] * n
    low = [0] * n
    timer = 0
    has_bridge = False

    def bridge_dfs(v, parent_edge):
        nonlocal timer, has_bridge
        tin[v] = low[v] = timer
        timer += 1

        for eid in adj[v]:
            if eid == parent_edge:
                continue
            a, b = edges[eid]
            to = b if a == v else a

            if tin[to] != -1:
                low[v] = min(low[v], tin[to])
            else:
                bridge_dfs(to, eid)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    has_bridge = True

    for v in range(n):
        if tin[v] == -1:
            bridge_dfs(v, -1)

    if has_bridge:
        print("NO")
        return

    # Connected components and bipartition test.
    side = [-1] * n
    components = []
    bipartite = []

    for start in range(n):
        if side[start] != -1:
            continue

        q = deque([start])
        side[start] = 0
        vertices = []
        ok = True

        while q:
            v = q.popleft()
            vertices.append(v)
            for eid in adj[v]:
                a, b = edges[eid]
                to = b if a == v else a
                if side[to] == -1:
                    side[to] = side[v] ^ 1
                    q.append(to)
                elif side[to] == side[v]:
                    ok = False

        components.append(vertices)
        bipartite.append(ok)

    color = [-1] * m

    # Cubic bipartite components are colored by repeatedly finding perfect
    # matchings.
    def color_bipartite_component(vertices):
        left = [v for v in vertices if side[v] == 0]

        for c in range(2):
            match_left = [-1] * n
            match_right = [-1] * n
            dist = [-1] * n

            def bfs():
                q = deque()
                found = False
                for v in left:
                    if match_left[v] == -1:
                        dist[v] = 0
                        q.append(v)
                    else:
                        dist[v] = -1

                while q:
                    v = q.popleft()
                    for eid in adj[v]:
                        if color[eid] != -1:
                            continue
                        a, b = edges[eid]
                        to = b if a == v else a
                        mv = match_right[to]
                        if mv == -1:
                            found = True
                        elif dist[mv] == -1:
                            dist[mv] = dist[v] + 1
                            q.append(mv)
                return found

            def dfs(v):
                for eid in adj[v]:
                    if color[eid] != -1:
                        continue
                    a, b = edges[eid]
                    to = b if a == v else a
                    mv = match_right[to]
                    if mv == -1 or (dist[mv] == dist[v] + 1 and dfs(mv)):
                        match_left[v] = eid
                        match_right[to] = v
                        return True
                dist[v] = -1
                return False

            matched = 0
            while bfs():
                for v in left:
                    if match_left[v] == -1 and dfs(v):
                        matched += 1

            if matched != len(left):
                return False

            for v in left:
                color[match_left[v]] = c

        for v in vertices:
            remaining = [eid for eid in adj[v] if color[eid] == -1]
            if len(remaining) != 1:
                return False
            color[remaining[0]] = 2

        return True

    for vertices, is_bip in zip(components, bipartite):
        if is_bip and not color_bipartite_component(vertices):
            print("NO")
            return

    FULL = 0b111
    used = [0] * n
    trail = []

    for eid, c in enumerate(color):
        if c != -1:
            u, v = edges[eid]
            used[u] |= 1 << c
            used[v] |= 1 << c

    def rollback(saved):
        while len(trail) > saved:
            eid = trail.pop()
            c = color[eid]
            u, v = edges[eid]
            used[u] ^= 1 << c
            used[v] ^= 1 << c
            color[eid] = -1

    def propagate(initial):
        queue = list(initial)
        qi = 0

        while qi < len(queue):
            eid, c = queue[qi]
            qi += 1

            if color[eid] != -1:
                if color[eid] != c:
                    return False
                continue

            u, v = edges[eid]
            bit = 1 << c
            if (used[u] & bit) or (used[v] & bit):
                return False

            color[eid] = c
            trail.append(eid)
            used[u] |= bit
            used[v] |= bit

            for x in (u, v):
                for ne in adj[x]:
                    if color[ne] != -1:
                        continue
                    a, b = edges[ne]
                    candidates = FULL & ~used[a] & ~used[b]
                    if candidates == 0:
                        return False
                    if candidates & (candidates - 1) == 0:
                        queue.append((ne, candidates.bit_length() - 1))

        return True

    def search(vertices):
        best_v = -1
        best_edges = None
        best_remaining = None
        best_score = -1

        complete = True
        for v in vertices:
            uncolored = [eid for eid in adj[v] if color[eid] == -1]
            if not uncolored:
                continue

            complete = False
            count_used = used[v].bit_count()

            if count_used == 1 and len(uncolored) == 2:
                remaining_mask = FULL & ~used[v]
                remaining = [
                    c for c in range(3) if remaining_mask & (1 << c)
                ]

                e0, e1 = uncolored
                u0, w0 = edges[e0]
                o0 = w0 if u0 == v else u0
                u1, w1 = edges[e1]
                o1 = w1 if u1 == v else u1
                score = used[o0].bit_count() + used[o1].bit_count()

                if score > best_score:
                    best_score = score
                    best_v = v
                    best_edges = (e0, e1)
                    best_remaining = remaining

        if complete:
            return True

        if best_v == -1:
            # Defensive fallback: fix the color permutation in an untouched
            # portion of the component.
            for v in vertices:
                uncolored = [eid for eid in adj[v] if color[eid] == -1]
                if len(uncolored) == 3 and used[v] == 0:
                    saved = len(trail)
                    if propagate([
                        (uncolored[0], 0),
                        (uncolored[1], 1),
                        (uncolored[2], 2),
                    ]) and search(vertices):
                        return True
                    rollback(saved)
                    return False
            return False

        e0, e1 = best_edges
        a, b = best_remaining

        options = ((a, b), (b, a))
        for c0, c1 in options:
            u0, v0 = edges[e0]
            u1, v1 = edges[e1]
            if not (FULL & ~used[u0] & ~used[v0] & (1 << c0)):
                continue
            if not (FULL & ~used[u1] & ~used[v1] & (1 << c1)):
                continue

            saved = len(trail)
            if propagate([(e0, c0), (e1, c1)]) and search(vertices):
                return True
            rollback(saved)

        return False

    for vertices, is_bip in zip(components, bipartite):
        if is_bip:
            continue

        root = vertices[0]
        root_edges = adj[root]
        saved = len(trail)

        if not propagate([
            (root_edges[0], 0),
            (root_edges[1], 1),
            (root_edges[2], 2),
        ]) or not search(vertices):
            rollback(saved)
            print("NO")
            return

    if any(c == -1 for c in color):
        print("NO")
        return

    print("YES")
    print(" ".join(str(c + 1) for c in color))


if __name__ == "__main__":
    main()