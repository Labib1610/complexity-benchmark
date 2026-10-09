import sys
from collections import deque

sys.setrecursionlimit(1000000)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 2:
        return

    n, m = data[0], data[1]
    edges = []
    adj = [[] for _ in range(n)]
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

    # A cubic graph with a bridge cannot have a proper 3-edge-coloring.
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
            if tin[to] == -1:
                bridge_dfs(to, eid)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    has_bridge = True
            else:
                low[v] = min(low[v], tin[to])

    for s in range(n):
        if tin[s] == -1:
            bridge_dfs(s, -1)

    if has_bridge:
        print("NO")
        return

    # Bipartite cubic graphs can be colored by extracting one perfect matching.
    side = [-1] * n
    bipartite = True
    for s in range(n):
        if side[s] != -1:
            continue
        side[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            for eid in adj[v]:
                a, b = edges[eid]
                to = b if a == v else a
                if side[to] == -1:
                    side[to] = side[v] ^ 1
                    q.append(to)
                elif side[to] == side[v]:
                    bipartite = False

    if bipartite:
        left = [v for v in range(n) if side[v] == 0]
        pair_left = [-1] * n
        pair_right = [-1] * n
        pair_edge = [-1] * n
        dist = [-1] * n

        def bfs_matching():
            q = deque()
            found = False
            for u in left:
                if pair_left[u] == -1:
                    dist[u] = 0
                    q.append(u)
                else:
                    dist[u] = -1

            while q:
                u = q.popleft()
                for eid in adj[u]:
                    a, b = edges[eid]
                    v = b if a == u else a
                    mate = pair_right[v]
                    if mate == -1:
                        found = True
                    elif dist[mate] == -1:
                        dist[mate] = dist[u] + 1
                        q.append(mate)
            return found

        def dfs_matching(u):
            for eid in adj[u]:
                a, b = edges[eid]
                v = b if a == u else a
                mate = pair_right[v]
                if mate == -1 or (dist[mate] == dist[u] + 1 and dfs_matching(mate)):
                    pair_left[u] = v
                    pair_right[v] = u
                    pair_edge[u] = eid
                    return True
            dist[u] = -1
            return False

        matching_size = 0
        while bfs_matching():
            for u in left:
                if pair_left[u] == -1 and dfs_matching(u):
                    matching_size += 1

        if matching_size != len(left):
            print("NO")
            return

        answer = [0] * m
        for u in left:
            answer[pair_edge[u]] = 1

        # The remaining graph is a union of even cycles.
        for start in range(m):
            if answer[start] != 0:
                continue
            current_vertex = edges[start][0]
            color = 2

            while True:
                next_edge = -1
                for eid in adj[current_vertex]:
                    if answer[eid] == 0:
                        next_edge = eid
                        break
                if next_edge == -1:
                    break

                answer[next_edge] = color
                color = 5 - color
                a, b = edges[next_edge]
                current_vertex = b if a == current_vertex else a

        print("YES")
        print(*answer)
        return

    # General exact CSP solver. Each edge domain is a 3-bit color mask.
    domains = [7] * m
    endpoints = edges
    trail = []

    permutations = (
        (1, 2, 4), (1, 4, 2),
        (2, 1, 4), (2, 4, 1),
        (4, 1, 2), (4, 2, 1)
    )

    def narrow(eid, new_mask, queue, in_queue):
        old = domains[eid]
        new_mask &= old
        if new_mask == old:
            return new_mask != 0
        if new_mask == 0:
            return False

        trail.append((eid, old))
        domains[eid] = new_mask
        u, v = endpoints[eid]
        if not in_queue[u]:
            in_queue[u] = True
            queue.append(u)
        if not in_queue[v]:
            in_queue[v] = True
            queue.append(v)
        return True

    def propagate(initial_vertices):
        queue = deque()
        in_queue = [False] * n
        for v in initial_vertices:
            if not in_queue[v]:
                in_queue[v] = True
                queue.append(v)

        while queue:
            v = queue.popleft()
            in_queue[v] = False
            e0, e1, e2 = adj[v]
            d0, d1, d2 = domains[e0], domains[e1], domains[e2]

            s0 = s1 = s2 = 0
            valid = False
            for c0, c1, c2 in permutations:
                if (d0 & c0) and (d1 & c1) and (d2 & c2):
                    valid = True
                    s0 |= c0
                    s1 |= c1
                    s2 |= c2

            if not valid:
                return False

            if not narrow(e0, s0, queue, in_queue):
                return False
            if not narrow(e1, s1, queue, in_queue):
                return False
            if not narrow(e2, s2, queue, in_queue):
                return False

        return True

    # Remove independent color permutation symmetry in each connected component.
    seen = [False] * n
    initial = []
    for s in range(n):
        if seen[s]:
            continue
        stack = [s]
        seen[s] = True
        while stack:
            v = stack.pop()
            for eid in adj[v]:
                a, b = edges[eid]
                to = b if a == v else a
                if not seen[to]:
                    seen[to] = True
                    stack.append(to)

        for eid, color in zip(adj[s], (1, 2, 4)):
            old = domains[eid]
            if not (old & color):
                print("NO")
                return
            if old != color:
                trail.append((eid, old))
                domains[eid] = color
                initial.extend(endpoints[eid])

    if not propagate(initial):
        print("NO")
        return

    def search():
        chosen = -1
        best_size = 4
        best_score = -1

        for eid, mask in enumerate(domains):
            count = mask.bit_count()
            if count == 1:
                continue
            if count < best_size:
                best_size = count
                chosen = eid
                u, v = endpoints[eid]
                best_score = sum(domains[x].bit_count() == 1 for x in adj[u]) + \
                             sum(domains[x].bit_count() == 1 for x in adj[v])
            elif count == best_size:
                u, v = endpoints[eid]
                score = sum(domains[x].bit_count() == 1 for x in adj[u]) + \
                        sum(domains[x].bit_count() == 1 for x in adj[v])
                if score > best_score:
                    chosen = eid
                    best_score = score

        if chosen == -1:
            return True

        mask = domains[chosen]
        bits = []
        while mask:
            bit = mask & -mask
            mask -= bit
            bits.append(bit)

        for bit in bits:
            checkpoint = len(trail)
            old = domains[chosen]
            trail.append((chosen, old))
            domains[chosen] = bit
            u, v = endpoints[chosen]

            if propagate((u, v)) and search():
                return True

            while len(trail) > checkpoint:
                eid, previous = trail.pop()
                domains[eid] = previous

        return False

    if not search():
        print("NO")
        return

    answer = [mask.bit_length() for mask in domains]
    print("YES")
    print(*answer)

if __name__ == "__main__":
    main()