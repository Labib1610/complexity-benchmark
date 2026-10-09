import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    k = int(input_data[2])

    if k > n:
        print("NO")
        return

    adj_orig = [0] * n
    idx = 3
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        adj_orig[u] |= 1 << v
        adj_orig[v] |= 1 << u

    # Order vertices by degree ascending
    order = sorted(range(n), key=lambda x: adj_orig[x].bit_count())
    orig_to_new = {order[i]: i for i in range(n)}

    adj = [0] * n
    for i in range(n):
        u = order[i]
        mask = 0
        for j in range(n):
            if (adj_orig[u] >> order[j]) & 1:
                mask |= 1 << j
        adj[i] = mask

    all_mask = (1 << n) - 1
    non_adj = [all_mask ^ adj[i] ^ (1 << i) for i in range(n)]

    max_size = [0] * (n + 1)
    best_set = []

    for i in range(n - 1, -1, -1):
        target = max_size[i + 1]
        if target == 0:
            max_size[i] = 1
            best_set = [i]
        else:
            found = False
            cur_best = []

            def search(cand_mask, cur_list):
                nonlocal found, cur_best
                if len(cur_list) == target:
                    found = True
                    cur_best = list(cur_list)
                    return True

                m = cand_mask
                while m:
                    v = (m & -m).bit_length() - 1
                    if len(cur_list) + max_size[v] < target:
                        break
                    m &= ~(1 << v)

                    cur_list.append(v)
                    if search(m & non_adj[v], cur_list):
                        return True
                    cur_list.pop()

                return False

            cand = non_adj[i] & ~((1 << (i + 1)) - 1)
            search(cand, [])

            if found:
                max_size[i] = target + 1
                best_set = [i] + cur_best
            else:
                max_size[i] = target

        if max_size[i] >= k:
            ans = [order[v] + 1 for v in best_set[:k]]
            print("YES")
            print(*(ans))
            return

    print("NO")


if __name__ == "__main__":
    solve()