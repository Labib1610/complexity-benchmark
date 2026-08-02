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

    # Adjacency list for the graph
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        adj[u].append(v)
        adj[v].append(u)

    # avail[u] is a bitmask of available colors for vertex u
    # Bit 0 -> Color 1, Bit 1 -> Color 2, Bit 2 -> Color 3
    # Initially all colors are available (1 | 2 | 4 = 7)
    avail = [7] * n
    fixed = [False] * n
    colors = [0] * n

    # Function to check if a valid 3-coloring exists for the remaining uncolored vertices
    # given the current partial coloring state.
    # Uses Minimum Remaining Values (MRV) heuristic for efficiency.
    def check_feasibility():
        best_u = -1
        min_pop = 4  # Max popcount is 3, so 4 is infinity
        
        # Find the uncolored vertex with the fewest available colors
        for u in range(n):
            if fixed[u]:
                continue
            a = avail[u]
            cnt = 0
            if a & 1: cnt += 1
            if a & 2: cnt += 1
            if a & 4: cnt += 1
            
            if cnt < min_pop:
                min_pop = cnt
                best_u = u
                if min_pop == 1:
                    break # 1 is the minimum possible non-zero value
        
        # If all vertices are fixed (or no uncolored vertices found), a solution exists
        if best_u == -1:
            return True
        
        # If any vertex has 0 available colors, no solution exists
        if min_pop == 0:
            return False
        
        # Try to assign each available color to best_u
        for c in range(1, 4):
            if avail[best_u] & (1 << (c - 1)):
                fixed[best_u] = True
                # colors[best_u] = c # Not strictly needed for logic
                
                changed = []
                conflict = False
                
                # Update neighbors
                for v in adj[best_u]:
                    if not fixed[v]:
                        old = avail[v]
                        avail[v] &= ~(1 << (c - 1))
                        changed.append((v, old))
                        if avail[v] == 0:
                            conflict = True
                            break
                
                if not conflict:
                    if check_feasibility():
                        # Revert changes before returning True
                        for v, old in changed:
                            avail[v] = old
                        fixed[best_u] = False
                        return True
                
                # Revert changes if conflict or recursive call failed
                for v, old in changed:
                    avail[v] = old
                fixed[best_u] = False
        
        return False

    result = []
    
    # Main loop: determine the color for each vertex 1..n in order
    # to find the lexicographically smallest sequence.
    for i in range(n):
        found_c = False
        for c in range(1, 4):
            # Check immediate conflict with already fixed neighbors
            conflict = False
            for v in adj[i]:
                if fixed[v]:
                    if colors[v] == c:
                        conflict = True
                        break
                else:
                    # Check if color c is available for neighbor v
                    if not (avail[v] & (1 << (c - 1))):
                        conflict = True
                        break
            
            if conflict:
                continue
            
            # Tentatively fix vertex i with color c
            fixed[i] = True
            # colors[i] = c
            
            neighbor_changed = []
            for v in adj[i]:
                if not fixed[v]:
                    neighbor_changed.append((v, avail[v]))
                    avail[v] &= ~(1 << (c - 1))
            
            # Check if a valid completion exists
            if check_feasibility():
                found_c = True
                result.append(c)
                # Keep the changes to neighbor avail masks since i is now fixed
                break
            else:
                # Revert changes if no valid completion exists
                for v, old in neighbor_changed:
                    avail[v] = old
                fixed[i] = False
                # colors[i] = 0
        
        if not found_c:
            print("NO")
            return

    print("YES")
    print(*(result))

if __name__ == '__main__':
    solve()