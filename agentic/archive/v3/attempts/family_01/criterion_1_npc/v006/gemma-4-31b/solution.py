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

    # To find the lexicographically smallest sequence, 
    # we try assigning 1, then 2, then 3 for each researcher in order.
    assignment = [0] * n

    def is_possible(current_node, color):
        # Check if assigning 'color' to 'current_node' is locally valid
        for neighbor in adj[current_node]:
            if neighbor < current_node:
                if assignment[neighbor] == color:
                    return False
        return True

    def check_3_colorable(start_node):
        # We need to check if the remaining graph can be 3-colored
        # given the fixed assignments of nodes 0 to start_node.
        # Since n is small (40), we can use backtracking with pruning.
        
        # However, for n=40, pure backtracking might be too slow.
        # But we only need to check if ANY valid completion exists.
        # We can use a simple backtracking search.
        
        temp_assignment = list(assignment)
        
        def backtrack(node):
            if node == n:
                return True
            
            # If node is already assigned (because it was processed in the outer loop)
            if node <= start_node:
                return backtrack(node + 1)
            
            # Try colors 1, 2, 3
            for c in (1, 2, 3):
                valid = True
                for neighbor in adj[node]:
                    if neighbor < node and temp_assignment[neighbor] == c:
                        valid = False
                        break
                if valid:
                    temp_assignment[node] = c
                    if backtrack(node + 1):
                        return True
                    temp_assignment[node] = 0
            return False

        # To speed up, we can check connectivity or use a more robust 3-coloring check.
        # Given the constraints and the "lexicographically smallest" requirement,
        # we will use a backtracking approach with a bit ofSC bitmask or similar.
        return backtrack(start_node + 1)

    # The aboveCL smallest means we try 1, then 2, then 3 for researcher 0, then 1... for 1, etc.
    # To optimize: for each step, we check if the remaining graph is still 3-colorable.
    
    def can_color(node_idx):
        # Backtracking to check if current partial assignment can be completed
        # Using a simple recursive search with some basic pruning.
        res = [0] * n
        for i in range(node_idx + 1):
            res[i] = assignment[i]
            
        def solve_recursive(idx):
            if idx == n:
                return True
            
            # Try colors 1, 2, 3
            # Optimization: try colors that are least restrictive or just 1,2,3
            for c in (1, 2, 3):
                ok = True
                for neighbor in adj[idx]:
                    if neighbor < idx and res[neighbor] == c:
                        ok = False
                        break
                if ok:
                    res[idx] = c
                    if solve_recursive(idx + 1):
                        return True
                    res[idx] = 0
            return False
        
        return solve_recursive(node_idx + 1)

    # Since n=40 is small but 3^40 is huge, we need an efficient check.
    # However, the "lexicographical" requirement means we must decide 
    # for node 0, then 1, etc.
    # A simple backtracking with a bit of pruning should work for n=40 
    # if the graph is not extremely dense/complex.
    
    # Let's use a more efficient backtracking for the 'can_color' check.
    def solve_full():
        res = [0] * n
        def backtrack(idx):
            if idx == n:
                return True
            
            # Heuristic: try colors in order 1, 2, 3
            for c in (1, 2, 3):
                ok = True
                for neighbor in adj[idx]:
                    if neighbor < idx and res[neighbor] == c:
                        ok = False
                        break
                if ok:
                    res[idx] = c
                    if backtrack(idx + 1):
                        return True
                    res[idx] = 0
            return False
        
        if backtrack(0):
            return res
        return None

    # The above is just to find ANY. To find lexicographically smallest:
    # For each node i from 0 to n-1:
    #   For color c in 1, 2, 3:
    #     assignment[i] = c
    #     if is_possible(i, c) and can_complete(i):
    #       break (keep c)
    
    def can_complete(current_node):
        # Check if the assignment from current_node + 1 to n-1 can be completed
        temp_assign = list(assignment)
        def backtrack(idx):
            if idx == n:
                return True
            
            # Try colors 1, 2, 3
            for c in (1, 2, 3):
                ok = True
                for neighbor in adj[idx]:
                    if neighbor < idx and temp_assign[neighbor] == c:
                        ok = False
                        break
                if ok:
                    temp_assign[idx] = c
                    if backtrack(idx + 1):
                        return True
                    temp_assign[idx] = 0
            return False
        
        return backtrack(current_node + 1)

    # The time limit is 2s. n=40 is small enough that if we are careful, 
    # a backtracking search with a bit of pruning (like degree-based ordering 
    # or just simple DFS) might pass.
    
    # Optimized backtracking for the "can_complete" check:
    def solve_lex():
        final_assignment = [0] * n
        
        def check(idx):
            if idx == n:
                return True
            
            # Try colors 1, 2, 3 for the current node
            for c in (1, 2, 3):
                # Check if color c is valid for node idx
                valid = True
                for neighbor in adj[idx]:
                    if neighbor < idx and final_assignment[neighbor] == c:
                        valid = False
                        break
                
                if valid:
                    final_assignment[idx] = c
                    # Now we need to check if this choice allows a valid coloring for the rest
                    # To avoid exponential blowup, we only do a deep check occasionally 
                    # or use a faster 3-coloring check.
                    # But for n=40, we can actually just backtrack the whole thing once.
                    if check(idx + 1):
                        return True
                    final_assignment[idx] = 0
            return False

        if check(0):
            return final_assignment
        return None

    result = solve_lex()
    if result:
        print("YES")
        print(*(result))
    else:
        print("NO")

solve()