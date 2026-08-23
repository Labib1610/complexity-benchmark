import sys

# Increase recursion depth for deep components in large graphs
sys.setrecursionlimit(300000)

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    ptr = 2
    for _ in range(m):
        u = int(input_data[ptr])
        v = int(input_data[ptr+1])
        ptr += 2
        if u == v:
            # A worker cannot be incompatible with themselves for a 2-block assignment
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)
    
    # color[i] will be 0 (unvisited), 1 (Block 1), or 2 (Block 2)
    color = [0] * (n + 1)
    
    # To get the lexicographically smallest sequence, we process workers 1 to n.
    # For each connected component, the first node encountered (the smallest index)
    # should be assigned to Block 1 if possible.
    for i in range(1, n + 1):
        if color[i] == 0:
            # Start BFS/DFS to color the component
            # We use a stack for iterative DFS to avoid recursion limits and be faster
            stack = [i]
            color[i] = 1 # Lexicographically smallest: assign the smallest index in component to 1
            
            component = []
            # We need to keep track of the component to potentially flip colors, 
            # but since we are assigning the smallest index to 1, and the 
            # bipartite coloring is forced once the first node is colored, 
            # this is already the lexicographically smallest for this component.
            
            # Standard Bipartite Check using Iterative DFS
            visited_in_batch = [i]
            q = [i]
            idx = 0
            while idx < len(q):
                u = q[idx]
                idx += 1
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
    
    # Output results
    print("YES")
    print(*(color[i] for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()