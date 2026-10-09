import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    it = iter(data)
    n = next(it)
    m = next(it)
    budget = next(it)

    graph = [[] for _ in range(n)]
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        graph[u].append(v)
        graph[v].append(u)

    if n == 1:
        if budget >= 0:
            print("YES")
            print(1)
        else:
            print("NO")
        return

    parent0 = [-1] * n
    order0 = [0]
    for v in order0:
        for u in graph[v]:
            if u != parent0[v]:
                parent0[u] = v
                order0.append(u)

    size0 = [1] * n
    for v in reversed(order0[1:]):
        size0[parent0[v]] += size0[v]

    centroids = []
    for v in range(n):
        largest = n - size0[v]
        for u in graph[v]:
            if parent0[u] == v:
                if size0[u] > largest:
                    largest = size0[u]
        if largest * 2 <= n:
            centroids.append(v)

    def solve(root):
        parent = [-2] * n
        parent[root] = -1
        order = [root]

        for v in order:
            for u in graph[v]:
                if parent[u] == -2:
                    parent[u] = v
                    order.append(u)

        size = [1] * n
        anchored_cost = [0] * n
        left_children = [[] for _ in range(n)]
        right_children = [[] for _ in range(n)]

        for v in reversed(order):
            children = [u for u in graph[v] if parent[u] == v]
            children.sort(key=lambda x: size[x], reverse=True)

            lc, rc = 1, 0
            extra = 0
            base = 1

            left = []
            right = []

            for u in children:
                size[v] += size[u]
                base += anchored_cost[u]

                if lc <= rc:
                    extra += size[u] * lc
                    lc += 1
                    left.append(u)
                else:
                    extra += size[u] * rc
                    rc += 1
                    right.append(u)

            anchored_cost[v] = base + extra
            left_children[v] = left
            right_children[v] = right

        root_children = [u for u in graph[root] if parent[u] == root]
        root_children.sort(key=lambda x: size[x], reverse=True)

        root_left = []
        root_right = []
        lc = rc = 0
        total_cost = 0

        for u in root_children:
            total_cost += anchored_cost[u]
            if lc <= rc:
                total_cost += size[u] * lc
                lc += 1
                root_left.append(u)
            else:
                total_cost += size[u] * rc
                rc += 1
                root_right.append(u)

        if total_cost > budget:
            return total_cost, None

        result = []
        root_items = []
        for u in root_left:
            root_items.append((0, u, True))
        root_items.append((1, root, False))
        for u in reversed(root_right):
            root_items.append((0, u, False))

        stack = list(reversed(root_items))

        while stack:
            typ, v, rev = stack.pop()
            if typ == 1:
                result.append(v)
                continue

            items = []
            for u in left_children[v]:
                items.append((0, u, True))
            items.append((1, v, False))
            for u in reversed(right_children[v]):
                items.append((0, u, False))

            if rev:
                transformed = []
                for t, x, r in reversed(items):
                    if t == 0:
                        transformed.append((0, x, not r))
                    else:
                        transformed.append((1, x, False))
                items = transformed

            for item in reversed(items):
                stack.append(item)

        positions = [0] * n
        for i, v in enumerate(result, 1):
            positions[v] = i

        return total_cost, positions

    best_cost = None
    best_positions = None

    for root in centroids:
        cost, positions = solve(root)
        if best_cost is None or cost < best_cost:
            best_cost = cost
            best_positions = positions

    if best_cost is None or best_cost > budget:
        print("NO")
    else:
        print("YES")
        print(*best_positions)

if __name__ == "__main__":
    main()