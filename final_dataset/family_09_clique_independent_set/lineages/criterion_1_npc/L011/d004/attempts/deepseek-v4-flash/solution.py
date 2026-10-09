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
    
    # Try to find independent set of size k
    # Use backtracking with pruning
    # We'll try to pick vertices in order
    
    # Precompute possible candidates for each position
    # Use recursion with bitmask of forbidden vertices
    
    # We'll use a simple recursive search with pruning:
    # At each step, we choose the next vertex with smallest degree among remaining candidates
    
    all_mask = (1 << n) - 1
    
    # For pruning: if remaining vertices + current size < k, fail
    
    def backtrack(chosen, forbidden, start):
        if bin(chosen).count("1") == k:
            return chosen
        # available vertices are those not chosen and not forbidden
        available = all_mask & ~(chosen | forbidden)
        if bin(available).count("1") + bin(chosen).count("1") < k:
            return None
        # Choose next vertex with smallest degree among available
        best_v = -1
        best_deg = n + 1
        temp = available
        while temp:
            lsb = temp & -temp
            v = (lsb.bit_length() - 1)
            deg = bin(adj[v] & available).count("1")
            if deg < best_deg:
                best_deg = deg
                best_v = v
            temp -= lsb
        if best_v == -1:
            return None
        # Try including best_v
        res = backtrack(chosen | (1 << best_v), forbidden | adj[best_v], start)
        if res is not None:
            return res
        # Try excluding best_v
        return backtrack(chosen, forbidden | (1 << best_v), start)
    
    result = backtrack(0, 0, 0)
    if result is None:
        print("NO")
    else:
        members = [i+1 for i in range(n) if (result >> i) & 1]
        print("YES")
        print(" ".join(map(str, members)))

if __name__ == "__main__":
    solve()