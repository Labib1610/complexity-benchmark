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
        idx += 2
        if u == v:
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)
        
    color = [0] * (n + 1)
    
    # We want lexicographically smallest sequence.
    # We iterate i from 1 to n. If node i is not colored, we try coloring it 1.
    # To maintain lexicographical order, for each connected component, 
    # we greedily try 1 for the smallest index node.
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # Start BFS/DFS for this component
            stack = [i]
            color[i] = 1
            component = []
            
            # Use a stack-based approach for DFS to avoid recursion depth issues
            # and to handle the lexicographical requirement correctly.
            # However, for a fixed component, fixing the first node's color 
            # determines the rest.
            
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
                        
    print("YES")
    print(*(color[1:]))

solve()