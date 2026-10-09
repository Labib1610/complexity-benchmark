import sys
sys.setrecursionlimit(10000)


def solve_block(vertices, graph):
    k = len(vertices)
    if k == 1:
        return [0]

    pos = {v: i for i, v in enumerate(vertices)}
    adj = [0] * k
    for i, v in enumerate(vertices):
        mask = graph[v]
        for u in vertices:
            j = pos[u]
            if (mask >> u) & 1:
                adj[i] |= 1 << j

    # Handle bipartite blocks directly.
    colors = [-1] * k
    bipartite = True
    for start in range(k):
        if colors[start] != -1:
            continue
        colors[start] = 0
        queue = [start]
        head = 0
        while head < len(queue):
            u = queue[head]
            head += 1
            x = adj[u]
            while x:
                bit = x & -x
                v = bit.bit_length() - 1
                x ^= bit
                if colors[v] == -1:
                    colors[v] = colors[u] ^ 1
                    queue.append(v)
                elif colors[v] == colors[u]:
                    bipartite = False
                    break
            if not bipartite:
                break
        if not bipartite:
            break
    if bipartite:
        return colors

    degrees = [a.bit_count() for a in adj]

    # Find a useful triangle and detect K4.
    best_triangle = None
    best_score = -1
    for i in range(k):
        x = adj[i] & ~((1 << (i + 1)) - 1)
        while x:
            bj = x & -x
            j = bj.bit_length() - 1
            x ^= bj
            common = adj[i] & adj[j] & ~((1 << (j + 1)) - 1)
            while common:
                bk = common & -common
                t = bk.bit_length() - 1
                common ^= bk
                if adj[i] & adj[j] & adj[t]:
                    return None
                score = degrees[i] + degrees[j] + degrees[t]
                if score > best_score:
                    best_score = score
                    best_triangle = (i, j, t)

    color = [-1] * k
    saturation = [0] * k
    uncolored = (1 << k) - 1

    def place_initial(v, c):
        nonlocal uncolored
        color[v] = c
        uncolored &= ~(1 << v)
        x = adj[v] & uncolored
        cm = 1 << c
        while x:
            bit = x & -x
            u = bit.bit_length() - 1
            x ^= bit
            saturation[u] |= cm

    if best_triangle is not None:
        place_initial(best_triangle[0], 0)
        place_initial(best_triangle[1], 1)
        place_initial(best_triangle[2], 2)
    else:
        u = max(range(k), key=lambda z: degrees[z])
        neighbors = adj[u]
        if neighbors == 0:
            place_initial(u, 0)
        else:
            candidates = []
            x = neighbors
            while x:
                bit = x & -x
                v = bit.bit_length() - 1
                x ^= bit
                candidates.append(v)
            v = max(candidates, key=lambda z: degrees[z])
            place_initial(u, 0)
            place_initial(v, 1)

    def dfs():
        nonlocal uncolored
        if uncolored == 0:
            return True

        x = uncolored
        chosen = -1
        best_key = (-1, -1, -1)
        while x:
            bit = x & -x
            v = bit.bit_length() - 1
            x ^= bit
            key = (
                saturation[v].bit_count(),
                (adj[v] & uncolored).bit_count(),
                degrees[v]
            )
            if key > best_key:
                best_key = key
                chosen = v

        available = (~saturation[chosen]) & 7
        if available == 0:
            return False

        options = []
        x = available
        neighbors = adj[chosen] & uncolored
        while x:
            cm = x & -x
            c = cm.bit_length() - 1
            x ^= cm
            impact = 0
            y = neighbors
            while y:
                bit = y & -y
                u = bit.bit_length() - 1
                y ^= bit
                if not (saturation[u] & cm):
                    impact += 1
            options.append((impact, c))
        options.sort()

        old_uncolored = uncolored
        uncolored &= ~(1 << chosen)

        for _, c in options:
            cm = 1 << c
            color[chosen] = c
            changed = []
            bad = False

            y = adj[chosen] & uncolored
            while y:
                bit = y & -y
                u = bit.bit_length() - 1
                y ^= bit
                old = saturation[u]
                new = old | cm
                if new != old:
                    changed.append((u, old))
                    saturation[u] = new
                    if new == 7:
                        bad = True

            if not bad and dfs():
                return True

            for u, old in reversed(changed):
                saturation[u] = old
            color[chosen] = -1

        uncolored = old_uncolored
        return False

    if dfs():
        return color
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
        graph[u] |= 1 << v
        graph[v] |= 1 << u

    # Remove vertices of current degree at most two. They can always be
    # restored after coloring the remaining graph.
    active = (1 << n) - 1
    degree = [graph[v].bit_count() for v in range(n)]
    queue = [v for v in range(n) if degree[v] <= 2]
    head = 0
    removed = []

    while head < len(queue):
        v = queue[head]
        head += 1
        if not ((active >> v) & 1) or degree[v] > 2:
            continue

        active &= ~(1 << v)
        removed.append(v)

        x = graph[v] & active
        while x:
            bit = x & -x
            u = bit.bit_length() - 1
            x ^= bit
            degree[u] -= 1
            if degree[u] == 2:
                queue.append(u)

    answer = [-1] * n

    # Find vertex-biconnected blocks of the remaining graph.
    discovery = [-1] * n
    low = [0] * n
    timer = 0
    edge_stack = []
    blocks = []

    def tarjan(u, parent):
        nonlocal timer
        discovery[u] = low[u] = timer
        timer += 1

        x = graph[u] & active
        while x:
            bit = x & -x
            v = bit.bit_length() - 1
            x ^= bit

            if discovery[v] == -1:
                edge_stack.append((u, v))
                tarjan(v, u)
                low[u] = min(low[u], low[v])

                if low[v] >= discovery[u]:
                    block_vertices = set()
                    while True:
                        a, b = edge_stack.pop()
                        block_vertices.add(a)
                        block_vertices.add(b)
                        if a == u and b == v:
                            break
                    blocks.append(list(block_vertices))
            elif v != parent and discovery[v] < discovery[u]:
                edge_stack.append((u, v))
                low[u] = min(low[u], discovery[v])

    x = active
    while x:
        bit = x & -x
        root = bit.bit_length() - 1
        if discovery[root] == -1:
            tarjan(root, -1)
            if (graph[root] & active) == 0:
                blocks.append([root])
        x ^= bit

    block_colors = []
    for block in blocks:
        result = solve_block(block, graph)
        if result is None:
            print("NO")
            return
        block_colors.append(result)

    # Build a tree-like adjacency between blocks through articulation vertices.
    occurrence = [[] for _ in range(n)]
    for bid, block in enumerate(blocks):
        for v in block:
            occurrence[v].append(bid)

    block_adj = [[] for _ in blocks]
    for v in range(n):
        ids = occurrence[v]
        if len(ids) > 1:
            root = ids[0]
            for other in ids[1:]:
                block_adj[root].append((other, v))
                block_adj[other].append((root, v))

    visited = [False] * len(blocks)
    for root in range(len(blocks)):
        if visited[root]:
            continue

        visited[root] = True
        for i, v in enumerate(blocks[root]):
            answer[v] = block_colors[root][i]

        bfs = [root]
        qh = 0
        while qh < len(bfs):
            b = bfs[qh]
            qh += 1

            for nb, shared in block_adj[b]:
                if visited[nb]:
                    continue
                visited[nb] = True
                bfs.append(nb)

                idx_shared = blocks[nb].index(shared)
                local_shared = block_colors[nb][idx_shared]
                global_shared = answer[shared]

                mapping = [-1, -1, -1]
                mapping[local_shared] = global_shared
                remaining_local = [c for c in range(3) if c != local_shared]
                remaining_global = [c for c in range(3) if c != global_shared]
                for a, bcol in zip(remaining_local, remaining_global):
                    mapping[a] = bcol

                for i, v in enumerate(blocks[nb]):
                    mapped = mapping[block_colors[nb][i]]
                    if answer[v] == -1:
                        answer[v] = mapped

    # Restore peeled vertices in reverse order.
    for v in reversed(removed):
        used = 0
        x = graph[v]
        while x:
            bit = x & -x
            u = bit.bit_length() - 1
            x ^= bit
            if answer[u] != -1:
                used |= 1 << answer[u]

        for c in range(3):
            if not (used >> c) & 1:
                answer[v] = c
                break

    print("YES")
    print(*[c + 1 for c in answer])


if __name__ == "__main__":
    main()