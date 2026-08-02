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
    # This means for node 1, we prefer 1. If we pick 1, we must propagate.
    # If that fails, we try 2.
    # Since this is a bipartite check, the connected components are independent.
    # For each component, we have two choices: (A, B) or (B, A).
    # To make the whole sequence lexicographically smallest, 
    # we look at the smallest index i in the component. 
    # We assign 1 to it if possible, else 2.
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # Component nodes
            component = []
            stack = [i]
            color[i] = 1
            component.append(i)
            
            # BFS/DFS to find all nodes in component
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
            
            # Now we have the component. The current assignment is (color[i]=1).
            # We check if this assignment is the lexicographically smallest.
            # The other option is swapping 1s and 2s.
            # We compare the two options based on the smallest index in the component.
            # Actually, the smallest index in the component is 'i' (since we iterate 1..n).
            # If color[i] is already 1, we are good. If it's 2, we must swap.
            if color[i] == 2:
                for node in component:
                    color[node] = 3 - color[node]
                    
    print("YES")
    print(*(color[1:]))

solve()