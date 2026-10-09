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
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        idx += 2

    ans = None

    def bk(R, P, X):
        nonlocal ans
        if ans is not None:
            return
        if len(R) == k:
            ans = list(R)
            return
        if len(R) + P.bit_count() < k:
            return
        if P == 0:
            return

        PX = P | X
        pivot = -1
        min_branches = n + 1

        temp = PX
        while temp:
            lsb = temp & -temp
            u = lsb.bit_length() - 1
            temp ^= lsb

            branches = (P & (adj[u] | (1 << u))).bit_count()
            if branches < min_branches:
                min_branches = branches
                pivot = u
                if min_branches <= 1:
                    break

        branch_mask = P & (adj[pivot] | (1 << pivot))

        while branch_mask:
            if ans is not None:
                return
            lsb = branch_mask & -branch_mask
            v = lsb.bit_length() - 1
            branch_mask ^= lsb

            R.append(v + 1)
            bk(R, P & ~adj[v] & ~(1 << v), X & ~adj[v])
            R.pop()

            P &= ~(1 << v)
            X |= 1 << v

    bk([], (1 << n) - 1, 0)

    if ans is not None:
        print("YES")
        print(*ans)
    else:
        print("NO")


if __name__ == "__main__":
    solve()