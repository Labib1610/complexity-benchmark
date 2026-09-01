import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # Convert to sets for fast conflict checking
    adj_set = [set(lst) for lst in adj]
    
    assignment = [0] * n  # 0 = unassigned, 1,2,3 = colors
    
    # MRV ordering: choose unassigned vertex with most constraints
    def select_unassigned():
        best = -1
        best_deg = -1
        for i in range(n):
            if assignment[i] == 0:
                # degree = number of unassigned neighbors
                deg = sum(1 for v in adj[i] if assignment[v] == 0)
                if deg > best_deg:
                    best_deg = deg
                    best = i
        return best
    
    # Backtracking search
    def backtrack():
        # Find next unassigned vertex
        v = select_unassigned()
        if v == -1:
            return True  # all assigned
        
        # Try colors in order 1,2,3 for lexicographic smallest
        for color in (1,2,3):
            # Check if color is valid
            conflict = False
            for u in adj[v]:
                if assignment[u] == color:
                    conflict = True
                    break
            if conflict:
                continue
            
            assignment[v] = color
            if backtrack():
                return True
            assignment[v] = 0
        
        return False
    
    if backtrack():
        print("YES")
        print(" ".join(str(x) for x in assignment))
    else:
        print("NO")

if __name__ == "__main__":
    solve()