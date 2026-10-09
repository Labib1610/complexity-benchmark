from itertools import combinations
import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    conflicts = set()
    idx = 3
    for _ in range(m):
        u = int(data[idx]) - 1  # Convert to 0-based indexing
        v = int(data[idx+1]) - 1
        conflicts.add((u, v))
        conflicts.add((v, u))
        idx += 2
    
    # Generate all possible combinations of k jobs
    jobs = list(range(n))
    for combo in combinations(jobs, k):
        # Check if this combination has any conflicts
        valid = True
        for i in range(k):
            for j in range(i+1, k):
                if (combo[i], combo[j]) in conflicts:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            # Found a valid combination
            print("YES")
            print(' '.join(str(x + 1) for x in combo))  # Convert back to 1-based indexing
            return
    
    print("NO")

if __name__ == "__main__":
    main()