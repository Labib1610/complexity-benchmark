import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m, k = data[0], data[1], data[2]
    full = (1 << n) - 1
    adj = [full ^ (1 << i) for i in range(n)]

    p = 3
    for _ in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        adj[u] &= ~(1 << v)
        adj[v] &= ~(1 << u)

    if k == 1:
        print("YES")
        print(1)
        return

    order = sorted(range(n), key=lambda x: adj[x].bit_count())
    position = [0] * n
    for i, v in enumerate(order):
        position[v] = i

    new_adj = [0] * n
    for i, old_v in enumerate(order):
        mask = adj[old_v]
        transformed = 0
        while mask:
            bit = mask & -mask
            old_u = bit.bit_length() - 1
            transformed |= 1 << position[old_u]
            mask ^= bit
        new_adj[i] = transformed
    adj = new_adj

    # Fast greedy attempts often find a valid clique immediately.
    for start in range(n):
        clique = [start]
        candidates = adj[start]
        while len(clique) < k and candidates:
            cm = candidates
            best_v = -1
            best_degree = -1
            while cm:
                bit = cm & -cm
                v = bit.bit_length() - 1
                degree = (adj[v] & candidates).bit_count()
                if degree > best_degree:
                    best_degree = degree
                    best_v = v
                cm ^= bit
            clique.append(best_v)
            candidates &= adj[best_v]

        if len(clique) >= k:
            answer = [order[v] + 1 for v in clique[:k]]
            print("YES")
            print(*answer)
            return

    path = []
    target = k

    def expand(candidates):
        remaining = candidates
        vertices = []
        colors = []
        color = 0

        while remaining:
            color += 1
            available = remaining
            while available:
                bit = available & -available
                v = bit.bit_length() - 1
                vertices.append(v)
                colors.append(color)

                remaining ^= bit
                available ^= bit
                available &= ~adj[v]

        depth = len(path)
        for i in range(len(vertices) - 1, -1, -1):
            if depth + colors[i] < target:
                return False

            v = vertices[i]
            bit = 1 << v
            path.append(v)

            if depth + 1 == target:
                return True

            next_candidates = candidates & adj[v]
            if next_candidates and expand(next_candidates):
                return True

            path.pop()
            candidates ^= bit

        return False

    if expand((1 << n) - 1):
        answer = [order[v] + 1 for v in path]
        print("YES")
        print(*answer)
    else:
        print("NO")

if __name__ == "__main__":
    main()