import sys

sys.setrecursionlimit(10000)


def solve_block(vertices, graph):
    k = len(vertices)
    vertices = sorted(vertices, key=lambda v: -sum(1 for u in vertices if u in graph[v]))
    index = {v: i for i, v in enumerate(vertices)}
    full = (1 << k) - 1
    adj = [0] * k

    for i, v in enumerate(vertices):
        mask = 0
        for u in graph[v]:
            j = index.get(u)
            if j is not None:
                mask |= 1 << j
        adj[i] = mask

    def bipartite(rem):
        unseen = rem
        side0 = 0
        side1 = 0

        while unseen:
            root = unseen & -unseen
            unseen ^= root
            side0 |= root
            queue = root

            while queue:
                bit = queue & -queue
                queue ^= bit
                v = bit.bit_length() - 1
                neighbors = adj[v] & rem

                if side0 & bit:
                    if neighbors & side0:
                        return None
                    new_vertices = neighbors & unseen
                    unseen ^= new_vertices
                    side1 |= new_vertices
                else:
                    if neighbors & side1:
                        return None
                    new_vertices = neighbors & unseen
                    unseen ^= new_vertices
                    side0 |= new_vertices

                queue |= new_vertices

        return side0, side1

    sides = bipartite(full)
    if sides is not None:
        side0, side1 = sides
        result = {}
        for i, v in enumerate(vertices):
            result[v] = 1 if side0 & (1 << i) else 2
        return result

    # Fast greedy DSATUR attempt.
    greedy_colors = [0] * k
    uncolored = full
    greedy_ok = True

    while uncolored:
        best = -1
        best_key = (-1, -1)

        candidates = uncolored
        while candidates:
            bit = candidates & -candidates
            candidates ^= bit
            v = bit.bit_length() - 1

            used = 0
            neighbors = adj[v]
            while neighbors:
                nb = neighbors & -neighbors
                neighbors ^= nb
                c = greedy_colors[nb.bit_length() - 1]
                if c:
                    used |= 1 << (c - 1)

            key = (used.bit_count(), adj[v].bit_count())
            if key > best_key:
                best_key = key
                best = v

        used = 0
        neighbors = adj[best]
        while neighbors:
            nb = neighbors & -neighbors
            neighbors ^= nb
            c = greedy_colors[nb.bit_length() - 1]
            if c:
                used |= 1 << (c - 1)

        available = 7 & ~used
        if not available:
            greedy_ok = False
            break

        chosen = available & -available
        greedy_colors[best] = chosen.bit_length()
        uncolored ^= 1 << best

    if greedy_ok:
        return {vertices[i]: greedy_colors[i] for i in range(k)}

    # A graph is 3-colorable iff some maximal independent set can be
    # one color class and the remaining graph is bipartite.
    complement_adj = [
        full ^ (1 << i) ^ adj[i]
        for i in range(k)
    ]

    answer = None

    def bron_kerbosch(independent, possible, excluded):
        nonlocal answer

        if possible == 0:
            if excluded == 0:
                remaining = full ^ independent
                partition = bipartite(remaining)
                if partition is not None:
                    side0, side1 = partition
                    result = [0] * k
                    for i in range(k):
                        bit = 1 << i
                        if independent & bit:
                            result[i] = 1
                        elif side0 & bit:
                            result[i] = 2
                        else:
                            result[i] = 3
                    answer = result
                    return True
            return False

        union = possible | excluded
        pivot = -1
        best_count = -1
        temp = union

        while temp:
            bit = temp & -temp
            temp ^= bit
            u = bit.bit_length() - 1
            count = (possible & complement_adj[u]).bit_count()
            if count > best_count:
                best_count = count
                pivot = u

        candidates = possible & ~complement_adj[pivot]

        while candidates:
            bit = candidates & -candidates
            candidates ^= bit
            v = bit.bit_length() - 1

            if bron_kerbosch(
                independent | bit,
                possible & complement_adj[v],
                excluded & complement_adj[v]
            ):
                return True

            possible ^= bit
            excluded |= bit

        return False

    bron_kerbosch(0, full, 0)

    if answer is None:
        return None

    return {vertices[i]: answer[i] for i in range(k)}


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    graph = [set() for _ in range(n)]

    pos = 2
    for _ in range(m):
        u = data[pos] - 1
        v = data[pos + 1] - 1
        pos += 2
        if u != v:
            graph[u].add(v)
            graph[v].add(u)

    # Split the graph into vertex-biconnected blocks. Different blocks
    # share at most one articulation vertex and can be colored independently.
    discovery = [-1] * n
    low = [0] * n
    timer = 0
    edge_stack = []
    blocks = []

    def dfs(u, parent):
        nonlocal timer
        discovery[u] = low[u] = timer
        timer += 1

        for v in graph[u]:
            if discovery[v] == -1:
                edge_stack.append((u, v))
                dfs(v, u)
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

    for start in range(n):
        if discovery[start] == -1:
            dfs(start, -1)

    colors = [0] * n
    local_solutions = []

    for block in blocks:
        solution = solve_block(block, graph)
        if solution is None:
            print("NO")
            return
        local_solutions.append(solution)

    memberships = [[] for _ in range(n)]
    for block_id, block in enumerate(blocks):
        for v in block:
            memberships[v].append(block_id)

    visited_blocks = [False] * len(blocks)

    def apply_block(block_id, parent_vertex=-1):
        visited_blocks[block_id] = True
        block = blocks[block_id]
        local = local_solutions[block_id]

        mapping = [0, 1, 2, 3]
        if parent_vertex != -1:
            local_color = local[parent_vertex]
            required_color = colors[parent_vertex]
            mapping[local_color], mapping[required_color] = (
                mapping[required_color],
                mapping[local_color],
            )

        for v in block:
            mapped = mapping[local[v]]
            if colors[v] == 0:
                colors[v] = mapped

        for articulation in block:
            for next_block in memberships[articulation]:
                if not visited_blocks[next_block]:
                    apply_block(next_block, articulation)

    for block_id in range(len(blocks)):
        if not visited_blocks[block_id]:
            apply_block(block_id)

    for v in range(n):
        if colors[v] == 0:
            colors[v] = 1

    print("YES")
    print(*colors)


if __name__ == "__main__":
    main()