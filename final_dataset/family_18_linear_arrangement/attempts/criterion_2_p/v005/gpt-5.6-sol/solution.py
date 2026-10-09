import sys
from functools import lru_cache

sys.setrecursionlimit(1_000_000)
INF = 10**30


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 3:
        return

    n, m, budget = data[0], data[1], data[2]
    if n <= 0 or m != n - 1 or len(data) != 3 + 2 * m:
        print("NO")
        return

    graph = [[] for _ in range(n)]
    edges = []
    idx = 3
    valid = True

    for _ in range(m):
        u = data[idx] - 1
        v = data[idx + 1] - 1
        idx += 2
        if not (0 <= u < n and 0 <= v < n) or u == v:
            valid = False
            continue
        graph[u].append(v)
        graph[v].append(u)
        edges.append((u, v))

    if not valid:
        print("NO")
        return

    if n == 1:
        print("YES")
        print(1)
        return

    # Verify connectivity.
    seen = [False] * n
    stack = [0]
    seen[0] = True
    count = 0
    while stack:
        u = stack.pop()
        count += 1
        for v in graph[u]:
            if not seen[v]:
                seen[v] = True
                stack.append(v)

    if count != n:
        print("NO")
        return

    if budget < n - 1:
        print("NO")
        return

    # A cheap placement may already satisfy the budget.
    order = []
    stack = [(0, -1)]
    while stack:
        u, p = stack.pop()
        order.append(u)
        for v in reversed(graph[u]):
            if v != p:
                stack.append((v, u))

    pos = [0] * n
    for i, u in enumerate(order):
        pos[u] = i + 1

    cheap_cost = sum(abs(pos[u] - pos[v]) for u, v in edges)
    if cheap_cost <= budget:
        print("YES")
        print(*pos)
        return

    # Directed component sizes.
    parent = [-1] * n
    traversal = [0]
    for u in traversal:
        for v in graph[u]:
            if v != parent[u]:
                parent[v] = u
                traversal.append(v)

    subtree = [1] * n
    for u in reversed(traversal):
        for v in graph[u]:
            if parent[v] == u:
                subtree[u] += subtree[v]

    def component_size(u, blocked):
        if parent[u] == blocked:
            return subtree[u]
        return n - subtree[blocked]

    @lru_cache(maxsize=None)
    def partition_value(sizes, anchored):
        k = len(sizes)
        if k <= 1:
            return 0
        if k == 2:
            return sizes[0] if anchored else 0

        total = 0
        dp = [0]

        for s in sizes:
            new_total = total + s
            ndp = [INF] * (new_total + 1)

            for left_sum, value in enumerate(dp):
                if value == INF:
                    continue

                # Put this component on the right side.
                nv = value + (total - left_sum)
                if nv < ndp[left_sum]:
                    ndp[left_sum] = nv

                # Put this component on the left side.
                nv = value + left_sum + (s if anchored else 0)
                nx = left_sum + s
                if nv < ndp[nx]:
                    ndp[nx] = nv

            dp = ndp
            total = new_total

        return min(dp)

    @lru_cache(maxsize=None)
    def anchored_cost(u, blocked):
        base = 1
        sizes = []

        for v in graph[u]:
            if v == blocked:
                continue
            base += anchored_cost(v, u)
            sizes.append(component_size(v, u))

        sizes.sort()
        return base + partition_value(tuple(sizes), True)

    best_cost = INF
    best_root = -1

    for u in range(n):
        base = 0
        sizes = []
        for v in graph[u]:
            base += anchored_cost(v, u)
            sizes.append(component_size(v, u))
        sizes.sort()
        value = base + partition_value(tuple(sizes), False)
        if value < best_cost:
            best_cost = value
            best_root = u

    if best_cost > budget:
        print("NO")
        return

    def recover_partition(items, anchored):
        # items are (size, vertex), sorted by size.
        k = len(items)
        if k == 0:
            return [], []

        dp = [0]
        total = 0
        choices = []

        for s, _ in items:
            new_total = total + s
            ndp = [INF] * (new_total + 1)
            choice = bytearray(new_total + 1)

            for left_sum, value in enumerate(dp):
                if value == INF:
                    continue

                nv = value + (total - left_sum)
                if nv < ndp[left_sum]:
                    ndp[left_sum] = nv
                    choice[left_sum] = 2

                nx = left_sum + s
                nv = value + left_sum + (s if anchored else 0)
                if nv < ndp[nx]:
                    ndp[nx] = nv
                    choice[nx] = 1

            choices.append(choice)
            dp = ndp
            total = new_total

        x = min(range(len(dp)), key=dp.__getitem__)
        on_left = [False] * k

        for i in range(k - 1, -1, -1):
            s = items[i][0]
            if choices[i][x] == 1:
                on_left[i] = True
                x -= s

        left = [items[i] for i in range(k) if on_left[i]]
        right = [items[i] for i in range(k) if not on_left[i]]
        return left, right

    @lru_cache(maxsize=None)
    def anchored_split(u, blocked):
        items = []
        for v in graph[u]:
            if v != blocked:
                items.append((component_size(v, u), v))
        items.sort(key=lambda z: (z[0], z[1]))
        left, right = recover_partition(items, True)
        return tuple(v for _, v in left), tuple(v for _, v in right)

    def root_split(u):
        items = [(component_size(v, u), v) for v in graph[u]]
        items.sort(key=lambda z: (z[0], z[1]))
        left, right = recover_partition(items, False)
        return tuple(v for _, v in left), tuple(v for _, v in right)

    final_order = []

    def emit_anchored(u, blocked, anchor_on_left):
        left, right = anchored_split(u, blocked)

        if anchor_on_left:
            for v in reversed(left):
                emit_anchored(v, u, False)
            final_order.append(u)
            for v in right:
                emit_anchored(v, u, True)
        else:
            for v in reversed(right):
                emit_anchored(v, u, False)
            final_order.append(u)
            for v in left:
                emit_anchored(v, u, True)

    left, right = root_split(best_root)
    for v in reversed(left):
        emit_anchored(v, best_root, False)
    final_order.append(best_root)
    for v in right:
        emit_anchored(v, best_root, True)

    if len(final_order) != n:
        print("NO")
        return

    answer = [0] * n
    for i, u in enumerate(final_order):
        answer[u] = i + 1

    actual_cost = sum(abs(answer[u] - answer[v]) for u, v in edges)
    if actual_cost > budget:
        print("NO")
        return

    print("YES")
    print(*answer)


if __name__ == "__main__":
    main()