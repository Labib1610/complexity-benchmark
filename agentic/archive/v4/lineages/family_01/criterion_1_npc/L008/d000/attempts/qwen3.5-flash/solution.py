import sys

# Increase recursion depth to accommodate N=40
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

    # Adjacency list: adj[u] will store neighbors v such that v > u
    # This optimization reduces the number of neighbors to iterate in forward checking
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        if u < v:
            adj[u].append(v)
        else:
            adj[v].append(u)

    # assignment[i] stores the color assigned to node i
    assignment = [0] * (n + 1)
    
    # forbidden[i] is a bitmask representing the colors forbidden for node i
    # by already colored neighbors.
    # Bit 0 (value 1) -> Color 1 forbidden
    # Bit 1 (value 2) -> Color 2 forbidden
    # Bit 2 (value 4) -> Color 3 forbidden
    # If (forbidden[i] == 7), then all colors are forbidden.
    forbidden = [0] * (n + 1)

    def backtrack(u):
        # Base case: all nodes colored
        if u > n:
            return True
        
        # Try colors 1, 2, 3 in order to find the lexicographically smallest solution
        for c in range(1, 4):
            # Check if color c is forbidden by neighbors < u
            # We use (c-1) to map color 1->bit 0, 2->bit 1, 3->bit 2
            if (forbidden[u] >> (c - 1)) & 1:
                continue
            
            # Forward checking: ensure that assigning c to u doesn't make any neighbor v > u impossible
            # We need to find neighbors v > u that will be affected (i.e., c becomes forbidden for them)
            # and check if this leads to a state where v has no valid colors.
            affected = []
            possible = True
            
            # Iterate over neighbors v > u
            for v in adj[u]:
                # If c is not already forbidden for v, it will be added to forbidden[v]
                if not ((forbidden[v] >> (c - 1)) & 1):
                    # Check if adding c makes forbidden[v] have all 3 colors (7)
                    if (forbidden[v] | (1 << (c - 1))) == 7:
                        possible = False
                        break
                    else:
                        affected.append(v)
            
            if not possible:
                continue
            
            # Apply constraints to neighbors
            for v in affected:
                forbidden[v] |= (1 << (c - 1))
            
            # Assign color to u
            assignment[u] = c
            
            # Recurse to next node
            if backtrack(u + 1):
                return True
            
            # Backtrack: revert changes
            assignment[u] = 0
            for v in affected:
                forbidden[v] &= ~(1 << (c - 1))
                
        return False

    if backtrack(1):
        print("YES")
        # Print the colors for nodes 1 to n
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()