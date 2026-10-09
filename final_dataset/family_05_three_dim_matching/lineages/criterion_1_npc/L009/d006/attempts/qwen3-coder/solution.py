from itertools import combinations
import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    paths = []
    index = 2
    for _ in range(t):
        x = int(data[index])
        y = int(data[index+1])
        z = int(data[index+2])
        paths.append((x, y, z))
        index += 3
    
    # Calculate target sum
    target = (100**(3*k + 1) - 100) // 99
    
    # Function to compute footprint of a path
    def footprint(x, y, z):
        return 100**x + 100**(k + y) + 100**(2*k + z)
    
    # Try all combinations of k paths
    for combo in combinations(paths, k):
        total = sum(footprint(x, y, z) for (x, y, z) in combo)
        if total == target:
            print("YES")
            for x, y, z in combo:
                print(x, y, z)
            return
    
    print("NO")

if __name__ == "__main__":
    main()