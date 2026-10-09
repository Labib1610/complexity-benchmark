import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m, k = data[0], data[1], data[2]
    conflict = [0] * n

    pos = 3
    for _ in range(m):
        u = data[pos] - 1
        v = data[pos + 1] - 1
        pos += 2
        conflict[u] |= 1 << v
        conflict[v] |= 1 << u

    if k == 1:
        print("YES")
        print(1)
        return

    full = (1 << n) - 1
    compatibility = [
        full & ~(1 << i) & ~conflict[i]
        for i in range(n)
    ]

    # Put lower-degree vertices first; reverse coloring order then tends to
    # branch on higher-degree vertices first.
    perm = sorted(range(n), key=lambda x: compatibility[x].bit_count())
    old_to_new = [0] * n
    for new, old in enumerate(perm):
        old_to_new[old] = new

    adj = [0] * n
    for new_u, old_u in enumerate(perm):
        mask = compatibility[old_u]
        new_mask = 0
        while mask:
            bit = mask & -mask
            old_v = bit.bit_length() - 1
            new_mask |= 1 << old_to_new[old_v]
            mask ^= bit
        adj[new_u] = new_mask

    # Fast greedy attempts before exact search.
    for start in range(n):
        clique = [start]
        candidates = adj[start]
        while len(clique) < k and candidates:
            q = candidates
            best_v = -1
            best_degree = -1
            while q:
                bit = q & -q
                v = bit.bit_length() - 1
                degree = (adj[v] & candidates).bit_count()
                if degree > best_degree:
                    best_degree = degree
                    best_v = v
                q ^= bit
            clique.append(best_v)
            candidates &= adj[best_v]

        if len(clique) >= k:
            answer = [perm[v] + 1 for v in clique[:k]]
            print("YES")
            print(*answer)
            return

    path = []
    solution = None

    def expand(candidates, depth):
        nonlocal solution

        need = k - depth
        if candidates.bit_count() < need:
            return False

        order = []
        bounds = []
        remaining = candidates
        color = 0

        # Greedy coloring: every color class is an independent set in the
        # compatibility graph, hence the number of colors is a clique bound.
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

        for i in range(len(order) - 1, -1, -1):
            if depth + bounds[i] < k:
                return False

            v = order[i]
            bit = 1 << v

            path.append(v)
            if depth + 1 == k:
                solution = path.copy()
                return True

            next_candidates = candidates & adj[v]
            if next_candidates.bit_count() >= k - depth - 1:
                if expand(next_candidates, depth + 1):
                    return True
            path.pop()

            candidates ^= bit

        return False

    if expand((1 << n) - 1, 0):
        answer = [perm[v] + 1 for v in solution]
        print("YES")
        print(*answer)
    else:
        print("NO")

if __name__ == "__main__":
    main()