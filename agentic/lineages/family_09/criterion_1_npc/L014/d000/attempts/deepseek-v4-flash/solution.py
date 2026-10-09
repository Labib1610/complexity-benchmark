import sys

def solve():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    adj = [0] * n
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)

    # If k is 1, always possible
    if k == 1:
        print("YES")
        print(1)
        return

    # Try to find independent set of size k
    # Use bitmask to represent candidate set
    candidates = (1 << n) - 1
    chosen = []

    # Backtracking with pruning
    def backtrack(start, chosen_set, candidates_mask):
        if len(chosen_set) == k:
            return chosen_set[:]
        if len(chosen_set) + bin(candidates_mask).count("1") < k:
            return None
        # Try vertices from start
        for v in range(start, n):
            if (candidates_mask >> v) & 1:
                # choose v
                chosen_set.append(v)
                # new candidates: remove v and its neighbors
                new_candidates = candidates_mask & ~(1 << v) & ~adj[v]
                res = backtrack(v + 1, chosen_set, new_candidates)
                if res is not None:
                    return res
                chosen_set.pop()
        return None

    res = backtrack(0, [], candidates)
    if res is None:
        print("NO")
    else:
        print("YES")
        print(" ".join(str(x + 1) for x in res))

if __name__ == "__main__":
    solve()