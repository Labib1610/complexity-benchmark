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
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        if u == v:
            print("NO")
            return
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
    
    # We need s_u & s_v = 0
    # States are 1 (binary 01) and 2 (binary 10)
    # 1 & 1 = 1 ≠ 0
    # 1 & 2 = 0 ✓
    # 2 & 2 = 2 ≠ 0
    # So adjacent nodes must have different states
    
    # This is a bipartite graph check
    color = [0] * (n + 1)  # 0: unvisited, 1: color 1, 2: color 2
    
    # Check each connected component
    for start in range(1, n + 1):
        if color[start] != 0:
            continue
        queue = deque()
        queue.append(start)
        color[start] = 1  # Assign color 1 to start node
        
        while queue:
            u = queue.popleft()
            current_color = color[u]
            next_color = 3 - current_color  # flips 1->2, 2->1
            
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = next_color
                    queue.append(v)
                elif color[v] == current_color:
                    print("NO")
                    return
    
    # If we reach here, the graph is bipartite
    # Now we need the lexicographically smallest assignment
    # In our coloring, color 1 should be state 1, color 2 should be state 2
    # But we want the lex smallest, so among valid assignments,
    # we prefer earlier positions to have smaller values
    
    # Actually, since we're just assigning colors and the constraints are symmetric,
    # any valid 2-coloring works. To get lex smallest, we should try to make
    # earlier-numbered nodes have state 1 if possible.
    
    # Let's reframe: for each component, we can choose which color gets state 1
    # To minimize lex order, for each component, look at the earliest node,
    # and assign it state 1.
    
    # But actually, our BFS already gives a valid 2-coloring.
    # To get the lex smallest, we can do as follows:
    # For each connected component, determine whether to flip the colors
    # based on making the result lexicographically smallest.
    
    # A simpler way: run BFS but always try to assign state 1 to lower-numbered nodes first
    
    final_state = [0] * (n + 1)
    
    visited = [False] * (n + 1)
    for start in range(1, n + 1):
        if visited[start]:
            continue
            
        # Determine the "canonical" assignment for this component
        # We'll do BFS again, but decide for each component whether to flip colors
        # to get the lex smallest result
        
        component_nodes = []
        queue = deque()
        queue.append(start)
        visited[start] = True
        component_nodes.append(start)
        
        temp_color = [0] * (n + 1)
        temp_color[start] = 1
        
        while queue:
            u = queue.popleft()
            c = temp_color[u]
            opp_c = 3 - c
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    temp_color[v] = opp_c
                    queue.append(v)
                    component_nodes.append(v)
                else:
                    if temp_color[v] == c:
                        print("NO")
                        return
        
        # Now, for this component, decide whether to flip colors
        # to get lex smallest
        # We want the node with the smallest index in this component to have state 1
        min_node = min(component_nodes)
        if temp_color[min_node] == 2:
            # Flip the colors for this component
            for v in component_nodes:
                final_state[v] = 3 - temp_color[v]
        else:
            for v in component_nodes:
                final_state[v] = temp_color[v]
    
    print("YES")
    print(" ".join(str(final_state[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    main()