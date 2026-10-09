import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m, k = data[0], data[1], data[2]
    friendship = [0] * n

    p = 3
    for _ in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        friendship[u] |= 1 << v
        friendship[v] |= 1 << u

    if k == 1:
        print("YES")
        print(1)
        return

    all_mask = (1 << n) - 1

    # Quickly try several minimum-degree greedy constructions.
    starts = [-1] + list(range(n))
    for start in starts:
        candidates = all_mask
        chosen = []

        if start >= 0:
            chosen.append(start)
            candidates &= ~(friendship[start] | (1 << start))

        while candidates and len(chosen) < k:
            x = candidates
            best = -1
            best_degree = n + 1
            while x:
                bit = x & -x
                v = bit.bit_length() - 1
                degree = (friendship[v] & candidates).bit_count()
                if degree < best_degree:
                    best_degree = degree
                    best = v
                x ^= bit

            chosen.append(best)
            candidates &= ~(friendship[best] | (1 << best))

        if len(chosen) >= k:
            print("YES")
            print(*(v + 1 for v in chosen[:k]))
            return

    # An independent set in the original graph is a clique in its complement.
    complement_old = [
        all_mask & ~(friendship[v] | (1 << v))
        for v in range(n)
    ]

    # Static ordering improves greedy coloring and branching.
    order_old = sorted(
        range(n),
        key=lambda v: (complement_old[v].bit_count(), v)
    )
    new_index = [0] * n
    for i, v in enumerate(order_old):
        new_index[v] = i

    adjacency = [0] * n
    for new_v, old_v in enumerate(order_old):
        mask = complement_old[old_v]
        converted = 0
        while mask:
            bit = mask & -mask
            old_u = bit.bit_length() - 1
            converted |= 1 << new_index[old_u]
            mask ^= bit
        adjacency[new_v] = converted

    stack = []
    answer = None

    def expand(candidates, depth):
        nonlocal answer

        if candidates.bit_count() < k - depth:
            return False

        vertices = []
        colors = []
        uncolored = candidates
        color = 0

        # Greedy coloring gives an upper bound on any clique extension.
        while uncolored:
            color += 1
            available = uncolored
            while available:
                bit = available & -available
                v = bit.bit_length() - 1
                vertices.append(v)
                colors.append(color)
                uncolored ^= bit
                available ^= bit
                available &= ~adjacency[v]

        for i in range(len(vertices) - 1, -1, -1):
            if depth + colors[i] < k:
                return False

            v = vertices[i]
            bit = 1 << v

            stack.append(v)
            if depth + 1 == k:
                answer = stack.copy()
                return True

            next_candidates = candidates & adjacency[v]
            if next_candidates.bit_count() >= k - depth - 1:
                if expand(next_candidates, depth + 1):
                    return True

            stack.pop()
            candidates ^= bit

        return False

    if expand((1 << n) - 1, 0):
        result = [order_old[v] + 1 for v in answer]
        print("YES")
        print(*result)
    else:
        print("NO")

if __name__ == "__main__":
    main()