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

    # Find a centroid to use as the central root.
    parent0 = [-1] * n
    order0 = [0]
    for v in order0:
        for u in graph[v]:
            if u != parent0[v]:
                parent0[u] = v
                order0.append(u)

    subtree0 = [1] * n
    for v in reversed(order0):
        if parent0[v] != -1:
            subtree0[parent0[v]] += subtree0[v]

    centroid = 0
    best_part = n + 1
    for v in range(n):
        largest = n - subtree0[v]
        for u in graph[v]:
            if parent0[u] == v:
                largest = max(largest, subtree0[u])
        if largest < best_part:
            best_part = largest
            centroid = v

    # Root the tree at the centroid.
    parent = [-1] * n
    order = [centroid]
    for v in order:
        for u in graph[v]:
            if u != parent[v]:
                parent[u] = v
                order.append(u)

    size = [1] * n
    anchored_cost = [0] * n
    children_sorted = [[] for _ in range(n)]
    anchored_left = [set() for _ in range(n)]

    for v in reversed(order):
        children = [u for u in graph[v] if parent[u] == v]
        children.sort(key=lambda x: size[x], reverse=True)
        children_sorted[v] = children

        total = 1
        base = 1  # Distance from the external anchor to v.
        effective_left = 1  # The external anchor acts as one left item.
        right_count = 0
        left_set = anchored_left[v]

        for u in children:
            s = size[u]
            total += s
            base += anchored_cost[u]

            if effective_left <= right_count:
                base += s * effective_left
                effective_left += 1
                left_set.add(u)
            else:
                base += s * right_count
                right_count += 1

        size[v] = total
        anchored_cost[v] = base

    # Unanchored arrangement at the centroid.
    root_left = set()
    left_count = 0
    right_count = 0
    root_cost = 0

    for u in children_sorted[centroid]:
        root_cost += anchored_cost[u]
        s = size[u]
        if left_count <= right_count:
            root_cost += s * left_count
            left_count += 1
            root_left.add(u)
        else:
            root_cost += s * right_count
            right_count += 1

    if root_cost > budget:
        print("NO")
        return

    # Generate the arrangement iteratively.
    arrangement = []
    stack = [(centroid, 0, True)]  # (vertex, orientation, is_root)

    while stack:
        v, orientation, is_root = stack.pop()
        children = children_sorted[v]
        left_set = root_left if is_root else anchored_left[v]

        left_desc = [u for u in children if u in left_set]
        right_desc = [u for u in children if u not in left_set]

        segments = []
        if orientation == 0:
            # Left blocks: far to near, then v, then right blocks: near to far.
            for u in left_desc:
                segments.append((u, 1, False))
            segments.append(v)
            for u in reversed(right_desc):
                segments.append((u, 0, False))
        else:
            # Reverse of the canonical orientation.
            for u in right_desc:
                segments.append((u, 1, False))
            segments.append(v)
            for u in reversed(left_desc):
                segments.append((u, 0, False))

        for item in reversed(segments):
            if isinstance(item, int):
                stack.append((~item, 0, False))
            else:
                stack.append(item)

        while stack and stack[-1][0] < 0:
            encoded, _, _ = stack.pop()
            arrangement.append(~encoded)

    position = [0] * n
    for i, v in enumerate(arrangement, 1):
        position[v] = i

    actual_cost = 0
    for v in range(n):
        for u in graph[v]:
            if v < u:
                actual_cost += abs(position[v] - position[u])

    if actual_cost > budget:
        print("NO")
    else:
        print("YES")
        print(*position)

if __name__ == "__main__":
    main()