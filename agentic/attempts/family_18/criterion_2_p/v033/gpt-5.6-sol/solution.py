import sys
from array import array


def print_arrangement(order, n):
    positions = [0] * n
    for i, vertex in enumerate(order, 1):
        positions[vertex] = i
    print("YES")
    print(*positions)


def arrangement_cost(order, edges, n):
    positions = [0] * n
    for i, vertex in enumerate(order):
        positions[vertex] = i
    return sum(abs(positions[u] - positions[v]) for u, v in edges)


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m, budget = data[0], data[1], data[2]
    adjacency = [[] for _ in range(n)]
    adjacency_masks = [0] * n
    edges = []

    p = 3
    for _ in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        adjacency[u].append(v)
        adjacency[v].append(u)
        adjacency_masks[u] |= 1 << v
        adjacency_masks[v] |= 1 << u
        edges.append((u, v))

    if n == 1:
        if budget >= 0:
            print("YES")
            print(1)
        else:
            print("NO")
        return

    degrees = [len(x) for x in adjacency]

    # Exact handling of paths.
    if max(degrees) <= 2:
        if budget < n - 1:
            print("NO")
            return
        start = next(i for i, d in enumerate(degrees) if d == 1)
        order = []
        previous = -1
        current = start
        while current != -1:
            order.append(current)
            nxt = -1
            for to in adjacency[current]:
                if to != previous:
                    nxt = to
                    break
            previous, current = current, nxt
        print_arrangement(order, n)
        return

    # Exact handling of stars.
    center = max(range(n), key=lambda x: degrees[x])
    if degrees[center] == n - 1:
        leaves = [v for v in range(n) if v != center]
        left_count = (n - 1) // 2
        order = leaves[:left_count] + [center] + leaves[left_count:]
        optimum = sum(abs(i - left_count) for i in range(n) if i != left_count)
        if optimum <= budget:
            print_arrangement(order, n)
        else:
            print("NO")
        return

    # General exact subset DP.
    # dp[S] is the minimum sum of cut sizes for all prefixes up to S.
    if n <= 22:
        total_masks = 1 << n
        cut = array('i', [0]) * total_masks
        dp = array('q', [0]) * total_masks

        for mask in range(1, total_masks):
            bit = mask & -mask
            vertex = bit.bit_length() - 1
            previous = mask ^ bit
            cut_value = (
                cut[previous]
                + degrees[vertex]
                - 2 * (adjacency_masks[vertex] & previous).bit_count()
            )
            cut[mask] = cut_value

            bits = mask
            best = 1 << 62
            while bits:
                b = bits & -bits
                value = dp[mask ^ b]
                if value < best:
                    best = value
                bits ^= b
            dp[mask] = best + cut_value

        full = total_masks - 1
        if dp[full] > budget:
            print("NO")
            return

        reverse_order = []
        mask = full
        while mask:
            target = dp[mask] - cut[mask]
            bits = mask
            chosen = 0
            while bits:
                bit = bits & -bits
                if dp[mask ^ bit] == target:
                    chosen = bit
                    break
                bits ^= bit
            reverse_order.append(chosen.bit_length() - 1)
            mask ^= chosen

        order = reverse_order[::-1]
        print_arrangement(order, n)
        return

    # For large instances, first use a valid lower bound.
    local_sum = 0
    for d in degrees:
        local_sum += ((d + 1) * (d + 1)) // 4
    lower_bound = max(n - 1, (local_sum + 1) // 2)
    if budget < lower_bound:
        print("NO")
        return

    # Construct several inexpensive valid arrangements.
    # Any one within budget is sufficient.
    roots = [center]
    # Tree centroid.
    parent = [-1] * n
    traversal = [0]
    for v in traversal:
        for to in adjacency[v]:
            if to != parent[v]:
                parent[to] = v
                traversal.append(to)
    subtree = [1] * n
    centroid = 0
    best_part = n
    for v in reversed(traversal):
        largest = n - subtree[v]
        for to in adjacency[v]:
            if parent[to] == v:
                subtree[v] += subtree[to]
                if subtree[to] > largest:
                    largest = subtree[to]
        if largest < best_part:
            best_part = largest
            centroid = v
    if centroid != center:
        roots.append(centroid)

    for root in roots:
        for descending in (False, True):
            par = [-1] * n
            size = [1] * n
            seq = [root]
            for v in seq:
                for to in adjacency[v]:
                    if to != par[v]:
                        par[to] = v
                        seq.append(to)
            for v in reversed(seq):
                if par[v] != -1:
                    size[par[v]] += size[v]

            order = []
            stack = [root]
            while stack:
                v = stack.pop()
                order.append(v)
                children = [to for to in adjacency[v] if to != par[v]]
                children.sort(key=lambda x: size[x], reverse=not descending)
                stack.extend(children)

            if arrangement_cost(order, edges, n) <= budget:
                print_arrangement(order, n)
                return

            reversed_order = order[::-1]
            if arrangement_cost(reversed_order, edges, n) <= budget:
                print_arrangement(reversed_order, n)
                return

    print("NO")


if __name__ == "__main__":
    main()