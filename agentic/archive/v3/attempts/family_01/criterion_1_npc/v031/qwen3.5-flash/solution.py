import sys

# Increase recursion depth to accommodate deep recursion trees if necessary
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

    # Adjacency list for the graph
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    # forbidden[u] stores a bitmask of colors used by neighbors of u
    # Bits: 0 for color 1, 1 for color 2, 2 for color 3
    # Initially 0 (no colors forbidden)
    forbidden = [0] * (n + 1)
    colors = [0] * (n + 1)
    
    # Precompute bit values for colors 1, 2, 3
    # color_bits[1] = 1 (001), color_bits[2] = 2 (010), color_bits[3] = 4 (100)
    color_bits = [0, 1, 2, 4]
    
    def backtrack(u):
        # Base case: all vertices colored
        if u > n:
            return True
        
        # Try colors 1, 2, 3 in order to ensure lexicographically smallest solution
        for c in range(1, 4):
            # Check if color c is forbidden by any already colored neighbor (neighbors < u)
            # forbidden[u] accumulates constraints from neighbors 1..u-1
            if not (forbidden[u] & color_bits[c]):
                colors[u] = c
                changed = []
                possible = True
                
                # Propagate constraint to neighbors > u
                for v in adj[u]:
                    if v > u:
                        # If color c is not yet forbidden for v
                        if not (forbidden[v] & color_bits[c]):
                            forbidden[v] |= color_bits[c]
                            changed.append(v)
                
                # Check if any neighbor became fully forbidden (all 3 colors used)
                # This is a necessary condition for the remaining graph to be 3-colorable
                for v in changed:
                    if forbidden[v] == 7: # 1 | 2 | 4 = 7
                        possible = False
                        break
                
                if possible:
                    if backtrack(u + 1):
                        return True
                
                # Backtrack: restore forbidden status for neighbors
                for v in changed:
                    forbidden[v] ^= color_bits[c] # Toggle the bit back to 0
                
                colors[u] = 0
        
        return False

    # Start backtracking from vertex 1
    if backtrack(1):
        print("YES")
        # Print the colors for vertices 1 to n
        print(*(colors[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()