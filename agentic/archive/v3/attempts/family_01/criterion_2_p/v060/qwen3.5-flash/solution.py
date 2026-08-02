import sys
from collections import deque

# Set recursion depth just in case, though iterative BFS is used.
sys.setrecursionlimit(200005)

def solve():
    # Read all input from standard input efficiently
    # sys.stdin.read().split() handles all whitespace (spaces, newlines)
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
    # Using 1-based indexing for convenience (nodes 1 to N)
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        
    # Array to store the assignment (1 or 2)
    # 0 indicates unassigned
    s = [0] * (n + 1)
    
    # Iterate through all nodes 1 to N
    # This order ensures that for any connected component, we encounter
    # the node with the smallest index first.
    for i in range(1, n + 1):
        if s[i] == 0:
            # Start BFS for the connected component containing i
            # To ensure lexicographically smallest sequence, we assign s[i] = 1.
            # Since i is the first node of this component encountered in the loop,
            # minimizing s[i] is the priority for lexicographical order.
            # If the graph is bipartite, we can always choose the orientation
            # such that the first node gets color 1.
            
            s[i] = 1
            queue = deque([i])
            
            while queue:
                u = queue.popleft()
                current_color = s[u]
                next_color = 3 - current_color  # Flip color: 1->2, 2->1
                
                for v in adj[u]:
                    if s[v] == 0:
                        s[v] = next_color
                        queue.append(v)
                    elif s[v] != next_color:
                        # Conflict detected: adjacent nodes have same color
                        # This means the graph is not bipartite
                        print("NO")
                        return

    # If no conflicts were found, a valid assignment exists
    print("YES")
    # Print the assignments for nodes 1 to N
    print(" ".join(map(str, s[1:])))

if __name__ == '__main__':
    solve()