def solve():
    import sys
    from itertools import product
    
    input = sys.stdin.read
    data = input().split()
    
    n, m = int(data[0]), int(data[1])
    
    # If no constraints, assign all to network 1
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
        
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-based indexing
        v = int(data[index+1]) - 1
        edges.append((u, v))
        index += 2
    
    # Try all 3^n combinations in lexicographical order
    # We'll use backtracking for efficiency
    assignment = [0] * n  # 0 means unassigned
    
    def is_valid(vertex, color):
        for u, v in edges:
            if u == vertex and assignment[v] == color:
                return False
            if v == vertex and assignment[u] == color:
                return False
        return True
    
    def backtrack(vertex):
        if vertex == n:
            return True
            
        for color in [1, 2, 3]:
            if is_valid(vertex, color):
                assignment[vertex] = color
                if backtrack(vertex + 1):
                    return True
                assignment[vertex] = 0  # Backtrack
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, assignment)))
    else:
        print("NO")

solve()