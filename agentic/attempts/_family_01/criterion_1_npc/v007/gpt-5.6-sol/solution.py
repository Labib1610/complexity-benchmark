import sys
from collections import deque

def solve_component(vertices, graph):
    k = len(vertices)
    index = {v: i for i, v in enumerate(vertices)}
    adj = [[] for _ in range(k)]

    for i, v in enumerate(vertices):
        mask = graph[v]
        while mask:
            bit = mask & -mask
            u = bit.bit_length() - 1
            mask ^= bit
            j = index.get(u)
            if j is not None:
                adj[i].append(j)

    # Handle bipartite components directly.
    bip_color = [-1] * k
    bipartite = True
    for start in range(k):
        if bip_color[start] != -1:
            continue
        bip_color[start] = 0
        q = deque([start])
        while q and bipartite:
            v = q.popleft()
            for u in adj[v]:
                if bip_color[u] == -1:
                    bip_color[u] = bip_color[v] ^ 1
                    q.append(u)
                elif bip_color[u] == bip_color[v]:
                    bipartite = False
                    break

    if bipartite:
        return bip_color

    colors = [-1] * k
    available = [7] * k
    color_count = [0, 0, 0]
    degrees = [len(x) for x in adj]
    colored_count = 0

    def rollback(assigned, changes):
        nonlocal colored_count
        for v in reversed(assigned):
            c = colors[v]
            color_count[c] -= 1
            colors[v] = -1
            colored_count -= 1
        for v, old_mask in reversed(changes):
            available[v] = old_mask

    def assign_and_propagate(start_v, start_c, assigned, changes):
        nonlocal colored_count
        queue = [(start_v, start_c)]
        pos = 0

        while pos < len(queue):
            v, c = queue[pos]
            pos += 1

            if colors[v] != -1:
                if colors[v] != c:
                    return False
                continue

            bit = 1 << c
            if not (available[v] & bit):
                return False

            colors[v] = c
            color_count[c] += 1
            colored_count += 1
            assigned.append(v)

            for u in adj[v]:
                if colors[u] != -1:
                    if colors[u] == c:
                        return False
                    continue

                old = available[u]
                new = old & ~bit
                if new == old:
                    continue

                changes.append((u, old))
                available[u] = new

                if new == 0:
                    return False
                if new & (new - 1) == 0:
                    queue.append((u, new.bit_length() - 1))

        return True

    def search():
        if colored_count == k:
            return True

        chosen = -1
        best_key = None

        for v in range(k):
            if colors[v] != -1:
                continue

            choices = available[v].bit_count()
            uncolored_degree = 0
            for u in adj[v]:
                if colors[u] == -1:
                    uncolored_degree += 1

            key = (-choices, uncolored_degree, degrees[v])
            if best_key is None or key > best_key:
                best_key = key
                chosen = v

        used_colors = sum(x > 0 for x in color_count)
        max_allowed_color = min(used_colors, 2)

        options = []
        mask = available[chosen]
        for c in range(max_allowed_color + 1):
            if mask & (1 << c):
                options.append(c)

        # Prefer colors that constrain fewer currently uncolored neighbors.
        options.sort(key=lambda c: sum(
            1 for u in adj[chosen]
            if colors[u] == -1 and (available[u] & (1 << c))
        ))

        for c in options:
            assigned = []
            changes = []

            if assign_and_propagate(chosen, c, assigned, changes):
                if search():
                    return True

            rollback(assigned, changes)

        return False

    if search():
        return colors
    return None


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    graph = [0] * n
    p = 2

    for _ in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2

        if u == v:
            print("NO")
            return

        graph[u] |= 1 << v
        graph[v] |= 1 << u

    # Remove vertices of current degree at most two. Such vertices can always
    # be colored greedily after the remaining graph has been colored.
    active = [True] * n
    degree = [graph[v].bit_count() for v in range(n)]
    queue = deque(v for v in range(n) if degree[v] <= 2)
    removed = []

    while queue:
        v = queue.popleft()
        if not active[v] or degree[v] > 2:
            continue

        active[v] = False
        removed.append(v)

        mask = graph[v]
        while mask:
            bit = mask & -mask
            u = bit.bit_length() - 1
            mask ^= bit
            if active[u]:
                degree[u] -= 1
                if degree[u] <= 2:
                    queue.append(u)

    answer = [-1] * n
    core_mask = 0
    for v in range(n):
        if active[v]:
            core_mask |= 1 << v

    unseen = core_mask
    while unseen:
        start_bit = unseen & -unseen
        start = start_bit.bit_length() - 1
        component_mask = 0
        frontier = start_bit
        unseen ^= start_bit

        while frontier:
            bit = frontier & -frontier
            frontier ^= bit
            v = bit.bit_length() - 1
            component_mask |= bit

            new_vertices = graph[v] & unseen
            unseen ^= new_vertices
            frontier |= new_vertices

        vertices = []
        mask = component_mask
        while mask:
            bit = mask & -mask
            vertices.append(bit.bit_length() - 1)
            mask ^= bit

        component_colors = solve_component(vertices, graph)
        if component_colors is None:
            print("NO")
            return

        for v, c in zip(vertices, component_colors):
            answer[v] = c

    for v in reversed(removed):
        used = 0
        mask = graph[v]
        while mask:
            bit = mask & -mask
            u = bit.bit_length() - 1
            mask ^= bit
            if answer[u] != -1:
                used |= 1 << answer[u]

        for c in range(3):
            if not (used & (1 << c)):
                answer[v] = c
                break

        if answer[v] == -1:
            print("NO")
            return

    print("YES")
    print(*(c + 1 for c in answer))


if __name__ == "__main__":
    main()