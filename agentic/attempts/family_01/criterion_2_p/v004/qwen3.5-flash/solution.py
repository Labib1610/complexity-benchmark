import sys
from collections import deque

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

    # Adjacency list to represent the graph
    adj = [[] for _ in range(n + 1)]
    
    # Parse edges
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    # Array to store the division assignment for each personnel
    # 0: unassigned, 1: division 1, 2: division 2
    colors = [0] * (n + 1)
    
    # Iterate through each personnel to ensure all connected components are processed
    # Processing in increasing order of ID (1 to n) ensures we pick the lexicographically smallest assignment
    # because for any component, the first node encountered (smallest ID) will be assigned 1,
    # which is the smallest possible value.
    for i in range(1, n + 1):
        if colors[i] == 0:
            # Start a BFS for the connected component containing i
            colors[i] = 1
            queue = deque([i])
            
            while queue:
                u = queue.popleft()
                
                for v in adj[u]:
                    if colors[v] == 0:
                        # Assign opposite division to neighbor (1->2, 2->1)
                        colors[v] = 3 - colors[u]
                        queue.append(v)
                    elif colors[v] == colors[u]:
                        # Conflict detected: adjacent nodes have the same division
                        # This implies the graph is not bipartite
                        print("NO")
                        return

    # If no conflicts found, output YES and the assignment
    print("YES")
    # Using sys.stdout.write for efficient output
    sys.stdout.write(' '.join(map(str, colors[1:])) + '\n')

if __name__ == '__main__':
    solve()