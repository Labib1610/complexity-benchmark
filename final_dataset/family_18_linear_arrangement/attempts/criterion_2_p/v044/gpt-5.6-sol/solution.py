import sys

def main():
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
        if budget >= 0:
            print("YES")
            print(1)
        else:
            print("NO")
        return

    parent = [-1] * n
    order = [0]
    for v in order:
        for u in graph[v]:
            if u != parent[v]:
                parent[u] = v
                order.append(u)

    subtree_size = [1] * n
    down_anchor = [0] * n

    for v in reversed(order):
        items = []
        base = 0
        for u in graph[v]:
            if parent[u] == v:
                subtree_size[v] += subtree_size[u]
                items.append(subtree_size[u])
                base += down_anchor[u] + 1

        items.sort(reverse=True)
        extra = 0
        for i, size in enumerate(items):
            extra += size * ((i + 1) // 2)
        down_anchor[v] = base + extra

    external_anchor = [0] * n
    external_size = [0] * n
    free_cost = [0] * n

    for v in order:
        items = []
        for u in graph[v]:
            if parent[u] == v:
                items.append((subtree_size[u], down_anchor[u], u))
            elif parent[v] == u:
                items.append((external_size[v], external_anchor[v], u))

        items.sort(key=lambda x: x[0], reverse=True)
        d = len(items)

        total_base = 0
        for size, anchor, u in items:
            total_base += anchor + 1

        free_extra = 0
        for i, (size, anchor, u) in enumerate(items):
            free_extra += size * (i // 2)
        free_cost[v] = total_base + free_extra

        prefix = [0] * (d + 1)
        for i, (size, anchor, u) in enumerate(items):
            prefix[i + 1] = prefix[i] + size * ((i + 1) // 2)

        shifted_suffix = [0] * (d + 1)
        for i in range(d - 1, -1, -1):
            coefficient = i // 2
            shifted_suffix[i] = shifted_suffix[i + 1] + items[i][0] * coefficient

        for i, (size, anchor, u) in enumerate(items):
            if parent[u] == v:
                extra_without = prefix[i] + shifted_suffix[i + 1]
                external_anchor[u] = total_base - (anchor + 1) + extra_without
                external_size[u] = n - subtree_size[u]

    best_root = min(range(n), key=lambda v: free_cost[v])
    minimum_cost = free_cost[best_root]

    if minimum_cost > budget:
        print("NO")
        return

    rooted_parent = [-1] * n
    rooted_order = [best_root]
    for v in rooted_order:
        for u in graph[v]:
            if u != rooted_parent[v]:
                rooted_parent[u] = v
                rooted_order.append(u)

    rooted_size = [1] * n
    for v in reversed(rooted_order):
        for u in graph[v]:
            if rooted_parent[u] == v:
                rooted_size[v] += rooted_size[u]

    layout = []
    stack = [(best_root, False, True)]

    while stack:
        v, flipped, is_free = stack.pop()

        children = [u for u in graph[v] if rooted_parent[u] == v]
        children.sort(key=lambda u: rooted_size[u], reverse=True)

        left = []
        right = []
        left_count = 0
        right_count = 0

        if is_free:
            for u in children:
                if right_count <= left_count:
                    right.append(u)
                    right_count += 1
                else:
                    left.append(u)
                    left_count += 1
        else:
            for u in children:
                if right_count <= left_count + 1:
                    right.append(u)
                    right_count += 1
                else:
                    left.append(u)
                    left_count += 1

        parts = []
        for u in left:
            parts.append((1, u, True))
        parts.append((0, v, False))
        for u in reversed(right):
            parts.append((1, u, False))

        if flipped:
            parts.reverse()

        for kind, x, reverse_child in reversed(parts):
            if kind == 0:
                stack.append((~x, False, False))
            else:
                stack.append((x, reverse_child ^ flipped, False))

        while stack and stack[-1][0] < 0:
            token, _, _ = stack.pop()
            layout.append(~token)

    position = [0] * n
    for pos, vertex in enumerate(layout, 1):
        position[vertex] = pos

    print("YES")
    print(*position)

if __name__ == "__main__":
    main()