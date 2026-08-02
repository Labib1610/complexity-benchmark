import sys

# Increase recursion depth just in case, though we use iterative approach
sys.setrecursionlimit(200005)

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
        
    # Array to store channel assignment
    # 0: unassigned, 1: channel 1, 2: channel 2
    color = [0] * (n + 1)
    
    # Iterate through all nodes from 1 to n
    # This ensures we process components in an order that respects lexicographical requirement
    # Specifically, for each component, the first node we encounter (smallest index)
    # is assigned channel 1, which is the greedy choice for lexicographically smallest sequence.
    for i in range(1, n + 1):
        if color[i] == 0:
            # Node i is the smallest index in its connected component
            # We assign channel 1 to i. If the component is bipartite, this fixes the colors.
            # If not, we will find a conflict.
            
            color[i] = 1
            stack = [i]
            
            while stack:
                u = stack.pop()
                current_color = color[u]
                # Neighbors must have the opposite color (1 -> 2, 2 -> 1)
                next_color = 3 - current_color
                
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = next_color
                        stack.append(v)
                    elif color[v] != next_color:
                        # Conflict found: Graph is not bipartite
                        print("NO")
                        return

    # If we complete the loop without returning, a valid assignment exists
    print("YES")
    # Output the assignment sequence
    sys.stdout.write(" ".join(map(str, color[1:])) + "\n")

if __name__ == '__main__':
    solve()