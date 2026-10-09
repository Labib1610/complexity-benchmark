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

    found = None

    def bron_kerbosch(R, P, X):
        nonlocal found
        if found is not None:
            return
        if len(R) >= k:
            found = R[:k]
            return
        if len(R) + P.bit_count() < k:
            return
        if P == 0 and X == 0:
            return

        # Choose pivot u in P | X minimizing |P & adj[u]|
        p_or_x = P | X
        best_u = -1
        min_branch = 100
        temp = p_or_x
        while temp:
            lsb = temp & -temp
            u = lsb.bit_length() - 1
            cnt = (P & adj[u]).bit_count()
            if cnt < min_branch:
                min_branch = cnt
                best_u = u
            temp ^= lsb

        # Branch on vertices in (P & adj[best_u]) and best_u (if best_u in P)
        branch_mask = P & adj[best_u]
        if (P >> best_u) & 1:
            branch_mask |= 1 << best_u

        temp = branch_mask
        while temp:
            lsb = temp & -temp
            v = lsb.bit_length() - 1
            R.append(v)
            bron_kerbosch(
                R, P & ~adj[v] & ~(1 << v), X & ~adj[v] & ~(1 << v)
            )
            if found is not None:
                return
            R.pop()
            P &= ~(1 << v)
            X |= 1 << v
            if len(R) + P.bit_count() < k:
                break
            temp ^= lsb

    initial_P = (1 << n) - 1
    bron_kerbosch([], initial_P, 0)

    if found is not None:
        print("YES")
        print(*(v + 1 for v in found))
    else:
        print("NO")


if __name__ == "__main__":
    solve()