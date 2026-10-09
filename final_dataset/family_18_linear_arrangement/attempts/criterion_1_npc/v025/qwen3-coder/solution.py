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
    
    links = []
    for _ in range(m):
        u = int(data[idx]) - 1  # Convert to 0-based indexing
        idx += 1
        v = int(data[idx]) - 1
        idx += 1
        links.append((u, v))
    
    # Try all permutations
    for perm in permutations(range(n)):
        total_power = 0
        valid = True
        for u, v in links:
            pos_u = perm[u]
            pos_v = perm[v]
            power = abs(pos_u - pos_v)
            total_power += power
            if total_power > B:
                valid = False
                break
        if valid and total_power <= B:
            print("YES")
            result = [str(x + 1) for x in perm]  # Convert back to 1-based indexing
            print(" ".join(result))
            return
    
    print("NO")

if __name__ == "__main__":
    main()