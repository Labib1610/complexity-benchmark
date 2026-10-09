import sys
from itertools import permutations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    B = int(data[2])
    
    dependencies = []
    index = 3
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-based indexing
        v = int(data[index+1]) - 1
        dependencies.append((u, v))
        index += 2
    
    # For small n, try all permutations
    if n <= 8:
        for perm in permutations(range(n)):
            total = 0
            for u, v in dependencies:
                pos_u = perm[u]
                pos_v = perm[v]
                total += abs(pos_u - pos_v)
                if total > B:
                    break
            if total <= B:
                print("YES")
                assignment = [0] * n
                for var in range(n):
                    assignment[perm[var]] = var + 1  # Convert back to 1-based
                print(' '.join(map(str, assignment)))
                return
        print("NO")
        return
    
    # For larger n, use heuristic: sort by degree
    degree = [0] * n
    for u, v in dependencies:
        degree[u] += 1
        degree[v] += 1
        
    # Create list of (degree, variable_index)
    var_degree = [(degree[i], i) for i in range(n)]
    # Sort by degree descending
    var_degree.sort(reverse=True)
    
    # Assign variables to positions: place high-degree variables towards the center
    assignment = [0] * n
    positions = list(range(1, n+1))
    # Sort positions by distance from median to assign central positions to high-degree vars
    median_pos = (n + 1) / 2.0
    positions.sort(key=lambda x: abs(x - median_pos))
    
    # Assign sorted variables to sorted positions
    var_list_sorted_by_degree = [var for deg, var in var_degree]
    # We want to assign high-degree variables to central positions
    # So we pair sorted variables with sorted positions
    var_pos_pairs = list(zip(var_list_sorted_by_degree, positions))
    var_pos_pairs.sort()  # Sort by variable index to maintain order
    
    assignment = [0] * n
    for var, pos in var_pos_pairs:
        assignment[var] = pos
        
    # Calculate total delay for this assignment
    total = 0
    for u, v in dependencies:
        pos_u = assignment[u]
        pos_v = assignment[v]
        total += abs(pos_u - pos_v)
        
    if total <= B:
        print("YES")
        print(' '.join(map(str, assignment)))
        return
        
    # If heuristic fails, try a few random permutations (optional improvement)
    # But since we need deterministic behavior and time constraints, skip this
    print("NO")

if __name__ == "__main__":
    main()