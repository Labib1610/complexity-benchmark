import sys
from array import array
from collections import deque

sys.setrecursionlimit(1_000_000)


def main():
    input_data = sys.stdin.buffer
    S, T, m = map(int, input_data.readline().split())

    original_u = array('i')
    original_v = array('i')
    degree_u = [0] * S
    degree_v = [0] * T

    for _ in range(m):
        u, v = map(int, input_data.readline().split())
        u -= 1
        v -= 1
        original_u.append(u)
        original_v.append(v)
        degree_u[u] += 1
        degree_v[v] += 1

    if m == 0:
        sys.stdout.write("YES\n\n")
        return

    D = max(max(degree_u), max(degree_v))

    def pack_vertices(degrees):
        mapping = [-1] * len(degrees)
        loads = []
        current = -1
        current_load = 0

        for vertex, deg in enumerate(degrees):
            if deg == 0:
                continue
            if current == -1 or current_load + deg > D:
                loads.append(0)
                current += 1
                current_load = 0
            mapping[vertex] = current
            current_load += deg
            loads[current] = current_load

        return mapping, loads

    map_u, loads_u = pack_vertices(degree_u)
    map_v, loads_v = pack_vertices(degree_v)

    n = max(len(loads_u), len(loads_v))
    loads_u.extend([0] * (n - len(loads_u)))
    loads_v.extend([0] * (n - len(loads_v)))

    left = array('i', (map_u[u] for u in original_u))
    right = array('i', (map_v[v] for v in original_v))

    deficit_u = [D - x for x in loads_u]
    deficit_v = [D - x for x in loads_v]

    i = j = 0
    while i < n and j < n:
        while i < n and deficit_u[i] == 0:
            i += 1
        while j < n and deficit_v[j] == 0:
            j += 1
        if i == n or j == n:
            break

        count = min(deficit_u[i], deficit_v[j])
        left.extend(array('i', [i]) * count)
        right.extend(array('i', [j]) * count)
        deficit_u[i] -= count
        deficit_v[j] -= count

    total_edges = len(left)
    colors = array('i', [0]) * m

    left_mate = array('i', [-1]) * total_edges
    right_mate = array('i', [-1]) * total_edges
    seen = array('I', [0]) * total_edges
    epoch = 0
    next_color = 1

    def split_even(edges):
        nonlocal epoch

        pending = [-1] * n
        for edge in edges:
            u = left[edge]
            other = pending[u]
            if other == -1:
                pending[u] = edge
            else:
                left_mate[edge] = other
                left_mate[other] = edge
                pending[u] = -1

        pending = [-1] * n
        for edge in edges:
            v = right[edge]
            other = pending[v]
            if other == -1:
                pending[v] = edge
            else:
                right_mate[edge] = other
                right_mate[other] = edge
                pending[v] = -1

        epoch += 1
        current_epoch = epoch
        first = []
        second = []

        for start in edges:
            if seen[start] == current_epoch:
                continue

            edge = start
            take_first = True

            while seen[edge] != current_epoch:
                seen[edge] = current_epoch

                if take_first:
                    first.append(edge)
                    edge = right_mate[edge]
                else:
                    second.append(edge)
                    edge = left_mate[edge]

                take_first = not take_first

        return first, second

    def perfect_matching(edges):
        adjacency = [[] for _ in range(n)]
        pair_u = [-1] * n
        pair_v = [-1] * n
        pair_edge = [-1] * n

        for edge in edges:
            adjacency[left[edge]].append(edge)

        matched = 0

        for edge in edges:
            u = left[edge]
            v = right[edge]
            if pair_u[u] == -1 and pair_v[v] == -1:
                pair_u[u] = v
                pair_v[v] = u
                pair_edge[u] = edge
                matched += 1

        distance = [-1] * n

        def dfs(u):
            for edge in adjacency[u]:
                v = right[edge]
                previous_u = pair_v[v]
                if previous_u == -1 or (
                    distance[previous_u] == distance[u] + 1 and dfs(previous_u)
                ):
                    pair_u[u] = v
                    pair_v[v] = u
                    pair_edge[u] = edge
                    return True

            distance[u] = -1
            return False

        while matched < n:
            queue = deque()

            for u in range(n):
                if pair_u[u] == -1:
                    distance[u] = 0
                    queue.append(u)
                else:
                    distance[u] = -1

            while queue:
                u = queue.popleft()
                next_distance = distance[u] + 1

                for edge in adjacency[u]:
                    previous_u = pair_v[right[edge]]
                    if previous_u != -1 and distance[previous_u] == -1:
                        distance[previous_u] = next_distance
                        queue.append(previous_u)

            progress = 0
            for u in range(n):
                if pair_u[u] == -1 and dfs(u):
                    progress += 1

            matched += progress

        return pair_edge

    def decompose(edges, degree):
        nonlocal epoch, next_color

        if degree == 1:
            color = next_color
            next_color += 1
            for edge in edges:
                if edge < m:
                    colors[edge] = color
            edges.clear()
            return

        if degree & 1:
            matching = perfect_matching(edges)
            color = next_color
            next_color += 1

            epoch += 1
            current_epoch = epoch

            for edge in matching:
                seen[edge] = current_epoch
                if edge < m:
                    colors[edge] = color

            remaining = [
                edge for edge in edges
                if seen[edge] != current_epoch
            ]
            edges.clear()

            first, second = split_even(remaining)
            remaining.clear()

            half = (degree - 1) // 2
            decompose(first, half)
            decompose(second, half)
        else:
            first, second = split_even(edges)
            edges.clear()

            half = degree // 2
            decompose(first, half)
            decompose(second, half)

    all_edges = list(range(total_edges))
    decompose(all_edges, D)

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, colors)))
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()