import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    k = int(input_data[2])

    if k == 0:
        print("YES")
        print()
        return

    adj = [0] * n
    idx = 3
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    all_mask = (1 << n) - 1

    ans = None

    def search(P, current_mask, current_size):
        nonlocal ans
        if current_size >= k:
            ans = current_mask
            return True

        if current_size + P.bit_count() < k:
            return False

        # Choose pivot p in P with minimum degree in G[P]
        min_deg = n + 1
        pivot = -1
        temp = P
        while temp:
            lsb = temp & -temp
            u = lsb.bit_length() - 1
            deg = (P & adj[u]).bit_count()
            if deg < min_deg:
                min_deg = deg
                pivot = u
                if deg == 0:
                    break
            temp &= temp - 1

        branch_mask = (1 << pivot) | (P & adj[pivot])
        curr_P = P

        while branch_mask:
            lsb = branch_mask & -branch_mask
            u = lsb.bit_length() - 1
            branch_mask &= branch_mask - 1

            if not (curr_P & (1 << u)):
                continue

            next_P = curr_P & ~adj[u] & ~(1 << u)
            if search(next_P, current_mask | (1 << u), current_size + 1):
                return True

            curr_P &= ~(1 << u)
            if current_size + curr_P.bit_count() < k:
                break

        return False

    if search(all_mask, 0, 0):
        print("YES")
        res = []
        for i in range(n):
            if (ans >> i) & 1:
                res.append(i + 1)
                if len(res) == k:
                    break
        print(*(res))
    else:
        print("NO")


if __name__ == "__main__":
    solve()