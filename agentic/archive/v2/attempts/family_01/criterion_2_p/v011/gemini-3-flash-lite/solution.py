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
        
    colors = [0] * (n + 1)
    
    # We want the lexicographically smallest configuration.
    # This means for each connected component, we try setting the first 
    # encountered node to 1, then propagate. If a conflict arises, 
    # it's impossible.
    
    for i in range(1, n + 1):
        if colors[i] == 0:
            # Start BFS/DFS for this component
            # To get lexicographically smallest, always try color 1 first
            stack = [(i, 1)]
            colors[i] = 1
            
            # Use a list to store nodes in this component to verify consistency
            component = []
            
            while stack:
                u, c = stack.pop()
                component.append(u)
                
                for v in adj[u]:
                    if colors[v] == 0:
                        colors[v] = 3 - c
                        stack.append((v, 3 - c))
                    elif colors[v] == c:
                        print("NO")
                        return
                        
    print("YES")
    print(*(colors[1:]))

solve()