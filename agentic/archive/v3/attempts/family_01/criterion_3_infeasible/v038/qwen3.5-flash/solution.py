import sys

# Increase recursion depth just in case, though not needed here
sys.setrecursionlimit(2000)

def solve():
    # Read all input at once for efficiency
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Precompute powers of 2 for bitmasking
    # 1 << i corresponds to vertex i
    # We use 1-based indexing for vertices, so we need up to n
    # adj_mask[u] will have bit v set if u and v are connected
    POW2 = [1 << i for i in range(n + 1)]
    
    adj = [[] for _ in range(n + 1)]
    adj_mask = [0] * (n + 1)
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        adj_mask[u] |= POW2[v]
        adj_mask[v] |= POW2[u]
            
    # Sort neighbors to ensure lexicographical order of b
    # Also remove duplicates if any
    for i in range(1, n + 1):
        adj[i] = sorted(list(set(adj[i])))
            
    # Iterate a from 1 to n to find the smallest 'a'
    for a in range(1, n + 1):
        # Iterate b in neighbors of a. Since adj[a] is sorted, b is increasing.
        for b in adj[a]:
            # We want a < b < c
            if b <= a:
                continue
            
            # Check for common neighbors c > b
            # common neighbors are bits set in both adj_mask[a] and adj_mask[b]
            common = adj_mask[a] & adj_mask[b]
            
            # We need the smallest bit in common that is > b
            # Shift common right by b + 1 to ignore bits <= b
            shifted = common >> (b + 1)
            
            if shifted:
                # Find the position of the lowest set bit in shifted
                # (shifted & -shifted) isolates the lowest set bit
                low_bit = shifted & -shifted
                # bit_length() of 2^k is k+1, so index is k = bit_length() - 1
                # The actual vertex index c is b + 1 + k
                c = (b + 1) + low_bit.bit_length() - 1
                
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()