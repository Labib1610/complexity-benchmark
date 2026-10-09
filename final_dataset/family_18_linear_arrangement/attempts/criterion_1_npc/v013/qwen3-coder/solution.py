import sys
from itertools import permutations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    B = int(data[2])
    
    links = []
    for i in range(m):
        u = int(data[3 + 2*i]) - 1  # Convert to 0-based indexing
        v = int(data[4 + 2*i]) - 1
        links.append((u, v))
    
    # Try all permutations
    for perm in permutations(range(n)):
        total_length = 0
        for u, v in links:
            pos_u = perm[u]
            pos_v = perm[v]
            total_length += abs(pos_u - pos_v)
            if total_length > B:
                break
        if total_length <= B:
            # Found a valid assignment
            result = [str(x + 1) for x in perm]  # Convert back to 1-based indexing
            print("YES")
            print(" ".join(result))
            return
    
    print("NO")

if __name__ == "__main__":
    main()