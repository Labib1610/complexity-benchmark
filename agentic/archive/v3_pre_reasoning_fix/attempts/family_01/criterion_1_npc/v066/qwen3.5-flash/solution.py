import sys

# Increase recursion depth to handle deep recursion trees up to N=40
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

    # out_adj[u] will store neighbors v such that v > u
    # This allows us to efficiently propagate constraints forward
    out_adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        if u < v:
            out_adj[u].append(v)
        else:
            out_adj[v].append(u)
            
    # color_count[v][c] stores the number of neighbors of v (with index < v) assigned color c
    # We use indices 1, 2, 3 for colors 1, 2, 3
    # This allows us to track which colors are forbidden for future nodes
    color_count = [[0] * 4 for _ in range(n + 1)]
    
    # forbidden_count[v] stores the number of colors that are forbidden for v
    # (i.e., colors with count > 0). If this reaches 3, v cannot be colored.
    forbidden_count = [0] * (n + 1)
    
    # Current assignment
    assignment = [0] * (n + 1)
    
    # To store the final result
    result = None
    
    def backtrack(u):
        nonlocal result
        
        # Base case: all units assigned successfully
        if u > n:
            result = assignment[1:]
            return True
        
        # Try colors 1, 2, 3 in lexicographical order to ensure smallest solution
        for c in range(1, 4):
            # Check if color c is valid for unit u
            # It is valid if no neighbor v < u has assigned color c
            if color_count[u][c] == 0:
                assignment[u] = c
                
                blocked = False
                
                # Apply constraints to neighbors v > u (forward checking)
                # We update their forbidden colors and check if any becomes completely blocked
                for v in out_adj[u]:
                    if color_count[v][c] == 0:
                        forbidden_count[v] += 1
                    color_count[v][c] += 1
                    if forbidden_count[v] == 3:
                        blocked = True
                
                if not blocked:
                    if backtrack(u + 1):
                        return True
                
                # Rollback constraints for this color attempt
                for v in out_adj[u]:
                    color_count[v][c] -= 1
                    if color_count[v][c] == 0:
                        forbidden_count[v] -= 1
        
        return False

    # Start backtracking from unit 1
    if backtrack(1):
        print("YES")
        print(*(result))
    else:
        print("NO")

if __name__ == '__main__':
    solve()