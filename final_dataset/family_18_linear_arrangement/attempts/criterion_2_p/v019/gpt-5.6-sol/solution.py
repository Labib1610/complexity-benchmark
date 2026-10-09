import sys
from array import array


def arrangement_cost(order, adj):
    pos = [0] * len(order)
    for i, v in enumerate(order):
        pos[v] = i
    total = 0
    for u in range(len(order)):
        pu = pos[u]
        for v in adj[u]:
            if u < v:
                total += abs(pu - pos[v])
    return total


def output_order(order):
    pos = [0] * len(order)
    for i, v in enumerate(order, 1):
        pos[v] = i
    print("YES")
    print(*pos)


def path_order(adj):
    n = len(adj)
    if n == 1:
        return [0]
    start = next(i for i in range(n) if len(adj[i]) == 1)
    order = []
    prev = -1
    cur = start
    while cur != -1:
        order.append(cur)
        nxt = -1
        for v in adj[cur]:
            if v != prev:
                nxt = v
                break
        prev, cur = cur, nxt
    return order


def star_order(adj):
    n = len(adj)
    center = next(i for i in range(n) if len(adj[i]) == n - 1)
    leaves = [i for i in range(n) if i != center]
    left_count = (n - 1) // 2
    return leaves[:left_count] + [center] + leaves[left_count:]


def centroid_heuristic(adj):
    n = len(adj)
    if n <= 1:
        return list(range(n))

    parent = [-1] * n
    traversal = [0]
    for u in traversal:
        for v in adj[u]:
            if v != parent[u]:
                parent[v] = u
                traversal.append(v)

    size = [1] * n
    for u in reversed(traversal):
        if parent[u] != -1:
            size[parent[u]] += size[u]

    centroid = 0
    for u in range(n):
        largest = n - size[u]
        for v in adj[u]:
            if parent[v] == u:
                largest = max(largest, size[v])
        if largest * 2 <= n:
            centroid = u
            break

    branches = []
    for start in adj[centroid]:
        seq = []
        stack = [(start, centroid)]
        while stack:
            u, p = stack.pop()
            seq.append(u)
            children = [v for v in adj[u] if v != p and v != centroid]
            children.sort(key=lambda x: len(adj[x]))
            for v in reversed(children):
                stack.append((v, u))
        branches.append(seq)

    branches.sort(key=len, reverse=True)
    left, right = [], []
    left_size = right_size = 0
    for branch in branches:
        if left_size <= right_size:
            left.append(branch)
            left_size += len(branch)
        else:
            right.append(branch)
            right_size += len(branch)

    left.sort(key=len, reverse=True)
    right.sort(key=len)

    order = []
    for branch in left:
        order.extend(reversed(branch))
    order.append(centroid)
    for branch in right:
        order.extend(branch)
    return order


def dense_subset_dp(adj_mask, degree, budget):
    n = len(adj_mask)
    states = 1 << n
    full = states - 1
    inf = budget + 1

    cuts = array('H', [0]) * states
    dp = array('q', [inf]) * states
    dp[0] = 0

    for mask in range(1, states):
        bit = mask & -mask
        previous = mask ^ bit
        v = bit.bit_length() - 1

        cut = cuts[previous] + degree[v] - 2 * ((adj_mask[v] & previous).bit_count())
        cuts[mask] = cut

        k = mask.bit_count()
        limit = budget - (n - 1 - k)
        if limit < 0 or cut > limit:
            continue

        best = inf
        x = mask
        theoretical = k - 1
        while x:
            b = x & -x
            value = dp[mask ^ b]
            if value < best:
                best = value
                if best == theoretical:
                    break
            x ^= b

        value = best + cut
        if value <= limit:
            dp[mask] = value

    if dp[full] > budget:
        return None

    reversed_order = []
    mask = full
    while mask:
        current = dp[mask]
        cut = cuts[mask]
        x = mask
        chosen = 0
        while x:
            bit = x & -x
            if dp[mask ^ bit] + cut == current:
                chosen = bit
                break
            x ^= bit
        if chosen == 0:
            return None
        reversed_order.append(chosen.bit_length() - 1)
        mask ^= chosen

    reversed_order.reverse()
    return reversed_order


def sparse_subset_dp(adj_mask, degree, budget):
    n = len(adj_mask)
    full = (1 << n) - 1
    base = n + 1

    layers = [{0: 0}]

    for k in range(1, n + 1):
        previous_layer = layers[-1]
        current_layer = {}
        limit = budget - (n - 1 - k)
        if limit < 0:
            return None

        for mask, encoded in previous_layer.items():
            old_cost, old_cut = divmod(encoded, base)
            available = full ^ mask
            while available:
                bit = available & -available
                available ^= bit
                v = bit.bit_length() - 1
                new_mask = mask | bit
                new_cut = old_cut + degree[v] - 2 * ((adj_mask[v] & mask).bit_count())
                new_cost = old_cost + new_cut

                if new_cost > limit:
                    continue

                old_encoded = current_layer.get(new_mask)
                if old_encoded is None or new_cost < old_encoded // base:
                    current_layer[new_mask] = new_cost * base + new_cut

        if not current_layer:
            return None
        layers.append(current_layer)

    if full not in layers[n]:
        return None

    reversed_order = []
    mask = full
    for k in range(n, 0, -1):
        encoded = layers[k][mask]
        current_cost, current_cut = divmod(encoded, base)
        x = mask
        chosen = 0
        while x:
            bit = x & -x
            previous = mask ^ bit
            previous_encoded = layers[k - 1].get(previous)
            if previous_encoded is not None:
                previous_cost = previous_encoded // base
                if previous_cost + current_cut == current_cost:
                    chosen = bit
                    break
            x ^= bit

        if chosen == 0:
            return None
        reversed_order.append(chosen.bit_length() - 1)
        mask ^= chosen

    reversed_order.reverse()
    return reversed_order


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m, budget = data[0], data[1], data[2]
    adj = [[] for _ in range(n)]
    adj_mask = [0] * n

    index = 3
    for _ in range(m):
        u = data[index] - 1
        v = data[index + 1] - 1
        index += 2
        adj[u].append(v)
        adj[v].append(u)
        adj_mask[u] |= 1 << v
        adj_mask[v] |= 1 << u

    if n == 1:
        if budget >= 0:
            output_order([0])
        else:
            print("NO")
        return

    if budget < n - 1:
        print("NO")
        return

    degree = [len(x) for x in adj]

    local_sum = 0
    for d in degree:
        local_sum += ((d + 1) * (d + 1)) // 4
    lower_bound = max(n - 1, (local_sum + 1) // 2)
    if budget < lower_bound:
        print("NO")
        return

    if max(degree) <= 2:
        order = path_order(adj)
        output_order(order)
        return

    if max(degree) == n - 1:
        order = star_order(adj)
        if arrangement_cost(order, adj) <= budget:
            output_order(order)
        else:
            print("NO")
        return

    identity = list(range(n))
    if arrangement_cost(identity, adj) <= budget:
        output_order(identity)
        return

    heuristic = centroid_heuristic(adj)
    if arrangement_cost(heuristic, adj) <= budget:
        output_order(heuristic)
        return

    if n <= 22:
        order = dense_subset_dp(adj_mask, degree, budget)
    else:
        order = sparse_subset_dp(adj_mask, degree, budget)

    if order is None:
        print("NO")
    else:
        output_order(order)


if __name__ == "__main__":
    main()