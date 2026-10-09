import sys

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

    parent = [-1] * n
    order = [0]
    for v in order:
        for u in adj[v]:
            if u != parent[v]:
                parent[u] = v
                order.append(u)

    subtree = [1] * n
    down_a = [0] * n

    for v in reversed(order):
        branches = []
        sum_a = 0
        for u in adj[v]:
            if parent[u] == v:
                subtree[v] += subtree[u]
                branches.append(subtree[u])
                sum_a += down_a[u]

        branches.sort(reverse=True)
        weighted = 0
        for i, size in enumerate(branches):
            weighted += size * ((i + 1) // 2)
        down_a[v] = 1 + sum_a + weighted

    up_a = [0] * n
    best_cost = None
    best_root = 0

    for v in order:
        items = []
        total_a = 0

        for u in adj[v]:
            if parent[u] == v:
                size = subtree[u]
                aval = down_a[u]
            else:
                size = n - subtree[v]
                aval = up_a[v]
            items.append((size, u, aval))
            total_a += aval

        items.sort(key=lambda x: x[0], reverse=True)
        d = len(items)

        free_weighted = 0
        anchored_weighted = 0
        for i, (size, _, _) in enumerate(items):
            free_weighted += size * (i // 2)
            anchored_weighted += size * ((i + 1) // 2)

        free_cost = total_a + free_weighted
        if best_cost is None or free_cost < best_cost:
            best_cost = free_cost
            best_root = v

        suffix_odd = [0] * (d + 1)
        for i in range(d - 1, -1, -1):
            suffix_odd[i] = suffix_odd[i + 1]
            if i & 1:
                suffix_odd[i] += items[i][0]

        for i, (size, u, aval) in enumerate(items):
            if parent[u] != v:
                continue
            excluded_weighted = (
                anchored_weighted
                - size * ((i + 1) // 2)
                - suffix_odd[i + 1]
            )
            up_a[u] = 1 + (total_a - aval) + excluded_weighted

    if best_cost > budget:
        print("NO")
        return

    def branch_size(v, u):
        if parent[u] == v:
            return subtree[u]
        return n - subtree[v]

    placement_order = []
    stack = [("F", best_root, -1, False)]

    while stack:
        kind, v, p, rev = stack.pop()

        if kind == "V":
            placement_order.append(v)
            continue

        children = [u for u in adj[v] if u != p]
        children.sort(key=lambda u: branch_size(v, u), reverse=True)

        pieces = []

        if kind == "F":
            left = children[0::2]
            right_outer_to_inner = children[1::2]

            for u in left:
                pieces.append(("A", u, v, True))
            pieces.append(("V", v, -1, False))
            for u in reversed(right_outer_to_inner):
                pieces.append(("A", u, v, False))

        elif not rev:
            left = children[1::2]
            right_outer_to_inner = children[0::2]

            for u in left:
                pieces.append(("A", u, v, True))
            pieces.append(("V", v, -1, False))
            for u in reversed(right_outer_to_inner):
                pieces.append(("A", u, v, False))

        else:
            right_outer_to_inner = children[0::2]
            left_outer_to_inner = children[1::2]

            for u in right_outer_to_inner:
                pieces.append(("A", u, v, True))
            pieces.append(("V", v, -1, False))
            for u in reversed(left_outer_to_inner):
                pieces.append(("A", u, v, False))

        for task in reversed(pieces):
            stack.append(task)

    position = [0] * n
    for pos, v in enumerate(placement_order, 1):
        position[v] = pos

    print("YES")
    print(*position)

if __name__ == "__main__":
    main()