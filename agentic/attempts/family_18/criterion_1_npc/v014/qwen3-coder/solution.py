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
    for i in range(m):
        u = int(data[3 + 2*i]) - 1  # Convert to 0-based indexing
        v = int(data[4 + 2*i]) - 1
        edges.append((u, v))
    
    # Try all permutations of slot assignments
    for perm in permutations(range(n)):
        total_wire = 0
        for u, v in edges:
            pos_u = perm[u]
            pos_v = perm[v]
            total_wire += abs(pos_u - pos_v)
            if total_wire > B:
                break
        if total_wire <= B:
            # Found a valid assignment
            result = [str(x + 1) for x in perm]  # Convert back to 1-based indexing
            print("YES")
            print(" ".join(result))
            return
    
    print("NO")

if __name__ == "__main__":
    main()