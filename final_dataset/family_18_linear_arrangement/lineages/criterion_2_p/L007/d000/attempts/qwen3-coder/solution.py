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
        index += 2
        edges.append((u, v))
    
    # Since m = n-1 and the graph is connected and has no cycles, it's a tree.
    # We can use a more efficient approach than checking all permutations.
    # However, given the constraints (n up to 8), we can try all permutations.
    
    if n > 8:
        # For larger n, we would need a smarter approach.
        # But based on typical contest constraints, n <= 8 is expected.
        pass
    
    # Generate all permutations of slot assignments (0-based)
    # Each permutation p means unit i is placed at slot p[i]
    for perm in permutations(range(n)):
        total_cost = 0
        valid = True
        for u, v in edges:
            pos_u = perm[u]
            pos_v = perm[v]
            cost = abs(pos_u - pos_v)
            total_cost += cost
            if total_cost > B:
                valid = False
                break
        if valid and total_cost <= B:
            # Found a valid assignment
            # Convert back to 1-based indexing
            result = [str(perm[i] + 1) for i in range(n)]
            print("YES")
            print(" ".join(result))
            return
    
    print("NO")

if __name__ == "__main__":
    main()