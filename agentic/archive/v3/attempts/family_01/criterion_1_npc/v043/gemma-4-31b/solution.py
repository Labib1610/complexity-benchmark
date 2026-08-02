import sys

def solve():
    # Increase recursion depth for deep backtracking
    sys.setrecursionlimit(2000)
    
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

    # s[i] stores the shift assigned to person i (0 means unassigned)
    s = [0] * (n + 1)

    def is_valid(u, shift):
        for v in adj[u]:
            if s[v] == shift:
                return False
        return True

    def backtrack(u):
        if u > n:
            return True
        
        # To get the lexicographically smallest sequence, 
        # try shifts 1, 2, 3 in order.
        for shift in (1, 2, 3):
            if is_valid(u, shift):
                s[u] = shift
                # Heuristic: Check if the remaining graph is still 3-colorable.
                # However, with N=40, simple backtracking with lexicographical 
                # order might be too slow without pruning.
                # But for N=40, we can try a basic backtracking first.
                if backtrack(u + 1):
                    return True
                s[u] = 0
        return False

    # For N=40, 3^40 is too large. We need a more efficient way to check 3-colorability.
    # But the problem asks for the lexicographically smallest, meaning we must 
    # try shift 1 for person 1, then check if the rest can be colored.
    
    def can_color(node, current_s):
        # A simple 3-coloring check for the remaining nodes
        # Using a basic backtracking with a bit of pruning
        if node > n:
            return True
        
        # Try to find a node with the fewest available colors (MRV heuristic)
        best_node = -1
        min_options = 4
        
        # To speed up, we only check nodes that are not yet colored
        for i in range(1, n + 1):
            if current_s[i] == 0:
                # Count available colors for node i
                used = {current_s[v] for v in adj[i] if current_s[v] != 0}
                options = 3 - len(used)
                if options < min_options:
                    min_options = options
                    best_node = i
                if options == 0: return False # Prune
        
        if best_node == -1: return True
        
        # Try colors for the best_node
        used = {current_s[v] for v in adj[best_node] if current_s[v] != 0}
        for color in (1, 2, 3):
            if color not in used:
                current_s[best_node] = color
                if can_color(node, current_s):
                    return True
                current_s[best_node] = 0
        return False

    # To find the lexicographically smallest, we fix s[i] one by one
    # and check if a valid 3-coloring exists for the remaining.
    final_s = [0] * (n + 1)
    for i in range(1, n + 1):
        found = False
        for shift in (1, 2, 3):
            if is_valid(i, shift):
                # Temporarily assign shift to person i
                final_s[i] = shift
                # Check if the rest of the graph can be 3-colored
                # We pass a copy of final_s to the checker
                if can_color(1, list(final_s)):
                    found = True
                    break
                final_s[i] = 0
        if not found:
            print("NO")
            return

    print("YES")
    print(*(final_s[1:]))

solve()