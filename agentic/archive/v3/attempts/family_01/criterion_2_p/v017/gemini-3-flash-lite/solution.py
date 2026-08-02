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
        
    # shift[i] = 0 (unassigned), 1, or 2
    shift = [0] * (n + 1)
    
    # To get the lexicographically smallest assignment, we iterate 1 to n.
    # For each unvisited component, we greedily try assigning 1 first.
    # If a component is connected, assigning the first node to 1 forces 
    # the rest of the component.
    
    for i in range(1, n + 1):
        if shift[i] == 0:
            # Start BFS/DFS for this component
            stack = [(i, 1)]
            shift[i] = 1
            component = []
            
            # Use stack for iterative DFS to avoid recursion depth issues
            # and collect component nodes to check consistency
            stack = [i]
            shift[i] = 1
            component = [i]
            
            idx_comp = 0
            while idx_comp < len(component):
                u = component[idx_comp]
                idx_comp += 1
                
                for v in adj[u]:
                    if shift[v] == 0:
                        shift[v] = 3 - shift[u]
                        component.append(v)
                    elif shift[v] == shift[u]:
                        print("NO")
                        return
                        
    print("YES")
    print(*(shift[1:]))

if __name__ == '__main__':
    solve()