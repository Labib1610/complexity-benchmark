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
    # Use backtracking with bitmasks
    # We'll try to pick vertices in increasing order
    chosen = []
    # available mask of vertices we can still pick
    # We'll use recursion

    # Precompute for each vertex the mask of vertices with index > it
    # to avoid picking same vertex twice and to keep order

    def backtrack(start, available, chosen):
        if len(chosen) == k:
            return True
        # If not enough remaining vertices to reach k, prune
        if bin(available).count("1") < k - len(chosen):
            return False
        # Try each vertex from start to n-1
        # We'll iterate over bits in available
        v = start
        while v < n:
            if (available >> v) & 1:
                # pick v
                chosen.append(v)
                # new available: remove v and its neighbors
                new_available = available & ~(1 << v) & ~adj[v]
                if backtrack(v + 1, new_available, chosen):
                    return True
                chosen.pop()
            v += 1
        return False

    # Initial available: all vertices
    initial_available = (1 << n) - 1
    if backtrack(0, initial_available, chosen):
        print("YES")
        print(" ".join(str(x + 1) for x in chosen))
    else:
        print("NO")

if __name__ == "__main__":
    solve()