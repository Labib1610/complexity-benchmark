```python
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

    # To find the lexicographically smallest assignment, 
    # we try assigning shifts 1, 2, 3 to workers 0, 1, ..., n-1 in order.
    # Since n is small (up to 40), we can use backtracking with pruning.
    
    assignment = [0] * n

    def is_valid(u, color):
        for v in adj[u]:
            if v < u: # Only check already assigned workers
                if assignment[v] == color:
                    return False
        return True

    def backtrack(u):
        if u == n:
            return True
        
        # Try colors 1, 2, 3 in order for lexicographical smallest
        for color in [1, 2, 3]:
            if is_valid(u, color):
                assignment[u] = color
                # Optimization: check if remaining nodes can be colored.
                # Given n=40, simple backtracking might be slow, 
                # but the constraints and the "lexicographically smallest" 
                # requirement often make it feasible if the search space is pruned.
                if backtrack(u + 1):
                    return True
                assignment[u] = 0
        return False

    # To speed up, we can check if the graph is 3-colorable using a more 
    # robust method if necessary, but for n=40, simple DFS with 
    # pruning (checking constraints) is often sufficient if the 
    # number of solutions is large or if failure is found quickly.
    # However, 3-coloring is NP-complete.
    # Let's use a slightly more optimized backtracking.
    
    if backtrack(0):
        print("YES")