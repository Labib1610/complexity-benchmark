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
        
    color = [0] * (n + 1)
    
    # To get the lexicographically smallest assignment (s1, s2, ..., sn),
    # we greedily try to assign group 1 to researcher i if possible.
    # If a researcher is not colored, we start a BFS/DFS.
    # Because we want s1 to be 1, s2 to be 1 if possible, etc.,
    # we iterate 1 to n and if uncolored, try assigning 1.
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # Start BFS/DFS for this connected component
            # To maintain lexicographical order, we try to set color 1
            stack = [(i, 1)]
            color[i] = 1
            component = []
            
            # Use a stack for non-recursive DFS to avoid depth limit
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