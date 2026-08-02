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
        
    # To get the lexicographically smallest assignment, we prefer 1 over 2.
    # We iterate from 1 to n. If a node is uncolored, try coloring it 1.
    # If that fails, try 2.
    
    color = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # Start BFS/DFS for the connected component
            stack = [i]
            color[i] = 1
            component = [i]
            
            # Use stack for iterative DFS to avoid recursion limit issues
            curr_idx = 0
            while curr_idx < len(component):
                u = component[curr_idx]
                curr_idx += 1
                
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        component.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
    
    print("YES")
    print(*(color[1:]))

if __name__ == '__main__':
    solve()