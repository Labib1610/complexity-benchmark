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
    # We'll do backtracking with pruning

    # Precompute for each node the set of nodes that are not its neighbors (including itself)
    # This helps in pruning

    # Simple backtracking
    chosen = []
    def backtrack(start, chosen_set):
        if len(chosen) == k:
            return True
        # Prune: not enough remaining nodes
        if n - start < k - len(chosen):
            return False
        for i in range(start, n):
            # Check if i can be added
            if (chosen_set & adj[i]) == 0:
                chosen.append(i)
                if backtrack(i + 1, chosen_set | (1 << i)):
                    return True
                chosen.pop()
        return False

    if backtrack(0, 0):
        print("YES")
        print(" ".join(str(x + 1) for x in chosen))
    else:
        print("NO")

if __name__ == "__main__":
    solve()