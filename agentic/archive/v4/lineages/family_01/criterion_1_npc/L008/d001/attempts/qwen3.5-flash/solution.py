import sys

# Increase recursion depth to handle deep recursion trees if necessary
sys.setrecursionlimit(5000)

def solve():
    # Read all input from standard input
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

    # count[v][c] stores the number of neighbors of v that are assigned color c
    # c is 1, 2, 3. We use indices 1, 2, 3.
    # Initialize with 0. Size is n + 1 for vertices 1..n.
    count = [[0] * 4 for _ in range(n + 1)]
    
    # color[i] stores the assigned color for task i
    color = [0] * (n + 1)
    
    # Helper function for backtracking
    def backtrack(k):
        # Base case: all tasks assigned
        if k > n:
            return True
        
        # Try colors 1, 2, 3 in increasing order to find lexicographically smallest
        for c in range(1, 4):
            # Check if color c is valid for task k
            # It is valid if no neighbor assigned so far (neighbors < k) has color c.
            # This is tracked by count[k][c].
            if count[k][c] == 0:
                # Tentatively assign c to k
                color[k] = c
                
                # Forward checking: update constraints for unassigned neighbors (v > k)
                # We need to track which neighbors we modified to revert correctly
                modified_neighbors = []
                valid_assignment = True
                
                for v in adj[k]:
                    if v > k:
                        # This neighbor is unassigned.
                        # We forbid color c for v.
                        count[v][c] += 1
                        modified_neighbors.append(v)
                        
                        # Forward checking: if v becomes uncolorable (all colors forbidden)
                        if count[v][1] > 0 and count[v][2] > 0 and count[v][3] > 0:
                            valid_assignment = False
                            break
                
                if valid_assignment:
                    if backtrack(k + 1):
                        return True
                
                # Backtrack: revert changes to count array
                for v in modified_neighbors:
                    count[v][c] -= 1
                
                # Reset color
                color[k] = 0
        
        # If no color works for k, this branch is invalid
        return False

    # Start backtracking from task 1
    if backtrack(1):
        print("YES")
        # Print the colors for tasks 1 to n
        print(*(color[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()