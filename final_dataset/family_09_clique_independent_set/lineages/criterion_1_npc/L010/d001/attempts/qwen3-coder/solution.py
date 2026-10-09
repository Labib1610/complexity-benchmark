from itertools import combinations

def main():
    n, m, k = map(int, input().split())
    
    # Create adjacency list to represent conflicts
    conflicts = set()
    for _ in range(m):
        u, v = map(int, input().split())
        conflicts.add((min(u, v), max(u, v)))
    
    # Generate all possible combinations of k devices
    devices = list(range(1, n + 1))
    
    # Check each combination of k devices
    for combo in combinations(devices, k):
        # Check if this combination has any conflicts
        valid = True
        for i in range(k):
            for j in range(i + 1, k):
                u, v = combo[i], combo[j]
                if (min(u, v), max(u, v)) in conflicts:
                    valid = False
                    break
            if not valid:
                break
        
        if valid:
            print("YES")
            print(*combo)
            return
    
    print("NO")

if __name__ == "__main__":
    main()