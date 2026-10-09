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

    if k == 1:
        print("YES")
        print(1)
        return

    adj_orig = [0] * n
    idx = 3
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        adj_orig[u] |= (1 << v)
        adj_orig[v] |= (1 << u)

    # In the complement graph, an edge exists if there is NO direct channel
    # adj_independent[i] contains all j != i such that (i, j) is NOT an edge in original graph
    full_mask = (1 << n) - 1
    adj_independent = [0] * n
    for i in range(n):
        adj_independent[i] = full_mask ^ adj_orig[i] ^ (1 << i)

    max_IS_suffix = [0] * (n + 1)
    best_IS = []

    def search(candidates, current_list):
        nonlocal best_IS
        if not candidates:
            if len(current_list) > len(best_IS):
                best_IS = list(current_list)
            return

        while candidates:
            # Pick the lowest indexed vertex
            v = (candidates & -candidates).bit_length() - 1
            if len(current_list) + max_IS_suffix[v] <= len(best_IS):
                break
            candidates &= ~(1 << v)
            search(candidates & adj_independent[v], current_list + [v])
            if len(best_IS) >= k:
                return

    for i in range(n - 1, -1, -1):
        candidates = adj_independent[i] & ((full_mask) ^ ((1 << (i + 1)) - 1))
        search(candidates, [i])
        max_IS_suffix[i] = len(best_IS)
        if len(best_IS) >= k:
            break

    if len(best_IS) >= k:
        print("YES")
        res = [x + 1 for x in best_IS[:k]]
        print(*(res))
    else:
        print("NO")

if __name__ == '__main__':
    solve()