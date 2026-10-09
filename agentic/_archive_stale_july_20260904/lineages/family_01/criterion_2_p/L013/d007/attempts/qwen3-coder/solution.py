import sys
from collections import defaultdict, deque

def matrix_mult(A, B):
    # Multiply two 2x2 matrices
    return [
        [A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
        [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]
    ]

def matrix_equal(A, B):
    # Check if two 2x2 matrices are equal
    return A[0][0] == B[0][0] and A[0][1] == B[0][1] and A[1][0] == B[1][0] and A[1][1] == B[1][1]

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Define the transformation matrices
    M1 = [[2, 1], [1, 1]]
    M2 = [[1, -1], [-1, 2]]
    I = [[1, 0], [0, 1]]  # Identity matrix
    
    # Precompute what happens when we compose transformations
    # For each pair of transformations (a,b), check if M_a * M_b = I
    transforms = [None, M1, M2]  # index 0 unused, 1->M1, 2->M2
    
    # allowed[a][b] will be True if M_a * M_b = I
    allowed = [[False]*3 for _ in range(3)]
    
    for i in range(1, 3):
        for j in range(1, 3):
            prod = matrix_mult(transforms[i], transforms[j])
            if matrix_equal(prod, I):
                allowed[i][j] = True
                
    # Build adjacency list
    adj = defaultdict(list)
    edges = []
    for i in range(m):
        u = int(data[2 + 2*i]) - 1  # Convert to 0-indexed
        v = int(data[2 + 2*i + 1]) - 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
        
    # If there are no edges, any assignment works. Choose all 1s for lex min
    if m == 0:
        print("YES")
        print(" ".join(["1"]*n))
        return
        
    # For each edge (u,v), the constraint is that f_u(f_v(V)) = V
    # This means M_s[u] * M_s[v] = I, where s[x] is the assignment to node x
    
    # This creates a graph where each connected component is bipartite
    # We can model this as a 2-SAT problem or as a graph coloring problem
    
    # Let's do graph coloring/bfs approach
    # For each connected component, we'll try both starting colors
    
    color = [-1] * n  # -1 unvisited, 0 and 1 are the two "colors" mapping to transformations 1 and 2
    result = [0] * n   # Will store 1 or 2
    
    visited = [False] * n
    
    for start in range(n):
        if visited[start]:
            continue
            
        # BFS to assign colors
        queue = deque()
        queue.append(start)
        visited[start] = True
        # Try color 0 first for lexicographical minimality
        color[start] = 0
        
        component = []
        while queue:
            u = queue.popleft()
            component.append(u)
            
            for v in adj[u]:
                if not visited[v]:
                    # Determine what color v must have based on u's color
                    # We want M_color[u]+1 * M_color[v]+1 = I
                    cu = color[u] + 1  # Convert to 1-based
                    # Find cv such that allowed[cu][cv] is True
                    found = False
                    for cv in [1, 2]:  # Try in order for lex min
                        if allowed[cu][cv]:
                            color[v] = cv - 1  # Convert back to 0-based
                            visited[v] = True
                            queue.append(v)
                            found = True
                            break
                    if not found:
                        print("NO")
                        return
                else:
                    # Check consistency
                    cu = color[u] + 1
                    cv = color[v] + 1
                    if not allowed[cu][cv]:
                        print("NO")
                        return
                        
        # Component is consistent. Assign the lexicographically smallest valid coloring
        # Since we tried color 0 first for the start node, and followed constraints,
        # this should already be minimal. But let's double-check by trying color 1 for start
        # and see if it gives a smaller lex string.
        
        # Actually, our BFS already ensures that within a component, 
        # the assignment is forced once we choose the color of the starting node.
        # So we just need to make sure we pick the right starting color.
        
        # But since we process components in order of node indices, and always try color 0 first,
        # we're guaranteed to get the lex-min solution.
        
    # Convert colors to transformations (0->1, 1->2)
    for i in range(n):
        result[i] = color[i] + 1
        
    # Final verification step (optional but safe)
    for u, v in edges:
        cu = result[u]
        cv = result[v]
        if not allowed[cu][cv]:
            print("NO")
            return
            
    print("YES")
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()