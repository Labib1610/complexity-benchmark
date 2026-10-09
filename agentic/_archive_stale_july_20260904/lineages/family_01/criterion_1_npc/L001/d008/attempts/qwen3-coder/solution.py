from itertools import product

def solve():
    n, m = map(int, input().split())
    
    # Read constraints
    constraints = []
    for _ in range(m):
        u, v = map(int, input().split())
        constraints.append((u-1, v-1))  # Convert to 0-indexed
    
    # Check if graph is 3-colorable
    # We'll use backtracking to find a valid 3-coloring
    coloring = [-1] * n
    
    def is_valid_color(node, color):
        for u, v in constraints:
            if u == node and coloring[v] == color:
                return False
            if v == node and coloring[u] == color:
                return False
        return True
    
    def backtrack(node):
        if node == n:
            return True
        
        for color in [1, 2, 3]:
            if is_valid_color(node, color):
                coloring[node] = color
                if backtrack(node + 1):
                    return True
                coloring[node] = -1
        return False
    
    # If no valid coloring exists
    if not backtrack(0):
        print("NO")
        return
    
    # Calculate interference for the valid coloring
    def calculate_interference(bands):
        A = [0] * n
        for j in range(n):
            A[j] = bands[j]
        
        for k in range(n - 1):
            for j in range(k + 1, n):
                A[j] += 3 * A[k]
        
        return sum(A)
    
    # Since we only have one valid coloring from backtrack, we output it
    min_interference = calculate_interference(coloring)
    best_coloring = coloring[:]
    
    # But we should check if there are other valid colorings with less interference
    # Generate all possible 3-colorings and check constraints
    for bands in product([1, 2, 3], repeat=n):
        # Check if this coloring satisfies all constraints
        valid = True
        for u, v in constraints:
            if bands[u] == bands[v]:
                valid = False
                break
        
        if valid:
            interference = calculate_interference(bands)
            if interference < min_interference:
                min_interference = interference
                best_coloring = list(bands)
    
    print("YES")
    print(*best_coloring)

solve()