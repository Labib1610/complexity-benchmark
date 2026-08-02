import sys

# Increase recursion depth for deep DFS in large graphs
sys.setrecursionlimit(300000)

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    ptr = 2
    for _ in range(m):
        u = int(input_data[ptr])
        v = int(input_data[ptr + 1])
        adj[u].append(v)
        adj[v].append(u)
        ptr += 2
        
    # colors: 0 = unvisited, 1 = Shift 1, 2 = Shift 2
    colors = [0] * (n + 1)
    
    # To get the lexicographically smallest sequence, for each connected component,
    # we must decide whether the first node visited (the smallest index in the component)
    # should be assigned 1 or 2.
    # However, since we want the smallest sequence (s1, s2, ..., sn), 
    # we should process nodes in increasing order of their index.
    # If node i is not yet colored, it's the smallest index in its component.
    # Assigning it 1 is always better than assigning it 2 if both are valid.
    
    for i in range(1, n + 1):
        if colors[i] == 0:
            # Start a BFS/DFS to color the component
            # We want to see if assigning colors[i] = 1 is possible.
            # In a bipartite graph, if we fix the color of one node, 
            # the colors of all other nodes in that component are determined.
            
            stack = [i]
            colors[i] = 1
            component = [i]
            
            # Standard BFS/DFS to check bipartiteness and color the component
            # Using a manual stack to avoid recursion depth issues
            visited_idx = 0
            while visited_idx < len(component):
                u = component[visited_idx]
                visited_idx += 1
                
                for v in adj[u]:
                    if colors[v] == 0:
                        colors[v] = 3 - colors[u]
                        component.append(v)
                    elif colors[v] == colors[u]:
                        print("NO")
                        return
            
            # Now we have a valid coloring for this component.
            # We need to decide if we should flip all colors in this component
            # to make the sequence (s_i, s_{i+1}, ...) lexicographically smallest.
            # The smallest index in this component is 'i'. 
            # We already set colors[i] = 1, which is the smallest possible value for the 
            # first element of the component's contribution to the sequence.
            # Since the colors of all other nodes in the component are fixed relative to i,
            # setting colors[i] = 1 is the optimal choice for the lexicographical minimum.
            # (If we set colors[i] = 2, the sequence would start with 2 instead of 1).
            
    print("YES")
    print(*(colors[1:]))

if __name__ == "__main__":
    solve()