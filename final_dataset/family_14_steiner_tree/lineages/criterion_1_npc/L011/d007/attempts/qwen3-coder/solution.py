import sys
from itertools import combinations

def find_min_cost(n, m, t, essential_vars, constraints):
    # If there's only one essential variable, no constraints needed
    if t <= 1:
        return 0
    
    # Convert essential_vars to a set for faster lookup
    essential_set = set(essential_vars)
    
    # Create a graph representation
    graph = [[] for _ in range(n + 1)]
    edge_weights = {}
    
    for u, v, w in constraints:
        graph[u].append((v, w))
        graph[v].append((u, w))
        edge_weights[(u, v)] = w
        edge_weights[(v, u)] = w
    
    # Generate all possible subsets of nodes that include all essential variables
    min_cost = float('inf')
    
    # Try all possible combinations of non-essential variables to include
    non_essential = [i for i in range(1, n + 1) if i not in essential_set]
    
    # Iterate through all possible subsets of non-essential variables
    for r in range(len(non_essential) + 1):
        for extra_nodes in combinations(non_essential, r):
            # Current set of nodes
            node_set = essential_vars + list(extra_nodes)
            node_set_size = len(node_set)
            
            # We need exactly node_set_size - 1 edges for a tree
            if node_set_size <= 1:
                min_cost = min(min_cost, 0)
                continue
            
            # Find minimum spanning tree on this subset using the available edges
            # Use Prim's algorithm
            included = [False] * (n + 1)
            min_edge = [float('inf')] * (n + 1)
            min_edge[node_set[0]] = 0
            
            mst_weight = 0
            nodes_in_mst = 0
            
            # Create a mapping for node indices in node_set
            node_index = {node_set[i]: i for i in range(len(node_set))}
            
            for _ in range(node_set_size):
                # Find the vertex with minimum key value
                u = -1
                for j in range(node_set_size):
                    if not included[node_set[j]]:
                        if u == -1 or min_edge[node_set[j]] < min_edge[u]:
                            u = node_set[j]
                
                # If no reachable node, this subset is disconnected
                if min_edge[u] == float('inf'):
                    break
                
                # Add the picked vertex to MST
                included[u] = True
                mst_weight += min_edge[u]
                nodes_in_mst += 1
                
                # Update key values of adjacent vertices
                for v, weight in graph[u]:
                    if v in node_index and not included[v] and weight < min_edge[v]:
                        min_edge[v] = weight
            
            # Check if we have a valid spanning tree
            if nodes_in_mst == node_set_size:
                # Now check the intermediary justification rule
                # Count degree of each non-essential node in the MST
                degree = [0] * (n + 1)
                
                # Reconstruct the MST edges to check degrees
                # This is a simplified check - in practice we'd need to track the actual MST edges
                # But since we're using Prim's, we can approximate this check
                
                # For simplicity, let's do a more precise check by actually building the MST
                # and then verifying the intermediary rule
                
                # Let's rebuild with edge tracking
                included_edges = [False] * len(constraints)
                included_nodes = [False] * (n + 1)
                min_edge_with_edge = [(float('inf'), -1, -1)] * (n + 1)  # (weight, u, v)
                min_edge_with_edge[node_set[0]] = (0, -1, -1)
                
                mst_weight_precise = 0
                nodes_in_mst_precise = 0
                mst_edges = []
                
                for _ in range(node_set_size):
                    u = -1
                    for j in range(node_set_size):
                        if not included_nodes[node_set[j]]:
                            if u == -1 or min_edge_with_edge[node_set[j]][0] < min_edge_with_edge[u][0]:
                                u = node_set[j]
                    
                    if min_edge_with_edge[u][0] == float('inf'):
                        break
                    
                    included_nodes[u] = True
                    mst_weight_precise += min_edge_with_edge[u][0]
                    nodes_in_mst_precise += 1
                    
                    # Add edge to MST if it exists
                    if min_edge_with_edge[u][1] != -1:
                        mst_edges.append((min_edge_with_edge[u][1], u))
                    
                    # Update adjacent vertices
                    for v, weight in graph[u]:
                        if v in node_index and not included_nodes[v] and weight < min_edge_with_edge[v][0]:
                            min_edge_with_edge[v] = (weight, u, v)
                
                if nodes_in_mst_precise == node_set_size:
                    # Check intermediary rule
                    degree_count = [0] * (n + 1)
                    for edge in mst_edges:
                        degree_count[edge[0]] += 1
                        degree_count[edge[1]] += 1
                    
                    valid = True
                    for node in node_set:
                        if node not in essential_set and degree_count[node] < 2:
                            valid = False
                            break
                    
                    if valid:
                        min_cost = min(min_cost, mst_weight_precise)
    
    return min_cost

# Read input
line1 = list(map(int, sys.stdin.readline().split()))
n, m, t = line1[0], line1[1], line1[2]

essential_vars = list(map(int, sys.stdin.readline().split()))

constraints = []
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    constraints.append((u, v, w))

# Solve and print result
result = find_min_cost(n, m, t, essential_vars, constraints)
print(result)