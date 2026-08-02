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
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    assignment = [0] * (n + 1)
    
    # We want lexicographically smallest assignment.
    # For each connected component, we try to assign 1 to the smallest index 
    # node in the component to ensure lexicographical order.
    
    for i in range(1, n + 1):
        if assignment[i] == 0:
            # Component not yet colored.
            # Start BFS/DFS from i, assigning 1 to i.
            stack = [(i, 1)]
            assignment[i] = 1
            component = []
            
            while stack:
                u, color = stack.pop()
                component.append((u, color))
                
                for v in adj[u]:
                    if assignment[v] == 0:
                        assignment[v] = 3 - color
                        stack.append((v, 3 - color))
                    elif assignment[v] == color:
                        print("NO")
                        return
            
            # Now we have a valid 2-coloring for this component.
            # However, we have two choices for this component:
            # 1. Keep as is.
            # 2. Flip all colors (1 becomes 2, 2 becomes 1).
            # To get lexicographically smallest, we compare the two configurations.
            
            # Let's find the first node in this component.
            # We want the color of the smallest index node in this component to be 1.
            min_node = min(comp[0] for comp in component)
            if assignment[min_node] == 2:
                for node, color in component:
                    assignment[node] = 3 - color
                    
    print("YES")
    print(*(assignment[1:]))

solve()