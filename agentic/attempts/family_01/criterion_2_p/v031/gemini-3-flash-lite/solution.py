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
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    # To get the lexicographically smallest assignment, we prefer 1 over 2.
    # We iterate 1 to n and assign 1 if possible.
    color = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # Start BFS/DFS for the connected component
            stack = [i]
            color[i] = 1
            component = [i]
            
            # Use stack to perform DFS
            idx_stack = 0
            while idx_stack < len(stack):
                u = stack[idx_stack]
                idx_stack += 1
                
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        stack.append(v)
                        component.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
            
            # Check if swapping colors in this component yields a lexicographically smaller result
            # For each component, we have two choices:
            # 1. Start with color[i] = 1
            # 2. Start with color[i] = 2
            # Since we want the lexicographically smallest sequence, we compare
            # the result of (color[i]=1 vs color[i]=2) at the first index i
            # Actually, simply greedily assigning 1 to the smallest uncolored node
            # in each component is sufficient because 1 < 2.
            
    print("YES")
    print(*(color[1:]))

solve()