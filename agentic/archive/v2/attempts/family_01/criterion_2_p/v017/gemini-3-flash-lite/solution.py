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
        
    # We want to find the lexicographically smallest assignment.
    # This means we prefer assigning 1 to worker i whenever possible.
    # We use a 2-coloring approach. For each connected component, we have two choices:
    # (Color 1, Color 2) or (Color 2, Color 1).
    # To get the lexicographically smallest, we try to put the first uncolored 
    # node in the component into shift 1.
    
    shift = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if shift[i] == 0:
            # Component not visited, start BFS/DFS
            component = []
            stack = [i]
            shift[i] = 1
            component.append(i)
            
            # Use stack to traverse component
            idx_stack = 0
            while idx_stack < len(component):
                u = component[idx_stack]
                idx_stack += 1
                for v in adj[u]:
                    if shift[v] == 0:
                        shift[v] = 3 - shift[u]
                        component.append(v)
                    elif shift[v] == shift[u]:
                        print("NO")
                        return
            
            # Now we have a valid 2-coloring for this component.
            # Let the coloring be C. We have two options:
            # Option A: keep current shift mapping
            # Option B: flip current shift mapping (1->2, 2->1)
            # We compare them lexicographically based on the smallest node index in the component.
            
            # Find the smallest node index in this component
            min_node = min(component)
            
            # If shift[min_node] is 2, it means we have a choice to make it 1.
            # To make it lexicographically smallest, we want the smallest node 
            # in the component to have shift 1 if possible.
            if shift[min_node] == 2:
                for node in component:
                    shift[node] = 3 - shift[node]
                    
    print("YES")
    print(*(shift[1:]))

solve()