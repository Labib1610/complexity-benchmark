import sys
from itertools import combinations

def find_shift_assignment(n, edges):
    # Initialize graph adjacency matrix and degree array
    G = [[False] * n for _ in range(n)]
    deg = [0] * n
    
    # Fill the adjacency matrix based on the given edges
    for u, v in edges:
        u -= 1
        v -= 1
        G[u][v] = True
        G[v][u] = True
        deg[u] += 1
        deg[v] += 1
    
    # Calculate number of shifts needed (max degree + 1)
    k = max(deg) + 1

    # Sort nodes by decreasing degree to prioritize larger degree nodes
    sorted_nodes = sorted(range(n), key=lambda x: -deg[x])
    
    # Initialize assignment array
    assg = [0] * n
    
    for i in range(k):
        used = set()
        
        for v in sorted_nodes:
            if assg[v] != 0:
                continue
            
            can_be_assigned = True
            for u in range(n):
                if G[v][u]:
                    if assg[u] == i + 1 or (assg[u] == 0 and (i + 1) in used):
                        can_be_assigned = False
                        break
            
            if not can_be_assigned:
                continue
            
            assg[v] = i + 1
            used.add(i + 1)
        
        # Check if all nodes are assigned
        if all(assg[v] != 0 for v in range(n)):
            return ["YES"] + list(map(str, assg))
    
    return ["NO"]

# Reading input from standard input
input_data = sys.stdin.read().split()
n = int(input_data[0])
m = int(input_data[1])

edges = []
index = 2
for _ in range(m):
    u = int(input_data[index])
    v = int(input_data[index + 1])
    edges.append((u, v))
    index += 2

# Get the result from the function
result = find_shift_assignment(n, edges)

# Print the result to standard output
sys.stdout.write("\n".join(result) + "\n")