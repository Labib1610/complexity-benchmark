import sys

# Increase recursion depth just in case, though iterative approach is used.
sys.setrecursionlimit(300000)

def solve():
    # Read all input from standard input efficiently
    # sys.stdin.read() reads the entire input into a string
    # .split() splits it by whitespace into a list of strings
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Create an iterator to parse integers efficiently
    # map(int, input_data) returns an iterator that yields integers
    iterator = map(int, input_data)
    
    try:
        n = next(iterator)
        m = next(iterator)
    except StopIteration:
        return

    # Build adjacency list for the graph
    # adj[i] will store the list of personnel incompatible with person i
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        try:
            u = next(iterator)
            v = next(iterator)
            adj[u].append(v)
            adj[v].append(u)
        except StopIteration:
            break
            
    # Array to store the slot assignment (1 or 2) for each person
    # 0 indicates unassigned
    colors = [0] * (n + 1)
    
    # Iterate through each person to handle disconnected components
    # We want the lexicographically smallest sequence s_1, s_2, ..., s_n.
    # This means we want s_1 to be 1 if possible. If s_1 is fixed (by a previous component or choice),
    # we move to s_2, and so on.
    # When we encounter an unassigned person 'i' in the loop (1 to n), it is the smallest index
    # in its connected component that hasn't been assigned yet.
    # To minimize the sequence, we must assign 'i' to slot 1.
    # Once 'i' is assigned to 1, the bipartite constraints force the assignments for all other
    # nodes in this component. If this leads to a conflict, then no valid assignment exists.
    
    for i in range(1, n + 1):
        if colors[i] != 0:
            continue
        
        # Start DFS traversal for the component containing i
        colors[i] = 1
        stack = [i]
        
        while stack:
            u = stack.pop()
            current_color = colors[u]
            next_color = 3 - current_color  # Toggle between 1 and 2
            
            for v in adj[u]:
                if colors[v] == 0:
                    colors[v] = next_color
                    stack.append(v)
                elif colors[v] != next_color:
                    # If a neighbor has the same color, the graph is not bipartite
                    print("NO")
                    return

    # If we successfully assign colors to all nodes without conflicts
    print("YES")
    # Output the assignment for persons 1 to n
    # Using sys.stdout.write for efficient output
    sys.stdout.write(" ".join(map(str, colors[1:])) + "\n")

if __name__ == '__main__':
    solve()