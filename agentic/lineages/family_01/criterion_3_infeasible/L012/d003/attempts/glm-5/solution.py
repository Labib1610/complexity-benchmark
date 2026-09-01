import sys

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    n, m = map(int, input[ptr:ptr+2])
    ptr +=2
    
    adj = [0] * (n + 1)  # using bitmask for adjacency
    
    for _ in range(m):
        u, v = map(int, input[ptr:ptr+2])
        ptr +=2
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    
    for a in range(1, n + 1):
        neighbors_a = adj[a]
        # Iterate through all b > a that are neighbors of a
        b_candidates = []
        for b in range(a + 1, n + 1):
            if (neighbors_a >> b) & 1:
                b_candidates.append(b)
        # Now for each b in b_candidates, check if there's a c > b that is neighbor of both a and b
        for b in b_candidates:
            common = adj[a] & adj[b]
            # We need c > b and c is in common
            # So find the smallest c > b in common
            # To find the smallest c > b, we can mask out bits <= b
            mask = (1 << (n + 1)) - 1
            mask &= ~((1 << (b + 1)) - 1)
            common &= mask
            if common:
                # Find the lowest set bit in common
                c = (common & -common).bit_length() - 1
                print(a, b, c)
                return
    # Shouldn't reach here per problem statement
    print(-1, -1, -1)

solve()