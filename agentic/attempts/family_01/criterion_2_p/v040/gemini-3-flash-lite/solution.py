import sys

# Increase recursion depth for deep DFS trees
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
    
    # To get the lexicographically smallest assignment (s1, s2, ..., sn),
    # we iterate from 1 to n. If a node is not yet assigned, we assign it
    # the smallest possible channel (1) and propagate the constraints.
    
    for i in range(1, n + 1):
        if assignment[i] == 0:
            # Start BFS/DFS for the connected component
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
            
    print("YES")
    print(*(assignment[1:]))

solve()