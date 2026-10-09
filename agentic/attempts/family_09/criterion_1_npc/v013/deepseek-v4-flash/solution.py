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

    # Try to find an independent set of size k
    # Use recursive backtracking with pruning
    # We'll order vertices by degree for better pruning
    deg = [bin(adj[i]).count("1") for i in range(n)]
    order = sorted(range(n), key=lambda x: deg[x])

    # We'll use bitmask to represent chosen set
    chosen = []
    # To speed up, we can use a recursive function
    # that tries to add vertices in order

    # Precompute for each vertex the set of vertices that are not adjacent to it
    # and not already chosen

    def backtrack(start, chosen_set, remaining):
        if remaining == 0:
            return True
        if start >= n:
            return False
        # Prune: if even taking all remaining vertices we can't reach k
        if n - start < remaining:
            return False
        # Try to take vertex order[start]
        v = order[start]
        if not (chosen_set & (1 << v)):
            # Check if v is not adjacent to any chosen
            if not (chosen_set & adj[v]):
                chosen.append(v + 1)
                if backtrack(start + 1, chosen_set | (1 << v), remaining - 1):
                    return True
                chosen.pop()
        # Skip vertex
        return backtrack(start + 1, chosen_set, remaining)

    if backtrack(0, 0, k):
        print("YES")
        print(" ".join(map(str, chosen)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()