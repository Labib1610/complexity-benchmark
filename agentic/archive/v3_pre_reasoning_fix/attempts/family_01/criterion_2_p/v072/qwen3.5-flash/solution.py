import sys
from collections import deque

def main():
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

    # Build adjacency list for the graph
    # Nodes are 1-indexed, so size is n + 1
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
    
    # Color array: 0 = unvisited, 1 = Period 1, 2 = Period 2
    color = [0] * (n + 1)
    
    # Iterate through nodes 1 to n to process connected components.
    # To achieve the lexicographically smallest assignment sequence:
    # We iterate from 1 to n. If we encounter an unvisited node 'i',
    # it is the smallest index in its connected component.
    # To minimize the sequence lexicographically, we must assign color 1 to 'i'
    # (since 1 < 2). This choice propagates to the rest of the component.
    for i in range(1, n + 1):
        if color[i] == 0:
            color[i] = 1
            queue = deque([i])
            
            while queue:
                u = queue.popleft()
                current_c = color[u]
                next_c = 3 - current_c  # Toggle between 1 and 2
                
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = next_c
                        queue.append(v)
                    elif color[v] == current_c:
                        # Conflict detected: adjacent nodes have the same color
                        print("NO")
                        return

    # If we complete the loop without conflicts, a valid assignment exists
    print("YES")
    # Output the assignment sequence separated by spaces
    sys.stdout.write(' '.join(map(str, color[1:])) + '\n')

if __name__ == '__main__':
    main()