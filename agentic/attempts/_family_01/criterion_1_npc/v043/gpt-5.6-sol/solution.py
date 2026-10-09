import sys

sys.setrecursionlimit(10000)


def solve_block(vertices, graph):
    k = len(vertices)
    if k == 1:
        return {vertices[0]: 0}

    index = {v: i for i, v in enumerate(vertices)}
    adj = [0] * k

    for i, v in enumerate(vertices):
        mask = 0
        for w in graph[v]:
            j = index.get(w)
            if j is not None:
                mask |= 1 << j
        adj[i] = mask

    root = max(range(k), key=lambda x: adj[x].bit_count())
    root_bit = 1 << root
    all_mask = (1 << k) - 1
    solution = None

    def dfs(uncolored, c0, c1, c2):
        nonlocal solution

        if uncolored == 0:
            solution = (c0, c1, c2)
            return True

        best = -1
        best_sat = -1
        best_deg = -1

        remaining = uncolored
        while remaining:
            bit = remaining & -remaining
            remaining -= bit
            v = bit.bit_length() - 1
            av = adj[v]

            forbidden = 0
            if av & c0:
                forbidden |= 1
            if av & c1:
                forbidden |= 2
            if av & c2:
                forbidden |= 4

            if forbidden == 7:
                return False

            sat = forbidden.bit_count()
            degree = (av & uncolored).bit_count()
            if sat > best_sat or (sat == best_sat and degree > best_deg):
                best = v
                best_sat = sat
                best_deg = degree

        bit = 1 << best
        av = adj[best]
        forbidden = 0
        if av & c0:
            forbidden |= 1
        if av & c1:
            forbidden |= 2
        if av & c2:
            forbidden |= 4

        if c1 == 0:
            color_limit = 2
        elif c2 == 0:
            color_limit = 3
        else:
            color_limit = 3

        classes = (c0, c1, c2)
        candidates = []

        for color in range(color_limit):
            if forbidden & (1 << color):
                continue

            cls = classes[color]
            impact = 0
            neighbors = av & uncolored
            while neighbors:
                nb = neighbors & -neighbors
                neighbors -= nb
                u = nb.bit_length() - 1
                if (adj[u] & cls) == 0:
                    impact += 1
            candidates.append((impact, color))

        candidates.sort()

        new_uncolored = uncolored ^ bit
        for _, color in candidates:
            if color == 0:
                if dfs(new_uncolored, c0 | bit, c1, c2):
                    return True
            elif color == 1:
                if dfs(new_uncolored, c0, c1 | bit, c2):
                    return True
            else:
                if dfs(new_uncolored, c0, c1, c2 | bit):
                    return True

        return False

    if not dfs(all_mask ^ root_bit, root_bit, 0, 0):
        return None

    result = {}
    for color, mask in enumerate(solution):
        while mask:
            bit = mask & -mask
            mask -= bit
            result[vertices[bit.bit_length() - 1]] = color
    return result


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    graph_sets = [set() for _ in range(n)]
    pos = 2

    for _ in range(m):
        u = data[pos] - 1
        v = data[pos + 1] - 1
        pos += 2

        if u == v:
            print("NO")
            return

        graph_sets[u].add(v)
        graph_sets[v].add(u)

    graph = [list(neighbors) for neighbors in graph_sets]

    discovery = [-1] * n
    low = [0] * n
    timer = 0
    edge_stack = []
    blocks = []

    def tarjan(u, parent):
        nonlocal timer
        discovery[u] = low[u] = timer
        timer += 1

        for v in graph[u]:
            if discovery[v] == -1:
                edge_stack.append((u, v))
                tarjan(v, u)
                low[u] = min(low[u], low[v])

                if low[v] >= discovery[u]:
                    vertices = set()
                    while True:
                        a, b = edge_stack.pop()
                        vertices.add(a)
                        vertices.add(b)
                        if a == u and b == v:
                            break
                    blocks.append(list(vertices))

            elif v != parent and discovery[v] < discovery[u]:
                edge_stack.append((u, v))
                low[u] = min(low[u], discovery[v])

    for start in range(n):
        if discovery[start] == -1:
            tarjan(start, -1)

    block_colorings = []
    for vertices in blocks:
        coloring = solve_block(vertices, graph)
        if coloring is None:
            print("NO")
            return
        block_colorings.append(coloring)

    vertex_blocks = [[] for _ in range(n)]
    for block_id, vertices in enumerate(blocks):
        for v in vertices:
            vertex_blocks[v].append(block_id)

    answer = [-1] * n
    visited = [False] * len(blocks)

    from collections import deque

    for root_block in range(len(blocks)):
        if visited[root_block]:
            continue

        visited[root_block] = True
        queue = deque([root_block])

        while queue:
            block_id = queue.popleft()
            vertices = blocks[block_id]
            local = block_colorings[block_id]

            shared = [v for v in vertices if answer[v] != -1]
            mapping = [-1, -1, -1]
            used_global = [False, False, False]

            for v in shared:
                lc = local[v]
                gc = answer[v]
                if mapping[lc] != -1 and mapping[lc] != gc:
                    print("NO")
                    return
                mapping[lc] = gc
                used_global[gc] = True

            remaining_global = [c for c in range(3) if not used_global[c]]
            p = 0
            for lc in range(3):
                if mapping[lc] == -1:
                    mapping[lc] = remaining_global[p]
                    p += 1

            for v in vertices:
                color = mapping[local[v]]
                if answer[v] != -1 and answer[v] != color:
                    print("NO")
                    return
                answer[v] = color

            for v in vertices:
                for next_block in vertex_blocks[v]:
                    if not visited[next_block]:
                        visited[next_block] = True
                        queue.append(next_block)

    for v in range(n):
        if answer[v] == -1:
            answer[v] = 0

    print("YES")
    print(*[c + 1 for c in answer])


if __name__ == "__main__":
    main()