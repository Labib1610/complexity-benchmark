import sys

# Increase recursion depth to handle deep recursion if necessary
sys.setrecursionlimit(5000)

def main():
    # Read all input from stdin
    # Using sys.stdin.read().split() is efficient for competitive programming
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency list for neighbors with index > current index
    # This helps in forward checking without checking index condition
    adj_greater = [[] for _ in range(n)]
    
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        
        # Direct edges from smaller index to larger index
        if u < v:
            adj_greater[u].append(v)
        else:
            adj_greater[v].append(u)
            
    # possible[i] stores a bitmask of allowed colors for node i
    # Colors 1, 2, 3 correspond to bits 0, 1, 2
    # Initial state: all colors allowed (111 binary = 7)
    possible = [7] * n
    
    # To store the current assignment
    assignment = [0] * n
    
    # History for backtracking to restore 'possible' array
    # We will use a local list for history in each recursive call to avoid global state issues
    # or just pass it? No, just create it.
    
    def backtrack(idx):
        # Base case: all nodes assigned
        if idx == n:
            return True
        
        # If no colors available for current node, backtrack
        if possible[idx] == 0:
            return False
        
        # Try colors 1, 2, 3 in order to ensure lexicographically smallest solution
        for c in range(1, 4):
            # Check if color c is allowed for node idx
            if (possible[idx] >> (c - 1)) & 1:
                # Save the current state of neighbors to restore later
                history = []
                valid_assignment = True
                
                # Update neighbors with index > idx
                # If any neighbor runs out of colors, this assignment is invalid
                for v in adj_greater[idx]:
                    old_val = possible[v]
                    # Remove color c from allowed colors of v
                    possible[v] &= ~(1 << (c - 1))
                    
                    if possible[v] == 0:
                        valid_assignment = False
                        # Restore changes made so far and break
                        for saved_v, saved_val in history:
                            possible[saved_v] = saved_val
                        break
                    
                    history.append((v, old_val))
                
                if valid_assignment:
                    # Assign color c to node idx
                    assignment[idx] = c
                    
                    # Recurse to the next node
                    if backtrack(idx + 1):
                        return True
                    
                    # Backtrack: restore the state of neighbors
                    for saved_v, saved_val in history:
                        possible[saved_v] = saved_val
                    
                    # Reset assignment (optional, as it will be overwritten)
                    assignment[idx] = 0
                else:
                    # If valid_assignment was False, we already restored history in the loop
                    pass
        
        return False

    if backtrack(0):
        print("YES")
        print(*(assignment))
    else:
        print("NO")

if __name__ == '__main__':
    main()