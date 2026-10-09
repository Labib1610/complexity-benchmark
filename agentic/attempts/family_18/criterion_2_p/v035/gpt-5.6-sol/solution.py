import sys
from array import array

def arrangement_from_root(root, graph, n):
    parent = [-1] * n
    parent[root] = root
    order = [root]

    for u in order:
        for v in graph[u]:
            if parent[v] == -1:
                parent[v] = u
                order.append(v)

    size = [1] * n
    children = [[] for _ in range(n)]
    for u in reversed(order[1:]):
        size[parent[u]] += size[u]
        children[parent[u]].append(u)

    for u in order:
        children[u].sort(key=lambda x: size[x])

    root_children = sorted(children[root], key=lambda x: size[x], reverse=True)
    left, right = [], []
    left_size = right_size = 0

    for v in root_children:
        if left_size <= right_size:
            left.append(v)
            left_size += size[v]
        else:
            right.append(v)
            right_size += size[v]

    left.sort(key=lambda x: size[x], reverse=True)
    right.sort(key=lambda x: size[x])

    def anchored_left(start):
        result = []
        stack = [start]
        while stack:
            u = stack.pop()
            result.append(u)
            ch = children[u]
            for i in range(len(ch) - 1, -1, -1):
                stack.append(ch[i])
        return result

    sequence = []
    for v in left:
        part = anchored_left(v)
        sequence.extend(reversed(part))

    sequence.append(root)

    for v in right:
        sequence.extend(anchored_left(v))

    return sequence


def arrangement_cost(sequence, edges, n):
    pos = [0] * n
    for i, u in enumerate(sequence):
        pos[u] = i
    return sum(abs(pos[u] - pos[v]) for u, v in edges)


def improve_adjacent(sequence, graph, initial_cost, operation_limit=2_000_000):
    n = len(sequence)
    pos = [0] * n
    for i, u in enumerate(sequence):
        pos[u] = i

    cost = initial_cost
    operations = 0

    for _ in range(5):
        changed = False
        i = 0
        while i + 1 < n:
            a = sequence[i]
            b = sequence[i + 1]
            operations += len(graph[a]) + len(graph[b])
            if operations > operation_limit:
                return sequence, cost

            delta = 0
            for x in graph[a]:
                if x == b:
                    continue
                if pos[x] < i:
                    delta += 1
                else:
                    delta -= 1

            for x in graph[b]:
                if x == a:
                    continue
                if pos[x] < i:
                    delta -= 1
                else:
                    delta += 1

            if delta < 0:
                sequence[i], sequence[i + 1] = b, a
                pos[a] = i + 1
                pos[b] = i
                cost += delta
                changed = True
                if i > 0:
                    i -= 1
                    continue
            i += 1

        if not changed:
            break

    return sequence, cost


def output_yes(sequence, n):
    positions = [0] * n
    for i, u in enumerate(sequence, 1):
        positions[u] = i
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, positions)))


def exact_subset_dp(graph, n, budget):
    total_masks = 1 << n
    neighbor_masks = [0] * n
    degrees = [0] * n

    for u in range(n):
        mask = 0
        for v in graph[u]:
            mask |= 1 << v
        neighbor_masks[u] = mask
        degrees[u] = len(graph[u])

    cuts = array('B', [0]) * total_masks
    inf = budget + 1
    dp = array('I', [inf]) * total_masks
    dp[0] = 0

    cut_arr = cuts
    dp_arr = dp
    neigh = neighbor_masks
    deg = degrees

    for mask in range(1, total_masks):
        bit = mask & -mask
        rest = mask ^ bit
        v = bit.bit_length() - 1
        cut_value = cut_arr[rest] + deg[v] - 2 * ((neigh[v] & rest).bit_count())
        cut_arr[mask] = cut_value

        best = inf
        bits = mask
        while bits:
            b = bits & -bits
            value = dp_arr[mask ^ b]
            if value < best:
                best = value
            bits ^= b

        value = best + cut_value
        if value > inf:
            value = inf
        dp_arr[mask] = value

    full = total_masks - 1
    if dp_arr[full] > budget:
        return None

    positions = [0] * n
    mask = full
    place = n

    while mask:
        target = dp_arr[mask] - cut_arr[mask]
        bits = mask
        chosen = -1
        while bits:
            bit = bits & -bits
            if dp_arr[mask ^ bit] == target:
                chosen = bit.bit_length() - 1
                break
            bits ^= bit

        if chosen < 0:
            return None

        positions[chosen] = place
        place -= 1
        mask ^= 1 << chosen

    return positions


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m, budget = data[0], data[1], data[2]
    graph = [[] for _ in range(n)]
    edges = []

    index = 3
    for _ in range(m):
        u = data[index] - 1
        v = data[index + 1] - 1
        index += 2
        graph[u].append(v)
        graph[v].append(u)
        edges.append((u, v))

    if n == 1:
        if budget >= 0:
            sys.stdout.write("YES\n1")
        else:
            sys.stdout.write("NO")
        return

    if budget < n - 1:
        sys.stdout.write("NO")
        return

    local_sum = 0
    lower_bound = n - 1
    for u in range(n):
        d = len(graph[u])
        k = d // 2
        if d % 2 == 0:
            local = k * (k + 1)
        else:
            local = (k + 1) * (k + 1)
        local_sum += local
        if local > lower_bound:
            lower_bound = local

    lower_bound = max(lower_bound, (local_sum + 1) // 2)
    if budget < lower_bound:
        sys.stdout.write("NO")
        return

    parent = [-1] * n
    parent[0] = 0
    order = [0]
    for u in order:
        for v in graph[u]:
            if parent[v] == -1:
                parent[v] = u
                order.append(v)

    size = [1] * n
    for u in reversed(order[1:]):
        size[parent[u]] += size[u]

    best_balance = n + 1
    centroids = []
    for u in range(n):
        largest = n - size[u]
        for v in graph[u]:
            if parent[v] == u and size[v] > largest:
                largest = size[v]
        if largest < best_balance:
            best_balance = largest
            centroids = [u]
        elif largest == best_balance:
            centroids.append(u)

    best_sequence = None
    best_cost = None

    for root in centroids:
        sequence = arrangement_from_root(root, graph, n)
        cost = arrangement_cost(sequence, edges, n)
        sequence, cost = improve_adjacent(sequence, graph, cost)

        if best_cost is None or cost < best_cost:
            best_cost = cost
            best_sequence = sequence

        if cost <= budget:
            output_yes(sequence, n)
            return

    if n <= 22:
        positions = exact_subset_dp(graph, n, budget)
        if positions is None:
            sys.stdout.write("NO")
        else:
            sys.stdout.write("YES\n")
            sys.stdout.write(" ".join(map(str, positions)))
        return

    if best_cost is not None and best_cost <= budget:
        output_yes(best_sequence, n)
    else:
        sys.stdout.write("NO")


if __name__ == "__main__":
    main()