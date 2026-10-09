import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m, k = data[0], data[1], data[2]
    reactive = [0] * n

    p = 3
    for _ in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        reactive[u] |= 1 << v
        reactive[v] |= 1 << u

    if k == 1:
        print("YES")
        print(1)
        return

    full_old = (1 << n) - 1
    compatible_old = [
        full_old & ~(reactive[i] | (1 << i))
        for i in range(n)
    ]

    vertex_order = sorted(
        range(n),
        key=lambda v: compatible_old[v].bit_count()
    )
    new_index = [0] * n
    for i, v in enumerate(vertex_order):
        new_index[v] = i

    adj = [0] * n
    for i, old_v in enumerate(vertex_order):
        mask = compatible_old[old_v]
        new_mask = 0
        while mask:
            bit = mask & -mask
            old_u = bit.bit_length() - 1
            new_mask |= 1 << new_index[old_u]
            mask ^= bit
        adj[i] = new_mask

    full = (1 << n) - 1

    def greedy(start):
        if start < 0:
            chosen = []
            candidates = full
        else:
            chosen = [start]
            candidates = adj[start]

        while candidates and len(chosen) < k:
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
            chosen.append(best_v)
            candidates &= adj[best_v]

        return chosen if len(chosen) >= k else None

    result = greedy(-1)
    if result is None:
        for v in range(n - 1, -1, -1):
            result = greedy(v)
            if result is not None:
                break

    if result is not None:
        answer = [vertex_order[v] + 1 for v in result[:k]]
        print("YES")
        print(*answer)
        return

    sys.setrecursionlimit(10000)
    path = []
    answer = None

    def expand(candidates):
        nonlocal answer

        depth = len(path)
        need = k - depth
        if candidates.bit_count() < need:
            return False

        order = []
        colors = []
        remaining = candidates
        color = 0

        while remaining:
            color += 1
            same_color = remaining
            while same_color:
                bit = same_color & -same_color
                v = bit.bit_length() - 1
                order.append(v)
                colors.append(color)

                remaining ^= bit
                same_color ^= bit
                same_color &= ~adj[v]

        if color < need:
            return False

        for i in range(len(order) - 1, -1, -1):
            if depth + colors[i] < k:
                return False

            v = order[i]
            bit = 1 << v
            path.append(v)

            if depth + 1 == k:
                answer = path.copy()
                return True

            next_candidates = candidates & adj[v]
            if next_candidates.bit_count() >= k - depth - 1:
                if expand(next_candidates):
                    return True

            path.pop()
            candidates ^= bit

        return False

    if expand(full):
        output = [vertex_order[v] + 1 for v in answer]
        print("YES")
        print(*output)
    else:
        print("NO")

if __name__ == "__main__":
    main()