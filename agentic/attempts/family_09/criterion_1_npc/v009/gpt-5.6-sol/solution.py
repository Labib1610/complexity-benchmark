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

    friendship = [0] * n
    p = 3
    for _ in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        friendship[u] |= 1 << v
        friendship[v] |= 1 << u

    all_vertices = (1 << n) - 1
    compatible = [
        all_vertices & ~(friendship[v] | (1 << v))
        for v in range(n)
    ]

    # Restrict to the (k-1)-core of the compatibility graph.
    active = all_vertices
    while True:
        removed = 0
        cur = active
        while cur:
            bit = cur & -cur
            v = bit.bit_length() - 1
            cur ^= bit
            if (compatible[v] & active).bit_count() < k - 1:
                removed |= bit
        if not removed:
            break
        active &= ~removed

    if active.bit_count() < k:
        print("NO")
        return

    vertices = []
    cur = active
    while cur:
        bit = cur & -cur
        vertices.append(bit.bit_length() - 1)
        cur ^= bit

    vertices.sort(key=lambda v: (compatible[v] & active).bit_count())

    size = len(vertices)
    old_to_new = {v: i for i, v in enumerate(vertices)}
    adjacency = [0] * size

    for i, old_v in enumerate(vertices):
        mask = compatible[old_v] & active
        new_mask = 0
        while mask:
            bit = mask & -mask
            old_u = bit.bit_length() - 1
            new_mask |= 1 << old_to_new[old_u]
            mask ^= bit
        adjacency[i] = new_mask

    full = (1 << size) - 1

    # Quickly try several greedy cliques.
    starts = sorted(range(size), key=lambda v: adjacency[v].bit_count(), reverse=True)
    for start in starts:
        clique = [start]
        candidates = adjacency[start]
        while candidates and len(clique) < k:
            scan = candidates
            best = -1
            best_score = -1
            while scan:
                bit = scan & -scan
                v = bit.bit_length() - 1
                score = (candidates & adjacency[v]).bit_count()
                if score > best_score:
                    best_score = score
                    best = v
                scan ^= bit
            clique.append(best)
            candidates &= adjacency[best]

        if len(clique) >= k:
            answer = [vertices[v] + 1 for v in clique[:k]]
            print("YES")
            print(*answer)
            return

    path = []
    answer = None
    target = k
    adj = adjacency

    sys.setrecursionlimit(10000)

    def expand(candidates, depth):
        nonlocal answer

        uncolored = candidates
        order = []
        bounds = []
        color = 0

        while uncolored:
            color += 1
            available = uncolored
            while available:
                bit = available & -available
                v = bit.bit_length() - 1
                order.append(v)
                bounds.append(color)

                uncolored ^= bit
                available ^= bit
                available &= ~adj[v]

        for i in range(len(order) - 1, -1, -1):
            if depth + bounds[i] < target:
                return False

            v = order[i]
            bit = 1 << v

            path.append(v)
            if depth + 1 == target:
                answer = path.copy()
                return True

            next_candidates = candidates & adj[v]
            if (next_candidates.bit_count() >= target - depth - 1
                    and expand(next_candidates, depth + 1)):
                return True

            path.pop()
            candidates ^= bit

        return False

    if expand(full, 0):
        result = [vertices[v] + 1 for v in answer]
        print("YES")
        print(*result)
    else:
        print("NO")

if __name__ == "__main__":
    main()