from itertools import permutations
import sys

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
    
    # Try all permutations of slot assignments
    modules = list(range(n))
    for perm in permutations(modules):
        total_length = 0
        valid = True
        # Calculate total cable length for this permutation
        for u, v in edges:
            pos_u = perm[u]
            pos_v = perm[v]
            length = abs(pos_u - pos_v)
            total_length += length
            # Early termination if already exceeds budget
            if total_length > B:
                valid = False
                break
        if valid and total_length <= B:
            # Found a valid assignment
            # Convert back to 1-based indexing for output
            result = [str(x + 1) for x in perm]
            print("YES")
            print(" ".join(result))
            return
    
    print("NO")

if __name__ == "__main__":
    main()