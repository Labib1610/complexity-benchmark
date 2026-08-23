import sys

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

    # Build adjacency list
    # Nodes are 1-indexed
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        
    # Array to store channel assignments (0: unassigned, 1: Channel 1, 2: Channel 2)
    color = [0] * (n + 1)
    
    # Iterate through each node to handle disconnected components
    for i in range(1, n + 1):
        if color[i] == 0:
            # Found a new component, start BFS
            # To ensure lexicographically smallest, assign Channel 1 to the first node encountered
            # (which is the smallest index in this component)
            color[i] = 1
            queue = [i]
            head = 0
            
            while head < len(queue):
                u = queue[head]
                head += 1
                
                c = color[u]
                next_c = 3 - c  # Switch between 1 and 2
                
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = next_c
                        queue.append(v)
                    elif color[v] == c:
                        # Conflict detected: graph is not bipartite
                        print("NO")
                        return
    
    # If no conflicts, solution exists
    print("YES")
    # Print the assignment for nodes 1 to n
    print(' '.join(map(str, color[1:])))

if __name__ == '__main__':
    solve()