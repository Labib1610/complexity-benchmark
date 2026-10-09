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
        u = int(data[idx]) - 1  # Convert to 0-based
        v = int(data[idx+1]) - 1
        edges.append((u, v))
        idx += 2
    
    # Try all permutations of slot assignments (0-based)
    for perm in permutations(range(n)):
        total_length = 0
        for u, v in edges:
            pos_u = perm[u]
            pos_v = perm[v]
            total_length += abs(pos_u - pos_v)
            if total_length > B:
                break
        if total_length <= B:
            # Found a valid assignment
            # Convert back to 1-based indexing
            assignment = [str(p + 1) for p in perm]
            print("YES")
            print(" ".join(assignment))
            return
    
    print("NO")

if __name__ == "__main__":
    main()