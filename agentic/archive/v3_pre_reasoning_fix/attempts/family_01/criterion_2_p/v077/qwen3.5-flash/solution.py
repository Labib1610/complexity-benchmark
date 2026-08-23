import sys
from collections import deque

def solve():
    # Read all input from standard input efficiently
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Build adjacency list for the graph
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        
    # Array to store colors: 0 = unvisited, 1 = color A, 2 = color B
    colors = [0] * (n + 1)
    
    # Iterate through all nodes 1 to n to handle disconnected components.
    # Since we iterate in increasing order, the first time we encounter an unvisited node 'i',
    # it is guaranteed to be the smallest index in its connected component.
    # To achieve the lexicographically smallest sequence, we must assign the smallest
    # index in each component the value 1 (since 1 < 2).
    # This choice fixes the coloring for the entire component (if bipartite).
    for i in range(1, n + 1):
        if colors[i] == 0:
            colors[i] = 1
            q = deque([i])
            
            while q:
                u = q.popleft()
                current_color = colors[u]
                next_color = 3 - current_color
                
                for v in adj[u]:
                    if colors[v] == 0:
                        colors[v] = next_color
                        q.append(v)
                    else:
                        if colors[v] != next_color:
                            print("NO")
                            return

    print("YES")
    # Print the colors for nodes 1 to n separated by spaces
    print(*(colors[1:]))

if __name__ == '__main__':
    solve()