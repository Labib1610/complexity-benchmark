import sys
from array import array

def arrangement_cost(order, adj):
    pos = [0] * len(order)
    for i, v in enumerate(order):
        pos[v] = i
    total = 0
    for u in range(len(adj)):
        for v in adj[u]:
            if u < v:
                total += abs(pos[u] - pos[v])
    return total, pos

def centroid_arrangement(adj):
    n = len(adj)
    removed = [False] * n
    parent = [-1] * n
    subtree = [0] * n

    def solve(start):
        parent[start] = -1
        stack = [start]
        nodes = []

        while stack:
            u = stack.pop()
            nodes.append(u)
            for v in adj[u]:
                if not removed[v] and v != parent[u]:
                    parent[v] = u
                    stack.append(v)

        total = len(nodes)
        for u in reversed(nodes):
            size = 1
            for v in adj[u]:
                if not removed[v] and parent[v] == u:
                    size += subtree[v]
            subtree[u] = size

        centroid = nodes[0]
        for u in nodes:
            largest = total - subtree[u]
            for v in adj[u]:
                if not removed[v] and parent[v] == u:
                    if subtree[v] > largest:
                        largest = subtree[v]
            if largest * 2 <= total:
                centroid = u
                break

        removed[centroid] = True
        blocks = []
        for neighbor in adj[centroid]:
            if not removed[neighbor]:
                seq = solve(neighbor)
                blocks.append((len(seq), seq, neighbor))

        blocks.sort(key=lambda item: item[0], reverse=True)
        left = []
        right = []
        left_size = 0
        right_size = 0

        for block in blocks:
            if left_size <= right_size:
                left.append(block)
                left_size += block[0]
            else:
                right.append(block)
                right_size += block[0]

        left.sort(key=lambda item: item[0], reverse=True)
        right.sort(key=lambda item: item[0])

        result = []
        for _, seq, neighbor in left:
            idx = seq.index(neighbor)
            if idx < len(seq) - 1 - idx:
                seq.reverse()
            result.extend(seq)

        result.append(centroid)

        for _, seq, neighbor in right:
            idx = seq.index(neighbor)
            if idx > len(seq) - 1 - idx:
                seq.reverse()
            result.extend(seq)

        return result

    return solve(0)

def exact_arrangement(adj, budget):
    n = len(adj)
    states = 1 << n
    cuts = bytearray(states)
    adjacency_masks = [0] * n
    degrees = [0] * n

    for u in range(n):
        mask = 0
        for v in adj[u]:
            mask |= 1 << v
        adjacency_masks[u] = mask
        degrees[u] = len(adj[u])

    for mask in range(1, states):
        bit = mask & -mask
        v = bit.bit_length() - 1
        rest = mask ^ bit
        cuts[mask] = (
            cuts[rest]
            + degrees[v]
            - 2 * ((adjacency_masks[v] & rest).bit_count())
        )

    INF = 0xFFFFFFFF
    dp = array('I', [INF]) * states
    dp[0] = 0

    second_bit = 2 if n >= 2 else 0

    for mask in range(1, states):
        # By reversal symmetry, restrict workstation 0 to occur before 1.
        if second_bit and (mask & second_bit) and not (mask & 1):
            continue

        remaining = mask
        best = INF
        while remaining:
            bit = remaining & -remaining
            value = dp[mask ^ bit]
            if value < best:
                best = value
            remaining ^= bit

        if best != INF:
            dp[mask] = best + cuts[mask]

    full = states - 1
    if dp[full] > budget:
        return None

    positions = [0] * n
    mask = full
    slot = n

    while mask:
        target = dp[mask] - cuts[mask]
        remaining = mask
        chosen = 0
        while remaining:
            bit = remaining & -remaining
            if dp[mask ^ bit] == target:
                chosen = bit
                break
            remaining ^= bit

        v = chosen.bit_length() - 1
        positions[v] = slot
        slot -= 1
        mask ^= chosen

    return positions

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m, budget = data[0], data[1], data[2]
    adj = [[] for _ in range(n)]
    index = 3

    for _ in range(m):
        u = data[index] - 1
        v = data[index + 1] - 1
        index += 2
        adj[u].append(v)
        adj[v].append(u)

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

    heuristic_order = centroid_arrangement(adj)
    heuristic_cost, heuristic_positions = arrangement_cost(heuristic_order, adj)

    if heuristic_cost <= budget:
        print("YES")
        print(*[p + 1 for p in heuristic_positions])
        return

    # Exact subset dynamic programming for the intended small instances.
    if n <= 22:
        positions = exact_arrangement(adj, budget)
        if positions is None:
            print("NO")
        else:
            print("YES")
            print(*positions)
        return

    print("NO")

if __name__ == "__main__":
    main()