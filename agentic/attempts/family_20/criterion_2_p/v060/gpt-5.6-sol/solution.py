import sys
from collections import deque

sys.setrecursionlimit(1_000_000)


def make_groups(degrees, capacity):
    vertices = [i for i, d in enumerate(degrees) if d]
    vertices.sort(key=degrees.__getitem__, reverse=True)

    size = 1
    while size < len(vertices) + 1:
        size <<= 1

    tree = [0] * (size << 1)
    remaining = []
    group = [-1] * len(degrees)

    for vertex in vertices:
        need = degrees[vertex]

        if not remaining or tree[1] < need:
            bin_id = len(remaining)
            remaining.append(capacity - need)
            group[vertex] = bin_id

            p = size + bin_id
            tree[p] = capacity - need
            p >>= 1
            while p:
                tree[p] = max(tree[p << 1], tree[p << 1 | 1])
                p >>= 1
        else:
            p = 1
            while p < size:
                left = p << 1
                if tree[left] >= need:
                    p = left
                else:
                    p = left | 1

            bin_id = p - size
            group[vertex] = bin_id
            remaining[bin_id] -= need
            tree[p] = remaining[bin_id]

            p >>= 1
            while p:
                tree[p] = max(tree[p << 1], tree[p << 1 | 1])
                p >>= 1

    return group, remaining


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n_left, n_right, m = data[0], data[1], data[2]

    if m == 0:
        sys.stdout.write("YES\n\n")
        return

    raw_u = [0] * m
    raw_v = [0] * m
    deg_left = [0] * n_left
    deg_right = [0] * n_right

    pos = 3
    for i in range(m):
        u = data[pos] - 1
        v = data[pos + 1] - 1
        pos += 2
        raw_u[i] = u
        raw_v[i] = v
        deg_left[u] += 1
        deg_right[v] += 1

    delta = max(max(deg_left), max(deg_right))

    left_group, left_remaining = make_groups(deg_left, delta)
    right_group, right_remaining = make_groups(deg_right, delta)

    left_count = len(left_remaining)
    right_count = len(right_remaining)
    vertex_count = max(left_count, right_count)

    if left_count < vertex_count:
        left_remaining.extend([delta] * (vertex_count - left_count))
    if right_count < vertex_count:
        right_remaining.extend([delta] * (vertex_count - right_count))

    edge_u = [0] * m
    edge_v = [0] * m
    for i in range(m):
        edge_u[i] = left_group[raw_u[i]]
        edge_v[i] = right_group[raw_v[i]]

    del raw_u, raw_v, deg_left, deg_right, left_group, right_group, data

    # Complete the grouped graph to a delta-regular bipartite multigraph.
    i = j = 0
    while i < vertex_count and j < vertex_count:
        while i < vertex_count and left_remaining[i] == 0:
            i += 1
        while j < vertex_count and right_remaining[j] == 0:
            j += 1
        if i == vertex_count or j == vertex_count:
            break

        take = min(left_remaining[i], right_remaining[j])
        edge_u.extend([i] * take)
        edge_v.extend([j] * take)
        left_remaining[i] -= take
        right_remaining[j] -= take

    del left_remaining, right_remaining

    total_edges = len(edge_u)
    answer = [0] * m

    def split_even(edges):
        q = len(edges)
        heads = [-1] * (vertex_count << 1)
        next_u = [-1] * q
        next_v = [-1] * q

        for local, edge in enumerate(edges):
            u = edge_u[edge]
            v = edge_v[edge] + vertex_count

            next_u[local] = heads[u]
            heads[u] = local
            next_v[local] = heads[v]
            heads[v] = local

        used = bytearray(q)
        first = []
        second = []

        for start in range(vertex_count << 1):
            while heads[start] != -1 and used[heads[start]]:
                local = heads[start]
                if start < vertex_count:
                    heads[start] = next_u[local]
                else:
                    heads[start] = next_v[local]

            if heads[start] == -1:
                continue

            stack_vertices = [start]
            stack_edges = []
            parity = 0

            while stack_vertices:
                vertex = stack_vertices[-1]

                while heads[vertex] != -1 and used[heads[vertex]]:
                    local = heads[vertex]
                    if vertex < vertex_count:
                        heads[vertex] = next_u[local]
                    else:
                        heads[vertex] = next_v[local]

                local = heads[vertex]
                if local == -1:
                    stack_vertices.pop()
                    if stack_edges:
                        edge_local = stack_edges.pop()
                        if parity == 0:
                            first.append(edges[edge_local])
                        else:
                            second.append(edges[edge_local])
                        parity ^= 1
                    continue

                if vertex < vertex_count:
                    heads[vertex] = next_u[local]
                else:
                    heads[vertex] = next_v[local]

                if used[local]:
                    continue

                used[local] = 1
                edge = edges[local]
                if vertex < vertex_count:
                    other = edge_v[edge] + vertex_count
                else:
                    other = edge_u[edge]

                stack_vertices.append(other)
                stack_edges.append(local)

        return first, second

    def perfect_matching(edges):
        q = len(edges)
        heads = [-1] * vertex_count
        nxt = [-1] * q

        for local, edge in enumerate(edges):
            u = edge_u[edge]
            nxt[local] = heads[u]
            heads[u] = local

        pair_u = [-1] * vertex_count
        pair_v = [-1] * vertex_count
        pair_edge = [-1] * vertex_count

        # A greedy initialization substantially reduces the augmenting work.
        for local, edge in enumerate(edges):
            u = edge_u[edge]
            v = edge_v[edge]
            if pair_u[u] == -1 and pair_v[v] == -1:
                pair_u[u] = v
                pair_v[v] = u
                pair_edge[u] = edge

        dist = [-1] * vertex_count

        def dfs(u, ptr):
            local = ptr[u]
            while local != -1:
                ptr[u] = nxt[local]
                edge = edges[local]
                v = edge_v[edge]
                other = pair_v[v]

                if other == -1 or (
                    dist[other] == dist[u] + 1 and dfs(other, ptr)
                ):
                    pair_u[u] = v
                    pair_v[v] = u
                    pair_edge[u] = edge
                    return True

                local = ptr[u]

            dist[u] = -1
            return False

        while True:
            queue = deque()
            for u in range(vertex_count):
                if pair_u[u] == -1:
                    dist[u] = 0
                    queue.append(u)
                else:
                    dist[u] = -1

            found = False
            while queue:
                u = queue.popleft()
                local = heads[u]
                while local != -1:
                    v = edge_v[edges[local]]
                    other = pair_v[v]
                    if other == -1:
                        found = True
                    elif dist[other] == -1:
                        dist[other] = dist[u] + 1
                        queue.append(other)
                    local = nxt[local]

            if not found:
                break

            ptr = heads[:]
            augmented = False
            for u in range(vertex_count):
                if pair_u[u] == -1 and dfs(u, ptr):
                    augmented = True
            if not augmented:
                break

        return pair_edge

    def color_graph(edges, degree, first_color):
        if degree == 1:
            for edge in edges:
                if edge < m:
                    answer[edge] = first_color
            return

        if degree & 1:
            matching = perfect_matching(edges)
            matched = bytearray(total_edges)

            for edge in matching:
                matched[edge] = 1
                if edge < m:
                    answer[edge] = first_color

            remaining = [edge for edge in edges if not matched[edge]]
            color_graph(remaining, degree - 1, first_color + 1)
        else:
            half = degree >> 1
            first, second = split_even(edges)
            color_graph(first, half, first_color)
            color_graph(second, half, first_color + half)

    color_graph(list(range(total_edges)), delta, 1)

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, answer)))
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()