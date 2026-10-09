import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m, k = data[0], data[1], data[2]

    if k == 1:
        print("YES")
        print(1)
        return

    friends = [0] * n
    pos = 3
    for _ in range(m):
        u = data[pos] - 1
        v = data[pos + 1] - 1
        pos += 2
        friends[u] |= 1 << v
        friends[v] |= 1 << u

    full = (1 << n) - 1
    compatible = [
        full & ~(friends[v] | (1 << v))
        for v in range(n)
    ]

    # Every vertex of a k-clique must belong to the (k-1)-core.
    active = full
    required_degree = k - 1

    while True:
        new_active = active
        bits = active
        while bits:
            bit = bits & -bits
            v = bit.bit_length() - 1
            bits ^= bit
            if (compatible[v] & active).bit_count() < required_degree:
                new_active ^= bit
        if new_active == active:
            break
        active = new_active
        if active.bit_count() < k:
            print("NO")
            return

    if active.bit_count() < k:
        print("NO")
        return

    vertices = []
    bits = active
    while bits:
        bit = bits & -bits
        v = bit.bit_length() - 1
        bits ^= bit
        vertices.append(v)

    vertices.sort(key=lambda v: (compatible[v] & active).bit_count())
    size = len(vertices)
    old_to_new = {v: i for i, v in enumerate(vertices)}

    adjacency = [0] * size
    for i, old_v in enumerate(vertices):
        neighbors = compatible[old_v] & active
        mask = 0
        while neighbors:
            bit = neighbors & -neighbors
            old_u = bit.bit_length() - 1
            neighbors ^= bit
            mask |= 1 << old_to_new[old_u]
        adjacency[i] = mask

    sys.setrecursionlimit(10000)

    def color_sort(candidates):
        order = []
        bounds = []
        remaining = candidates
        color = 0

        while remaining:
            color += 1
            available = remaining
            while available:
                bit = available & -available
                v = bit.bit_length() - 1

                order.append(v)
                bounds.append(color)

                remaining ^= bit
                available &= ~(bit | adjacency[v])

        return order, bounds

    def search(candidates, depth, selected):
        if depth + candidates.bit_count() < k:
            return 0

        order, bounds = color_sort(candidates)

        for i in range(len(order) - 1, -1, -1):
            if depth + bounds[i] < k:
                return 0

            v = order[i]
            bit = 1 << v
            new_selected = selected | bit

            if depth + 1 == k:
                return new_selected

            new_candidates = candidates & adjacency[v]
            if new_candidates.bit_count() >= k - depth - 1:
                result = search(new_candidates, depth + 1, new_selected)
                if result:
                    return result

            candidates ^= bit

        return 0

    result = search((1 << size) - 1, 0, 0)

    if not result:
        print("NO")
        return

    answer = []
    while result:
        bit = result & -result
        i = bit.bit_length() - 1
        result ^= bit
        answer.append(vertices[i] + 1)

    answer.sort()
    print("YES")
    print(*answer)

if __name__ == "__main__":
    main()