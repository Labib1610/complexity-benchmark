import sys
from array import array
from collections import deque
import random

def arrangement_cost(order, edges, n):
    pos = [0] * n
    for i, v in enumerate(order):
        pos[v] = i
    return sum(abs(pos[u] - pos[v]) for u, v in edges)

def exact_solve(n, adjmask):
    total = 1 << n
    inf = 10**18

    cuts = array('b', [0]) * total
    dp = array('q', [inf]) * total
    choice = array('b', [-1]) * total
    degrees = [adjmask[i].bit_count() for i in range(n)]
    dp[0] = 0

    for mask in range(1, total):
        bit = mask & -mask
        v = bit.bit_length() - 1
        prev = mask ^ bit
        cuts[mask] = cuts[prev] + degrees[v] - 2 * ((adjmask[v] & prev).bit_count())

        best = inf
        best_v = -1
        bits = mask
        while bits:
            b = bits & -bits
            u = b.bit_length() - 1
            value = dp[mask ^ b]
            if value < best:
                best = value
                best_v = u
            bits ^= b

        dp[mask] = best + cuts[mask]
        choice[mask] = best_v

    mask = total - 1
    reverse_order = []
    while mask:
        v = choice[mask]
        reverse_order.append(v)
        mask ^= 1 << v
    reverse_order.reverse()
    return dp[total - 1], reverse_order

def rooted_data(root, adj):
    n = len(adj)
    parent = [-1] * n
    order = [root]
    for v in order:
        for u in adj[v]:
            if u != parent[v]:
                parent[u] = v
                order.append(u)

    size = [1] * n
    children = [[] for _ in range(n)]
    for v in reversed(order):
        p = parent[v]
        if p != -1:
            size[p] += size[v]
            children[p].append(v)

    for v in range(n):
        children[v].sort(key=lambda x: (size[x], x))
    return parent, size, children

def subtree_preorder(start, children, reverse_sort=False):
    result = []
    stack = [start]
    while stack:
        v = stack.pop()
        result.append(v)
        ch = children[v]
        if reverse_sort:
            stack.extend(ch)
        else:
            stack.extend(reversed(ch))
    return result

def projective_order(root, adj, tie_flip=False):
    _, size, children = rooted_data(root, adj)
    left = []
    right = []
    left_sum = 0
    right_sum = 0

    root_children = children[root][:]
    root_children.sort(key=lambda x: (size[x], x))

    for c in root_children:
        if left_sum < right_sum or (left_sum == right_sum and tie_flip):
            left.append(c)
            left_sum += size[c]
        else:
            right.append(c)
            right_sum += size[c]

    result = []
    for c in reversed(left):
        part = subtree_preorder(c, children)
        result.extend(reversed(part))
    result.append(root)
    for c in right:
        result.extend(subtree_preorder(c, children))
    return result

def dfs_order(root, adj, descending=False):
    _, size, children = rooted_data(root, adj)
    for v in range(len(adj)):
        children[v].sort(key=lambda x: (size[x], x), reverse=descending)
    return subtree_preorder(root, children)

def bfs_order(root, adj, degree_first=False):
    n = len(adj)
    parent = [-1] * n
    result = []
    q = deque([root])
    parent[root] = root
    while q:
        v = q.popleft()
        result.append(v)
        nxt = [u for u in adj[v] if parent[u] == -1]
        if degree_first:
            nxt.sort(key=lambda x: (-len(adj[x]), x))
        else:
            nxt.sort()
        for u in nxt:
            parent[u] = v
            q.append(u)
    return result

def improve_order(order, edges, adj, rounds=12):
    n = len(order)
    if n <= 1:
        return order

    pos = [0] * n
    for i, v in enumerate(order):
        pos[v] = i

    def swap_delta(a, b):
        if a == b:
            return 0
        pa, pb = pos[a], pos[b]
        seen = set()
        delta = 0
        for x in (a, b):
            for y in adj[x]:
                e = (x, y) if x < y else (y, x)
                if e in seen:
                    continue
                seen.add(e)
                old = abs(pos[e[0]] - pos[e[1]])
                p0 = pb if e[0] == a else pa if e[0] == b else pos[e[0]]
                p1 = pb if e[1] == a else pa if e[1] == b else pos[e[1]]
                delta += abs(p0 - p1) - old
        return delta

    for _ in range(rounds):
        changed = False
        i = 0
        while i + 1 < n:
            a, b = order[i], order[i + 1]
            if swap_delta(a, b) < 0:
                order[i], order[i + 1] = b, a
                pos[a], pos[b] = i + 1, i
                changed = True
                if i:
                    i -= 1
                    continue
            i += 1
        if not changed:
            break

    rng = random.Random(712367821)
    attempts = min(30 * n, 200000)
    for _ in range(attempts):
        i = rng.randrange(n)
        j = rng.randrange(n)
        if i == j:
            continue
        a, b = order[i], order[j]
        if swap_delta(a, b) < 0:
            order[i], order[j] = b, a
            pos[a], pos[b] = j, i

    return order

def lower_bound(n, adj):
    incidence = 0
    for v in range(n):
        d = len(adj[v])
        q = d // 2
        if d % 2 == 0:
            incidence += q * (q + 1)
        else:
            incidence += (q + 1) * (q + 1)
    return max(n - 1, (incidence + 1) // 2)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m, budget = data[0], data[1], data[2]
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
        if budget >= 0:
            print("YES")
            print(1)
        else:
            print("NO")
        return

    if n <= 21:
        adjmask = [0] * n
        for v in range(n):
            mask = 0
            for u in adj[v]:
                mask |= 1 << u
            adjmask[v] = mask

        optimum, order = exact_solve(n, adjmask)
        if optimum > budget:
            print("NO")
            return

        positions = [0] * n
        for i, v in enumerate(order, 1):
            positions[v] = i
        print("YES")
        print(*positions)
        return

    if lower_bound(n, adj) > budget:
        print("NO")
        return

    _, sizes, _ = rooted_data(0, adj)
    centroid = min(
        range(n),
        key=lambda v: max(
            n - sizes[v],
            max((sizes[u] for u in adj[v] if sizes[u] < sizes[v]), default=0)
        )
    )

    candidates = {0, n - 1, centroid}
    by_degree = sorted(range(n), key=lambda v: (-len(adj[v]), v))
    candidates.update(by_degree[:min(12, n)])

    leaves = [v for v in range(n) if len(adj[v]) <= 1]
    if leaves:
        step = max(1, len(leaves) // 8)
        candidates.update(leaves[::step][:8])

    if n <= 80:
        candidates.update(range(n))
    else:
        rng = random.Random(918273645)
        for _ in range(12):
            candidates.add(rng.randrange(n))

    best_order = list(range(n))
    best_cost = arrangement_cost(best_order, edges, n)

    def consider(order):
        nonlocal best_order, best_cost
        cost = arrangement_cost(order, edges, n)
        if cost < best_cost:
            best_cost = cost
            best_order = order[:]
        return cost <= budget

    for root in candidates:
        generated = [
            projective_order(root, adj, False),
            projective_order(root, adj, True),
            dfs_order(root, adj, False),
            dfs_order(root, adj, True),
            bfs_order(root, adj, False),
            bfs_order(root, adj, True),
        ]
        for order in generated:
            if consider(order):
                positions = [0] * n
                for i, v in enumerate(order, 1):
                    positions[v] = i
                print("YES")
                print(*positions)
                return

    best_order = improve_order(best_order, edges, adj)
    best_cost = arrangement_cost(best_order, edges, n)

    if best_cost <= budget:
        positions = [0] * n
        for i, v in enumerate(best_order, 1):
            positions[v] = i
        print("YES")
        print(*positions)
    else:
        print("NO")

if __name__ == "__main__":
    main()