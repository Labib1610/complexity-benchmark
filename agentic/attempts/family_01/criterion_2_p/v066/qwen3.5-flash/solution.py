import sys

def solve():
    # Read all input from standard input at once for efficiency
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Build the graph using an adjacency list
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        
    # Array to store the color of each node (0: uncolored, 1: color A, 2: color B)
    colors = [0] * (n + 1)
    
    # Iterate through each node from 1 to n.
    # If a node is uncolored, it belongs to a new connected component.
    # To achieve the lexicographically smallest sequence, we assign color 1 
    # to the smallest index node in each component.
    for i in range(1, n + 1):
        if colors[i] == 0:
            colors[i] = 1
            stack = [i]
            
            while stack:
                u = stack.pop()
                current_color = colors[u]
                next_color = 3 - current_color  # Switch between 1 and 2
                
                for v in adj[u]:
                    if colors[v] == 0:
                        colors[v] = next_color
                        stack.append(v)
                    elif colors[v] != next_color:
                        # If a neighbor has the same color as current node, it's not bipartite
                        print("NO")
                        return
    
    # If we successfully colored all components without conflict
    print("YES")
    # Print the colors for nodes 1 to n separated by spaces
    print(' '.join(map(str, colors[1:])))

if __name__ == '__main__':
    solve()