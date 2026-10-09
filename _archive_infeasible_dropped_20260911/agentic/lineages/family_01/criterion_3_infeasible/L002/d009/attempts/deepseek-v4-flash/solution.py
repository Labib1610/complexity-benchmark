import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [0] * (n + 1)
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    
    # Iterate over a, b, c in sorted order
    for a in range(1, n - 1):
        for b in range(a + 1, n):
            # Precompute masks for a and b
            mask_ab = (1 << a) | (1 << b)
            # Check if a and b have at least one neighbor among themselves
            a_has_b = (adj[a] >> b) & 1
            b_has_a = (adj[b] >> a) & 1
            for c in range(b + 1, n + 1):
                # Check c has at least one neighbor among a,b
                if not (adj[c] & mask_ab):
                    continue
                # Compute internal sets
                set_a = 0
                if a_has_b:
                    set_a |= 1
                if (adj[a] >> c) & 1:
                    set_a |= 2
                if set_a == 0:
                    continue
                
                set_b = 0
                if b_has_a:
                    set_b |= 1
                if (adj[b] >> c) & 1:
                    set_b |= 2
                if set_b == 0:
                    continue
                
                set_c = 0
                if (adj[c] >> a) & 1:
                    set_c |= 1
                if (adj[c] >> b) & 1:
                    set_c |= 2
                if set_c == 0:
                    continue
                
                if set_a != set_b and set_a != set_c and set_b != set_c:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()