import sys

# Increase recursion depth to handle deep recursion in backtracking
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

    # Adjacency list
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
    
    # colors array: 0 = uncolored, 1, 2, 3 = colors
    colors = [0] * (n + 1)
    result = []
    
    # Check validity of the current partial assignment
    def check_valid():
        # Identify uncolored vertices
        uncolored = [i for i in range(1, n + 1) if colors[i] == 0]
        if not uncolored:
            return True
        
        # allowed[v] is a bitmask of allowed colors for vertex v
        # bit 0 -> color 1, bit 1 -> color 2, bit 2 -> color 3
        # Initially all colors allowed (111 binary = 7)
        allowed = [7] * (n + 1)
        
        # Propagate constraints from already colored neighbors
        for v in uncolored:
            for neighbor in adj[v]:
                c = colors[neighbor]
                if c != 0:
                    # c is 1, 2, 3 -> bits 0, 1, 2
                    mask = 1 << (c - 1)
                    allowed[v] &= ~mask
            if allowed[v] == 0:
                return False
        
        # Find connected components of uncolored vertices
        visited = [False] * (n + 1)
        components = []
        
        for v in uncolored:
            if not visited[v]:
                comp = []
                stack = [v]
                visited[v] = True
                while stack:
                    u = stack.pop()
                    comp.append(u)
                    for neighbor in adj[u]:
                        if colors[neighbor] == 0 and not visited[neighbor]:
                            visited[neighbor] = True
                            stack.append(neighbor)
                components.append(comp)
        
        # Check if each component can be validly colored
        for comp in components:
            if not solve_component(comp, allowed):
                return False
        return True

    def solve_component(vertices, allowed):
        # Work on a copy of vertices to avoid modifying the list passed by caller
        current_vertices = list(vertices)
        # History to restore allowed state if we backtrack (return False)
        # We only need to restore if we return False
        history = []
        
        # Unit Propagation: Force colors where only 1 option remains
        while True:
            best_v = -1
            best_bit = 0
            found_unit = False
            
            # Find a vertex with exactly 1 allowed color
            for v in current_vertices:
                if allowed[v] == 0:
                    # Invalid state
                    # Restore history before returning False
                    for h_v, h_val in reversed(history):
                        allowed[h_v] = h_val
                    return False
                
                # Count set bits
                # Using bin().count('1') is efficient enough for small integers
                if bin(allowed[v]).count('1') == 1:
                    best_v = v
                    best_bit = allowed[v] & -allowed[v] # Isolate lowest set bit
                    found_unit = True
                    break
            
            if not found_unit:
                break
            
            # Assign color to best_v
            # Update neighbors
            for neighbor in adj[best_v]:
                # Only update neighbors that are still uncolored (in current_vertices)
                # Note: neighbors outside current_vertices are already colored or in other components
                if colors[neighbor] == 0:
                    old_val = allowed[neighbor]
                    allowed[neighbor] &= ~best_bit
                    history.append((neighbor, old_val))
                    if allowed[neighbor] == 0:
                        # Conflict
                        for h_v, h_val in reversed(history):
                            allowed[h_v] = h_val
                        return False
            
            # Remove best_v from current_vertices
            current_vertices.remove(best_v)
        
        # If no uncolored vertices left, valid coloring found
        if not current_vertices:
            return True
            
        # MRV Branching: Pick vertex with minimum remaining values
        best_v = -1
        min_pop = 4
        
        for v in current_vertices:
            pop = bin(allowed[v]).count('1')
            if pop < min_pop:
                min_pop = pop
                best_v = v
        
        # Identify neighbors to update during branching
        neighbors_to_update = []
        for neighbor in adj[best_v]:
            if colors[neighbor] == 0:
                neighbors_to_update.append(neighbor)
        
        # Try each allowed color for best_v
        temp = allowed[best_v]
        while temp > 0:
            bit = temp & -temp
            temp ^= bit
            
            # Save state for neighbors to restore on backtrack
            saved_state = []
            for neighbor in neighbors_to_update:
                saved_state.append((neighbor, allowed[neighbor]))
                allowed[neighbor] &= ~bit
            
            # Recurse with best_v removed
            new_vertices = [x for x in current_vertices if x != best_v]
            if solve_component(new_vertices, allowed):
                return True
            
            # Restore state
            for neighbor, old_val in saved_state:
                allowed[neighbor] = old_val
                
        return False

    # Main loop: Determine lexicographically smallest assignment
    for i in range(1, n + 1):
        found = False
        # Try colors 1, 2, 3
        for c in [1, 2, 3]:
            # Check compatibility with already colored neighbors
            ok = True
            for neighbor in adj[i]:
                if colors[neighbor] == c:
                    ok = False
                    break
            if not ok:
                continue
            
            # Tentatively assign
            colors[i] = c
            # Check if this assignment can be extended
            if check_valid():
                result.append(c)
                found = True
                break
            else:
                # Backtrack
                colors[i] = 0
        
        if not found:
            print("NO")
            return

    print("YES")
    print(*(result))

if __name__ == '__main__':
    solve()