import sys
from array import array


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m, k = data[0], data[1], data[2]
    friends = [0] * n

    pos = 3
    for _ in range(m):
        u = data[pos] - 1
        v = data[pos + 1] - 1
        pos += 2
        friends[u] |= 1 << v
        friends[v] |= 1 << u

    if k == 1:
        print("YES")
        print(1)
        return

    # Try several minimum-degree greedy constructions first.
    starts = [-1] + list(range(n))
    all_vertices = (1 << n) - 1

    for start in starts:
        if start == -1:
            chosen = []
            remaining = all_vertices
        else:
            chosen = [start]
            remaining = all_vertices & ~(1 << start) & ~friends[start]

        while remaining and len(chosen) < k:
            scan = remaining
            best_v = -1
            best_degree = n + 1
            while scan:
                bit = scan & -scan
                v = bit.bit_length() - 1
                degree = (friends[v] & remaining).bit_count()
                if degree < best_degree:
                    best_degree = degree
                    best_v = v
                scan ^= bit

            chosen.append(best_v)
            remaining &= ~(1 << best_v)
            remaining &= ~friends[best_v]

        if len(chosen) >= k:
            print("YES")
            print(" ".join(str(v + 1) for v in chosen[:k]))
            return

    # Meet in the middle.
    left_n = n // 2
    right_n = n - left_n
    left_count = 1 << left_n
    left_full = left_count - 1

    left_non_neighbors = [0] * left_n
    for v in range(left_n):
        left_non_neighbors[v] = left_full & ~friends[v] & ~(1 << v)

    # alpha[mask] is the maximum independent-set size in the left-side mask.
    alpha = bytearray(left_count)
    a = alpha
    non_neighbors = left_non_neighbors

    for mask in range(1, left_count):
        bit = mask & -mask
        v = bit.bit_length() - 1
        rest = mask ^ bit

        without_v = a[rest]
        with_v = 1 + a[rest & non_neighbors[v]]
        a[mask] = with_v if with_v > without_v else without_v

    def reconstruct_left(mask, need):
        result = []
        while mask and need:
            bit = mask & -mask
            v = bit.bit_length() - 1
            rest = mask ^ bit

            if a[mask] == a[rest]:
                mask = rest
            else:
                result.append(v)
                need -= 1
                mask = rest & non_neighbors[v]
        return result

    if a[left_full] >= k:
        answer = reconstruct_left(left_full, k)
        print("YES")
        print(" ".join(str(v + 1) for v in answer))
        return

    right_full = (1 << right_n) - 1
    right_adj = [0] * right_n
    allowed_left = [0] * right_n

    for i in range(right_n):
        v = left_n + i
        right_adj[i] = (friends[v] >> left_n) & right_full
        allowed_left[i] = left_full & ~friends[v]

    # A greedy coloring of the complement gives an upper bound on the
    # independent-set size of the right half.
    uncolored = right_full
    right_upper = 0
    while uncolored:
        right_upper += 1
        available = uncolored
        while available:
            bit = available & -available
            v = bit.bit_length() - 1
            uncolored ^= bit
            available ^= bit
            available &= right_adj[v]

    if a[left_full] + right_upper < k:
        print("NO")
        return

    right_count = 1 << right_n
    independent_size = bytearray(right_count)
    independent_size[0] = 1  # Stored value is actual size + 1.

    compatible_left = array('I', [0]) * right_count
    compatible_left[0] = left_full

    found_mask = -1
    found_allowed = 0

    sizes = independent_size
    compat = compatible_left
    radj = right_adj
    cross = allowed_left
    target = k

    for mask in range(1, right_count):
        bit = mask & -mask
        v = bit.bit_length() - 1
        rest = mask ^ bit
        previous_size = sizes[rest]

        if previous_size and not (radj[v] & rest):
            current_size = previous_size + 1
            sizes[mask] = current_size
            allowed = compat[rest] & cross[v]
            compat[mask] = allowed

            if current_size - 1 + a[allowed] >= target:
                found_mask = mask
                found_allowed = allowed
                break

    if found_mask == -1:
        print("NO")
        return

    answer = []
    scan = found_mask
    while scan and len(answer) < k:
        bit = scan & -scan
        v = bit.bit_length() - 1
        answer.append(left_n + v)
        scan ^= bit

    need = k - len(answer)
    if need:
        answer.extend(reconstruct_left(found_allowed, need))

    print("YES")
    print(" ".join(str(v + 1) for v in answer[:k]))


if __name__ == "__main__":
    main()