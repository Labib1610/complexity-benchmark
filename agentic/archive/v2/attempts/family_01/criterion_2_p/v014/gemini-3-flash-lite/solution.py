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
    
    # To get the lexicographically smallest result, we try to assign 1 to node i if possible.
    # This is a standard 2-coloring problem.
    # We iterate 1 to n. If node i is unassigned, we start a BFS/DFS.
    # To be lexicographically smallest, when starting a component, we prefer assigning 1.
    
    for i in range(1, n + 1):
        if assignment[i] == 0:
            # Start BFS for this component
            # We want the smallest lexicographical result.
            # For each connected component, we have two possible colorings (swap 1 and 2).
            # We pick the one that makes the first node in the component (by index) 1.
            component = []
            stack = [i]
            assignment[i] = 1
            component.append(i)
            
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
    
    print("YES")
    print(*(assignment[1:]))

solve()