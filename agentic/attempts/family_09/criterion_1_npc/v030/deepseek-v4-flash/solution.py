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
    
    # Try to find independent set of size k using backtracking
    # We'll use bitmask representation
    all_mask = (1 << n) - 1
    
    # Bron–Kerbosch style might be overkill; simple recursive backtracking works for n=46
    # We'll sort vertices by degree for better pruning
    deg = [bin(adj[i]).count("1") for i in range(n)]
    order = sorted(range(n), key=lambda x: deg[x])
    
    # memoization for (position, available_mask) not needed if we backtrack properly
    
    best = []
    
    def backtrack(start, chosen, avail):
        nonlocal best
        if len(chosen) == k:
            best = chosen[:]
            return True
        if len(chosen) + bin(avail).count("1") < k:
            return False
        # iterate over available vertices from start
        for i in range(start, n):
            v = order[i]
            if avail & (1 << v):
                # choose v
                new_avail = avail & ~adj[v] & ~(1 << v)
                if backtrack(i + 1, chosen + [v], new_avail):
                    return True
        return False
    
    if backtrack(0, [], all_mask):
        print("YES")
        print(" ".join(str(x + 1) for x in best))
    else:
        print("NO")

if __name__ == "__main__":
    solve()