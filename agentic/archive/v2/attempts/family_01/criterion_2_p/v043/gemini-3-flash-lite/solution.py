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
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    assignment = [0] * (n + 1)
    
    # We want lexicographically smallest assignment.
    # This means we prefer 1 over 2 for each person i from 1 to n.
    # If a component is not yet assigned, try assigning 1 first.
    
    for i in range(1, n + 1):
        if assignment[i] == 0:
            # Start BFS/DFS for the connected component
            component = []
            stack = [i]
            assignment[i] = 1
            component.append(i)
            
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if assignment[v] == 0:
                        assignment[v] = 3 - assignment[u]
                        stack.append(v)
                        component.append(v)
                    elif assignment[v] == assignment[u]:
                        print("NO")
                        return
            
            # Now we have a valid 2-coloring for this component.
            # However, we must ensure the lexicographical smallest assignment.
            # A component has two possible colorings: (c1, c2, ...) or (3-c1, 3-c2, ...).
            # We check which one is lexicographically smaller at the first index i.
            # Actually, because we iterate 1 to n, the first node i in the component
            # is always the smallest index. To make the sequence smallest, we 
            # MUST assign 1 to the smallest index in the component if possible.
            # Our current assignment already does this because we set assignment[i] = 1.
            
    print("YES")
    print(*(assignment[1:]))

solve()