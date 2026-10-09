import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m, k = data[0], data[1], data[2]
    graph = [0] * n

    p = 3
    for _ in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        graph[u] |= 1 << v
        graph[v] |= 1 << u

    if k == 1:
        print("YES")
        print(1)
        return

    full = (1 << n) - 1
    complement = [
        full & ~(graph[v] | (1 << v))
        for v in range(n)
    ]

    # Relabel vertices by decreasing degree in the complement graph.
    original = sorted(range(n), key=lambda v: complement[v].bit_count(), reverse=True)
    position = [0] * n
    for new_v, old_v in enumerate(original):
        position[old_v] = new_v

    adj = [0] * n
    for new_v, old_v in enumerate(original):
        mask = complement[old_v]
        new_mask = 0
        while mask:
            bit = mask & -mask
            old_u = bit.bit_length() - 1
            new_mask |= 1 << position[old_u]
            mask ^= bit
        adj[new_v] = new_mask

    # Fast greedy attempts.
    for start in range(n):
        clique = [start]
        candidates = adj[start]
        while candidates and len(clique) < k:
            scan = candidates
            best_v = -1
            best_degree = -1
            while scan:
                bit = scan & -scan
                v = bit.bit_length() - 1
                degree = (adj[v] & candidates).bit_count()
                if degree > best_degree:
                    best_degree = degree
                    best_v = v
                scan ^= bit
            clique.append(best_v)
            candidates &= adj[best_v]

        if len(clique) == k:
            answer = [original[v] + 1 for v in clique]
            print("YES")
            print(*answer)
            return

    path = []
    solution = None

    def expand(candidates):
        nonlocal solution

        need = k - len(path)
        if candidates.bit_count() < need:
            return False

        order = []
        bounds = []
        remaining = candidates
        color = 0

        # Greedy coloring gives an upper bound on any clique.
        while remaining:
            color += 1
            available = remaining
            while available:
                bit = available & -available
                v = bit.bit_length() - 1
                order.append(v)
                bounds.append(color)
                remaining ^= bit
                available ^= bit
                available &= ~adj[v]

        current_candidates = candidates

        for i in range(len(order) - 1, -1, -1):
            if len(path) + bounds[i] < k:
                return False

            v = order[i]
            bit = 1 << v
            path.append(v)

            if len(path) == k:
                solution = path.copy()
                return True

            next_candidates = current_candidates & adj[v]
            if next_candidates.bit_count() >= k - len(path):
                if expand(next_candidates):
                    return True

            path.pop()
            current_candidates ^= bit

        return False

    if expand(full):
        answer = [original[v] + 1 for v in solution]
        print("YES")
        print(*answer)
    else:
        print("NO")

if __name__ == "__main__":
    main()