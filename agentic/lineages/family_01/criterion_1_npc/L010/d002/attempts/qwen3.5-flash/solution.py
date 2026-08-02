import sys

# Increase recursion depth to accommodate deep recursion trees if necessary
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

    # assignment[i] stores the color of register i (0 if unassigned)
    # forbidden[i] is a bitmask representing forbidden colors for register i
    # Colors 1, 2, 3 correspond to bits 0, 1, 2
    assignment = [0] * (n + 1)
    forbidden = [0] * (n + 1)

    def backtrack(u):
        # If we have assigned colors to all registers, we found a solution
        if u > n:
            return True
        
        # Try colors 1, 2, 3 in increasing order to ensure lexicographically smallest solution
        for c in range(1, 4):
            # Check if color c is valid for register u
            # It's valid if it's not forbidden by any already assigned neighbor
            if (forbidden[u] >> (c - 1)) & 1:
                continue
            
            # Assign color c to register u
            assignment[u] = c
            
            # Forward checking: update forbidden colors for unassigned neighbors
            updated_neighbors = []
            possible = True
            
            for v in adj[u]:
                # Only update neighbors that are not yet assigned (v > u)
                if assignment[v] == 0:
                    bit = 1 << (c - 1)
                    # Only update if the color was not already forbidden
                    if not (forbidden[v] & bit):
                        forbidden[v] |= bit
                        updated_neighbors.append(v)
                        # If all colors are forbidden for any neighbor, this choice is invalid
                        if forbidden[v] == 7:
                            possible = False
                            break
            
            if possible:
                # Recurse to the next register
                if backtrack(u + 1):
                    return True
            
            # Backtrack: unassign u and revert forbidden masks
            assignment[u] = 0
            for v in updated_neighbors:
                forbidden[v] &= ~(1 << (c - 1))
        
        return False

    # Start backtracking from register 1
    if backtrack(1):
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, assignment[1:])) + "\n")
    else:
        sys.stdout.write("NO\n")

if __name__ == '__main__':
    solve()