import sys
from array import array
from collections import deque


def arrangement_cost(order, adj):
    pos = [0] * len(order)
    for i, v in enumerate(order):
        pos[v] = i
    total = 0
    for u in range(len(order)):
        pu = pos[u]
        for v in adj[u]:
            if v > u:
                total += abs(pu - pos[v])
    return total


def improve_order(order, adj, passes=6):
    n = len(order)
    order = order[:]
    pos = [0] * n
    for i, v in enumerate(order):
        pos[v] = i

    for _ in range(passes):
        changed = False
        i = 0
        while i + 1 < n:
            a, b = order[i], order[i + 1]
            delta = 0

            for x in adj[a]:
                if x != b:
                    delta += abs((i + 1) - pos[x]) - abs(i - pos[x])
            for x in adj[b]:
                if x != a:
                    delta += abs(i - pos[x]) - abs((i + 1) - pos[x])

            if delta < 0:
                order[i], order[i + 1] = b, a
                pos[a], pos[b] = i + 1, i
                changed = True
            i += 1

        if not changed:
            break
    return order


def positions_from_order(order):
    pos = [0] * len(order)
    for i, v in enumerate(order, 1):
        pos[v] = i
    return pos


def farthest(start, adj):
    n = len(adj)
    dist = [-1] * n
    parent = [-1] * n
    q = deque([start])
    dist[start] = 0
    last = start
    while q:
        u = q.popleft()
        last = u
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                parent[v] = u
                q.append(v)
    return last, dist, parent


def get_centroid(adj):
    n = len(adj)
    parent = [-1] * n
    order = [0]
    for u in order:
        for v in adj[u]:
            if v != parent[u]:
                parent[v] = u
                order.append(v)

    size = [1] * n
    for u in reversed(order):
        if parent[u] != -1:
            size[parent[u]] += size[u]

    centroid = 0
    best = n + 1
    for u in range(n):
        largest = n - size[u]
        for v in adj[u]:
            if parent[v] == u:
                largest = max(largest, size[v])
        if largest < best:
            best = largest
            centroid = u
    return centroid


def dfs_order(root, adj, reverse_key=False):
    n = len(adj)
    parent = [-2] * n
    parent[root] = -1
    result = []
    stack = [root]

    while stack:
        u = stack.pop()
        result.append(u)
        children = [v for v in adj[u] if v != parent[u]]
        children.sort(key=lambda x: (len(adj[x]), x), reverse=reverse_key)
        for v in reversed(children):
            parent[v] = u
            stack.append(v)
    return result


def bfs_order(root, adj, reverse_key=False):
    n = len(adj)
    seen = bytearray(n)
    seen[root] = 1
    q = deque([root])
    result = []

    while q:
        u = q.popleft()
        result.append(u)
        children = [v for v in adj[u] if not seen[v]]
        children.sort(key=lambda x: (len(adj[x]), x), reverse=reverse_key)
        for v in children:
            seen[v] = 1
            q.append(v)
    return result


def exact_array_dp(n, adj_masks, degrees, budget):
    total_masks = 1 << n
    inf = budget + 1

    cut = array('H', [0]) * total_masks
    dp = array('Q', [inf]) * total_masks
    parent_choice = bytearray(total_masks)
    dp[0] = 0

    for mask in range(1, total_masks):
        low = mask & -mask
        v = low.bit_length() - 1
        prev = mask ^ low
        c = cut[prev] + degrees[v] - 2 * ((adj_masks[v] & prev).bit_count())
        cut[mask] = c

        best = inf
        bits = mask
        best_v = -1
        while bits:
            bit = bits & -bits
            u = bit.bit_length() - 1
            value = dp[mask ^ bit]
            if value < best:
                best = value
                best_v = u
            bits ^= bit

        if best >= inf:
            continue

        value = best + c
        k = mask.bit_count()
        remaining_lower_bound = max(0, n - 1 - k)
        if value + remaining_lower_bound <= budget:
            dp[mask] = value
            parent_choice[mask] = best_v + 1

    full = total_masks - 1
    if dp[full] > budget:
        return None

    pos = [0] * n
    mask = full
    k = n
    while mask:
        v = parent_choice[mask] - 1
        if v < 0:
            return None
        pos[v] = k
        mask ^= 1 << v
        k -= 1
    return pos


def exact_sparse_dp(n, adj_masks, degrees, budget):
    full = (1 << n) - 1
    current = {0: 0}
    parent_choice = {}

    for k in range(1, n):
        nxt = {}
        future_lower_bound = n - 1 - k

        for mask, value in current.items():
            old_cut = 0
            if mask:
                for u in range(n):
                    if (mask >> u) & 1:
                        old_cut += degrees[u] - 2 * ((adj_masks[u] & mask).bit_count())
                old_cut //= 1
                # The expression above equals the cut, since internal edges
                # contribute zero after summing deg - 2*internal-neighbors.
            missing = full ^ mask
            while missing:
                bit = missing & -missing
                v = bit.bit_length() - 1
                new_mask = mask | bit

                new_cut = old_cut + degrees[v] - 2 * ((adj_masks[v] & mask).bit_count())
                new_value = value + new_cut

                if new_value + future_lower_bound <= budget:
                    previous = nxt.get(new_mask)
                    if previous is None or new_value < previous:
                        nxt[new_mask] = new_value
                        parent_choice[new_mask] = v
                missing ^= bit

        current = nxt
        if not current:
            return None

    best_mask = None
    best_value = budget + 1
    for mask, value in current.items():
        if value <= budget and value < best_value:
            best_value = value
            best_mask = mask

    if best_mask is None:
        return None

    remaining_bit = full ^ best_mask
    remaining_vertex = remaining_bit.bit_length() - 1
    pos = [0] * n
    pos[remaining_vertex] = n

    mask = best_mask
    k = n - 1
    while mask:
        v = parent_choice[mask]
        pos[v] = k
        mask ^= 1 << v
        k -= 1
    return pos


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m, budget = data[0], data[1], data[2]
    adj = [[] for _ in range(n)]
    idx = 3
    for _ in range(m):
        u = data[idx] - 1
        v = data[idx + 1] - 1
        idx += 2
        adj[u].append(v)
        adj[v].append(u)

    if n == 1:
        if budget >= 0:
            print("YES")
            print(1)
        else:
            print("NO")
        return

    if budget < n - 1:
        print("NO")
        return

    degrees = [len(x) for x in adj]

    # Paths attain the universal lower bound n-1.
    if max(degrees) <= 2:
        start = next(i for i, d in enumerate(degrees) if d == 1)
        order = []
        prev = -1
        u = start
        while u != -1:
            order.append(u)
            nxt = -1
            for v in adj[u]:
                if v != prev:
                    nxt = v
                    break
            prev, u = u, nxt
        print("YES")
        print(*positions_from_order(order))
        return

    # Stars can be solved directly.
    center = max(range(n), key=lambda x: degrees[x])
    if degrees[center] == n - 1:
        leaves = [v for v in range(n) if v != center]
        center_pos = (n + 1) // 2
        order = leaves[:center_pos - 1] + [center] + leaves[center_pos - 1:]
        cost = arrangement_cost(order, adj)
        if cost <= budget:
            print("YES")
            print(*positions_from_order(order))
        else:
            print("NO")
        return

    centroid = get_centroid(adj)
    diameter_a, _, _ = farthest(0, adj)
    diameter_b, _, diameter_parent = farthest(diameter_a, adj)

    diameter_path = []
    x = diameter_b
    while x != -1:
        diameter_path.append(x)
        if x == diameter_a:
            break
        x = diameter_parent[x]
    diameter_center = diameter_path[len(diameter_path) // 2]

    roots = []
    for r in (0, centroid, center, diameter_a, diameter_b, diameter_center):
        if r not in roots:
            roots.append(r)

    candidates = [list(range(n))]
    for root in roots:
        candidates.append(dfs_order(root, adj, False))
        candidates.append(dfs_order(root, adj, True))
        candidates.append(bfs_order(root, adj, False))
        candidates.append(bfs_order(root, adj, True))

    best_order = None
    best_cost = 10**30

    for order in candidates:
        for candidate in (order, list(reversed(order))):
            improved = improve_order(candidate, adj)
            cost = arrangement_cost(improved, adj)
            if cost < best_cost:
                best_cost = cost
                best_order = improved
            if cost <= budget:
                print("YES")
                print(*positions_from_order(improved))
                return

    adj_masks = [0] * n
    for u in range(n):
        mask = 0
        for v in adj[u]:
            mask |= 1 << v
        adj_masks[u] = mask

    if n <= 21:
        answer = exact_array_dp(n, adj_masks, degrees, budget)
    else:
        answer = exact_sparse_dp(n, adj_masks, degrees, budget)

    if answer is None:
        print("NO")
    else:
        print("YES")
        print(*answer)


if __name__ == "__main__":
    main()