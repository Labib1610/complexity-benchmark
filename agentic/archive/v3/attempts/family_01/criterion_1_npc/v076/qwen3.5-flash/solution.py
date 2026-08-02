import sys

# Increase recursion depth to handle potential depth up to N=40
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
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        
    # Remove duplicate edges if any (though input should be simple)
    for i in range(1, n + 1):
        if len(adj[i]) > 1:
            adj[i] = list(set(adj[i]))

    # assignment[i] stores the color assigned to node i (0 if unassigned)
    # Colors are 1, 2, 3.
    assignment = [0] * (n + 1)
    
    # forbidden[i] stores a bitmask of colors forbidden for node i by its colored neighbors.
    # Bit k corresponds to color k+1.
    # e.g., if color 1 is forbidden, bit 0 is set.
    forbidden = [0] * (n + 1)

    def backtrack(u):
        # Base case: all nodes 1..n assigned
        if u > n:
            return True
        
        # Try colors 1, 2, 3 in order for lexicographically smallest solution
        for c in range(1, 4):
            # Check if color c is forbidden for u by colored neighbors
            if (forbidden[u] >> (c - 1)) & 1:
                continue
            
            # Forward checking:
            # Check if assigning c to u makes any uncolored neighbor impossible to color
            possible = True
            mask = 1 << (c - 1)
            
            for v in adj[u]:
                if assignment[v] == 0:
                    # If v's forbidden set becomes full (7 = 111 binary)
                    if (forbidden[v] | mask) == 7:
                        possible = False
                        break
            
            if possible:
                # Assign color c to u
                assignment[u] = c
                
                # Update forbidden sets for uncolored neighbors
                for v in adj[u]:
                    if assignment[v] == 0:
                        forbidden[v] |= mask
                
                # Recurse
                if backtrack(u + 1):
                    return True
                
                # Backtrack
                assignment[u] = 0
                for v in adj[u]:
                    if assignment[v] == 0:
                        forbidden[v] &= ~mask
        
        return False

    if backtrack(1):
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, assignment[1:])) + "\n")
    else:
        sys.stdout.write("NO\n")

if __name__ == '__main__':
    solve()