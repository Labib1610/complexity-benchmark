import sys
from collections import defaultdict, deque

def solve():
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
        v = int(data[index + 1]) - 1
        index += 2
        edges.append((u, v))
        graph[u].append(v)
        graph[v].append(u)
    
    # 0 means unset, 1 means factor 1, 2 means factor 2
    color = [0] * n
    
    # Check if the graph is bipartite (since product must be 2, one must be 1 and other 2)
    # So each edge connects a node with value 1 to a node with value 2
    for i in range(n):
        if color[i] == 0:
            queue = deque()
            queue.append(i)
            color[i] = 1  # Assign 1 to the starting node
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                neighbor_color = 3 - current_color  # 1 -> 2, 2 -> 1
                
                for neighbor in graph[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = neighbor_color
                        queue.append(neighbor)
                    elif color[neighbor] != neighbor_color:
                        print("NO")
                        return
    
    # Now we have a valid 2-coloring. We need to choose the lex smallest assignment.
    # For each component, we can choose which color is 1 and which is 2.
    # We want to minimize in lexicographical order.
    
    # Let's find connected components
    visited = [False] * n
    components = []
    
    for i in range(n):
        if not visited[i]:
            comp_nodes = []
            queue = deque([i])
            visited[i] = True
            comp_nodes.append(i)
            
            while queue:
                node = queue.popleft()
                for nei in graph[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        queue.append(nei)
                        comp_nodes.append(nei)
            
            components.append(comp_nodes)
    
    # For each component, decide whether to flip colors to get lex smallest
    result = [0] * n
    
    for comp in components:
        # Two options: original coloring or flipped
        option1 = []
        option2 = []
        
        for node in comp:
            c = color[node]
            option1.append((node, c))
            option2.append((node, 3 - c))
        
        # Build arrays for comparison
        arr1 = [0] * n
        arr2 = [0] * n
        
        for node, val in option1:
            arr1[node] = val
        for node, val in option2:
            arr2[node] = val
            
        # Find first differing index
        k = 0
        while k < n and arr1[k] == arr2[k]:
            k += 1
            
        if k == n:
            # All same, choose option1 (original)
            chosen = option1
        elif arr1[k] < arr2[k]:
            chosen = option1
        else:
            chosen = option2
            
        for node, val in chosen:
            result[node] = val
    
    # But wait, we should handle isolated nodes (no edges). They can be set to 1.
    for i in range(n):
        if color[i] == 0:
            result[i] = 1
    
    print("YES")
    print(" ".join(map(str, result)))

solve()