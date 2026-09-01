def solve():
    import sys
    from itertools import product
    
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index+1]) - 1
        edges.append((u, v))
        index += 2
    
    # Precompute the energy contribution for each pair of levels
    # levels are 1, 2, 3 => indices 0, 1, 2
    energy_matrix = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(3)]
    
    for i in range(3):
        for j in range(3):
            cu, cv = i + 1, j + 1
            p0 = (cu - cv) ** 2
            p1 = -4
            q0 = (cu - cv) ** 2 - 5
            q1 = -1
            energy = p0 * q0 + p1 * q1
            energy_matrix[i][j] = energy
    
    # For efficiency, we'll use backtracking with constraint propagation
    # But given the constraints, let's try a more direct approach
    
    # Since we need total energy = 0, and each edge contributes a specific value,
    # we can check all possible assignments.
    # However, n up to 40 makes 3^40 impossible.
    # But since we're looking for total energy = 0, and each edge has a fixed contribution
    # based on the levels of its endpoints, we can think of this as a constraint satisfaction problem.
    
    # Let's consider that the only way total energy = 0 is if every edge contributes 0.
    # So for every edge (u,v), energy_matrix[c[u]][c[v]] == 0
    
    # When does energy_matrix[i][j] == 0?
    # p0 = (cu - cv)^2, p1 = -4
    # q0 = (cu - cv)^2 - 5, q1 = -1
    # energy = p0*q0 + p1*q1 = (cu-cv)^2 * ((cu-cv)^2 - 5) + (-4)*(-1) 
    #        = (cu-cv)^2 * ((cu-cv)^2 - 5) + 4
    # Let x = (cu-cv)^2
    # energy = x(x-5) + 4 = x^2 - 5x + 4 = (x-1)(x-4)
    # So energy = 0 when x=1 or x=4
    # That means (cu-cv)^2 = 1 or (cu-cv)^2 = 4
    # So |cu-cv| = 1 or |cu-cv| = 2
    
    # Levels are 1,2,3
    # Differences: |1-2|=1, |1-3|=2, |2-3|=1
    # So energy=0 iff |c[u] - c[v]| is 1 or 2
    # But |1-2|=1, |1-3|=2, |2-3|=1
    # Check which pairs give energy 0:
    allowed_pairs = set()
    for i in range(3):
        for j in range(3):
            if energy_matrix[i][j] == 0:
                allowed_pairs.add((i, j))
    
    # Now the problem becomes: assign colors {0,1,2} to nodes such that for every edge,
    # the pair of colors is in allowed_pairs
    
    # This is a list coloring problem. We can solve it with backtracking.
    
    # For each node, initially all colors {0,1,2} are possible
    # Then we do constraint propagation and search
    
    # But let's think again. What are the allowed pairs?
    # Let's compute them:
    allowed_for_edge = []
    for i in range(3):
        for j in range(3):
            if energy_matrix[i][j] == 0:
                allowed_for_edge.append((i,j))
                
    # Actually, let's just compute when energy is 0:
    valid_pairs = [[False]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            if energy_matrix[i][j] == 0:
                valid_pairs[i][j] = True
                
    # So we need to color the graph with 3 colors such that for every edge,
    # the pair of colors is in valid_pairs
    
    # Backtracking with constraint checking
    assignment = [-1] * n
    
    def is_valid_pair(c1, c2):
        return valid_pairs[c1][c2]
    
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    def backtrack(node):
        if node == n:
            return True
            
        # Try colors 0, 1, 2 in order for lexicographically smallest
        for color in range(3):
            # Check if this color is compatible with all neighbors that are already colored
            ok = True
            for neighbor in adj[node]:
                if assignment[neighbor] != -1:
                    if not is_valid_pair(color, assignment[neighbor]):
                        ok = False
                        break
            if ok:
                assignment[node] = color
                if backtrack(node + 1):
                    return True
                assignment[node] = -1
        return False
    
    # Start backtracking from node 0
    if m == 0:
        # No edges, any assignment works, choose lex smallest: all 1s
        print("YES")
        result = [1] * n
        print(' '.join(map(str, result)))
        return
        
    if backtrack(0):
        print("YES")
        result = []
        for i in range(n):
            result.append(assignment[i] + 1)  # Convert back to 1-based
        print(' '.join(map(str, result)))
    else:
        print("NO")

solve()