from itertools import combinations
import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    # Create adjacency list to represent conflicts
    conflicts = [set() for _ in range(n + 1)]
    
    index = 3
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        conflicts[u].add(v)
        conflicts[v].add(u)
        index += 2
    
    # Generate all combinations of k employees
    for combo in combinations(range(1, n + 1), k):
        valid = True
        # Check if any two in the combination conflict
        for i in range(k):
            for j in range(i + 1, k):
                if combo[j] in conflicts[combo[i]]:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            print("YES")
            print(' '.join(map(str, combo)))
            return
    
    print("NO")

if __name__ == "__main__":
    main()