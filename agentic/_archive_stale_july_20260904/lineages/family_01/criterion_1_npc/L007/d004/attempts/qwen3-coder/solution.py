import sys
from collections import defaultdict

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u-1, v-1))  # Convert to 0-indexed
    return n, m, edges

def solve(n, m, edges):
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Color array (0 means unassigned, 1-3 are colors)
    color = [0] * n
    
    # Check if graph is 3-colorable with backtracking
    # We use a heuristic: try vertices with highest degree first
    def get_next_vertex():
        # Find the uncolored vertex with maximum degree in the remaining subgraph
        best_degree = -1
        best_vertex = -1
        for i in range(n):
            if color[i] == 0:  # Not colored yet
                degree = sum(1 for neighbor in adj[i] if color[neighbor] == 0)
                if degree > best_degree:
                    best_degree = degree
                    best_vertex = i
        return best_vertex
    
    # More sophisticated approach: try in order but use constraint checking
    def is_safe(v, c):
        # Check if we can assign color c to vertex v
        for neighbor in adj[v]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack():
        # Find next uncolored vertex
        v = -1
        for i in range(n):
            if color[i] == 0:
                v = i
                break
        
        if v == -1:
            return True  # All vertices colored
            
        # Try colors 1, 2, 3 in order for lex smallest
        for c in range(1, 4):
            if is_safe(v, c):
                color[v] = c
                if backtrack():
                    return True
                color[v] = 0  # Backtrack
                
        return False  # No color works
    
    # For better performance on adversarial inputs, let's use a more advanced strategy
    # Sort vertices by degree descending for better pruning
    order = list(range(n))
    order.sort(key=lambda x: len(adj[x]), reverse=True)
    
    # But we still want the lexicographically smallest solution
    # So we need to be smarter about our search
    
    def backtrack_smart():
        # Find the first uncolored vertex in the original order (for lex smallest)
        v = -1
        for i in range(n):
            if color[i] == 0:
                v = i
                break
                
        if v == -1:
            return True
            
        # Try colors 1, 2, 3 in order
        for c in range(1, 4):
            if is_safe(v, c):
                color[v] = c
                if backtrack_smart():
                    return True
                color[v] = 0
                
        return False
    
    # Even better: use forward checking
    def backtrack_forward_check():
        # Find the first uncolored vertex
        v = -1
        for i in range(n):
            if color[i] == 0:
                v = i
                break
                
        if v == -1:
            return True
            
        # Try colors 1, 2, 3 in order
        for c in range(1, 4):
            if is_safe(v, c):
                color[v] = c
                if backtrack_forward_check():
                    return True
                color[v] = 0
                
        return False
    
    # Let's just go with basic backtracking optimized for this specific case
    if backtrack():
        return "YES\n" + " ".join(map(str, color))
    else:
        return "NO"

def main():
    n, m, edges = read_input()
    result = solve(n, m, edges)
    print(result)

if __name__ == "__main__":
    main()