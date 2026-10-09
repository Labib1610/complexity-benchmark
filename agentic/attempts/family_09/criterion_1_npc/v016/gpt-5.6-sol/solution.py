import sys
from array import array

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m, k = data[0], data[1], data[2]
    adj = [0] * n
    p = 3
    for _ in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    if k == 1:
        print("YES")
        print(1)
        return

    # Quick greedy attempt.
    orders = [
        sorted(range(n), key=lambda v: adj[v].bit_count()),
        sorted(range(n), key=lambda v: adj[v].bit_count(), reverse=True),
        list(range(n))
    ]
    for order in orders:
        chosen = []
        used = 0
        for v in order:
            if not (adj[v] & used):
                chosen.append(v)
                used |= 1 << v
                if len(chosen) == k:
                    print("YES")
                    print(*(v + 1 for v in chosen))
                    return

    left_n = n // 2
    right_n = n - left_n
    all_right = (1 << right_n) - 1

    left_adj = [0] * left_n
    right_allowed = [all_right] * left_n
    right_adj = [0] * right_n

    left_mask_all = (1 << left_n) - 1

    for i in range(left_n):
        left_adj[i] = adj[i] & left_mask_all
        cross = (adj[i] >> left_n) & all_right
        right_allowed[i] = all_right ^ cross

    for j in range(right_n):
        right_adj[j] = (adj[left_n + j] >> left_n) & all_right

    # dp[mask] = maximum independent set size inside mask in the right half.
    right_size = 1 << right_n
    dp = bytearray(right_size)
    dp_local = dp
    radj = right_adj

    for mask in range(1, right_size):
        bit = mask & -mask
        v = bit.bit_length() - 1
        rest = mask ^ bit
        exclude = dp_local[rest]
        include = 1 + dp_local[rest & ~radj[v]]
        dp_local[mask] = include if include > exclude else exclude

    def reconstruct_right(mask, need):
        result = []
        while need:
            bit = mask & -mask
            v = bit.bit_length() - 1
            rest = mask ^ bit
            if dp_local[rest] >= need:
                mask = rest
            else:
                result.append(left_n + v)
                mask = rest & ~radj[v]
                need -= 1
        return result

    if dp_local[all_right] >= k:
        result = reconstruct_right(all_right, k)
        print("YES")
        print(*(v + 1 for v in result))
        return

    # Limited include-first search, useful for quickly finding large solutions.
    node_limit = 30000
    nodes = 0
    found = None

    def search(candidates, available_right, selected_mask, selected_count):
        nonlocal nodes, found
        if found is not None or nodes >= node_limit:
            return
        nodes += 1

        need = k - selected_count
        if need <= 0:
            found = (selected_mask, available_right)
            return
        if dp_local[available_right] >= need:
            found = (selected_mask, available_right)
            return
        if selected_count + candidates.bit_count() + dp_local[available_right] < k:
            return
        if not candidates:
            return

        bit = candidates & -candidates
        v = bit.bit_length() - 1
        rest = candidates ^ bit

        search(
            rest & ~left_adj[v],
            available_right & right_allowed[v],
            selected_mask | bit,
            selected_count + 1
        )
        if found is None:
            search(rest, available_right, selected_mask, selected_count)

    search((1 << left_n) - 1, all_right, 0, 0)

    if found is not None:
        lm, rm = found
        left_vertices = [i for i in range(left_n) if (lm >> i) & 1]
        if len(left_vertices) >= k:
            answer = left_vertices[:k]
        else:
            answer = left_vertices + reconstruct_right(rm, k - len(left_vertices))
        print("YES")
        print(*(v + 1 for v in answer))
        return

    # Exhaustively enumerate left subsets. For each independent subset, store
    # the right vertices compatible with every selected left vertex.
    left_size = 1 << left_n
    INVALID = 1 << 31
    compatible = array('I', [0]) * left_size
    compatible[0] = all_right

    comp = compatible
    ladj = left_adj
    rallow = right_allowed

    answer_left = -1
    answer_right_mask = 0

    for mask in range(1, left_size):
        bit = mask & -mask
        v = bit.bit_length() - 1
        rest = mask ^ bit
        previous = comp[rest]

        if (previous & INVALID) or (ladj[v] & rest):
            comp[mask] = INVALID
            continue

        available = previous & rallow[v]
        comp[mask] = available
        count_left = mask.bit_count()

        if count_left >= k or count_left + dp_local[available] >= k:
            answer_left = mask
            answer_right_mask = available
            break

    if answer_left == -1:
        print("NO")
        return

    left_vertices = [i for i in range(left_n) if (answer_left >> i) & 1]
    if len(left_vertices) >= k:
        answer = left_vertices[:k]
    else:
        answer = left_vertices + reconstruct_right(
            answer_right_mask, k - len(left_vertices)
        )

    print("YES")
    print(*(v + 1 for v in answer))

if __name__ == "__main__":
    main()