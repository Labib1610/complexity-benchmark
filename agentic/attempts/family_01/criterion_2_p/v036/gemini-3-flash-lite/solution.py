import sys

# Increase recursion depth for deep graphs
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
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    assignment = [0] * (n + 1)
    
    # To get the lexicographically smallest result, we iterate through
    # workers 1 to n. For each unvisited component, we try assigning
    # the current worker to Zone 1. If it fails, we try Zone 2.
    
    for i in range(1, n + 1):
        if assignment[i] == 0:
            # Try setting assignment[i] = 1
            component = []
            stack = [(i, 1)]
            assignment[i] = 1
            possible = True
            
            # Use a list to keep track of this component's nodes for potential rollback
            comp_nodes = [i]
            
            idx_stack = 0
            while idx_stack < len(stack):
                u, color = stack[idx_stack]
                idx_stack += 1
                
                for v in adj[u]:
                    if assignment[v] == 0:
                        assignment[v] = 3 - color
                        stack.append((v, 3 - color))
                        comp_nodes.append(v)
                    elif assignment[v] == color:
                        possible = False
                        break
                if not possible:
                    break
            
            if not possible:
                # Rollback and try assigning 2
                for node in comp_nodes:
                    assignment[node] = 0
                
                stack = [(i, 2)]
                assignment[i] = 2
                possible = True
                comp_nodes = [i]
                
                idx_stack = 0
                while idx_stack < len(stack):
                    u, color = stack[idx_stack]
                    idx_stack += 1
                    
                    for v in adj[u]:
                        if assignment[v] == 0:
                            assignment[v] = 3 - color
                            stack.append((v, 3 - color))
                            comp_nodes.append(v)
                        elif assignment[v] == color:
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