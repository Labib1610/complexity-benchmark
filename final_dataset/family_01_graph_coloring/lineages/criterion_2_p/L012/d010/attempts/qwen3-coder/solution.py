import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    adj = [[] for _ in range(n)]
    edge_indices = [[] for _ in range(n)]
    
    idx = 2
    for i in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        idx += 2
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
        edge_indices[u].append(i)
        edge_indices[v].append(i)
    
    # If no constraints, assign all 1s
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Color each component with BFS
    color = [-1] * n
    visited = [False] * n
    
    for start in range(n):
        if visited[start]:
            continue
            
        # BFS to check bipartiteness and get a valid coloring
        queue = deque()
        queue.append(start)
        visited[start] = True
        color[start] = 0  # Start with color 0
        
        while queue:
            u = queue.popleft()
            current_color = color[u]
            opposite_color = 1 - current_color
            
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    color[v] = opposite_color
                    queue.append(v)
                else:
                    # Check if the edge constraint is satisfied
                    if color[v] == current_color:
                        print("NO")
                        return
    
    # Now we have a valid 2-coloring. We need the lexicographically smallest.
    # That means we prefer color 0 to map to 1 and color 1 to map to 2.
    # But we can also swap colors in each component to get a lex smaller result.
    
    # Actually, since we fixed the starting node's color to 0, and the graph is bipartite,
    # the coloring is determined. To make it lex smallest, for each component,
    # we should choose whether to map 0->1,1->2 or 0->2,1->1 based on which gives lex smaller.
    
    # Let's re-process components to allow choosing the better mapping.
    
    color_final = [-1] * n
    visited_final = [False] * n
    
    for start in range(n):
        if visited_final[start]:
            continue
            
        # Collect all nodes in this component
        component = []
        queue = deque()
        queue.append(start)
        visited_final[start] = True
        component.append(start)
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not visited_final[v]:
                    visited_final[v] = True
                    queue.append(v)
                    component.append(v)
        
        # Try both mappings for this component and pick the lex smaller one
        # Mapping 0: color -> color+1 (0->1, 1->2)
        # Mapping 1: color -> 2-color (0->2, 1->1)
        
        def get_assignment(mapping_type):
            assgn = [0] * len(component)
            for i, node in enumerate(component):
                c = color[node]
                if mapping_type == 0:
                    assgn[i] = c + 1
                else:
                    assgn[i] = 2 - c
            return assgn
        
        # Get the two possible assignments for this component
        comp_nodes_sorted = sorted(component)
        assgn0_list = get_assignment(0)
        assgn1_list = get_assignment(1)
        
        # Create sequences for comparison
        seq0 = []
        seq1 = []
        node_to_index = {node: i for i, node in enumerate(comp_nodes_sorted)}
        
        temp_assgn0 = [0] * len(component)
        temp_assgn1 = [0] * len(component)
        for i, node in enumerate(component):
            pos = node_to_index[node]
            c = color[node]
            temp_assgn0[pos] = c + 1
            temp_assgn1[pos] = 2 - c
            
        # Compare sequences
        use_mapping = 0 if temp_assgn0 <= temp_assgn1 else 1
        
        # Assign the chosen mapping
        for node in component:
            c = color[node]
            if use_mapping == 0:
                color_final[node] = c + 1
            else:
                color_final[node] = 2 - c
    
    # Final validation: check all edges
    for u, v in edges:
        if color_final[u] == color_final[v]:
            print("NO")
            return
            
    print("YES")
    print(" ".join(map(str, color_final)))

if __name__ == "__main__":
    main()