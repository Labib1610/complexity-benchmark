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
    
    colors = [0] * (n + 1)
    
    # We want lexicographically smallest assignment.
    # This means for each connected component, we try to assign 1 to the smallest 
    # node index, and propagate.
    
    for i in range(1, n + 1):
        if colors[i] == 0:
            # Start BFS/DFS for this component.
            # To get lexicographically smallest, we greedily pick 1 for the 
            # smallest node in the component.
            stack = [(i, 1)]
            colors[i] = 1
            component = []
            
            # Use a stack for iterative DFS to avoid recursion limits
            # and to handle component processing
            comp_nodes = []
            q = [i]
            colors[i] = 1
            head = 0
            while head < len(q):
                u = q[head]
                head += 1
                comp_nodes.append(u)
                for v in adj[u]:
                    if colors[v] == 0:
                        colors[v] = 3 - colors[u]
                        q.append(v)
                    elif colors[v] == colors[u]:
                        print("NO")
                        return
            
            # The assignment is now fixed for this component.
            # To ensure lexicographical smallest, we check if swapping 1s and 2s
            # yields a smaller sequence.
            # The sequence is lexicographically smallest if the first node 
            # encountered (smallest index) has value 1.
            # Our BFS/DFS logic already assigns 1 to the 'root' of the component.
            
    print("YES")
    print(*(colors[1:]))

solve()