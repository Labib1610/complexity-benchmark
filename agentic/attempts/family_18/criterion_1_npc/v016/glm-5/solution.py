import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    try:
        n = int(next(it))
        m = int(next(it))
        B = int(next(it))
    except StopIteration:
        return
    
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
    
    # Check if any edge connects the same module (shouldn't happen based on problem)
    # Check if any edge requires length >= n
    # Since modules are distinct, min length is 1, max is n-1.
    # If n=1, no edges possible (m must be 0).
    # If n=1 and m=0, B >= 0 is required.
    
    # We try two permutations:
    # 1. Identity: p[i] = i
    # 2. Reverse: p[i] = n + 1 - i
    
    # Calculate total length for identity permutation
    total_len_id = 0
    for u, v in edges:
        length = abs(u - v)
        # Check constraint 3: length < n
        # For identity, length = abs(u-v). Since u,v in [1,n], max diff is n-1.
        # So constraint 3 is always satisfied for identity.
        total_len_id += length
    
    if total_len_id <= B:
        print("YES")
        print(" ".join(map(str, range(1, n + 1))))
        return
    
    # Calculate total length for reverse permutation
    total_len_rev = 0
    for u, v in edges:
        # p[u] = n + 1 - u
        # p[v] = n + 1 - v
        # diff = abs((n+1-u) - (n+1-v)) = abs(v - u) = abs(u - v)
        # Same length as identity.
        total_len_rev += abs(u - v)
    
    if total_len_rev <= B:
        print("YES")
        print(" ".join(map(str, range(n, 0, -1))))
        return
    
    print("NO")

if __name__ == '__main__':
    solve()