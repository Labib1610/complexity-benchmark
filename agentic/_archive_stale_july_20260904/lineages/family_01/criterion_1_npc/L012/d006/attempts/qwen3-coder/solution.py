from collections import defaultdict
import sys

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    adj = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # Try all valid colorings for connected components
    # Each component can be colored with at most 2 colors from {1,2,3}
    
    # Color each component
    color = [0] * (n + 1)  # 1-indexed
    visited = [False] * (n + 1)
    
    # Check if we can 2-color a component (bipartite check)
    def bipartite_check(start):
        queue = [start]
        color[start] = 1
        visited[start] = True
        
        while queue:
            node = queue.pop(0)
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    color[neighbor] = 3 - color[node]  # Flip between 1 and 2
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
        return True
    
    # Find connected components and check if each is bipartite
    components = []
    comp_colors = []  # To store available colors for each component
    
    for i in range(1, n + 1):
        if not visited[i]:
            # New component
            # Check if it's bipartite
            if not bipartite_check(i):
                print("NO")
                return
            
            # Collect nodes in this component
            comp_nodes = []
            for j in range(1, n + 1):
                if color[j] != 0 and (j == i or visited[j]):
                    comp_nodes.append(j)
            
            components.append(comp_nodes)
    
    # Now we need to assign actual colors from {1,2,3} to components
    # such that for each edge, endpoints have different colors
    
    # For each component, we have two color classes
    # We can choose which real colors to use for these classes
    
    best_assignment = None
    min_hash = float('inf')
    
    # Generate all valid assignments
    # For each component, decide which 2 of 3 colors to use
    # But since we want to minimize hash, we should try assignments systematically
    
    # Let's try a different approach: enumerate all valid global colorings
    
    # Since each component is bipartite, we can try all combinations
    # But this might be too many. Let's think differently.
    
    # Actually, let's do backtracking with constraint checking
    
    def get_component_structure(node):
        # Get all nodes in component and their bipartition
        visited_local = [False] * (n + 1)
        color_local = [0] * (n + 1)
        
        def dfs(v, c):
            visited_local[v] = True
            color_local[v] = c
            part1 = []
            part2 = []
            if c == 1:
                part1.append(v)
            else:
                part2.append(v)
                
            for u in adj[v]:
                if not visited_local[u]:
                    p1, p2 = dfs(u, 3 - c)
                    part1.extend(p1)
                    part2.extend(p2)
                # Check for odd cycle during traversal
                elif color_local[u] == c:
                    return None, None  # Not bipartite
                    
            return part1, part2
        
        return dfs(node, 1)
    
    # Reset visited for component analysis
    visited_comp = [False] * (n + 1)
    component_info = []
    
    for i in range(1, n + 1):
        if not visited_comp[i]:
            part_result = get_component_structure(i)
            if part_result[0] is None:  # Not bipartite
                print("NO")
                return
            part1, part2 = part_result
            component_info.append((part1, part2))
            for node in part1 + part2:
                visited_comp[node] = True
    
    # Now try all valid color assignments to minimize hash
    # For each component, we have two parts that must have different colors
    # We can choose any 2 different colors from {1,2,3} for the parts
    
    # Try all 6 permutations for each component and pick the best
    from itertools import permutations
    
    def calculate_hash(colors):
        h = 0
        power = 2 ** (2 * n - 2)
        for i in range(1, n + 1):
            h += colors[i] * power
            power //= 4
        return h
    
    # Brute force small cases
    # Generate all valid colorings
    final_coloring = [0] * (n + 1)
    found = False
    
    # Try all combinations of color assignments to components
    num_components = len(component_info)
    
    # For each component, we have 6 ways to assign 2 colors to its parts
    color_options = list(permutations([1, 2, 3], 2))  # [(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)]
    
    def backtrack(comp_idx, current_coloring):
        nonlocal found, min_hash, best_assignment
        
        if comp_idx == num_components:
            # Check if this coloring satisfies all constraints
            valid = True
            for u, v in edges:
                if current_coloring[u] == current_coloring[v]:
                    valid = False
                    break
            
            if valid:
                h = calculate_hash(current_coloring)
                if h < min_hash:
                    min_hash = h
                    best_assignment = current_coloring[:]
            return
        
        part1, part2 = component_info[comp_idx]
        for c1, c2 in color_options:
            old_colors = {}
            # Assign c1 to part1, c2 to part2
            for node in part1:
                old_colors[node] = current_coloring[node]
                current_coloring[node] = c1
            for node in part2:
                old_colors[node] = current_coloring[node]
                current_coloring[node] = c2
                
            backtrack(comp_idx + 1, current_coloring)
            
            # Restore
            for node in part1 + part2:
                current_coloring[node] = old_colors[node]
    
    # Initialize with a default coloring
    initial_coloring = [1] * (n + 1)
    backtrack(0, initial_coloring)
    
    if min_hash == float('inf'):
        print("NO")
    else:
        print("YES")
        result = []
        for i in range(1, n + 1):
            result.append(str(best_assignment[i]))
        print(" ".join(result))

solve()