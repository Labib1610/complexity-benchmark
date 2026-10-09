import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    k = int(input_data[2])

    adj = [0] * n
    idx = 3
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    current_set = []

    def solve_max_deg_1(cand_mask):
        res = []
        rem = cand_mask
        while rem:
            v = (rem & -rem).bit_length() - 1
            res.append(v)
            rem &= ~(1 << v)
            rem &= ~adj[v]
        return res

    def search(cand_mask):
        if len(current_set) >= k:
            return True

        if len(current_set) + cand_mask.bit_count() < k:
            return False

        # Find vertex in cand_mask with maximum degree in induced subgraph
        max_deg = -1
        best_v = -1

        rem = cand_mask
        while rem:
            v = (rem & -rem).bit_length() - 1
            deg = (adj[v] & cand_mask).bit_count()
            if deg > max_deg:
                max_deg = deg
                best_v = v
            rem &= rem - 1

        if max_deg <= 1:
            is_set = solve_max_deg_1(cand_mask)
            if len(current_set) + len(is_set) >= k:
                needed = k - len(current_set)
                current_set.extend(is_set[:needed])
                return True
            return False

        # Branch 1: Include best_v
        current_set.append(best_v)
        next_cand = cand_mask & ~adj[best_v] & ~(1 << best_v)
        if search(next_cand):
            return True
        current_set.pop()

        # Branch 2: Exclude best_v
        next_cand = cand_mask & ~(1 << best_v)
        if search(next_cand):
            return True

        return False

    initial_mask = (1 << n) - 1
    if search(initial_mask):
        print("YES")
        print(*(x + 1 for x in current_set[:k]))
    else:
        print("NO")


if __name__ == "__main__":
    solve()