import sys

def solve():
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    # State: current assignment of artifacts 0 to n-1
    # assignment[i] = 0 (unassigned), 1, 2, or 3
    assignment = [0] * n

    def is_valid(u, color):
        for v in adj[u]:
            if assignment[v] == color:
                return False
        return True

    def can_color(u):
        """
        Check if the remaining artifacts can be colored with 3 colors
        given the current partial assignment.
        Since n is small (up to 40), we use backtracking with pruning.
        """
        if u == n:
            return True
        
        # If already assigned by the lexicographical greedy process
        if assignment[u] != 0:
            return can_color(u + 1)
        
        # Try colors for the current node
        # To speed up, we can use a simple heuristic or just try colors
        # However, we need to know if *any* valid coloring exists.
        # For n=40, 3-coloring is NP-complete, but with current constraints,
        # we can optimize.
        
        # Optimization: try colors that are less constrained
        for color in [1, 2, 3]:
            if is_valid(u, color):
                assignment[u] = color
                if can_color(u + 1):
                    return True
                assignment[u] = 0
        return False

    # To find the lexicographically smallest sequence, we try to assign 
    # the smallest possible color (1, then 2, then 3) to artifact i,
    # and then check if the rest of the graph can still be 3-colored.
    
    # Because n=40 is small but 3-coloring is hard, we need a robust check.
    # We use a backtracking search with a bit of pruning.
    
    def check_possible(start_node):
        # Copy current assignment to avoid mutating the main one during check
        temp_assignment = list(assignment)
        
        def backtrack(u):
            if u == n:
                return True
            if temp_assignment[u] != 0:
                return backtrack(u + 1)
            
            # Try colors
            for c in [1, 2, 3]:
                valid = True
C
                for v in adj[u]:
                    if temp_assignment[v] == c:
                        valid = False
                        C                break
                if valid:
                    temp_assignment[u] = c
                    if backtrack(u + 1):
                        return True
                    temp_assignment[u] = 0
            return False
        
        # Optimization: The backtrack function above is slow. 
        # We use a slightly more efficient version.
        return backtrack(start_node)

    # Since we need lexicographical smallest, we greedily pick color 1, 2, 3 for each node.
    # To check if a choice is viable, we need to see if the remaining can be 3-colored.
    # Given n=40, we can use a simple backtracking with a bit of optimization.
    
    # Optimized 3-coloring check
    def is_3_colorable(u, current_assignment):
        if u == n:
            return True
        if current_assignment[u] != P_ASSIGN[u]: # This is not quite right, need a local copy
            pass
        # See below for the actual implementation inside the loop
        return False

    # Redefining the check to be more efficient
    def check(u):
        # current_assignment is the state of 'assignment'
        # We need to check if nodes from u+1 to n-1 can be colored.
        # Since we are deciding for node u, we check if assignment[0...u] can be extended.
        
        # Local helper for backtracking
        local_assign = list(assignment)
        
        def solve_recursive(curr):
            if curr == n:
                return True
            if local_assign[curr] != 0:
                return solve_recursive(curr + 1)
            
            # Try colors
            for c in (1, 2, 3):
                ok = True
                for v in adj[curr]:
                    if local_assign[v] == c:
                        ok = False
                        break
                if ok:
                    local_assign[curr] = c
                    if solve_recursive(curr + 1):
                        return True
                    localB local_assign[curr] = 0
            return False
        
        return solve_recursive(u + 1)

    # To handle n=40, we need a faster 3-coloring check.
    # A simple backtracking might be too slow, but since we only need to know
    # if ANY coloring exists, we can use a few heuristics.
    
    import random
    def fast_check(u):
        local_assign = list(assignment)
        
        def solve_rec(curr):
            if curr == n: return True
            if local_assign[curr] != 0: return solve_rec(curr + 1)
            
            # Heuristic: try colors that are least used or just 1,2,3
            for c in (1, 2, 3):
                ok = True
                for v in adj[curr]:
                    if local_assign[v] == c:
                        ok = False
                        break
                if ok:
                    local_assign[curr] = c
                    if solve_rec(curr + 1): return True
                    local_assign[curr] = 0
            return False
        
        return solve_rec(u + 1)

    # To avoid TLE on n=40, we can use a more efficient 3-coloring check
    # or a simple backtracking if the graph is sparse.
    # Let's use the greedy approach with a basic backtracking check.
    
    # The actual loop to determine the lexicographically smallest sequence:
    for i in range(n):
        found = False
        for color in [1, 2, 3]:
            # Check if 'color' is valid for artifact i
            if is_valid(i, color):
                assignment[i] = color
                if fast_check(i):
                    found = True
                    break
                assignment[i] = 0
        if not found:
            print("NO")
            return

    print("YES")
    print(*(assignment))

# The fast_check above might still be slow. Let's refine it.
# Using a basic backtracking with a simple pruning:
def solve_final():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data: return
    n, m = int(input_data[0]), int(input_data[1])
    adj = [[] for _ in range(n)]
    for i in range(m):
        u, v = int(input_data[2+2*i])-1, int(input_data[3+2*i])-1
        adj[u].append(v)
        adj[v].append(u)

    res = [0] * n

    def can_color(idx, current_res):
        if idx == n: return True
        if current_res[idx] != 0: return can_color(idx + 1, current_res)
        
        for c in (1, 2, 3):
            possible = True
            for neighbor in adj[idx]:
                if current_res[neighbor] == c:
                    possible = False
                    break
            if possible:
                current_res[idx] = c
                if can_color(idx + 1, current_res): return True
                current_res[idx] = 0
        return False

    for i in range(n):
        possible_overall = False
        for c in (1, 2, 3):
            # Check if assigning color c to node i is valid
            valid_now = True
            for neighbor in adj[i]:
                if neighbor < i and res[neighbor] == c:
                    valid_now = False
                    break
            
            if valid_now:
                res[i] = c
                # Check if this choice allows a full 3-coloring
                if can_color(i + 1, list(res)):
                    possible_overall = True
                    break
                res[i] = 0
        
        if not possible_overall:
            print("NO")
            return

    print("YES")
    print(*(res))

solve_final()