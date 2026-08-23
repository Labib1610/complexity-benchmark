import sys

# Increase recursion depth to handle potential deep recursion trees
sys.setrecursionlimit(5000)

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

    # Adjacency list for the graph
    # Using 1-based indexing for employees as per problem statement
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    # valid_colors[i] is a bitmask of allowed colors for node i.
    # Colors are 1, 2, 3, mapped to bits 0, 1, 2 respectively.
    # Initially all colors are allowed (mask 111 binary = 7).
    valid_colors = [7] * (n + 1)
    
    # Array to store the assigned color for each node (0 means unassigned)
    color = [0] * (n + 1)

    # Recursive backtracking function to find a valid assignment
    # We assign colors in order 1 to n to satisfy the lexicographical requirement.
    # The first valid complete assignment found will be the lexicographically smallest
    # because we try colors 1, 2, 3 in order for each node.
    def backtrack(idx):
        # Base case: all nodes assigned successfully
        if idx > n:
            return True
        
        # If current node has no valid colors, this path is invalid
        if valid_colors[idx] == 0:
            return False
            
        # Try to assign colors 1, 2, 3 in increasing order
        for c in range(1, 4):
            # Check if color c is allowed for node idx based on already colored neighbors
            if (valid_colors[idx] >> (c - 1)) & 1:
                # Forward checking:
                # If we assign c to idx, we must ensure that for every uncolored neighbor v,
                # v still has at least one valid color available.
                # Specifically, if valid_colors[v] has only c available, assigning c to idx
                # would leave v with 0 colors, making it uncolorable.
                
                possible_c = True
                for v in adj[idx]:
                    if v > idx: # Only check uncolored neighbors
                        # If v has only color c available, we cannot assign c to idx
                        if valid_colors[v] == (1 << (c - 1)):
                            possible_c = False
                            break
                
                if possible_c:
                    # Assign color c to idx
                    color[idx] = c
                    
                    # Update valid colors for uncolored neighbors
                    # We need to record changes to revert them on backtrack
                    affected_neighbors = []
                    for v in adj[idx]:
                        if v > idx:
                            valid_colors[v] &= ~(1 << (c - 1))
                            affected_neighbors.append(v)
                    
                    # Recurse to next node
                    if backtrack(idx + 1):
                        return True
                    
                    # Backtrack: Revert changes
                    for v in affected_neighbors:
                        valid_colors[v] |= (1 << (c - 1))
                    
                    color[idx] = 0
                    
        return False

    # Start backtracking from the first employee
    if backtrack(1):
        print("YES")
        print(*(color[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()