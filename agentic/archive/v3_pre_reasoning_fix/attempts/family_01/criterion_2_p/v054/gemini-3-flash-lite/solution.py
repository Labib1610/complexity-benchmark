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
    
    # To get the lexicographically smallest sequence, we iterate 1 to n.
    # For each unassigned node, we try assigning it to 1, then check if 
    # it leads to a valid 2-coloring of its connected component.
    
    for i in range(1, n + 1):
        if assignment[i] == 0:
            # Try assigning 1 to node i and perform BFS/DFS
            component = []
            stack = [i]
            assignment[i] = 1
            component.append(i)
            
            # Use stack for iterative DFS to avoid recursion limits
            idx_comp = 0
            while idx_comp < len(component):
                u = component[idx_comp]
                idx_comp += 1
                for v in adj[u]:
                    if assignment[v] == 0:
                        assignment[v] = 3 - assignment[u]
                        component.append(v)
                    elif assignment[v] == assignment[u]:
                        print("NO")
                        return
            
            # The assignment is now fixed for this component.
            # If the current assignment is not the lexicographically smallest
            # (i.e., we assigned 1 but could have assigned 2), we might need
            # to swap 1s and 2s. However, the greedy choice 1 is always better.
            # The only constraint is that we must pick the valid assignment
            # that is lexicographically smallest. Since we always try assigning 1
            # to the first encountered node of a component, this is the smallest.
            
    print("YES")
    print(*(assignment[1:]))

solve()