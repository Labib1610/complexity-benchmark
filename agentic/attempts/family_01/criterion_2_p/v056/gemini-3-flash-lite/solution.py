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
    
    # We want the lexicographically smallest assignment.
    # This means for each connected component, we try to set the first node
    # to 1, then propagate. If that's impossible, set to 2.
    assignment = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if assignment[i] == 0:
            # Try assigning 1 to the first node of this component
            component = []
            stack = [i]
            assignment[i] = 1
            component.append(i)
            
            possible = True
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if assignment[v] == 0:
                        assignment[v] = 3 - assignment[u]
                        stack.append(v)
                        component.append(v)
                    elif assignment[v] == assignment[u]:
                        possible = False
                        break
                if not possible:
                    break
            
            if not possible:
                # Reset component and try assigning 2 to the start node
                for node in component:
                    assignment[node] = 0
                
                stack = [i]
                assignment[i] = 2
                possible = True
                while stack:
                    u = stack.pop()
                    for v in adj[u]:
                        if assignment[v] == 0:
                            assignment[v] = 3 - assignment[u]
                            stack.append(v)
                        elif assignment[v] == assignment[u]:
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