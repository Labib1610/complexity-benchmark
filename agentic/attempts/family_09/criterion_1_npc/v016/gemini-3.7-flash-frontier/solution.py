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
        v = int(input_data[idx+1]) - 1
        idx += 2
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    
    # Precompute popcounts if needed, or use int.bit_count() in Python 3.10+
    # Python 3.10+ has int.bit_count()
    
    found = None
    chosen = []

    def search(P):
        nonlocal found
        if len(chosen) == k:
            found = list(chosen)
            return True
        
        if len(chosen) + P.bit_count() < k:
            return False
        
        # Choose a pivot u in P that maximizes bit_count(P & adj[u])
        # to minimize the number of branches: bit_count(P & ~adj[u])
        best_u = -1
        max_inter = -1
        
        temp_P = P
        while temp_P > 0:
            lsb = temp_P & -temp_P
            u = lsb.bit_length() - 1
            inter = (P & adj[u]).bit_count()
            if inter > max_inter:
                max_inter = inter
                best_u = u
            temp_P ^= lsb
        
        # Branch candidates are vertices in P that are not neighbors of best_u (including best_u itself)
        candidates = P & ~adj[best_u]
        
        while candidates > 0:
            if len(chosen) + P.bit_count() < k:
                return False
            lsb = candidates & -candidates
            v = lsb.bit_length() - 1
            candidates ^= lsb
            
            chosen.append(v + 1)
            if search(P & ~adj[v] & ~(1 << v)):
                return True
            chosen.pop()
            
            # Remove v from P for subsequent branches
            P ^= (1 << v)
            
        return False

    initial_P = (1 << n) - 1
    if search(initial_P):
        print("YES")
        print(*(found[:k]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()