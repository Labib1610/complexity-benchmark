import sys

def solve():
    # Increase recursion depth for deep backtracking if necessary
    sys.setrecursionlimit(2000)
    
    # Read n and m
    try:
        line1 = sys.stdin.readline().split()
        if not line1:
            return
        n, m = map(int, line1)
    except ValueError:
        return

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)

    # assignment[i] stores the block for individual i (0-indexed)
    # 0: unassigned, 1, 2, 3: assigned blocks
    assignment = [0] * n

    def is_valid(u, color):
        for v in adj[u]:
            if assignment[v] == color:
                return False
        return True

    def can_color(u):
        """
        Check if the remaining graph can be 3-colored given current assignments.
        Since n is small (40), we can use backtracking with pruning.
        However, to speed up, we only check the connected components.
        """
        # To check if a graph is 3-colorable is NP-complete.
        # But with n=40, a simple backtracking might work if we are careful.
        # However, the lexicographical requirement means we must try 1, then 2, then 3
        # for each node in order. The 'can_color' check is for feasibility.
        
        # For the specific constraints and the requirement of lexicographically smallest,
        # we can just backtrack directly.
        return True

    def backtrack(u):
        if u == n:
            return True
        
        # Try colors 1, 2, 3 in order for lexicographical smallest result
        for color in [1, 2, 3]:
            if is_valid(u, color):
                assignment[u] = color
                # To optimize, one could add a check here to see if the remaining 
                # graph is still 3-colorable, but with n=40, simple backtracking
                # might be slow. Let's refine the backtracking.
                if backtrack(u + 1):
                    return True
                assignment[u] = 0
        return False

    # The simple backtracking above is O(3^n), which is too slow for n=40.
    # We need a more efficient way to check 3-colorability or a better search.
    # However, the problem asks for the lexicographically smallest sequence.
    # This means for node 0, we try 1, then 2, then 3. 
    # Once we pick a color for node 0, we check if the rest is 3-colorable.
    
    def is_3_colorable(node_idx, current_assignment):
        # Simple backtracking to check 3-colorability of the remaining nodes
        # Use a local assignment to avoid mutating the global one
        temp_assignment = list(current_assignment)
        
        def check(idx):
            if idx == n:
                return True
            if temp_assignment[idx] != 0:
                return check(idx + 1)
            
            # Try colors
            for c in [1, 2, 3]:
                ok = True
                for v in adj[idx]:
                    if temp_assignment[v] == c:
                        ok = False
                        break
                if ok:
                    temp_assignment[idx] = c
                    if check(idx + 1):
                        return True
                    temp_assignment[idx] = 0
            return False
        
        return check(node_idx)

    # To find the lexicographically smallest, we must greedily pick the smallest
    # possible color for each node and ensure the remaining graph is 3-colorable.
    # Since n=40 is small but not that small, we use a more optimized 3-color check.
    
    def solve_lex():
        res = [0] * n
        for i in range(n):
            found = False
            for color in [1, 2, 3]:
                # Check if assigning 'color' to 'i' is locally valid
                ok_local = True
                for v in adj[i]:
                    if v < i and res[v] == color:
                        ok_local = False
                        break
                
                if ok_local:
                    # Check if the rest of the graph can be 3-colored
                    res[i] = color
                    # To speed up, we only check if the remaining nodes [i+1, n-1]
                    # can be colored given the assignments for [0, i].
                    if is_3_colorable_fast(i + 1, res):
                        found = True
                        break
                    res[i] = 0
            if not found:
                return None
        return res

    def is_3_colorable_fast(start_node, current_assignment):
        # Optimized 3-coloring check using basic pruning
        temp_assign = list(current_assignment)
        
        def backtrack_fast(idx):
            if idx == n:
                return True
            if temp_assign[idx] != 0:
                return backtrack_fast(idx + 1)
            
            # Heuristic: try colors that are least restrictive or just 1,2,3
            for c in [1, 2, 3]:
                ok = True
                for v in adj[idx]:
                    if temp_assign[v] == c:
                        ok = False
                        break
                if ok:
                    temp_assign[idx] = c
                    if backtrack_fast(idx + 1):
                        return True
                    temp_assign[idx] = 0
            return False
        
        return backtrack_fast(start_node)

    # The above is still potentially slow. Let's use a more robust 3-color check.
    # Given n=40, we can use bitmasks for available colors.
    def solve_final():
        res = [0] * n
        
        def can_finish(idx, current_res):
            # Use a more efficient 3-coloring check
            # For n=40, we can use a simple backtracking with a bit of optimization
            temp = list(current_res)
            
            def search(u):
                if u == n: return True
                if temp[u] != 0: return search(u + 1)
                
                # Try colors
                used = 0
                for v in adj[u]:
                    if temp[v] != 0:
                        used |= (1 << temp[v])
                
                for c in [1, 2, 3]:
                    if not (used & (1 << c)):
                        temp[u] = c
                        if search(u + 1): return True
                        temp[u] = 0
                return False
            
            return search(idx)

        for i in range(n):
            possible = False
            for c in [1, 2, 3]:
                # Check if c is valid for i
                valid = True
                for v in adj[i]:
                    if v < i and res[v] == c:
                        valid = False
                        break
                if valid:
                    res[i] = c
                    if can_finish(i + 1, res):
                        possible = True
                        break
                    res[i] = 0
            if not possible:
                print("NO")
                return
        
        print("YES")
        print(*(res))

    solve_final()

solve()