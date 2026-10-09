import sys

def solve_block(vertices, graph):
    k = len(vertices)
    index = {v: i for i, v in enumerate(vertices)}
    adj = [0] * k

    for i, u in enumerate(vertices):
        mask = 0
        for v in graph[u]:
            j = index.get(v)
            if j is not None:
                mask |= 1 << j
        adj[i] = mask

    full = (1 << k) - 1

    def bipartite(mask):
        colors = [0] * k
        for start in range(k):
            if not (mask >> start) & 1 or colors[start]:
                continue
            colors[start] = 1
            queue = [start]
            head = 0

            while head < len(queue):
                u = queue[head]
                head += 1
                next_color = 3 - colors[u]
                neighbors = adj[u] & mask

                while neighbors:
                    bit = neighbors & -neighbors
                    neighbors ^= bit
                    v = bit.bit_length() - 1

                    if colors[v] == 0:
                        colors[v] = next_color
                        queue.append(v)
                    elif colors[v] != next_color:
                        return None
        return colors

    colors = bipartite(full)
    if colors is not None:
        return colors

    complement = [full ^ (1 << i) ^ adj[i] for i in range(k)]
    answer = None

    def bron_kerbosch(p, x, independent):
        nonlocal answer

        if p == 0:
            if x == 0:
                remaining = full ^ independent
                rest_colors = bipartite(remaining)
                if rest_colors is not None:
                    result = rest_colors
                    bits = independent
                    while bits:
                        bit = bits & -bits
                        bits ^= bit
                        result[bit.bit_length() - 1] = 3
                    answer = result
                    return True
            return False

        possible_pivots = p | x
        pivot = -1
        best = -1

        while possible_pivots:
            bit = possible_pivots & -possible_pivots
            possible_pivots ^= bit
            u = bit.bit_length() - 1
            score = (p & complement[u]).bit_count()
            if score > best:
                best = score
                pivot = u

        candidates = p & ~complement[pivot]

        while candidates:
            bit = candidates & -candidates
            candidates ^= bit
            v = bit.bit_length() - 1

            if bron_kerbosch(
                p & complement[v],
                x & complement[v],
                independent | bit
            ):
                return True

            p ^= bit
            x |= bit

        return False

    bron_kerbosch(full, 0, 0)
    return answer


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    graph = [[] for _ in range(n)]

    pos = 2
    for _ in range(m):
        u = data[pos] - 1
        v = data[pos + 1] - 1
        pos += 2
        graph[u].append(v)
        graph[v].append(u)

    sys.setrecursionlimit(10000)

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

    for i in range(n):
        if discovery[i] == -1:
            tarjan(i, -1)

    memberships = [[] for _ in range(n)]
    for block_id, vertices in enumerate(blocks):
        for v in vertices:
            memberships[v].append(block_id)

    assignment = [0] * n
    seen_blocks = [False] * len(blocks)

    def process_block(block_id, parent_vertex):
        seen_blocks[block_id] = True
        vertices = blocks[block_id]
        local_colors = solve_block(vertices, graph)

        if local_colors is None:
            return False

        mapping = [0, 1, 2, 3]
        if parent_vertex != -1 and assignment[parent_vertex] != 0:
            parent_index = vertices.index(parent_vertex)
            current = local_colors[parent_index]
            target = assignment[parent_vertex]
            if current != target:
                mapping[current], mapping[target] = mapping[target], mapping[current]

        for i, v in enumerate(vertices):
            color = mapping[local_colors[i]]
            if assignment[v] != 0 and assignment[v] != color:
                return False
            assignment[v] = color

        for v in vertices:
            for next_block in memberships[v]:
                if not seen_blocks[next_block]:
                    if not process_block(next_block, v):
                        return False

        return True

    for block_id in range(len(blocks)):
        if not seen_blocks[block_id]:
            if not process_block(block_id, -1):
                print("NO")
                return

    for i in range(n):
        if assignment[i] == 0:
            assignment[i] = 1

    print("YES")
    print(*assignment)


if __name__ == "__main__":
    main()