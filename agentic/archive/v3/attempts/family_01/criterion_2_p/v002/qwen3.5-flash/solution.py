import sys
from collections import deque

# Increase recursion depth just in case, though we use iterative BFS.
sys.setrecursionlimit(200005)

def main():
    # Read all input from stdin at once for speed
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
    # Using 1-based indexing for convenience
    adj = [[] for _ in range(n + 1)]
    
    # Parse edges
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        
    # Array to store the chamber assignment (1 or 2)
    # 0 indicates unvisited
    chamber = [0] * (n + 1)
    
    # Iterate through all nodes to handle disconnected components
    # We iterate from 1 to n to ensure we process components starting from their smallest node index
    for i in range(1, n + 1):
        if chamber[i] == 0:
            # Start BFS for the component containing i
            # To ensure lexicographically smallest sequence, assign chamber 1 to the 
            # first node encountered in the component (which is the smallest index in that component)
            chamber[i] = 1
            queue = deque([i])
            
            while queue:
                u = queue.popleft()
                current_chamber = chamber[u]
                next_chamber = 3 - current_chamber  # Toggle between 1 and 2
                
                for v in adj[u]:
                    if chamber[v] == 0:
                        chamber[v] = next_chamber
                        queue.append(v)
                    elif chamber[v] != next_chamber:
                        # Conflict found: graph is not bipartite
                        print("NO")
                        return

    # If no conflicts found, print YES and the assignment
    print("YES")
    # Output the assignments for nodes 1 to n
    # Using sys.stdout.write for potentially faster output on large N
    # though print is likely sufficient.
    print(*(chamber[1:]))

if __name__ == '__main__':
    main()