import sys

# Increase recursion depth for deep DFS
sys.setrecursionlimit(500000)

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
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    color = [0] * (n + 1)
    ans = [0] * (n + 1)
    
    # We want lexicographically smallest assignment.
    # For each connected component, we have two possible colorings (c and not c).
    # We choose the coloring that makes the first vertex in the component 1 if possible.
    # If the first vertex is already assigned, we follow the forced constraints.
    
    for i in range(1, n + 1):
        if color[i] == 0:
            component = []
            stack = [i]
            color[i] = 1
            component.append(i)
            
            # BFS to find component and check bipartiteness
            head = 0
            while head < len(component):
                u = component[head]
                head += 1
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        component.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
            
            # Determine which coloring to pick for this component
            # Find the smallest index in this component
            first_in_comp = min(component)
            
            # If we set color[first_in_comp] = 1, is it valid?
            # Yes, because if color[first_in_comp] was 2, we just flip all colors.
            if color[first_in_comp] == 2:
                for node in component:
                    color[node] = 3 - color[node]
            
            for node in component:
                ans[node] = color[node]
                
    print("YES")
    print(*(ans[1:]))

solve()