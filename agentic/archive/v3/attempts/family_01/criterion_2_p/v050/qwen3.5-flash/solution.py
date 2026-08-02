import sys

def solve():
    # Read all input from standard input efficiently
    # sys.stdin.read() reads the entire input as a string
    # .split() splits by whitespace (spaces, newlines, tabs)
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency list for the graph
    # Using 1-based indexing for convenience to match worker IDs 1 to n
    # Pre-allocating lists is efficient
    adj = [[] for _ in range(n + 1)]
    
    # Reading m edges
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        
    # Array to store the color of each worker
    # 0: uncolored, 1: block 1, 2: block 2
    color = [0] * (n + 1)
    
    # Iterate through each worker from 1 to n
    # This ensures we process components in order of their smallest index
    # which helps in achieving the lexicographically smallest sequence.
    # For any connected component, the first node we encounter (smallest index)
    # determines the coloring of the entire component. To minimize lexicographically,
    # we must assign color 1 to this node.
    for i in range(1, n + 1):
        if color[i] == 0:
            # Start a traversal (DFS) for this component
            color[i] = 1
            stack = [i]
            
            while stack:
                u = stack.pop()
                current_c = color[u]
                next_c = 3 - current_c  # Switch between 1 and 2
                
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = next_c
                        stack.append(v)
                    elif color[v] != next_c:
                        # Conflict detected: graph is not bipartite
                        sys.stdout.write("NO\n")
                        return

    # If we successfully colored all workers
    sys.stdout.write("YES\n")
    # Output the colors for workers 1 to n
    # Using sys.stdout.write with join is faster than printing in a loop for large N
    sys.stdout.write(" ".join(map(str, color[1:])) + "\n")

if __name__ == '__main__':
    solve()