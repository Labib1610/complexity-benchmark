import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    edges = []
    graph = defaultdict(list)
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index+1]) - 1
        index += 2
        edges.append((u, v))
        graph[u].append(v)
        graph[v].append(u)
    
    # The constraint is sum of (r_u - r_v)^2 = m
    # Since r_u, r_v ∈ {1,2}, (r_u - r_v)^2 ∈ {0,1}
    # So we need exactly m edges where r_u ≠ r_v
    # This is equivalent to finding a bipartition where exactly m edges cross the partition
    
    # First check if the graph has a valid coloring (bipartite)
    color = [-1] * n
    components = []
    visited = [False] * n
    
    for start in range(n):
        if visited[start] or not graph[start]:
            continue
        # BFS to find component and check bipartiteness
        queue = deque()
        queue.append(start)
        color[start] = 0
        visited[start] = True
        comp_nodes = []
        
        is_bipartite = True
        while queue:
            u = queue.popleft()
            comp_nodes.append(u)
            current_color = color[u]
            for v in graph[u]:
                if color[v] == -1:
                    color[v] = 1 - current_color
                    visited[v] = True
                    queue.append(v)
                elif color[v] == current_color:
                    is_bipartite = False
        
        if not is_bipartite:
            print("NO")
            return
            
        components.append(comp_nodes)
    
    # For isolated nodes (not in any edge), assign 1
    # Now for each component, we can choose which side gets 1 or 2
    # We want to minimize the number of edges that are "satisfied" (i.e., have different endpoints)
    # And we want exactly m such edges
    
    # Let's build a model: for each component, we can choose to flip or not
    # Flipping swaps which color class gets 1 or 2
    # For each component, compute how many edges are satisfied with normal coloring vs flipped
    
    # But actually, let's think differently.
    # Each component is bipartite. Let's say parts are A and B.
    # If we assign 1 to A and 2 to B: satisfied edges = E_AB
    # If we assign 2 to A and 1 to B: satisfied edges = E_AB
    # Wait, that's the same. No, because satisfied means r_u != r_v, i.e., they are in different parts.
    # So for a component, the number of satisfied edges is always the number of edges between A and B.
    # So the total satisfied edges is fixed.
    
    # Compute total number of edges that are satisfied in any valid 2-coloring
    total_satisfied = 0
    component_info = []  # list of (nodes_in_A, nodes_in_B, edges_between_A_B)
    
    for comp_nodes in components:
        # Re-color this component properly
        local_color = {}
        queue_local = deque()
        start_node = comp_nodes[0]
        local_color[start_node] = 0
        queue_local.append(start_node)
        
        A = set()
        B = set()
        A.add(start_node)
        
        edge_count = 0
        while queue_local:
            u = queue_local.popleft()
            c = local_color[u]
            for v in graph[u]:
                edge_count += 1
                if v not in local_color:
                    local_color[v] = 1 - c
                    if local_color[v] == 0:
                        A.add(v)
                    else:
                        B.add(v)
                    queue_local.append(v)
                elif local_color[v] == local_color[u]:
                    print("NO")
                    return
        
        edge_count //= 2  # since we counted each edge twice
        component_info.append((list(A), list(B), edge_count))
        total_satisfied += edge_count
    
    if total_satisfied != m:
        print("NO")
        return
        
    # Now we need to construct the assignment
    # For each component, we can choose which part gets 1 or 2, but it doesn't change the count
    # We just need to make the result lexicographically smallest
    
    # Assign colors to minimize lex order
    result = [1] * n  # default for isolated vertices
    
    for A, B, _ in component_info:
        # Try both assignments and pick the lex smaller one
        option1 = {}
        option2 = {}
        
        for u in A:
            option1[u] = 1
            option2[u] = 2
        for u in B:
            option1[u] = 2
            option2[u] = 1
            
        # Compare which one gives lexicographically smaller sequence
        use_option = option1
        for i in range(n):
            if i in option1:
                val1 = option1[i]
                val2 = option2[i]
                if val1 < val2:
                    use_option = option1
                    break
                elif val2 < val1:
                    use_option = option2
                    break
                    
        for u in A:
            result[u] = use_option[u]
        for u in B:
            result[u] = use_option[u]
            
    print("YES")
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()