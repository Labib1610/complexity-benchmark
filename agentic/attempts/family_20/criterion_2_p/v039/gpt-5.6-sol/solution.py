import sys
from array import array
from collections import deque

sys.setrecursionlimit(1_000_000)


def pack_vertices(degrees, capacity):
    mapping = array('i', [-1]) * len(degrees)
    loads = []
    current = -1
    load = 0

    for vertex, degree in enumerate(degrees):
        if degree == 0:
            continue
        if current == -1 or load + degree > capacity:
            if current >= 0:
                loads.append(load)
            current += 1
            load = 0
        mapping[vertex] = current
        load += degree

    if current >= 0:
        loads.append(load)

    return mapping, loads


def main():
    inp = sys.stdin.buffer
    first = inp.readline().split()
    if not first:
        return

    n_u, n_d, m = map(int, first)

    if m == 0:
        sys.stdout.write("YES\n\n")
        return

    original_u = array('i')
    original_v = array('i')
    degree_u = [0] * n_u
    degree_v = [0] * n_d

    for _ in range(m):
        u, v = map(int, inp.readline().split())
        u -= 1
        v -= 1
        original_u.append(u)
        original_v.append(v)
        degree_u[u] += 1
        degree_v[v] += 1

    delta = max(max(degree_u), max(degree_v))

    map_u, loads_u = pack_vertices(degree_u, delta)
    map_v, loads_v = pack_vertices(degree_v, delta)

    bin_count = max(len(loads_u), len(loads_v))
    loads_u.extend([0] * (bin_count - len(loads_u)))
    loads_v.extend([0] * (bin_count - len(loads_v)))

    edge_u = array('i')
    edge_v = array('i')

    for i in range(m):
        edge_u.append(map_u[original_u[i]])
        edge_v.append(map_v[original_v[i]])

    del original_u, original_v, map_u, map_v, degree_u, degree_v

    deficit_u = [delta - x for x in loads_u]
    deficit_v = [delta - x for x in loads_v]
    del loads_u, loads_v

    i = 0
    j = 0
    while i < bin_count and j < bin_count:
        while i < bin_count and deficit_u[i] == 0:
            i += 1
        while j < bin_count and deficit_v[j] == 0:
            j += 1
        if i == bin_count or j == bin_count:
            break

        count = min(deficit_u[i], deficit_v[j])
        edge_u.extend(array('i', [i]) * count)
        edge_v.extend(array('i', [j]) * count)
        deficit_u[i] -= count
        deficit_v[j] -= count

    del deficit_u, deficit_v

    total_edges = len(edge_u)
    answer = array('i', [0]) * m
    partner_left = array('i', [0]) * total_edges
    partner_right = array('i', [0]) * total_edges
    marked = bytearray(total_edges)

    def split_even(edges):
        last = [-1] * bin_count
        for e in edges:
            u = edge_u[e]
            previous = last[u]
            if previous < 0:
                last[u] = e
            else:
                partner_left[e] = previous
                partner_left[previous] = e
                last[u] = -1

        last = [-1] * bin_count
        for e in edges:
            v = edge_v[e]
            previous = last[v]
            if previous < 0:
                last[v] = e
            else:
                partner_right[e] = previous
                partner_right[previous] = e
                last[v] = -1

        first_half = []
        second_half = []
        append_first = first_half.append
        append_second = second_half.append

        for start in edges:
            if marked[start]:
                continue

            current = start
            use_right = True
            side = 0

            while not marked[current]:
                marked[current] = 1
                if side == 0:
                    append_first(current)
                else:
                    append_second(current)

                if use_right:
                    current = partner_right[current]
                else:
                    current = partner_left[current]

                use_right = not use_right
                side ^= 1

        for e in edges:
            marked[e] = 0

        return first_half, second_half

    def perfect_matching(edges, degree):
        edge_count = len(edges)
        adjacency = [0] * edge_count
        counts = [0] * bin_count

        for e in edges:
            u = edge_u[e]
            position = u * degree + counts[u]
            adjacency[position] = e
            counts[u] += 1

        pair_u = [-1] * bin_count
        pair_v = [-1] * bin_count
        pair_edge = [-1] * bin_count

        matched = 0
        for e in edges:
            u = edge_u[e]
            v = edge_v[e]
            if pair_u[u] < 0 and pair_v[v] < 0:
                pair_u[u] = v
                pair_v[v] = u
                pair_edge[u] = e
                matched += 1

        distance = [-1] * bin_count

        while matched < bin_count:
            queue = deque()
            for u in range(bin_count):
                if pair_u[u] < 0:
                    distance[u] = 0
                    queue.append(u)
                else:
                    distance[u] = -1

            found = False
            while queue:
                u = queue.popleft()
                start = u * degree
                end = start + degree
                next_distance = distance[u] + 1

                for p in range(start, end):
                    e = adjacency[p]
                    v = edge_v[e]
                    other_u = pair_v[v]
                    if other_u < 0:
                        found = True
                    elif distance[other_u] < 0:
                        distance[other_u] = next_distance
                        queue.append(other_u)

            if not found:
                break

            pointer = [u * degree for u in range(bin_count)]

            for root in range(bin_count):
                if pair_u[root] >= 0:
                    continue

                stack = [root]
                path_edges = []
                augmented = False

                while stack:
                    u = stack[-1]
                    end = u * degree + degree
                    descended = False

                    while pointer[u] < end:
                        e = adjacency[pointer[u]]
                        pointer[u] += 1
                        v = edge_v[e]
                        other_u = pair_v[v]

                        if other_u < 0:
                            full_path = path_edges
                            full_path.append(e)

                            for index, path_edge in enumerate(full_path):
                                path_u = stack[index]
                                path_v = edge_v[path_edge]
                                pair_u[path_u] = path_v
                                pair_v[path_v] = path_u
                                pair_edge[path_u] = path_edge

                            matched += 1
                            augmented = True
                            break

                        if distance[other_u] == distance[u] + 1:
                            path_edges.append(e)
                            stack.append(other_u)
                            descended = True
                            break

                    if augmented:
                        break
                    if descended:
                        continue

                    distance[u] = -1
                    stack.pop()
                    if path_edges:
                        path_edges.pop()

        return pair_edge

    tasks = [(list(range(total_edges)), delta)]
    color = 1

    while tasks:
        edges, degree = tasks.pop()

        if degree == 1:
            for e in edges:
                if e < m:
                    answer[e] = color
            color += 1
            continue

        if degree & 1:
            matching = perfect_matching(edges, degree)

            for e in matching:
                marked[e] = 1
                if e < m:
                    answer[e] = color

            remaining = [e for e in edges if not marked[e]]

            for e in matching:
                marked[e] = 0

            color += 1
            tasks.append((remaining, degree - 1))
        else:
            first_half, second_half = split_even(edges)
            half_degree = degree // 2
            tasks.append((second_half, half_degree))
            tasks.append((first_half, half_degree))

    output = "YES\n" + " ".join(map(str, answer)) + "\n"
    sys.stdout.write(output)


if __name__ == "__main__":
    main()