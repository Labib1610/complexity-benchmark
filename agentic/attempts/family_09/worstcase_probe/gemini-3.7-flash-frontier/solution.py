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

    ans = None

    def dfs(cand, count, chosen_mask):
        nonlocal ans
        if ans is not None:
            return
        if count == k:
            ans = chosen_mask
            return
        if count + cand.bit_count() < k:
            return

        # Pick vertex in candidate set with maximum degree in the candidate subgraph
        best_v = -1
        max_deg = -1
        temp = cand
        while temp:
            v = (temp & -temp).bit_length() - 1
            deg = (adj[v] & cand).bit_count()
            if deg > max_deg:
                max_deg = deg
                best_v = v
            temp &= temp - 1

        # Branch 1: include best_v in independent set
        dfs(cand & ~adj[best_v] & ~(1 << best_v), count + 1, chosen_mask | (1 << best_v))
        if ans is not None:
            return

        # Branch 2: exclude best_v from independent set
        dfs(cand & ~(1 << best_v), count, chosen_mask)

    dfs((1 << n) - 1, 0, 0)

    if ans is not None:
        print("YES")
        res = [str(i + 1) for i in range(n) if (ans >> i) & 1]
        print(" ".join(res))
    else:
        print("NO")

if __name__ == '__main__':
    solve()