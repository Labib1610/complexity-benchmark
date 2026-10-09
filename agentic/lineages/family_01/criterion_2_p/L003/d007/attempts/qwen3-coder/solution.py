import sys
from collections import defaultdict, deque

def matrix_multiply(A, B):
    """Multiply two 4x4 matrices"""
    result = [[0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                result[i][j] += A[i][k] * B[k][j]
    return result

def is_zero_matrix(M):
    """Check if a 4x4 matrix is all zeros"""
    for i in range(4):
        for j in range(4):
            if M[i][j] != 0:
                return False
    return True

# Define the two matrices
M1 = [
    [-8, -5, 4, 5],
    [-10, -6, 5, 6],
    [-16, -10, 8, 10],
    [-10, -6, 5, 6]
]

M2 = [
    [6, 1, -2, -2],
    [10, -4, -2, 0],
    [10, 13, -6, -10],
    [13, -12, -1, 4]
]

# Precompute problematic combinations
# Check M1*M1, M1*M2, M2*M1, M2*M2
products = {}
products[(1,1)] = matrix_multiply(M1, M1)
products[(1,2)] = matrix_multiply(M1, M2)
products[(2,1)] = matrix_multiply(M2, M1)
products[(2,2)] = matrix_multiply(M2, M2)

# Check which combinations lead to zero matrix (in either direction)
forbidden = set()
for s1 in [1, 2]:
    for s2 in [1, 2]:
        if is_zero_matrix(products[(s1, s2)]) or is_zero_matrix(products[(s2, s1)]):
            forbidden.add((s1, s2))
            forbidden.add((s2, s1))

# Read input
n, m = map(int, sys.stdin.readline().split())
edges = []
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    edges.append((u-1, v-1))  # Convert to 0-indexed

# Build adjacency list
adj = defaultdict(list)
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)

# Check if bipartite (2-colorable) - this is necessary because we can't have
# adjacent nodes with modes that form forbidden pairs
# But we also need to consider the constraint that certain mode pairs are forbidden

# For our specific case, let's check what pairs are actually forbidden
# From the problem, we need to avoid M_u * M_v = 0 or M_v * M_u = 0

# Let's compute which mode pairs are forbidden:
# (1,1): Check M1*M1 and M1*M1 - both same
# (1,2): Check M1*M2 and M2*M1 
# (2,1): Check M2*M1 and M1*M2 - same as above
# (2,2): Check M2*M2 and M2*M2 - both same

bad_pairs = set()
for s1 in [1, 2]:
    for s2 in [1, 2]:
        if (s1, s2) in forbidden:
            bad_pairs.add((s1, s2))

# This is a graph coloring problem with constraints
# We want to color vertices with colors 1,2 such that no edge connects vertices
# with a bad pair of colors

# This is equivalent to checking if we can 2-color the graph with additional constraints

def solve():
    if n == 0:
        return [1] * 0
    
    # Color array: 0=unvisited, 1=color1, 2=color2
    color = [0] * n
    visited = [False] * n
    
    # For each connected component
    for start in range(n):
        if visited[start]:
            continue
            
        # BFS to color the component
        queue = deque([start])
        color[start] = 1  # Start with color 1 for lex smallest
        visited[start] = True
        
        while queue:
            node = queue.popleft()
            node_color = color[node]
            
            # Check all neighbors
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    # Try to assign a valid color
                    found_color = False
                    # Try colors 1, 2 in order for lex smallest result
                    for c in [1, 2]:
                        if (node_color, c) not in bad_pairs:
                            color[neighbor] = c
                            visited[neighbor] = True
                            queue.append(neighbor)
                            found_color = True
                            break
                    
                    if not found_color:
                        return None  # No valid coloring
                else:
                    # Already colored, check if the pair is valid
                    if (color[node], color[neighbor]) in bad_pairs:
                        return None
    
    return color

result = solve()
if result is None:
    print("NO")
else:
    print("YES")
    print(' '.join(map(str, result)))