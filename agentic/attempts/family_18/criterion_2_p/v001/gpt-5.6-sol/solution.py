import sys
import random
from array import array

def arrangement_cost(order, edges):
    pos = [0] * len(order)
    for i, v in enumerate(order):
        pos[v] = i
    return sum(abs(pos[u] - pos[v]) for u, v in edges)

def improve_adjacent(order, adj, max_passes=8):
    n = len(order)
    pos = [0] * n
    for i, v in enumerate(order):
        pos[v] = i

    for _ in range(max_passes):
        changed = False
        i = 0
        while i + 1 < n:
            a, b = order[i], order[i + 1]
            delta = 0

            for x in adj[a]:
                if x == b:
                    continue
                px = pos[x]
                delta += 1 if px < i else -1

            for x in adj[b]:
                if x == a:
                    continue
                px = pos[x]
                delta += -1 if px < i + 1 else 1

            if delta < 0:
                order[i], order[i + 1] = b, a
                pos[a], pos[b] = i + 1, i
                changed = True
                if i:
                    i -= 1
                    continue
            i += 1

        if not changed:
            break
    return order

def dfs_order(adj, root, randomized=False):
    n = len(adj)
    parent = [-2] * n
    parent[root] = -1
    order = []
    stack = [root]

    while stack:
        v = stack.pop()
        order.append(v)
        children = [x for x in adj[v] if x != parent[v]]
        if randomized:
            random.shuffle(children)
        else:
            children.sort(key=lambda x: len(adj[x]))
        for x in reversed(children):
            if parent[x] == -2:
                parent[x] = v
                stack.append(x)
    return order

def centroid_layout(adj):
    n = len(adj)
    blocked = bytearray(n)
    sys.setrecursionlimit(max(1000000, n * 2 + 10))

    def build(vertices, requested_anchor):
        total = len(vertices)
        start = vertices[0]
        parent = {start: -1}
        traversal = [start]

        for v in traversal:
            for x in adj[v]:
                if blocked[x] or x == parent[v]:
                    continue
                parent[x] = v
                traversal.append(x)

        size = {}
        centroid = start
        best = total + 1

        for v in reversed(traversal):
            s = 1
            largest = 0
            for x in adj[v]:
                if blocked[x] or parent.get(x) != v:
                    continue
                sx = size[x]
                s += sx
                if sx > largest:
                    largest = sx
            outside = total - s
            if outside > largest:
                largest = outside
            size[v] = s
            if largest < best:
                best = largest
                centroid = v

        blocked[centroid] = 1
        components = []

        for nb in adj[centroid]:
            if blocked[nb]:
                continue
            comp = []
            stack = [(nb, centroid)]
            while stack:
                v, p = stack.pop()
                comp.append(v)
                for x in adj[v]:
                    if not blocked[x] and x != p:
                        stack.append((x, v))
            child_order, anchor_pos = build(comp, nb)
            components.append([len(comp), child_order, anchor_pos])

        components.sort(key=lambda z: z[0], reverse=True)
        left, right = [], []
        left_size = right_size = 0

        for item in components:
            if left_size <= right_size:
                left.append(item)
                left_size += item[0]
            else:
                right.append(item)
                right_size += item[0]

        left.sort(key=lambda z: z[0], reverse=True)   # outer to inner
        right.sort(key=lambda z: z[0])                # inner to outer

        result = []

        for _, block, anchor_pos in left:
            if anchor_pos < len(block) - 1 - anchor_pos:
                block = block[::-1]
            result.extend(block)

        result.append(centroid)

        for _, block, anchor_pos in right:
            if anchor_pos > len(block) - 1 - anchor_pos:
                block = block[::-1]
            result.extend(block)

        anchor_index = result.index(requested_anchor) if requested_anchor is not None else 0
        return result, anchor_index

    return build(list(range(n)), None)[0]

def exact_minimum_arrangement(adj):
    n = len(adj)
    total_masks = 1 << n
    neighbor_masks = [0] * n
    degrees = [0] * n

    for v in range(n):
        mask = 0
        for x in adj[v]:
            mask |= 1 << x
        neighbor_masks[v] = mask
        degrees[v] = len(adj[v])

    cuts = array('H', [0]) * total_masks
    dp = array('I', [0]) * total_masks

    for mask in range(1, total_masks):
        bit = mask & -mask
        v = bit.bit_length() - 1
        prev = mask ^ bit
        cuts[mask] = cuts[prev] + degrees[v] - 2 * ((neighbor_masks[v] & prev).bit_count())

        best = 0xFFFFFFFF
        bits = mask
        while bits:
            b = bits & -bits
            val = dp[mask ^ b]
            if val < best:
                best = val
            bits ^= b
        dp[mask] = best + cuts[mask]

    order = [0] * n
    mask = total_masks - 1

    for index in range(n - 1, -1, -1):
        target = dp[mask] - cuts[mask]
        bits = mask
        while bits:
            b = bits & -bits
            if dp[mask ^ b] == target:
                v = b.bit_length() - 1
                order[index] = v
                mask ^= b
                break
            bits ^= b

    return int(dp[total_masks - 1]), order

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 3:
        return

    n, m, budget = data[0], data[1], data[2]
    adj = [[] for _ in range(n)]
    edges = []
    p = 3

    for _ in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))

    if n == 1:
        if budget >= 0:
            print("YES")
            print(1)
        else:
            print("NO")
        return

    lower_sum = 0
    lower_max = 0
    for v in range(n):
        d = len(adj[v])
        q = d // 2
        if d % 2 == 0:
            g = q * (q + 1)
        else:
            g = (q + 1) * (q + 1)
        lower_sum += g
        if g > lower_max:
            lower_max = g

    lower_bound = max(lower_max, (lower_sum + 1) // 2, n - 1)
    if budget < lower_bound:
        print("NO")
        return

    candidates = [list(range(n)), list(reversed(range(n)))]

    try:
        candidates.append(centroid_layout(adj))
    except RecursionError:
        pass

    roots = [0, max(range(n), key=lambda v: len(adj[v]))]
    for root in roots:
        candidates.append(dfs_order(adj, root, False))

    if n <= 50000:
        random.seed(712367821)
        for _ in range(2):
            candidates.append(dfs_order(adj, random.randrange(n), True))

    best_order = None
    best_cost = 10**30

    for order in candidates:
        order = improve_adjacent(order, adj)
        cost = arrangement_cost(order, edges)
        if cost < best_cost:
            best_cost = cost
            best_order = order[:]
        if cost <= budget:
            positions = [0] * n
            for i, v in enumerate(order):
                positions[v] = i + 1
            print("YES")
            print(*positions)
            return

    if n <= 22:
        optimum, order = exact_minimum_arrangement(adj)
        if optimum <= budget:
            positions = [0] * n
            for i, v in enumerate(order):
                positions[v] = i + 1
            print("YES")
            print(*positions)
        else:
            print("NO")
        return

    print("NO")

if __name__ == "__main__":
    main()