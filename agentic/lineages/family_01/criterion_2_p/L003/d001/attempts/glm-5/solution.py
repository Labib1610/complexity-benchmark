import sys

# Increase recursion depth just in case, though we use iterative BFS/DFS
sys.setrecursionlimit(1 << 25)

def solve():
    # Read all input at once
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
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        
    # Sort adjacency lists to process neighbors in order.
    # This helps in finding the lexicographically smallest valid configuration.
    for i in range(n + 1):
        adj[i].sort()
        
    # Colors: 0 = uncolored, 1 = color 1, 2 = color 2
    colors = [0] * (n + 1)
    
    # Process nodes from 1 to n to ensure lexicographically smallest result
    for i in range(1, n + 1):
        if colors[i] == 0:
            # Start a BFS for this component
            # We assign color 1 to the starting node 'i' because we iterate
            # nodes in increasing order and we want the smallest valid color.
            colors[i] = 1
            queue = [i]
            head = 0
            
            while head < len(queue):
                u = queue[head]
                head += 1
                
                for v in adj[u]:
                    if colors[v] == 0:
                        # Constraint: s_u + s_v = 3 => s_v = 3 - s_u
                        colors[v] = 3 - colors[u]
                        queue.append(v)
                    else:
                        # Check if the constraint is satisfied
                        if colors[u] + colors[v] != 3:
                            sys.stdout.write("NO\n")
                            return

    sys.stdout.write("YES\n")
    # Output colors for nodes 1 to n
    sys.stdout.write(' '.join(map(str, colors[1:])) + '\n')

if __name__ == '__main__':
    solve()