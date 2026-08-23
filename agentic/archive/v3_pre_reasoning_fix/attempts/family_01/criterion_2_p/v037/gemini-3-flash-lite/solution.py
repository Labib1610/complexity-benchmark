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
        idx += 2
        if u == v:
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)
        
    color = [0] * (n + 1)
    
    # To get the lexicographically smallest, we must decide 1 or 2
    # for each node in order 1 to n.
    # If a node is not colored, we try to color it 1.
    # If that forces a conflict, we check if 2 is possible.
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # Try setting color[i] = 1
            stack = [(i, 1)]
            color[i] = 1
            component = []
            
            possible = True
            comp_idx = 0
            
            # Using a manual stack to perform BFS/DFS to color the component
            q = [i]
            component.append(i)
            while comp_idx < len(component):
                u = component[comp_idx]
                comp_idx += 1
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        component.append(v)
                    elif color[v] == color[u]:
                        possible = False
                        break
                if not possible:
                    break
            
            if not possible:
                # Reset component and try setting color[i] = 2
                for node in component:
                    color[node] = 0
                
                color[i] = 2
                component = [i]
                comp_idx = 0
                possible = True
                while comp_idx < len(component):
                    u = component[comp_idx]
                    comp_idx += 1
                    for v in adj[u]:
                        if color[v] == 0:
                            color[v] = 3 - color[u]
                            component.append(v)
                        elif color[v] == color[u]:
                            possible = False
                            break
                    if not possible:
                        break
                
                if not possible:
                    print("NO")
                    return
                    
    print("YES")
    print(*(color[1:]))

solve()