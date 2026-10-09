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
    if k == 0:
        print("YES")
        print()
        return

    edge = [0] * n
    idx = 3
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        edge[u] |= 1 << v
        edge[v] |= 1 << u

    compat = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if not ((edge[i] >> j) & 1):
                compat[i] |= 1 << j

    max_size = [0] * (n + 1)
    found_clique = []

    def search(candidates_mask, current_path, target_size):
        nonlocal found_clique
        if len(current_path) == target_size:
            found_clique = list(current_path)
            return True

        cand = candidates_mask
        while cand > 0:
            p = cand & -cand
            v = p.bit_length() - 1

            if len(current_path) + max_size[v] < target_size:
                return False

            cand &= cand - 1

            if search(candidates_mask & compat[v], current_path + [v], target_size):
                return True

        return False

    for i in range(n - 1, -1, -1):
        found_clique = []
        if search(compat[i], [i], max_size[i + 1] + 1):
            max_size[i] = max_size[i + 1] + 1
            if max_size[i] >= k:
                print("YES")
                res = [x + 1 for x in found_clique[:k]]
                print(*(res))
                return
        else:
            max_size[i] = max_size[i + 1]

    print("NO")


if __name__ == "__main__":
    solve()