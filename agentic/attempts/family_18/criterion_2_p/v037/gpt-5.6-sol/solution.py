import sys
from array import array
from collections import deque


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m, budget = data[0], data[1], data[2]
    graph = [[] for _ in range(n)]
    adj_mask = [0] * n

    idx = 3
    edges = []
    for _ in range(m):
        u = data[idx] - 1
        v = data[idx + 1] - 1
        idx += 2
        graph[u].append(v)
        graph[v].append(u)
        adj_mask[u] |= 1 << v
        adj_mask[v] |= 1 << u
        edges.append((u, v))

    if n == 1:
        if budget >= 0:
            print("YES")
            print(1)
        else:
            print("NO")
        return

    if budget < n - 1:
        print("NO")
        return

    degree_lb_sum = 0
    for g in graph:
        d = len(g)
        k = d // 2
        if d & 1:
            degree_lb_sum += (k + 1) * (k + 1)
        else:
            degree_lb_sum += k * (k + 1)

    if (degree_lb_sum + 1) // 2 > budget:
        print("NO")
        return

    def cost_and_positions(order):
        pos = [0] * n
        for p, v in enumerate(order, 1):
            pos[v] = p
        total = 0
        for u, v in edges:
            total += abs(pos[u] - pos[v])
            if total > budget:
                return total, pos
        return total, pos

    def emit(order):
        _, pos = cost_and_positions(order)
        print("YES")
        print(*pos)

    # Paths have the obvious optimal arrangement.
    if max(map(len, graph)) <= 2:
        start = next(i for i in range(n) if len(graph[i]) <= 1)
        order = []
        prev = -1
        cur = start
        while cur != -1:
            order.append(cur)
            nxt = -1
            for w in graph[cur]:
                if w != prev:
                    nxt = w
                    break
            prev, cur = cur, nxt
        if n - 1 <= budget:
            emit(order)
        else:
            print("NO")
        return

    # Exact optimal arrangement for a star.
    center = max(range(n), key=lambda x: len(graph[x]))
    if len(graph[center]) == n - 1:
        leaves = graph[center]
        left_count = len(leaves) // 2
        order = leaves[:left_count] + [center] + leaves[left_count:]
        total, _ = cost_and_positions(order)
        if total <= budget:
            emit(order)
        else:
            print("NO")
        return

    # Quickly accept easy YES instances before running the exact subset DP.
    candidates = [list(range(n)), list(reversed(range(n)))]
    roots = [0, center]
    leaf = next((i for i in range(n) if len(graph[i]) == 1), 0)
    roots.append(leaf)

    for root in dict.fromkeys(roots):
        for mode in range(3):
            parent = [-1] * n
            order = []
            stack = [root]
            parent[root] = root
            while stack:
                v = stack.pop()
                order.append(v)
                children = [w for w in graph[v] if parent[w] == -1]
                if mode == 1:
                    children.sort(key=lambda x: len(graph[x]))
                elif mode == 2:
                    children.sort(key=lambda x: len(graph[x]), reverse=True)
                for w in reversed(children):
                    parent[w] = v
                    stack.append(w)
            if len(order) == n:
                candidates.append(order)

        seen = [False] * n
        seen[root] = True
        q = deque([root])
        bfs = []
        while q:
            v = q.popleft()
            bfs.append(v)
            for w in graph[v]:
                if not seen[w]:
                    seen[w] = True
                    q.append(w)
        candidates.append(bfs)

    for order in candidates:
        total, _ = cost_and_positions(order)
        if total <= budget:
            emit(order)
            return

    # dp[S] is the minimum sum of cut sizes after placing exactly S.
    # Adding S as the current prefix contributes cut(S).
    size = 1 << n
    inf = budget + 1

    if inf <= 0xFFFFFFFF:
        dp = array('I', [0]) * size
    else:
        dp = array('Q', [0]) * size

    if n <= 255:
        cuts = array('B', [0]) * size
    elif n <= 65535:
        cuts = array('H', [0]) * size
    else:
        cuts = array('I', [0]) * size

    dp[0] = 0

    for mask in range(1, size):
        bit = mask & -mask
        v = bit.bit_length() - 1
        rest = mask ^ bit
        cut = cuts[rest] + len(graph[v]) - 2 * ((adj_mask[v] & rest).bit_count())
        cuts[mask] = cut

        best = inf
        bits = mask
        while bits:
            b = bits & -bits
            val = dp[mask ^ b]
            if val < best:
                best = val
            bits ^= b

        value = best + cut
        if value > inf:
            value = inf
        dp[mask] = value

    full = size - 1
    if dp[full] > budget:
        print("NO")
        return

    reverse_order = []
    mask = full
    while mask:
        target = dp[mask] - cuts[mask]
        bits = mask
        chosen = 0
        while bits:
            b = bits & -bits
            if dp[mask ^ b] == target:
                chosen = b
                break
            bits ^= b
        v = chosen.bit_length() - 1
        reverse_order.append(v)
        mask ^= chosen

    order = reverse_order[::-1]
    emit(order)


if __name__ == "__main__":
    main()