import sys

# Increase recursion depth for deep DFS
sys.setrecursionlimit(500000)

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
    
    # To get the lexicographically smallest assignment, we iterate from 1 to n.
    # If a person is not assigned, we try assigning them to slot 1 first,
    # then propagate constraints using BFS/DFS.
    
    for i in range(1, n + 1):
        if assignment[i] == 0:
            # Start a new component
            # Try assigning current node to 1
            stack = [(i, 1)]
            assignment[i] = 1
            component = []
            
            possible = True
            while stack:
                u, slot = stack.pop()
                component.append((u, slot))
                
                for v in adj[u]:
                    if assignment[v] == 0:
                        assignment[v] = 3 - slot
                        stack.append((v, 3 - slot))
                    elif assignment[v] == slot:
                        possible = False
                        break
                if not possible:
                    break
            
            if not possible:
                # Try assigning to 2
                for node, _ in component:
                    assignment[node] = 0
                
                stack = [(i, 2)]
                assignment[i] = 2
                possible = True
                while stack:
                    u, slot = stack.pop()
                    for v in adj[u]:
                        if assignment[v] == 0:
                            assignment[v] = 3 - slot
                            stack.append((v, 3 - slot))
                        elif assignment[v] == slot:
                            possible = False
                            break
                    if not possible:
                        break
                
                if not possible:
                    print("NO")
                    return

    print("YES")
    print(*(assignment[1:]))

solve()