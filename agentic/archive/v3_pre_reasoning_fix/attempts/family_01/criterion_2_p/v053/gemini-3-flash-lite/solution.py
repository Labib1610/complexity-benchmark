import sys

# Increase recursion depth for deep DFS
sys.setrecursionlimit(300000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    color = [0] * (n + 1)
    
    # We want lexicographically smallest assignment.
    # For each connected component, we have two possible colorings (swapping 1s and 2s).
    # To be lexicographically smallest, for each component, we should choose the coloring 
    # that results in the smaller value (1 or 2) for the smallest index node in that component.
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # Component found. Perform BFS/DFS to find all nodes.
            component = []
            stack = [i]
            color[i] = 1
            component.append(i)
            
            idx_comp = 0
            while idx_comp < len(component):
                u = component[idx_comp]
                idx_comp += 1
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        component.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
            
            # Now we check if we should flip this component.
            # The component is colored with 1s and 2s.
            # If the node with the smallest index in this component is currently 2,
            # we must flip all 1s to 2s and all 2s to 1s to make it lexicographically smaller.
            min_node = min(component)
            if color[min_node] == 2:
                for node in component:
                    color[node] = 3 - color[node]
                    
    print("YES")
    print(*(color[1:]))

solve()