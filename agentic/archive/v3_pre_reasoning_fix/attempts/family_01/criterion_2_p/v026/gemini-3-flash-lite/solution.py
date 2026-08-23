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
        
    assignment = [0] * (n + 1)
    
    # We want lexicographically smallest assignment.
    # This means for each unit i from 1 to n, if not assigned,
    # try assigning 1. If that leads to a contradiction, try 2.
    # This is equivalent to checking bipartiteness components.
    # For each connected component, we have two possible colorings.
    # Let the component be C. If we fix the color of the smallest node 
    # in C to 1, the rest of the component is determined.
    
    for i in range(1, n + 1):
        if assignment[i] == 0:
            # Component not visited. Try assigning 1 to the smallest node i.
            component = []
            stack = [(i, 1)]
            assignment[i] = 1
            component.append(i)
            
            possible = True
            ptr = 0
            while ptr < len(component):
                u = component[ptr]
                ptr += 1
                for v in adj[u]:
                    if assignment[v] == 0:
                        assignment[v] = 3 - assignment[u]
                        component.append(v)
                    elif assignment[v] == assignment[u]:
                        print("NO")
                        return
            
    print("YES")
    print(*(assignment[1:]))

solve()