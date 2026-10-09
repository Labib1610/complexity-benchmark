import sys
from itertools import permutations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    B = int(data[2])
    
    edges = []
    idx = 3
    for _ in range(m):
        u = int(data[idx]) - 1  # Convert to 0-based indexing
        v = int(data[idx+1]) - 1
        edges.append((u, v))
        idx += 2
    
    # Try all permutations of bay assignments (positions 0 to n-1)
    for perm in permutations(range(n)):
        # Check compliance directive 2: sum of positions should be n(n-1)/2 (0-based)
        if sum(perm) != n*(n-1)//2:
            continue
            
        # Calculate total harness length
        total_length = 0
        valid = True
        for u, v in edges:
            pos_u = perm[u]
            pos_v = perm[v]
            length = abs(pos_u - pos_v)
            # Check compliance directive 3: each harness length < n
            if length >= n:
                valid = False
                break
            total_length += length
        
        if not valid:
            continue
            
        # Check compliance directive 4: total length <= B
        if total_length <= B:
            # Found a valid assignment
            # Convert back to 1-based indexing for output
            result = [str(x + 1) for x in perm]
            print("YES")
            print(" ".join(result))
            return
    
    print("NO")

if __name__ == "__main__":
    main()