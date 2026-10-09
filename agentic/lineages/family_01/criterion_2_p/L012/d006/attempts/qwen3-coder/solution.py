import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-based indexing
        v = int(data[index+1]) - 1
        edges.append((u, v))
        index += 2
    
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Color array: 0 means unvisited, 1 and 2 are the two colors
    color = [0] * n
    visited = [False] * n
    
    # Check bipartiteness for each component using BFS
    for start in range(n):
        if visited[start]:
            continue
        queue = deque()
        queue.append(start)
        color[start] = 1
        visited[start] = True
        
        while queue:
            node = queue.popleft()
            current_color = color[node]
            next_color = 3 - current_color  # flips 1->2 and 2->1
            
            for neighbor in adj[node]:
                # Check if the edge length constraint is satisfied
                # The constraint is: sqrt((u-v)^2 + (h_u - h_v)^2) = sqrt((u-v)^2 + 1)
                # This implies (h_u - h_v)^2 = 1 => |h_u - h_v| = 1
                # So adjacent nodes must have different heights (colors 1 and 2)
                if not visited[neighbor]:
                    visited[neighbor] = True
                    color[neighbor] = next_color
                    queue.append(neighbor)
                else:
                    # If already visited, check consistency
                    if color[neighbor] != next_color:
                        print("NO")
                        return
    
    # If we reach here, a valid 2-coloring exists
    # Now we need to choose the coloring that minimizes the weighted sum
    # For each component, we can choose to flip all colors or not
    # We'll do a second BFS/DFS to determine the best assignment per component
    
    # To minimize sum h_i * 3^(n-1-i), we prefer more 1's earlier
    # But since we must satisfy constraints, we just pick a valid coloring
    
    # Let's just use the coloring we found, but ensure it's the lex smallest
    # Actually, the problem asks for minimizing sum h_i * 3^(n-i)
    # Since 3^(n-i) decreases with increasing i, we want smaller h_i for smaller i
    # But we're constrained by the graph structure (bipartite coloring)
    # So within the constraints, we can choose the coloring that gives minimum sum
    
    # For a connected bipartite graph, there are two valid colorings (swap 1 and 2)
    # We can choose the one that minimizes the sum
    
    # Let's re-traverse each component and decide the best coloring
    
    # Reset visited for component traversal
    visited = [False] * n
    final_color = [0] * n
    
    for start in range(n):
        if visited[start]:
            continue
        # Collect all nodes in this component
        component = []
        queue = deque([start])
        visited[start] = True
        component.append(start)
        
        while queue:
            node = queue.popleft()
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    component.append(neighbor)
        
        # For this component, we have two possible colorings
        # One where color[start] = 1, the other where color[start] = 2
        # Compute sum for both and pick the better one
        
        # Current assignment based on previous BFS
        sum1 = 0
        sum2 = 0
        mapping1 = {}  # original_color -> new_color
        mapping2 = {}  # original_color -> flipped new_color
        
        # Determine mappings
        orig_c1 = color[start]
        orig_c2 = 3 - orig_c1
        
        # Mapping 1: keep original
        mapping1[orig_c1] = 1
        mapping1[orig_c2] = 2
        # Mapping 2: flip
        mapping2[orig_c1] = 2
        mapping2[orig_c2] = 1
        
        for u in component:
            c_orig = color[u]
            c1 = mapping1[c_orig]
            c2 = mapping2[c_orig]
            power = n - 1 - u
            weight = 3 ** power
            sum1 += c1 * weight
            sum2 += c2 * weight
        
        # Choose the mapping that gives smaller sum
        chosen_mapping = mapping1 if sum1 <= sum2 else mapping2
        
        # Assign final colors
        for u in component:
            final_color[u] = chosen_mapping[color[u]]
    
    # Verify all edges satisfy the constraint
    for u, v in edges:
        if abs(final_color[u] - final_color[v]) != 1:
            print("NO")
            return
    
    print("YES")
    print(' '.join(map(str, final_color)))

if __name__ == "__main__":
    main()