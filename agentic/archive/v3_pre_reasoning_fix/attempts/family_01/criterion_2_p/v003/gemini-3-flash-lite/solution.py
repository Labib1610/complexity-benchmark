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
        
    # We want the lexicographically smallest assignment.
    # This means for each component 1 to n, we try to assign Mode 1 if possible.
    # If not, we try Mode 2.
    # This is a standard 2-coloring problem.
    # Since we want the lexicographically smallest, we iterate 1..n.
    # If a component is unvisited, we start a BFS/DFS.
    # To prioritize Mode 1, we always try to assign 1 to the first node of a component.
    
    assignment = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if assignment[i] == 0:
            # Start BFS/DFS for this connected component
            # To get lexicographically smallest, we force the first node of the 
            # component to be 1.
            stack = [(i, 1)]
            assignment[i] = 1
            
            while stack:
                u, mode = stack.pop()
                
                for v in adj[u]:
                    if assignment[v] == 0:
                        assignment[v] = 3 - mode
                        stack.append((v, assignment[v]))
                    elif assignment[v] == mode:
                        print("NO")
                        return
                        
    print("YES")
    print(*(assignment[1:]))

solve()