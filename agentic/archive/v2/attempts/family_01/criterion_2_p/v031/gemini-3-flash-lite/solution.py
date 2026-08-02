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
    
    # We want lexicographically smallest assignment.
    # This means for each connected component, we try to assign 1 to the 
    # smallest numbered node in that component.
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # Start BFS/DFS for this component
            # To get lexicographically smallest, we must process nodes in order
            # and decide their colors.
            # A component is bipartite if and only if it has no odd cycles.
            # If it is bipartite, there are exactly two valid colorings for the component.
            # We want the one that makes the sequence (s_1, ..., s_n) lexicographically smallest.
            
            component = []
            stack = [i]
            color[i] = 1
            component.append(i)
            
            # Use a list to store nodes in the component
            q = [i]
            head = 0
            while head < len(q):
                u = q[head]
                head += 1
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
            
            # The component is colored. Now, check if we can flip it.
            # The current assignment is one valid coloring.
            # The other is flipping all 1s to 2s and 2s to 1s.
            # We want the one that gives the smaller value at the smallest index i in the component.
            
            # Find the smallest node index in this component
            min_node = min(q)
            
            # If color[min_node] is 2, we can flip the whole component to make it 1
            if color[min_node] == 2:
                for node in q:
                    color[node] = 3 - color[node]
                    
    print("YES")
    print(*(color[1:]))

solve()