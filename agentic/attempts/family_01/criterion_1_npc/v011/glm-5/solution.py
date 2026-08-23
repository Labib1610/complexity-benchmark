import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [set() for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].add(v)
        adj[v].add(u)
    
    # For each vertex, list of forbidden colors (neighbors already assigned)
    forbidden = [set() for _ in range(n)]
    color = [0] * n
    
    # We use backtracking with pruning.
    # To find lexicographically smallest, we try colors 1, 2, 3 in order.
    
    # Simple backtracking might be slow for n=40 if the graph is dense.
    # But for 3-coloring, we can use the fact that if a vertex has >= 3 neighbors
    # already colored with distinct colors, it's impossible.
    # Also, if a vertex has 3 forbidden colors, we backtrack.
    
    # We can also use a heuristic: process vertices with most constraints first?
    # But lexicographical order requires us to assign in order 0, 1, 2, ..., n-1.
    # So we must process in that order to guarantee lexicographically smallest.
    
    # Optimization: 
    # If a vertex has 3 neighbors in the "future" (not yet colored) that form a clique,
    # and current vertex has 2 forbidden colors, then those 3 future neighbors must
    # use the remaining color, but they can't if they are a clique.
    # This is complex to implement.
    
    # Let's try simple backtracking with basic pruning.
    
    def backtrack(idx):
        if idx == n:
            return True
        
        for c in range(1, 4):
            if c not in forbidden[idx]:
                # Check if this assignment creates a "dead end" for future vertices
                # Specifically, if any uncolored neighbor now has 3 forbidden colors
                possible = True
                for neighbor in adj[idx]:
                    if neighbor > idx: # uncolored neighbor (since we process in order)
                        if len(forbidden[neighbor]) == 2 and c not in forbidden[neighbor]:
                            # This neighbor would have 3 forbidden colors
                            possible = False
                            break
                
                if possible:
                    color[idx] = c
                    # Add c to forbidden sets of neighbors
                    added_to = []
                    for neighbor in adj[idx]:
                        if neighbor > idx:
                            if c not in forbidden[neighbor]:
                                forbidden[neighbor].add(c)
                                added_to.append(neighbor)
                    
                    if backtrack(idx + 1):
                        return True
                    
                    # Backtrack: remove c from forbidden sets
                    for neighbor in added_to:
                        forbidden[neighbor].remove(c)
        
        return False
    
    if backtrack(0):
        print("YES")
        print(' '.join(map(str, color)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()