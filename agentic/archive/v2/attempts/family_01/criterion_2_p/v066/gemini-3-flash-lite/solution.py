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
    
    # To get the lexicographically smallest sequence, we prioritize assigning 1
    # whenever possible in the iteration order 1 to n.
    for i in range(1, n + 1):
        if color[i] == 0:
            # Start BFS/DFS for the connected component
            stack = [i]
            color[i] = 1
            component = []
            
            # Use a stack-based approach to color the component
            # To maintain lexicographical order, we process nodes in increasing order
            # However, for 2-coloring, the coloring is fixed once the first node is set.
            # We must check if the component is bipartite.
            
            comp_nodes = []
            q = [i]
            color[i] = 1
            comp_nodes.append(i)
            
            head = 0
            while head < len(q):
                u = q[head]
                head += 1
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        q.append(v)
                        comp_nodes.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
            
            # The component is bipartite. We have two choices for this component:
            # swap 1s and 2s. We choose the one that makes the sequence 
            # lexicographically smaller.
            # Compare the first node 'i' which is the smallest index in this component.
            # If color[i] is 2, swapping makes color[i] = 1, which is smaller.
            if color[i] == 2:
                for node in comp_nodes:
                    color[node] = 3 - color[node]
                    
    print("YES")
    print(*(color[1:]))

solve()