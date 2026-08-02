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
        
    # We want the lexicographically smallest assignment.
    # This means s_1 should be 1 if possible. If s_1=1 is fixed,
    # we propagate constraints. If a component is not fixed by 
    # previous choices, we start with the smallest node index 
    # and assign it 1.
    
    color = [0] * (n + 1)
    
    # To get lexicographically smallest, we iterate 1 to n.
    # If node i is uncolored, we try to color it 1.
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # Start BFS/DFS for this connected component
            # To ensure lexicographical smallest, we greedily assign 1
            stack = [(i, 1)]
            color[i] = 1
            component = []
            
            # Use a stack for non-recursive DFS to avoid recursion limits
            comp_stack = [i]
            component.append(i)
            
            while comp_stack:
                u = comp_stack.pop()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        comp_stack.append(v)
                        component.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
            
    print("YES")
    print(*(color[1:]))

solve()