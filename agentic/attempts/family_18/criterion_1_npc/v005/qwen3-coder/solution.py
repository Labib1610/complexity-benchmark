import sys
from itertools import permutations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    B = int(data[idx])
    idx += 1
    
    edges = []
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        edges.append((u-1, v-1))  # Convert to 0-based indexing
    
    # Try all permutations
    for perm in permutations(range(n)):
        total = 0
        for u, v in edges:
            pos_u = perm[u]
            pos_v = perm[v]
            total += abs(pos_u - pos_v)
            if total > B:
                break
        if total <= B:
            # Found a valid permutation
            print("YES")
            print(' '.join(str(x+1) for x in perm))  # Convert back to 1-based indexing
            return
    
    print("NO")

if __name__ == "__main__":
    main()