import sys


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m, budget = data[0], data[1], data[2]
    graph = [[] for _ in range(n)]
    idx = 3

    for _ in range(m):
        u = data[idx] - 1
        v = data[idx + 1] - 1
        idx += 2
        graph[u].append(v)
        graph[v].append(u)

    if n == 1:
        print("YES")
        print(1)
        return

    if m != n - 1:
        print("NO")
        return

    # Find a centroid.
    parent0 = [-1] * n
    order0 = [0]
    for u in order0:
        for v in graph[u]:
            if v != parent0[u]:
                parent0[v] = u
                order0.append(v)

    if len(order0) != n:
        print("NO")
        return

    subtree0 = [1] * n
    for u in reversed(order0):
        if parent0[u] != -1:
            subtree0[parent0[u]] += subtree0[u]

    centroid = 0
    for u in range(n):
        largest = n - subtree0[u]
        for v in graph[u]:
            if parent0[v] == u:
                largest = max(largest, subtree0[v])
        if largest * 2 <= n:
            centroid = u
            break

    # Root the tree at the centroid.
    parent = [-1] * n
    order = [centroid]
    for u in order:
        for v in graph[u]:
            if v != parent[u]:
                parent[v] = u
                order.append(v)

    subtree = [1] * n
    for u in reversed(order):
        if parent[u] != -1:
            subtree[parent[u]] += subtree[u]

    # dp[u][p] = minimum cost inside subtree u when u is at local position p.
    dp = [None] * n
    child_info = [None] * n
    decisions = [None] * n

    for u in reversed(order):
        children = [v for v in graph[u] if parent[v] == u]
        info = []

        for v in children:
            child_dp = dp[v]
            size_v = subtree[v]

            best_left = None
            best_left_pos = 1
            best_right = None
            best_right_pos = 1

            for p, value in child_dp.items():
                left_value = value + (size_v - p + 1)
                if best_left is None or left_value < best_left:
                    best_left = left_value
                    best_left_pos = p

                right_value = value + p
                if best_right is None or right_value < best_right:
                    best_right = right_value
                    best_right_pos = p

            info.append((
                v,
                size_v,
                best_left,
                best_left_pos,
                best_right,
                best_right_pos
            ))

        info.sort(key=lambda x: x[1])

        current = {0: 0}
        processed_size = 0
        node_decisions = []

        for v, size_v, base_left, pos_left, base_right, pos_right in info:
            new_cost = {}
            choice = bytearray(processed_size + size_v + 1)

            for left_size, value in current.items():
                right_size = processed_size - left_size

                # Put this child on the right.
                nr = left_size
                cand = value + base_right + right_size
                old = new_cost.get(nr)
                if old is None or cand < old:
                    new_cost[nr] = cand
                    choice[nr] = 0

                # Put this child on the left.
                nl = left_size + size_v
                cand = value + base_left + left_size
                old = new_cost.get(nl)
                if old is None or cand < old:
                    new_cost[nl] = cand
                    choice[nl] = 1

            current = new_cost
            processed_size += size_v
            node_decisions.append(choice)

        dp[u] = {left_size + 1: value for left_size, value in current.items()}
        child_info[u] = info
        decisions[u] = node_decisions

        for v in children:
            dp[v] = None

    root_dp = dp[centroid]
    root_pos, minimum_cost = min(root_dp.items(), key=lambda item: item[1])

    if minimum_cost > budget:
        print("NO")
        return

    # Reconstruct the ordering iteratively.
    arrangement = []
    stack = [(centroid, root_pos)]

    while stack:
        u, wanted_pos = stack.pop()

        if wanted_pos == 0:
            arrangement.append(u)
            continue

        info = child_info[u]
        node_decisions = decisions[u]
        left_size = wanted_pos - 1

        sides = [False] * len(info)
        child_positions = [0] * len(info)

        for i in range(len(info) - 1, -1, -1):
            v, size_v, _, pos_left, _, pos_right = info[i]
            if node_decisions[i][left_size]:
                sides[i] = True
                child_positions[i] = pos_left
                left_size -= size_v
            else:
                child_positions[i] = pos_right

        left_indices = [i for i in range(len(info)) if sides[i]]
        right_indices = [i for i in range(len(info)) if not sides[i]]

        # Desired order:
        # reversed(left processing order), u, right processing order.
        # Push in reverse because stack is LIFO.
        for i in reversed(right_indices):
            stack.append((info[i][0], child_positions[i]))

        stack.append((u, 0))

        for i in left_indices:
            stack.append((info[i][0], child_positions[i]))

    position = [0] * n
    for p, vertex in enumerate(arrangement, 1):
        position[vertex] = p

    actual_cost = 0
    for u in range(n):
        for v in graph[u]:
            if u < v:
                actual_cost += abs(position[u] - position[v])

    if actual_cost > budget:
        print("NO")
        return

    print("YES")
    print(*position)


if __name__ == "__main__":
    solve()