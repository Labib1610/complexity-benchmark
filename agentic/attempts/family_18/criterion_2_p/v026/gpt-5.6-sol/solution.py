import sys
from array import array

def exact_minimum_arrangement(n, adj_masks):
    size = 1 << n
    cut = array('i', [0]) * size

    for mask in range(1, size):
        bit = mask & -mask
        v = bit.bit_length() - 1
        prev = mask ^ bit
        cut[mask] = cut[prev] + adj_masks[v].bit_count() - 2 * (adj_masks[v] & prev).bit_count()

    inf = 10**18
    dp = array('q', [inf]) * size
    parent = bytearray(size)
    dp[0] = 0

    for mask in range(1, size):
        bits = mask
        best = inf
        best_v = 0
        while bits:
            bit = bits & -bits
            v = bit.bit_length() - 1
            value = dp[mask ^ bit]
            if value < best:
                best = value
                best_v = v
            bits ^= bit
        dp[mask] = best + cut[mask]
        parent[mask] = best_v

    order_rev = []
    mask = size - 1
    while mask:
        v = parent[mask]
        order_rev.append(v)
        mask ^= 1 << v

    order = order_rev[::-1]
    position = [0] * n
    for i, v in enumerate(order, 1):
        position[v] = i

    return dp[size - 1], position


def projective_arrangement(n, graph):
    parent = [-1] * n
    children = [[] for _ in range(n)]
    traversal = [0]
    parent[0] = 0

    for u in traversal:
        for v in graph[u]:
            if parent[v] == -1:
                parent[v] = u
                children[u].append(v)
                traversal.append(v)

    subtree_size = [1] * n
    anchored_cost = [0] * n
    rope = [None] * n

    for u in reversed(traversal):
        items = []
        base_cost = 0

        for v in children[u]:
            subtree_size[u] += subtree_size[v]
            base_cost += anchored_cost[v]
            items.append((subtree_size[v], v))

        items.sort()
        k = len(items)

        if k == 0:
            anchored_cost[u] = 1
            rope[u] = [u]
            continue

        all_equal = all(items[i][0] == items[0][0] for i in range(1, k))

        if all_equal:
            s = items[0][0]
            best_value = None
            best_left_count = 0

            for left_count in range(k + 1):
                right_count = k - left_count
                offsets = s * (
                    left_count * (left_count - 1) // 2
                    + right_count * (right_count - 1) // 2
                )
                left_size = left_count * s
                value = offsets + left_size + 1
                if best_value is None or value < best_value:
                    best_value = value
                    best_left_count = left_count

            left_flags = [i < best_left_count for i in range(k)]
            anchored_cost[u] = base_cost + best_value
        else:
            dp = {0: 0}
            decisions = []
            processed = 0

            for s, _ in items:
                ndp = {}
                chose_left = set()

                for left_size, value in dp.items():
                    right_size = processed - left_size

                    right_value = value + right_size
                    old = ndp.get(left_size)
                    if old is None or right_value < old:
                        ndp[left_size] = right_value

                    new_left_size = left_size + s
                    left_value = value + left_size
                    old = ndp.get(new_left_size)
                    if old is None or left_value < old:
                        ndp[new_left_size] = left_value
                        chose_left.add(new_left_size)

                dp = ndp
                decisions.append(chose_left)
                processed += s

            target_left = min(dp, key=lambda x: dp[x] + x + 1)
            anchored_cost[u] = base_cost + dp[target_left] + target_left + 1

            left_flags = [False] * k
            current = target_left
            for i in range(k - 1, -1, -1):
                s = items[i][0]
                if current in decisions[i]:
                    left_flags[i] = True
                    current -= s

        left_items = []
        right_items = []

        for flag, (_, v) in zip(left_flags, items):
            if flag:
                left_items.append(v)
            else:
                right_items.append(v)

        parts = []
        for v in reversed(left_items):
            parts.append((rope[v], True))
        parts.append(u)
        for v in right_items:
            parts.append((rope[v], False))
        rope[u] = parts

    root = 0
    items = sorted((subtree_size[v], v) for v in children[root])
    base_cost = sum(anchored_cost[v] for v in children[root])
    k = len(items)

    if k == 0:
        final_rope = [root]
        root_cost = 0
    else:
        all_equal = all(items[i][0] == items[0][0] for i in range(1, k))

        if all_equal:
            s = items[0][0]
            best_value = None
            best_left_count = 0

            for left_count in range(k + 1):
                right_count = k - left_count
                value = s * (
                    left_count * (left_count - 1) // 2
                    + right_count * (right_count - 1) // 2
                )
                if best_value is None or value < best_value:
                    best_value = value
                    best_left_count = left_count

            left_flags = [i < best_left_count for i in range(k)]
            root_cost = base_cost + best_value
        else:
            dp = {0: 0}
            decisions = []
            processed = 0

            for s, _ in items:
                ndp = {}
                chose_left = set()

                for left_size, value in dp.items():
                    right_size = processed - left_size

                    right_value = value + right_size
                    old = ndp.get(left_size)
                    if old is None or right_value < old:
                        ndp[left_size] = right_value

                    new_left_size = left_size + s
                    left_value = value + left_size
                    old = ndp.get(new_left_size)
                    if old is None or left_value < old:
                        ndp[new_left_size] = left_value
                        chose_left.add(new_left_size)

                dp = ndp
                decisions.append(chose_left)
                processed += s

            target_left = min(dp, key=dp.get)
            root_cost = base_cost + dp[target_left]

            left_flags = [False] * k
            current = target_left
            for i in range(k - 1, -1, -1):
                s = items[i][0]
                if current in decisions[i]:
                    left_flags[i] = True
                    current -= s

        left_items = []
        right_items = []
        for flag, (_, v) in zip(left_flags, items):
            if flag:
                left_items.append(v)
            else:
                right_items.append(v)

        final_rope = []
        for v in reversed(left_items):
            final_rope.append((rope[v], True))
        final_rope.append(root)
        for v in right_items:
            final_rope.append((rope[v], False))

    order = []
    stack = [(final_rope, False)]

    while stack:
        node, flipped = stack.pop()

        if isinstance(node, int):
            order.append(node)
            continue

        if not flipped:
            iterator = reversed(node)
            for part in iterator:
                if isinstance(part, int):
                    stack.append((part, False))
                else:
                    child_rope, child_flip = part
                    stack.append((child_rope, child_flip))
        else:
            for part in node:
                if isinstance(part, int):
                    stack.append((part, False))
                else:
                    child_rope, child_flip = part
                    stack.append((child_rope, not child_flip))

    position = [0] * n
    for i, v in enumerate(order, 1):
        position[v] = i

    return root_cost, position


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m, budget = data[0], data[1], data[2]
    graph = [[] for _ in range(n)]
    edges = []
    idx = 3

    for _ in range(m):
        u = data[idx] - 1
        v = data[idx + 1] - 1
        idx += 2
        graph[u].append(v)
        graph[v].append(u)
        edges.append((u, v))

    if n <= 20:
        masks = [0] * n
        for u, v in edges:
            masks[u] |= 1 << v
            masks[v] |= 1 << u
        cost, position = exact_minimum_arrangement(n, masks)
    else:
        _, position = projective_arrangement(n, graph)
        cost = 0
        for u, v in edges:
            cost += abs(position[u] - position[v])

    if cost <= budget:
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, position)))
        sys.stdout.write("\n")
    else:
        sys.stdout.write("NO\n")


if __name__ == "__main__":
    main()