import sys
from collections import deque

sys.setrecursionlimit(1000000)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    adj = [[] for _ in range(n)]
    ends = [None] * m

    p = 2
    for eid in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        ends[eid] = (u, v)
        adj[u].append((v, eid))
        adj[v].append((u, eid))

    if any(len(adj[v]) != 3 for v in range(n)):
        print("NO")
        return

    tin = [-1] * n
    low = [0] * n
    timer = 0
    has_bridge = False
    components = []

    def tarjan(v, parent_edge, vertices):
        nonlocal timer, has_bridge
        tin[v] = low[v] = timer
        timer += 1
        vertices.append(v)

        for to, eid in adj[v]:
            if eid == parent_edge:
                continue
            if tin[to] == -1:
                tarjan(to, eid, vertices)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    has_bridge = True
            else:
                low[v] = min(low[v], tin[to])

    for v in range(n):
        if tin[v] == -1:
            vertices = []
            tarjan(v, -1, vertices)
            components.append(vertices)

    if has_bridge:
        print("NO")
        return

    permutations = (
        (1, 2, 4), (1, 4, 2),
        (2, 1, 4), (2, 4, 1),
        (4, 1, 2), (4, 2, 1)
    )

    support0 = [0] * 512
    support1 = [0] * 512
    support2 = [0] * 512

    for a in range(1, 8):
        for b in range(1, 8):
            for c in range(1, 8):
                s0 = s1 = s2 = 0
                for x, y, z in permutations:
                    if (a & x) and (b & y) and (c & z):
                        s0 |= x
                        s1 |= y
                        s2 |= z
                idx = (a << 6) | (b << 3) | c
                support0[idx] = s0
                support1[idx] = s1
                support2[idx] = s2

    incident = [[eid for _, eid in adj[v]] for v in range(n)]
    masks = [7] * m
    bit_count = [0, 1, 1, 2, 1, 2, 2, 3]

    def solve_component(vertices):
        component_edges = []
        seen_edges = set()
        for v in vertices:
            for eid in incident[v]:
                if eid not in seen_edges:
                    seen_edges.add(eid)
                    component_edges.append(eid)

        trail = []

        def restrict_edge(eid, allowed, q):
            old = masks[eid]
            new = old & allowed
            if new == 0:
                return False
            if new != old:
                trail.append((eid, old))
                masks[eid] = new
                u, v = ends[eid]
                q.append(u)
                q.append(v)
            return True

        def propagate(q):
            while q:
                v = q.popleft()
                e0, e1, e2 = incident[v]
                a, b, c = masks[e0], masks[e1], masks[e2]
                idx = (a << 6) | (b << 3) | c

                s0 = support0[idx]
                if s0 == 0:
                    return False

                if not restrict_edge(e0, s0, q):
                    return False
                if not restrict_edge(e1, support1[idx], q):
                    return False
                if not restrict_edge(e2, support2[idx], q):
                    return False
            return True

        root = vertices[0]
        q = deque()
        for eid, color_bit in zip(incident[root], (1, 2, 4)):
            if not restrict_edge(eid, color_bit, q):
                return False
        if not propagate(q):
            return False

        def dfs():
            chosen = -1
            best_size = 4
            best_score = -1

            for eid in component_edges:
                mask = masks[eid]
                size = bit_count[mask]
                if size == 1:
                    continue

                u, v = ends[eid]
                score = 0
                for other in incident[u]:
                    if other != eid:
                        score += 3 - bit_count[masks[other]]
                for other in incident[v]:
                    if other != eid:
                        score += 3 - bit_count[masks[other]]

                if size < best_size or (size == best_size and score > best_score):
                    best_size = size
                    best_score = score
                    chosen = eid

            if chosen == -1:
                return True

            options = masks[chosen]
            while options:
                bit = options & -options
                options -= bit
                mark = len(trail)
                q = deque()

                if restrict_edge(chosen, bit, q) and propagate(q) and dfs():
                    return True

                while len(trail) > mark:
                    eid, old = trail.pop()
                    masks[eid] = old

            return False

        return dfs()

    for vertices in components:
        if not solve_component(vertices):
            print("NO")
            return

    colors = [mask.bit_length() for mask in masks]
    print("YES")
    print(*colors)

if __name__ == "__main__":
    main()