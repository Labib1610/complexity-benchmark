import sys

# Increase recursion depth to handle deep recursion if necessary
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
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        
    # Global state for coloring and history stack
    color = [0] * (n + 1)
    history = [] # Stack of (node, old_color)
    
    # Helper to get available colors for a node
    def get_available(u):
        forbidden = set()
        for v in adj[u]:
            if color[v] != 0:
                forbidden.add(color[v])
        return [c for c in [1, 2, 3] if c not in forbidden]
    
    # Recursive search for feasibility (used by check)
    # This function tries to color the remaining uncolored nodes.
    # It uses MRV (Minimum Remaining Values) heuristic.
    def search():
        best_node = -1
        min_avail = 4
        avail_colors = []
        
        # Find uncolored node with minimum available colors
        for u in range(1, n + 1):
            if color[u] == 0:
                avail = get_available(u)
                if not avail:
                    return False # Impossible
                if len(avail) < min_avail:
                    min_avail = len(avail)
                    avail_colors = avail
                    best_node = u
        
        if best_node == -1:
            return True # All nodes colored successfully
        
        if min_avail == 1:
            # Forced assignment
            c = avail_colors[0]
            color[best_node] = c
            history.append((best_node, c))
            if search():
                return True
            color[best_node] = 0
            history.pop()
            return False
        
        # Try all available colors
        for c in avail_colors:
            color[best_node] = c
            history.append((best_node, c))
            if search():
                return True
            color[best_node] = 0
            history.pop()
            
        return False

    # Function to check if a valid coloring exists for the remaining nodes
    def check(start_node):
        # Save the current history length to restore later
        start_hist_len = len(history)
        res = search()
        # Restore history to state before this check
        while len(history) > start_hist_len:
            node, old_val = history.pop()
            color[node] = old_val
        return res

    # Main recursive solver to find lexicographically first solution
    def main_solve(i):
        if i > n:
            return True
        
        # Try shifts 1, 2, 3 for worker i
        for c in range(1, 4):
            # Check validity with already colored neighbors
            valid = True
            for v in adj[i]:
                if color[v] == c:
                    valid = False
                    break
            
            if valid:
                color[i] = c
                history.append((i, c))
                
                # Pruning: check if a valid completion exists
                if check(i + 1):
                    # If valid completion exists, proceed to find the rest
                    if main_solve(i + 1):
                        return True
                
                # Backtrack
                color[i] = 0
                history.pop()
        
        return False

    # Execute the solver
    if main_solve(1):
        print("YES")
        print(*(color[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()