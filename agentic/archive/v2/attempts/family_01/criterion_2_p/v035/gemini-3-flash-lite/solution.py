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
    
    # colors: 0 = unassigned, 1 = shift 1, 2 = shift 2
    colors = [0] * (n + 1)
    
    # To get lexicographically smallest assignment:
    # We iterate i from 1 to n. If not colored, try coloring 1.
    # If that fails, try coloring 2.
    
    for i in range(1, n + 1):
        if colors[i] == 0:
            # Start BFS/DFS for this component
            # We want to pick the assignment that is lexicographically smallest.
            # However, the choice for a component is constrained by its edges.
            # For each connected component, there are at most 2 valid assignments
            # (swapping 1s and 2s). We pick the one that makes the first node
            # in the component 1 if possible.
            
            component = []
            stack = [i]
            colors[i] = 1
            component.append(i)
            
            # Use a stack for iterative DFS to avoid recursion depth issues
            idx_comp = 0
            while idx_comp < len(component):
                u = component[idx_comp]
                idx_comp += 1
                for v in adj[u]:
                    if colors[v] == 0:
                        colors[v] = 3 - colors[u]
                        component.append(v)
                    elif colors[v] == colors[u]:
                        print("NO")
                        return
            
            # Check if this component's assignment is the lexicographically smallest
            # The component nodes are already colored such that colors[i] = 1.
            # Let's see if we can swap 1s and 2s to get a better sequence.
            # The current assignment has colors[i] = 1.
            # If we swap, colors[i] becomes 2. 
            # Since we want lexicographically smallest, 1 is always better than 2.
            # So we keep the assignment where the first node of the component is 1.
    
    print("YES")
    print(*(colors[1:]))

solve()