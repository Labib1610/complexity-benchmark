import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, input().split())
    
    # Build adjacency list
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Check the resonance condition: 2(s_u^2 + s_v^2) = 5*s_u*s_v
    # Let's check all possible assignments for s_u and s_v
    # s_u=1, s_v=1: 2(1+1) = 4, 5*1*1 = 5 → 4 ≠ 5
    # s_u=1, s_v=2: 2(1+4) = 10, 5*1*2 = 10 → 10 = 10 ✓
    # s_u=2, s_v=1: 2(4+1) = 10, 5*2*1 = 10 → 10 = 10 ✓
    # s_u=2, s_v=2: 2(4+4) = 16, 5*2*2 = 20 → 16 ≠ 20
    # So valid assignments are (1,2) and (2,1) - this is a bipartite graph constraint
    
    # Color the graph with 2 colors (1 and 2)
    color = [0] * (n + 1)  # 0: unvisited, 1: color 1, 2: color 2
    visited = [False] * (n + 1)
    
    for start in range(1, n + 1):
        if not visited[start]:
            # BFS to check bipartiteness
            queue = deque([start])
            color[start] = 1
            visited[start] = True
            
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        color[v] = 3 - color[u]  # Flip color (1->2, 2->1)
                        queue.append(v)
                    elif color[v] == color[u]:
                        # Not bipartite - no valid assignment
                        print("NO")
                        return
    
    # If we reach here, the graph is bipartite and a valid assignment exists
    # To minimize structural weight, we want smaller values (1) at higher indices
    # Since we can choose which color is 1 and which is 2 for each component,
    # we should make the color that appears more frequently at higher indices be 1
    
    # For each connected component, count how many nodes have each color
    # and decide which color should be 1 and which should be 2
    components = []
    visited_comp = [False] * (n + 1)
    
    for start in range(1, n + 1):
        if not visited_comp[start]:
            # Find all nodes in this component
            component_nodes = []
            queue = deque([start])
            visited_comp[start] = True
            component_nodes.append(start)
            
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if not visited_comp[v]:
                        visited_comp[v] = True
                        component_nodes.append(v)
                        queue.append(v)
            
            components.append(component_nodes)
    
    # For each component, decide optimal coloring to minimize weight
    final_color = color[:]  # Copy of the initial coloring
    
    for component in components:
        count_1 = sum(1 for node in component if color[node] == 1)
        count_2 = len(component) - count_1
        
        # If there are more 2s than 1s, swap the colors in this component
        # to minimize the structural weight
        if count_2 > count_1:
            for node in component:
                final_color[node] = 3 - color[node]
    
    print("YES")
    result = [str(final_color[i]) for i in range(1, n + 1)]
    print(" ".join(result))

solve()