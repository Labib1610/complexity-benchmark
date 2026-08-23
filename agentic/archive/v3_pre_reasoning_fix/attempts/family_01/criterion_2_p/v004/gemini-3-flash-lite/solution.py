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
        idx += 2
        if u == v:
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)
        
    # color: 0 = unassigned, 1 = div 1, 2 = div 2
    color = [0] * (n + 1)
    
    # To get lexicographically smallest, we iterate 1 to n.
    # When a node is unvisited, we try assigning it '1' first.
    for i in range(1, n + 1):
        if color[i] == 0:
            stack = [i]
            color[i] = 1
            
            # Use a stack-based DFS to check bipartiteness
            # To ensure lexicographically smallest, we want to assign 1 whenever possible.
            # However, the connected component structure is fixed.
            # For each component, we have two choices for the starting node (1 or 2).
            # To be lexicographically smallest, we want the smallest index in the
            # component to be 1.
            
            component = []
            q = [i]
            component.append(i)
            head = 0
            while head < len(q):
                u = q[head]
                head += 1
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        q.append(v)
                        component.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
            
            # If the current component's smallest index is already 1, we are good.
            # If it was assigned 2, we must flip it.
            if color[i] == 2:
                for node in component:
                    color[node] = 3 - color[node]
                    
    print("YES")
    print(*(color[1:]))

solve()