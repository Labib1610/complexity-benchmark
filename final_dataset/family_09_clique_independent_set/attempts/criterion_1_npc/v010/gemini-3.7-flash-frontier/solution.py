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

    def dfs(candidates, rem_k):
        if rem_k == 0:
            return []
        if candidates.bit_count() < rem_k:
            return None

        # Choose pivot p in candidates with minimum degree in candidates
        min_deg = n + 1
        best_p = -1

        temp = candidates
        while temp:
            lsb = temp & -temp
            v = lsb.bit_length() - 1
            deg = (candidates & adj[v]).bit_count()
            if deg < min_deg:
                min_deg = deg
                best_p = v
                if deg == 0:
                    break
            temp ^= lsb

        # Branching set: {best_p} U (candidates & adj[best_p])
        branch = (candidates & adj[best_p]) | (1 << best_p)
        curr_cand = candidates

        while branch:
            lsb = branch & -branch
            v = lsb.bit_length() - 1
            branch ^= lsb

            if (curr_cand & (1 << v)) == 0:
                continue

            next_cand = curr_cand & ~adj[v] & ~(1 << v)
            res = dfs(next_cand, rem_k - 1)
            if res is not None:
                res.append(v + 1)
                return res

            curr_cand &= ~(1 << v)
            if curr_cand.bit_count() < rem_k:
                break

        return None

    initial_candidates = (1 << n) - 1
    result = dfs(initial_candidates, k)

    if result is not None:
        print("YES")
        print(*(result))
    else:
        print("NO")


if __name__ == "__main__":
    solve()