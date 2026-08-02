import sys

# Increase recursion depth for deep graphs
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
        
    color = [0] * (n + 1)
    
    # We want the lexicographically smallest sequence.
    # We iterate i from 1 to n. If color[i] is not assigned, 
    # we try assigning 1 (the smallest possible channel).
    # Then we perform BFS/DFS to propagate the constraints.
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # Start BFS from i to color this connected component
            # To get lexicographically smallest, we try setting color[i] = 1
            stack = [(i, 1)]
            color[i] = 1
            component = []
            
            # Use a list as stack for DFS
            while stack:
                u, c = stack.pop()
                component.append((u, c))
                
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - c
                        stack.append((v, 3 - c))
                    elif color[v] == c:
                        print("NO")
                        return
            
    print("YES")
    print(*(color[1:]))

solve()