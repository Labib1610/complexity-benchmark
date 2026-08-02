import sys

# Increase recursion depth for deep graphs
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
        
    # We need the lexicographically smallest assignment.
    # This means for researcher 1, we prefer 1, then 2.
    # For researcher 2, we prefer 1, then 2, and so on.
    # This is a standard 2-coloring problem.
    
    color = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # Start BFS/DFS for this component.
            # To get lexicographically smallest, we try to assign 1 to the 
            # first unassigned node of each component.
            stack = [i]
            color[i] = 1
            
            while stack:
                u = stack.pop()
                
                # Sort neighbors to process in a deterministic order if needed,
                # but for 2-coloring, the component's coloring is fixed once 
                # the first node is assigned.
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        stack.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
                        
    print("YES")
    print(*(color[1:]))

solve()