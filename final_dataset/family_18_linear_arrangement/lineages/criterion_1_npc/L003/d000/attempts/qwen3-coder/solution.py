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
    index = 3
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-based indexing
        v = int(data[index+1]) - 1
        edges.append((u, v))
        index += 2
    
    # Try all permutations of zone assignments (positions 0 to n-1)
    for perm in permutations(range(n)):
        total_length = 0
        valid = True
        for u, v in edges:
            pos_u = perm[u]
            pos_v = perm[v]
            total_length += abs(pos_u - pos_v)
            if total_length > B:
                valid = False
                break
        if valid and total_length <= B:
            # Found a valid assignment
            # Convert back to 1-based indexing for output
            result = [str(perm[i] + 1) for i in range(n)]
            print("YES")
            print(" ".join(result))
            return
    
    print("NO")

if __name__ == "__main__":
    main()