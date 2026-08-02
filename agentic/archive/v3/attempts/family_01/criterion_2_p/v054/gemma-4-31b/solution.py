import sys

# Increase recursion depth for deep graphs
sys.setrecursionlimit(300000)

def solve():
    # Use fast I/O
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
        
    # color[i] will be 0 (unvisited), 1 (Slot 1), or 2 (Slot 2)
    color = [0] * (n + 1)
    
    # To get the lexicographically smallest sequence, for each connected component,
    # we want to assign 1 to the smallest index in that component if possible.
    # Since the graph is bipartite, once the color of one node in a component is fixed,
    # all other nodes in that component are determined.
    # For a component C, there are only two valid colorings: 
    # (s_i) and (3 - s_i).
    # To minimize lexicographically, we look at the first node (smallest index) 
    # in the component and assign it 1.
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # Start BFS/DFS from node i. Since we process i from 1 to n,
            # assigning color[i] = 1 will always be the best choice for the 
            # lexicographical minimum of the sequence.
            stack = [i]
            color[i] = 1
            component = [i]
            
            # Standard BFS to color the component
            ptr = 0
            while ptr < len(stack):
                u = stack[ptr]
                ptr += 1
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        stack.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
    
    print("YES")
    print(*(color[1:]))

if __name__ == "__main__":
    solve()