import sys
from functools import lru_cache

sys.setrecursionlimit(1_000_000)
INF = 10**30

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    raise SystemExit

it = iter(data)
n = next(it)
m = next(it)
B = next(it)

graph = [[] for _ in range(n)]
for _ in range(m):
    u = next(it) - 1
    v = next(it) - 1
    graph[u].append(v)
    graph[v].append(u)

if n == 1:
    print("YES")
    print(1)
    raise SystemExit

def partition_cost(sizes, anchored=False):
    sizes = sorted(sizes)
    dp = [0]
    processed = 0

    for s in sizes:
        ndp = [INF] * (processed + s + 1)
        for left_size, value in enumerate(dp):
            if value == INF:
                continue

            # Put this component on the right.
            nv = value + (processed - left_size)
            if nv < ndp[left_size]:
                ndp[left_size] = nv

            # Put this component on the left.
            nx = left_size + s
            nv = value + left_size
            if nv < ndp[nx]:
                ndp[nx] = nv

        dp = ndp
        processed += s

    if anchored:
        return min(value + left_size for left_size, value in enumerate(dp))
    return min(dp)

@lru_cache(maxsize=None)
def message(u, parent):
    children = [v for v in graph[u] if v != parent]
    if not children:
        return 1, 0

    items = []
    base = 0
    total_size = 1

    for v in children:
        child_size, child_anchor = message(v, u)
        items.append(child_size)
        total_size += child_size
        base += child_anchor + 1

    return total_size, base + partition_cost(items, anchored=True)

def root_cost(root):
    sizes = []
    base = 0
    for v in graph[root]:
        child_size, child_anchor = message(v, root)
        sizes.append(child_size)
        base += child_anchor + 1
    return base + partition_cost(sizes, anchored=False)

# For moderate instances, examine every possible top-level root.
# For large instances, centroids and high-degree vertices are the useful
# candidates while avoiding excessive repeated exclusion knapsacks.
if n <= 450:
    candidates = list(range(n))
else:
    parent = [-1] * n
    order = [0]
    for u in order:
        for v in graph[u]:
            if v != parent[u]:
                parent[v] = u
                order.append(v)

    subtree = [1] * n
    for u in reversed(order[1:]):
        subtree[parent[u]] += subtree[u]

    centroid_scores = []
    for u in range(n):
        largest = n - subtree[u]
        for v in graph[u]:
            if parent[v] == u:
                largest = max(largest, subtree[v])
        centroid_scores.append((largest, u))

    candidates = {0}
    for _, u in sorted(centroid_scores)[:8]:
        candidates.add(u)
    for u in sorted(range(n), key=lambda x: len(graph[x]), reverse=True)[:8]:
        candidates.add(u)
    candidates = list(candidates)

best_root = -1
best_cost = INF
for r in candidates:
    value = root_cost(r)
    if value < best_cost:
        best_cost = value
        best_root = r

if best_cost > B:
    print("NO")
    raise SystemExit

def choose_partition(items, anchored):
    # items are (subtree_size, child_vertex)
    items = sorted(items)
    stages = []
    dp = [0]
    processed = 0

    for s, _ in items:
        ndp = [INF] * (processed + s + 1)
        choice = bytearray([255]) * (processed + s + 1)

        for left_size, value in enumerate(dp):
            if value == INF:
                continue

            # Right side.
            nv = value + processed - left_size
            if nv < ndp[left_size]:
                ndp[left_size] = nv
                choice[left_size] = 0

            # Left side.
            nx = left_size + s
            nv = value + left_size
            if nv < ndp[nx]:
                ndp[nx] = nv
                choice[nx] = 1

        stages.append(choice)
        dp = ndp
        processed += s

    if anchored:
        target = min(range(len(dp)), key=lambda x: dp[x] + x)
    else:
        target = min(range(len(dp)), key=lambda x: dp[x])

    sides = [0] * len(items)
    for i in range(len(items) - 1, -1, -1):
        s = items[i][0]
        side = stages[i][target]
        sides[i] = side
        if side == 1:
            target -= s

    left = []
    right = []
    for item, side in zip(items, sides):
        if side == 1:
            left.append(item)
        else:
            right.append(item)

    # Components are processed from nearest to farthest in ascending size.
    # Physical left-to-right order reverses the left side.
    left.reverse()
    return left, right

def build_left_anchored(u, parent):
    items = []
    for v in graph[u]:
        if v != parent:
            size, _ = message(v, u)
            items.append((size, v))

    left, right = choose_partition(items, anchored=True)
    result = []

    for _, v in left:
        child_order = build_left_anchored(v, u)
        child_order.reverse()  # Attachment vertex faces right.
        result.extend(child_order)

    result.append(u)

    for _, v in right:
        result.extend(build_left_anchored(v, u))

    return result

def build_root(root):
    items = []
    for v in graph[root]:
        size, _ = message(v, root)
        items.append((size, v))

    left, right = choose_partition(items, anchored=False)
    result = []

    for _, v in left:
        child_order = build_left_anchored(v, root)
        child_order.reverse()
        result.extend(child_order)

    result.append(root)

    for _, v in right:
        result.extend(build_left_anchored(v, root))

    return result

order = build_root(best_root)
position = [0] * n
for i, vertex in enumerate(order, 1):
    position[vertex] = i

actual_cost = 0
for u in range(n):
    for v in graph[u]:
        if u < v:
            actual_cost += abs(position[u] - position[v])

if actual_cost > B:
    print("NO")
else:
    print("YES")
    print(*position)