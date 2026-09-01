import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Since x_u^2 + x_v^2 = 5 and x_u, x_v in {1,2}
    # Only valid pairs are (1,2) and (2,1) since 1+4=5
    # So for every edge, one endpoint must be 1 and the other 2
    # This is equivalent to checking if the graph is bipartite
    
    color = [0] * (n + 1)  # 0: unvisited, 1: color 1, 2: color 2
    
    # Check each component
    for start in range(1, n + 1):
        if color[start] == 0:
            # BFS to check bipartiteness and assign colors
            queue = deque()
            queue.append(start)
            color[start] = 1  # Assign color 1 to start node
            
            while queue:
                u = queue.popleft()
                current_color = color[u]
                next_color = 3 - current_color  # flips 1->2 and 2->1
                
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = next_color
                        queue.append(v)
                    elif color[v] != next_color:
                        # Not bipartite - impossible to assign states
                        print("NO")
                        return
    
    # If we reach here, the graph is bipartite and we have a valid 2-coloring
    # We need the lexicographically smallest assignment
    # That means we want x_1 to be as small as possible, then x_2, etc.
    # In our coloring, we can choose which color represents 1 and which represents 2
    # For node 1, if it's colored 2, we'd prefer to swap colors so that node 1 gets state 1
    # But we must maintain the bipartite property
    
    # To get lex smallest, we decide the mapping based on the color of node 1
    # If color[1] == 2, we swap the meanings (color 2 -> state 1, color 1 -> state 2)
    # If color[1] == 1 or 0, we keep (color 1 -> state 1, color 2 -> state 2)
    
    # Actually, some nodes might be isolated (no edges). For those, we can assign state 1
    # to make the sequence lexicographically smaller
    
    result = []
    for i in range(1, n + 1):
        if color[i] == 0:
            # Isolated node - assign 1
            result.append(1)
        else:
            result.append(color[i])
    
    # But wait, we need to ensure this is truly lexicographically minimal
    # Let's think differently:
    # In a connected component, once we fix the color of one node, the rest are determined
    # To minimize lexicographically, for the first node that has an edge, 
    # we should try assigning it state 1
    
    # Let's re-assign with proper handling for lex smallest
    final_state = [0] * (n + 1)
    
    visited = [False] * (n + 1)
    
    for start in range(1, n + 1):
        if not visited[start]:
            # Do BFS again to assign states properly for lex order
            queue = deque()
            # For the root, choose state 1 to try to make lex smallest
            # But actually, we need to be more careful
            # Let's just follow the existing color but adjust for lex order
            
            # In the current color scheme:
            # If we map color 1 -> state 1 and color 2 -> state 2, we get one solution
            # If we map color 1 -> state 2 and color 2 -> state 1, we get another
            # We want the lexicographically smallest one
            
            # So for the first node in the component (by index), 
            # if its color is 2, we should swap the mapping
            
            # Find the first node in this component
            first_node_in_component = start
            
            queue.append(first_node_in_component)
            visited[first_node_in_component] = True
            
            # Decide mapping to get lex smallest
            if color[first_node_in_component] == 1:
                color1_to_state = 1
                color2_to_state = 2
            else:
                color1_to_state = 2
                color2_to_state = 1
                
            final_state[first_node_in_component] = color1_to_state if color[first_node_in_component] == 1 else color2_to_state
            
            while queue:
                u = queue.popleft()
                u_state = final_state[u]
                required_v_state = 3 - u_state  # because 1^2 + 2^2 = 2^2 + 1^2 = 5
                
                for v in adj[u]:
                    if not visited[v]:
                        # Determine what state v should have based on u
                        # But also check consistency with its color
                        visited[v] = True
                        # What state should v have?
                        target_state = required_v_state
                        
                        # Check if this is consistent with the color mapping
                        if color[v] == 1:
                            expected_state = color1_to_state
                        else:
                            expected_state = color2_to_state
                            
                        if target_state != expected_state:
                            # This indicates a logic issue, but since we confirmed bipartiteness,
                            # it should be fine. Just assign according to the constraint.
                            pass  # The constraint takes precedence over color mapping in terms of correctness
                            
                        final_state[v] = target_state
                        queue.append(v)
    
    # Handle isolated nodes - they can be assigned state 1 for lex smallest
    for i in range(1, n + 1):
        if final_state[i] == 0:
            final_state[i] = 1
    
    print("YES")
    print(' '.join(map(str, final_state[1:])))

if __name__ == "__main__":
    main()