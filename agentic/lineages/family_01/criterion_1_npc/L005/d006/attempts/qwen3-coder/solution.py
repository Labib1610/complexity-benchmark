from collections import defaultdict

def determinant(p_u, p_v):
    # Matrix M = [[1, p_u, p_u^2], [1, p_v, p_v^2], [1, 4, 16]]
    # Determinant = 1*(p_v*16 - p_v^2*4) - p_u*(16 - p_v^2) + p_u^2*(4 - p_v)
    # Simplifying:
    # = 16*p_v - 4*p_v^2 - 16*p_u + p_u*p_v^2 + 4*p_u^2 - p_u^2*p_v
    # = p_v*(16 - 4*p_v) + p_u*(-16 + p_v^2) + p_u^2*(4 - p_v)
    # Or expanding differently:
    # = (p_v - p_u)(p_v^2 - 16) - (p_u - 4)(p_v^2 - p_v*p_u)
    # Let's compute directly:
    det = (p_v - p_u)*(p_v + p_u - 8) + (4 - p_u)*(p_v**2 - p_u**2)
    return det

def is_valid_pair(p_u, p_v):
    # Check if determinant is non-zero
    M = [[1, p_u, p_u**2], [1, p_v, p_v**2], [1, 4, 16]]
    det = M[0][0]*(M[1][1]*M[2][2] - M[1][2]*M[2][1]) - M[0][1]*(M[1][0]*M[2][2] - M[1][2]*M[2][0]) + M[0][2]*(M[1][0]*M[2][1] - M[1][1]*M[2][0])
    return det != 0

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1  # Convert to 0-based indexing
        v = int(data[idx+1]) - 1
        edges.append((u, v))
        idx += 2
    
    # For each pair of frequencies, precompute validity with beacon=4
    valid = [[False]*4 for _ in range(4)]
    for i in range(1,4):
        for j in range(1,4):
            valid[i][j] = is_valid_pair(i, j)
    
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Try all assignments in lexicographical order using backtracking
    assignment = [0] * n  # 0 means unassigned
    
    def backtrack(pos):
        if pos == n:
            return True
            
        for freq in range(1, 4):
            # Check if assigning freq to pos is valid with all neighbors
            valid_assignment = True
            for neighbor in adj[pos]:
                if assignment[neighbor] != 0:
                    if not valid[freq][assignment[neighbor]]:
                        valid_assignment = False
                        break
            if valid_assignment:
                assignment[pos] = freq
                if backtrack(pos + 1):
                    return True
                assignment[pos] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(' '.join(map(str, assignment)))
    else:
        print("NO")

solve()