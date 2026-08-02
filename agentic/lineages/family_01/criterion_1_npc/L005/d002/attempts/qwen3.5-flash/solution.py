import sys

# Increase recursion depth to handle potential deep recursion
sys.setrecursionlimit(5000)

def solve():
    # Read all input from stdin
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency list for the graph
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
    
    # s array to store colors, 0 means uncolored
    # We use 1-based indexing for convenience to match problem statement
    s = [0] * (n + 1)

    # Function to check if current partial assignment can be completed
    # This uses a backtracking approach with MRV (Minimum Remaining Values) heuristic for speed
    def can_color():
        # Identify uncolored vertices
        uncolored = [i for i in range(1, n + 1) if s[i] == 0]
        
        if not uncolored:
            return True
        
        # MRV Heuristic: Pick the uncolored vertex with the fewest valid colors
        best_vertex = -1
        min_valid_cnt = 4
        best_forbidden = 0
        
        # Iterate through uncolored vertices to find the best one
        for u in uncolored:
            # Calculate forbidden colors from neighbors
            forbidden = 0
            for v in adj[u]:
                if s[v] != 0:
                    forbidden |= (1 << s[v])
            
            # Count valid colors (1, 2, 3)
            # We can use bitwise operations
            valid_cnt = 0
            for c in range(1, 4):
                if not ((forbidden >> c) & 1):
                    valid_cnt += 1
            
            if valid_cnt == 0:
                return False
            
            if valid_cnt < min_valid_cnt:
                min_valid_cnt = valid_cnt
                best_vertex = u
                best_forbidden = forbidden
                if min_valid_cnt == 1:
                    break
        
        # If we found a vertex to color
        if best_vertex != -1:
            # Try valid colors for best_vertex
            # We use the precomputed best_forbidden
            for c in range(1, 4):
                if not ((best_forbidden >> c) & 1):
                    s[best_vertex] = c
                    if can_color():
                        return True
                    s[best_vertex] = 0
            
            return False
        else:
            return True

    # Main loop to determine s[1]...s[n] lexicographically
    possible = True
    for i in range(1, n + 1):
        if not possible:
            break
        
        found_color = False
        for c in range(1, 4):
            # Check if c is valid for i given current s
            # We only need to check neighbors that are already colored
            valid_local = True
            for v in adj[i]:
                if s[v] != 0 and s[v] == c:
                    valid_local = False
                    break
            
            if valid_local:
                s[i] = c
                # Check if this choice allows the rest to be colored
                if can_color():
                    found_color = True
                    break
                else:
                    s[i] = 0
        
        if not found_color:
            possible = False
            break
    
    if possible:
        print("YES")
        print(*(s[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()