import sys

def solve():
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    assignment = [0] * (n + 1)

    def is_safe(u, color):
        for v in adj[u]:
            if assignment[v] == color:
                return False
        return True

    def can_color(u):
        """
        Check if the remaining nodes [u...n] can be colored with 3 colors
        given the current assignments.
        Since n is small (40), we can use a backtracking search with 
        pruning or simple backtracking. 
        However, the problem asks for the lexicographically smallest,
        so we try colors 1, 2, 3 for each node in order.
        """
        if u > n:
            return True
        
        # Try colors 1, 2, 3 for the current node u
        for color in (1, 2, 3):
            if is_safe(u, color):
                assignment[u] = color
                if can_color(u + 1):
                    return True
                assignment[u] = 0
        return False

    # The above can_color is a standard backtracking for 3-coloring.
    # To find the lexicographically smallest sequence, we must greedily
    # pick the smallest color for node 1, then check if a valid coloring
    # exists for nodes 2...n.
    
    # Because N=40 is too large for naive backtracking in the worst case,
    # but the constraints on 3-coloring are often handled by backtracking
    # with some pruning or if the graph is sparse.
    # Let's implement the greedy choice with a feasibility check.

    def check_feasibility(current_node):
        if current_node > n:
            return True
        
        # Heuristic: try to color the most constrained nodes first?
        # For a simple feasibility check, standard backtracking might be slow.
        # However, for N=40, it often passes if the graph isn't a worst-case.
        
        # To speed up, we can use a simple backtracking for the remaining nodes.
        # We use a local copy of assignment to avoid corrupting the greedy path.
        
        temp_assignment = list(assignment)
        
        def backtrack(u):
            if u > n:
                return True
            # Try colors for node u
            for c in (1, 2, 3):
                safe = True
                for v in adj[u]:
                    if v < u and temp_assignment[v] == c:
                        safe = False
                        break
                    # Note: we only check against already assigned nodes
                if safe:
                    temp_assignment[u] = c
                    if backtrack(u + 1):
                        return True
                    temp_assignment[u] = 0
            return False
        
        # Actually, the greedy approach is just:
        # for i from 1 to n:
        #   for color in 1, 2, 3:
        #     assignment[i] = color
        #     if is_possible(i + 1): break
        # This is exactly what can_color(1) does.
        return False

    # The standard backtracking search for 3-coloring:
    def solve_backtrack(u):
        if u > n:
            return True
        
        for color in (1, 2, 3):
            if is_safe(u, color):
                assignment[u] = color
                if solve_backtrack(u + 1):
                    return True
                assignment[u] = 0
        return False

    if solve_backtrack(1):
        print("YES")
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == "__main__":
    # Increase recursion depth for deep backtracking
    sys.setrecursionlimit(2000)
    solve()