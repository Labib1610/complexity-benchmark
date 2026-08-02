from itertools import permutations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        edges.append((u - 1, v - 1))
        index += 2
    
    # Try all permutations of shifts (1, 2, 3)
    for perm in permutations([1, 2, 3]):
        assignment = [-1] * n
        valid = True
        
        # Assign shifts to first three workers according to the permutation
        if n >= 3:
            assignment[0], assignment[1], assignment[2] = perm[:3]
        
        # If there are more than 3 workers, assign shifts cyclically based on the permutation
        for i in range(3, n):
            assignment[i] = perm[i % 3]
        
        # Check if this assignment is valid with respect to all edges
        for u, v in edges:
            if assignment[u] == assignment[v]:
                valid = False
                break
        
        if valid:
            print("YES")
            print(' '.join(map(str, assignment)))
            return
    
    # If no valid assignment found
    print("NO")

if __name__ == "__main__":
    main()