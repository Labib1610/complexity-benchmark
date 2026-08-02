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
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    # The problem is 2-coloring a graph. 
    # To get the lexicographically smallest assignment (s1, s2, ..., sn),
    # we greedily try to set si = 1 whenever possible.
    
    color = [0] * (n + 1)
    
    # We iterate 1 to n. If a node is uncolored, we must assign it a color.
    # To minimize the sequence lexicographically, we prefer 1.
    # If we assign state 1 to a node, all its neighbors must be 2, and so on.
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # Start a BFS/DFS component
            # To make the global sequence lexicographically smallest:
            # We try to set the current node i to 1.
            stack = [(i, 1)]
            color[i] = 1
            component = []
            
            possible = True
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
            
            # Check if this component's assignment is the best possible.
            # Actually, for bipartite components, there are only two ways to color:
            # (c1, c2, ...) or (3-c1, 3-c2, ...).
            # We want the one that results in the smaller value at the first node
            # of the component (which is the smallest index in the component).
            
            # Since we iterate i from 1 to n, the first node encountered in a component
            # is the smallest index. We already assigned it 1. This is always
            # lexicographically better than assigning it 2.
            pass
            
    print("YES")
    print(*(color[1:]))

solve()