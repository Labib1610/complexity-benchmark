import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build graph
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Color array: 0 = unvisited, 1 and 2 are the two colors
    color = [0] * (n + 1)
    visited = [False] * (n + 1)
    
    # Check bipartiteness for each connected component
    for start in range(1, n + 1):
        if visited[start]:
            continue
            
        queue = deque()
        queue.append(start)
        visited[start] = True
        color[start] = 1  # Start with color 1
        
        while queue:
            u = queue.popleft()
            current_color = color[u]
            next_color = 2 if current_color == 1 else 1
            
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    color[v] = next_color
                    queue.append(v)
                elif color[v] != next_color:
                    print("NO")
                    return
    
    # If we reach here, the graph is bipartite
    # We need the lexicographically smallest assignment
    # That means we prefer to assign person i to period 1 if possible
    # Since our coloring already ensures bipartiteness, and we started with color[1] = 1,
    # we just need to make sure node 1 gets color 1.
    # But actually, we want the lex smallest among all valid colorings.
    # A valid coloring can be (color) or (3-color). 
    # To get lex smallest, for each component, we choose the coloring that gives smaller value to node with smallest index in that component.
    
    # Let's re-do the coloring to ensure lex smallest
    color_final = [0] * (n + 1)
    visited_final = [False] * (n + 1)
    
    for start in range(1, n + 1):
        if visited_final[start]:
            continue
            
        # BFS to find component and determine which coloring is lex smaller
        component_nodes = []
        queue = deque()
        queue.append(start)
        visited_final[start] = True
        color_temp = {start: 1}
        component_nodes.append(start)
        
        bipartite = True
        while queue and bipartite:
            u = queue.popleft()
            current_color = color_temp[u]
            next_color = 2 if current_color == 1 else 1
            
            for v in adj[u]:
                if v not in color_temp:
                    color_temp[v] = next_color
                    visited_final[v] = True
                    component_nodes.append(v)
                    queue.append(v)
                elif color_temp[v] != next_color:
                    bipartite = False
                    break
        
        if not bipartite:
            print("NO")
            return
            
        # Determine which coloring is lex smaller
        min_node = min(component_nodes)
        if color_temp[min_node] == 1:
            # Keep as is
            for node in component_nodes:
                color_final[node] = color_temp[node]
        else:
            # Flip colors
            for node in component_nodes:
                color_final[node] = 3 - color_temp[node]
    
    print("YES")
    print(" ".join(str(color_final[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    main()