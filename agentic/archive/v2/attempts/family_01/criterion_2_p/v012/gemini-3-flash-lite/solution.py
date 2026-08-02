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
        idx += 2
        if u == v:
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)
        
    assignment = [0] * (n + 1)
    
    # We want the lexicographically smallest assignment.
    # This means for each person i from 1 to n, we prefer assigning 1.
    # If we assign 1, we must ensure it doesn't conflict with any already 
    # assigned neighbors. If it conflicts, we must assign 2.
    # If 2 also conflicts, then it's impossible.
    
    # Since this is a 2-coloring problem, each connected component can be 
    # colored in at most 2 ways (swapping 1s and 2s).
    # To get the lexicographically smallest assignment, for each component,
    # we check if the first node (smallest index) can be 1. If it can, we
    # fix it and propagate. If it leads to a contradiction, we must set it to 2.
    
    visited = [False] * (n + 1)
    
    for i in range(1, n + 1):
        if not visited[i]:
            # Collect component
            component = []
            stack = [i]
            visited[i] = True
            while stack:
                u = stack.pop()
                component.append(u)
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
            
            # Try assigning 1 to the smallest index node in the component
            # Because we want to minimize the sequence, we always try to set
            # the smallest indexed node of a component to 1.
            comp_nodes = sorted(component)
            start_node = comp_nodes[0]
            
            # Two possibilities for this component:
            # 1. start_node = 1
            # 2. start_node = 2
            
            def get_coloring(start_val):
                color = {start_node: start_val}
                q = [start_node]
                while q:
                    u = q.pop()
                    for v in adj[u]:
                        if v not in color:
                            color[v] = 3 - color[u]
                            q.append(v)
                        elif color[v] == color[u]:
                            return None
                return color

            c1 = get_coloring(1)
            c2 = get_coloring(2)
            
            if c1 is None and c2 is None:
                print("NO")
                return
            
            # Choose the one that is lexicographically smaller
            # We compare the sequences based on the sorted order of nodes
            if c1 is None:
                best = c2
            elif c2 is None:
                best = c1
            else:
                # Compare c1 and c2
                for node in comp_nodes:
                    if c1[node] < c2[node]:
                        best = c1
                        break
                    elif c1[node] > c2[node]:
                        best = c2
                        break
                else:
                    best = c1
            
            for node in component:
                assignment[node] = best[node]
                
    print("YES")
    print(*(assignment[1:]))

solve()