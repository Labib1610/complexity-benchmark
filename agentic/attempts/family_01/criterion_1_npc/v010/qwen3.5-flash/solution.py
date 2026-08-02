import sys

# Increase recursion depth to handle potential deep recursion, though N=40 is small.
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

    # Adjacency list for the graph
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    # s stores the current assignment. s[i] = 0 means unassigned.
    # We will build the lexicographically smallest solution.
    s = [0] * (n + 1)

    # Function to check if a valid coloring exists for the current state
    # state is a copy of the current assignment s
    def check_completion(state):
        # We use a recursive backtracking solver with MRV (Minimum Remaining Values) heuristic.
        # This finds *any* valid completion if one exists.
        
        def dfs(current_state):
            # Find unassigned vertex with minimum available colors
            best_u = -1
            min_colors = 4
            best_avail_mask = 0
            
            # Iterate over all vertices to find the best one
            for u in range(1, n + 1):
                if current_state[u] == 0:
                    # Calculate available colors for u
                    used_colors = 0
                    for v in adj[u]:
                        if current_state[v] != 0:
                            used_colors |= (1 << (current_state[v] - 1))
                    
                    avail = 7 & (~used_colors)
                    # Count set bits manually for performance
                    count = (avail & 1) + ((avail >> 1) & 1) + ((avail >> 2) & 1)
                    
                    if count == 0:
                        return False # Dead end
                    
                    if count < min_colors:
                        min_colors = count
                        best_u = u
                        best_avail_mask = avail
                        if count == 1:
                            break # No need to search further, 1 is the minimum possible
            
            if min_colors == 4:
                # All vertices are assigned
                return True
            
            # Try colors for best_u
            # We try colors in increasing order (1, 2, 3)
            # best_avail_mask tells us which colors are valid.
            for c in range(1, 4):
                if (1 << (c - 1)) & best_avail_mask:
                    current_state[best_u] = c
                    if dfs(current_state):
                        return True
                    current_state[best_u] = 0
            
            return False

        return dfs(state)

    # Main loop to determine the lexicographically smallest assignment
    for i in range(1, n + 1):
        found = False
        for c in range(1, 4):
            # Check if assigning c to i is valid with respect to already assigned neighbors
            # Neighbors < i are already assigned in s.
            # Neighbors > i are unassigned (0 in s), so they don't constrain c yet.
            conflict = False
            for v in adj[i]:
                if s[v] != 0:
                    if s[v] == c:
                        conflict = True
                        break
            
            if conflict:
                continue
            
            # If valid, check if the rest of the graph can be colored
            s[i] = c
            
            # We need to check if there exists a valid coloring for vertices i+1...n
            # given s[1...i]. We pass a copy of s to check_completion because it modifies the state.
            # check_completion will return True if a completion exists.
            state_copy = s[:] 
            if check_completion(state_copy):
                found = True
                break
            else:
                s[i] = 0 # Backtrack
        
        if not found:
            print("NO")
            return

    print("YES")
    # Print the solution vector s[1]...s[n]
    print(*(s[1:]))

if __name__ == '__main__':
    solve()