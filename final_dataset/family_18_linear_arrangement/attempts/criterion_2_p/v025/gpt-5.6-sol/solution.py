import sys

sys.setrecursionlimit(1_000_000)


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m, B = data[0], data[1], data[2]
    adj = [[] for _ in range(n)]
    edges = []

    idx = 3
    for _ in range(m):
        u = data[idx] - 1
        v = data[idx + 1] - 1
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))

    if n == 1:
        print("YES")
        print(1)
        return

    # Find a centroid to use as the root.
    parent0 = [-1] * n
    order0 = [0]
    for v in order0:
        for u in adj[v]:
            if u != parent0[v]:
                parent0[u] = v
                order0.append(u)

    subtree0 = [1] * n
    for v in reversed(order0):
        if parent0[v] != -1:
            subtree0[parent0[v]] += subtree0[v]

    centroid = 0
    best_part = n
    for v in range(n):
        largest = n - subtree0[v]
        for u in adj[v]:
            if parent0[u] == v:
                largest = max(largest, subtree0[u])
        if largest < best_part:
            best_part = largest
            centroid = v

    parent = [-1] * n
    order = [centroid]
    children = [[] for _ in range(n)]

    for v in order:
        for u in adj[v]:
            if u != parent[v]:
                parent[u] = v
                children[v].append(u)
                order.append(u)

    size = [1] * n

    # costs[v] maps the position of v inside its subtree block (1-based)
    # to the minimum cost of all edges internal to that subtree.
    costs = [None] * n
    sorted_children = [None] * n
    decision_masks = [None] * n
    left_root_positions = [None] * n
    right_root_positions = [None] * n

    INF = 10**30

    for v in reversed(order):
        if not children[v]:
            size[v] = 1
            costs[v] = {1: 0}
            sorted_children[v] = []
            decision_masks[v] = []
            left_root_positions[v] = []
            right_root_positions[v] = []
            continue

        children[v].sort(key=lambda x: size[x])
        chs = children[v]
        sorted_children[v] = chs

        q_left = []
        q_right = []
        anchor_left = []
        anchor_right = []

        total_size = 1
        for u in chs:
            su = size[u]
            total_size += su

            best_l = INF
            best_r = INF
            best_ql = 1
            best_qr = 1

            for q, value in costs[u].items():
                val_l = value + su + 1 - q
                if val_l < best_l:
                    best_l = val_l
                    best_ql = q

                val_r = value + q
                if val_r < best_r:
                    best_r = val_r
                    best_qr = q

            anchor_left.append(best_l)
            anchor_right.append(best_r)
            q_left.append(best_ql)
            q_right.append(best_qr)

        left_root_positions[v] = q_left
        right_root_positions[v] = q_right

        dp = {0: 0}
        processed = 0
        masks = []

        for i, u in enumerate(chs):
            su = size[u]
            al = anchor_left[i]
            ar = anchor_right[i]
            nd = {}
            mask = 0

            for left_sum, value in dp.items():
                # Put this child on the right, outside all prior right blocks.
                new_left = left_sum
                candidate = value + ar + (processed - left_sum)
                old = nd.get(new_left)
                if old is None or candidate < old:
                    nd[new_left] = candidate

                # Put this child on the left, outside all prior left blocks.
                new_left = left_sum + su
                candidate = value + al + left_sum
                old = nd.get(new_left)
                if old is None or candidate < old:
                    nd[new_left] = candidate
                    mask |= 1 << new_left
                elif candidate == old:
                    # Either transition is valid; retain an existing right
                    # transition when present.
                    pass

            dp = nd
            processed += su
            masks.append(mask)

        size[v] = total_size
        costs[v] = {left_sum + 1: value for left_sum, value in dp.items()}
        decision_masks[v] = masks

    root_position, minimum_cost = min(costs[centroid].items(), key=lambda item: item[1])

    if minimum_cost > B:
        print("NO")
        return

    position = [0] * n

    def reconstruct(v, root_pos, block_start):
        chs = sorted_children[v]
        d = len(chs)

        side_left = [False] * d
        current_left_sum = root_pos - 1

        for i in range(d - 1, -1, -1):
            if (decision_masks[v][i] >> current_left_sum) & 1:
                side_left[i] = True
                current_left_sum -= size[chs[i]]

        position[v] = block_start + root_pos - 1

        left_children = []
        right_children = []

        for i, u in enumerate(chs):
            if side_left[i]:
                left_children.append((i, u))
            else:
                right_children.append((i, u))

        cursor = block_start

        # Left blocks are stored near-to-far, hence placed in reverse order.
        for i, u in reversed(left_children):
            reconstruct(u, left_root_positions[v][i], cursor)
            cursor += size[u]

        cursor = position[v] + 1

        # Right blocks are placed near-to-far.
        for i, u in right_children:
            reconstruct(u, right_root_positions[v][i], cursor)
            cursor += size[u]

    reconstruct(centroid, root_position, 1)

    actual_cost = 0
    for u, v in edges:
        actual_cost += abs(position[u] - position[v])

    if actual_cost > B:
        print("NO")
        return

    print("YES")
    print(*position)


if __name__ == "__main__":
    main()