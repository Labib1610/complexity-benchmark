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

    # Fast greedy attempt.
    candidates = (1 << n) - 1
    greedy = []
    while candidates:
        x = candidates
        best_v = -1
        best_deg = n + 1
        while x:
            bit = x & -x
            v = bit.bit_length() - 1
            d = (friendship[v] & candidates).bit_count()
            if d < best_deg:
                best_deg = d
                best_v = v
            x ^= bit

        greedy.append(best_v)
        candidates &= ~(friendship[best_v] | (1 << best_v))

    if len(greedy) >= k:
        ans = [v + 1 for v in greedy[:k]]
        sys.stdout.write("YES\n" + " ".join(map(str, ans)) + "\n")
        return

    # Put higher-degree vertices in the searched half.
    order = sorted(range(n), key=lambda v: friendship[v].bit_count(), reverse=True)
    position = [0] * n
    for i, v in enumerate(order):
        position[v] = i

    graph = [0] * n
    for i, old_v in enumerate(order):
        mask = friendship[old_v]
        new_mask = 0
        while mask:
            bit = mask & -mask
            old_u = bit.bit_length() - 1
            new_mask |= 1 << position[old_u]
            mask ^= bit
        graph[i] = new_mask

    def clique_cover_bound(mask, adj):
        # Partition into friendship cliques. An independent set takes at most
        # one vertex from each clique.
        count = 0
        remaining = mask
        while remaining:
            count += 1
            possible = remaining
            while possible:
                bit = possible & -possible
                v = bit.bit_length() - 1
                remaining ^= bit
                possible &= adj[v] & remaining
        return count

    all_mask = (1 << n) - 1
    if clique_cover_bound(all_mask, graph) < k:
        sys.stdout.write("NO\n")
        return

    right_size = n // 2
    left_size = n - right_size

    full_left = (1 << left_size) - 1
    full_right = (1 << right_size) - 1

    left_friend = [graph[i] & full_left for i in range(left_size)]
    right_allowed_after_select = [0] * right_size

    for j in range(right_size):
        right_friends = (graph[left_size + j] >> left_size) & full_right
        right_allowed_after_select[j] = full_right ^ right_friends

    cross_allowed = [0] * left_size
    for i in range(left_size):
        right_friends = (graph[i] >> left_size) & full_right
        cross_allowed[i] = full_right ^ right_friends

    # best[mask] = maximum independent-set size inside the right-half mask.
    size = 1 << right_size
    best = bytearray(size)
    allowed = right_allowed_after_select

    for mask in range(1, size):
        bit = mask & -mask
        rest = mask ^ bit
        v = bit.bit_length() - 1

        without_v = best[rest]
        with_v = best[rest & allowed[v]] + 1
        best[mask] = with_v if with_v > without_v else without_v

    answer_left = None
    answer_right_mask = 0
    selected = []

    def cover_left(mask):
        count = 0
        remaining = mask
        while remaining:
            count += 1
            possible = remaining
            while possible:
                bit = possible & -possible
                v = bit.bit_length() - 1
                remaining ^= bit
                possible &= left_friend[v] & remaining
        return count

    def cover_combined(left_mask, right_mask):
        remaining = left_mask | (right_mask << left_size)
        count = 0
        while remaining:
            count += 1
            possible = remaining
            while possible:
                bit = possible & -possible
                v = bit.bit_length() - 1
                remaining ^= bit
                possible &= graph[v] & remaining
        return count

    sys.setrecursionlimit(10000)

    def search(avail_left, avail_right, chosen_count):
        nonlocal answer_left, answer_right_mask

        right_best = best[avail_right]
        if chosen_count + right_best >= k:
            answer_left = selected.copy()
            answer_right_mask = avail_right
            return True

        if not avail_left:
            return False

        if chosen_count + avail_left.bit_count() + right_best < k:
            return False

        left_bound = cover_left(avail_left)
        if chosen_count + left_bound + right_best < k:
            return False

        if chosen_count + cover_combined(avail_left, avail_right) < k:
            return False

        bit = avail_left & -avail_left
        v = bit.bit_length() - 1
        rest = avail_left ^ bit

        # Include v.
        selected.append(v)
        next_left = rest & ~left_friend[v]
        next_right = avail_right & cross_allowed[v]
        if search(next_left, next_right, chosen_count + 1):
            return True
        selected.pop()

        # Exclude v.
        if search(rest, avail_right, chosen_count):
            return True

        return False

    if not search(full_left, full_right, 0):
        sys.stdout.write("NO\n")
        return

    need = k - len(answer_left)
    right_vertices = []
    mask = answer_right_mask

    while need > 0 and mask:
        bit = mask & -mask
        rest = mask ^ bit
        v = bit.bit_length() - 1

        without_v = best[rest]
        with_v = best[rest & allowed[v]] + 1

        if with_v > without_v:
            right_vertices.append(left_size + v)
            need -= 1
            mask = rest & allowed[v]
        else:
            mask = rest

    chosen_reordered = answer_left + right_vertices
    result = [order[v] + 1 for v in chosen_reordered[:k]]

    sys.stdout.write("YES\n" + " ".join(map(str, result)) + "\n")


if __name__ == "__main__":
    main()