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
    
    # We want the lexicographically smallest assignment.
    # This means for person 1, we prefer 1. If 1 leads to a conflict, we try 2.
    # This is a standard 2-coloring problem on a graph.
    # Since we want lexicographical smallest, we iterate 1 to n.
    # If a node is unvisited, we try assigning it 1.
    
    for i in range(1, n + 1):
        if assignment[i] == 0:
            # BFS/DFS to color the connected component
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
            
            # The component is valid. Now check if we could have made it 
            # lexicographically smaller. Actually, the greedy choice 
            # for the first node of each component is always 1.
            # Because if we assign 1 to the first node of a component, 
            # all other nodes in that component are forced. 
            # If we assigned 2, the sequence would be lexicographically larger.
            
    print("YES")
    print(*(assignment[1:]))

solve()