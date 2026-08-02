import sys

# Increase recursion depth for deep DFS
sys.setrecursionlimit(10**6)

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
    
    # To get lexicographically smallest result, we try to assign 1 to node i if possible.
    # We iterate 1..n. If uncolored, we must color the connected component.
    # Within a component, we can pick color 1 or 2 for the first node visited.
    # To keep it lexicographically smallest, we should try assigning 1 to the 
    # smallest index node in the component.
    
    result = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if color[i] == 0:
            component = []
            stack = [i]
            color[i] = 1
            component.append(i)
            
            # BFS or DFS to find all nodes in component
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
            
            # Now we have a valid 2-coloring for this component.
            # There are two possible assignments:
            # 1. current color[v]
            # 2. 3 - color[v]
            # We compare them lexicographically.
            
            comp_nodes = sorted(component)
            
            # Assignment 1: color[v]
            # Assignment 2: 3 - color[v]
            
            # To be lexicographically smallest, we check the first node in the 
            # sorted component list. We want result[comp_nodes[0]] to be 1.
            # If color[comp_nodes[0]] == 1, keep it. Else flip.
            
            if color[comp_nodes[0]] == 2:
                for node in component:
                    color[node] = 3 - color[node]
                    
    print("YES")
    print(*(color[1:]))

solve()