import sys
from array import array

def output_yes(position):
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, position)))

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m, budget = data[0], data[1], data[2]
    adj = [0] * n
    graph = [[] for _ in range(n)]
    edges = []

    p = 3
    for _ in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        graph[u].append(v)
        graph[v].append(u)
        edges.append((u, v))

    if n == 1:
        if budget >= 0:
            output_yes([1])
        else:
            print("NO")
        return

    if budget < m:
        print("NO")
        return

    identity_cost = sum(abs(u - v) for u, v in edges)
    if identity_cost <= budget:
        output_yes(list(range(1, n + 1)))
        return

    # A quick tree traversal arrangement may avoid the exponential DP
    # when the budget is generous.
    root = max(range(n), key=lambda x: len(graph[x]))
    order = []
    stack = [(root, -1)]
    while stack:
        v, parent = stack.pop()
        order.append(v)
        for to in reversed(graph[v]):
            if to != parent:
                stack.append((to, v))

    if len(order) == n:
        traversal_pos = [0] * n
        for i, v in enumerate(order, 1):
            traversal_pos[v] = i
        traversal_cost = sum(
            abs(traversal_pos[u] - traversal_pos[v]) for u, v in edges
        )
        if traversal_cost <= budget:
            output_yes(traversal_pos)
            return

    size = 1 << n
    cuts = array('I', [0]) * size
    dp = array('I', [0]) * size
    degrees = [len(g) for g in graph]
    upper_bound = m * (n - 1)
    inf = upper_bound + 1

    for mask in range(1, size):
        bit = mask & -mask
        v = bit.bit_length() - 1
        rest = mask ^ bit

        cut = cuts[rest] + degrees[v] - 2 * ((adj[v] & rest).bit_count())
        cuts[mask] = cut

        best = inf
        x = mask
        while x:
            b = x & -x
            value = dp[mask ^ b]
            if value < best:
                best = value
            x ^= b

        value = best + cut
        dp[mask] = value if value <= upper_bound else inf

    full = size - 1
    if dp[full] > budget:
        print("NO")
        return

    position = [0] * n
    mask = full
    slot = n

    while mask:
        target = dp[mask] - cuts[mask]
        x = mask
        while x:
            bit = x & -x
            if dp[mask ^ bit] == target:
                v = bit.bit_length() - 1
                position[v] = slot
                slot -= 1
                mask ^= bit
                break
            x ^= bit

    output_yes(position)

if __name__ == "__main__":
    main()