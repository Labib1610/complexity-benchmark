import sys

# Increase recursion depth to handle N=40 safely, though default 1000 is enough.
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

    # Precompute adjacency lists for optimization.
    # adj_before[u] contains neighbors v such that v < u.
    # adj_after[u] contains neighbors v such that v > u.
    # This allows us to quickly check constraints from already assigned nodes
    # and update constraints for unassigned nodes.
    adj_before = [[] for _ in range(n + 1)]
    adj_after = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        if u < v:
            adj_before[v].append(u)
            adj_after[u].append(v)
        else:
            adj_before[u].append(v)
            adj_after[v].append(u)
            
    # forbidden[v] stores a bitmask of colors forbidden for vertex v.
    # Bit 0 corresponds to color 1, bit 1 to color 2, bit 2 to color 3.
    # If bit k is set, color k+1 cannot be used.
    forbidden = [0] * (n + 1)
    ans = [0] * (n + 1)
    
    # Recursive backtracking function to assign channels
    def backtrack(u):
        # Base case: all transmitters assigned
        if u > n:
            return True
        
        # Try channels 1, 2, 3 in order to ensure lexicographically smallest sequence
        for c in range(1, 4):
            # Check validity against already assigned neighbors (v < u)
            valid = True
            for v in adj_before[u]:
                if ans[v] == c:
                    valid = False
                    break
            if not valid:
                continue
            
            # If valid, apply constraints to neighbors v > u (Forward Checking)
            mask = 1 << (c - 1)
            modified = []
            can_extend = True
            
            for v in adj_after[u]:
                old_forbidden = forbidden[v]
                forbidden[v] |= mask
                # If all 3 colors are forbidden (111 in binary = 7), this branch is invalid
                if forbidden[v] == 7:
                    can_extend = False
                    # Revert changes made in this step
                    for prev_v, prev_old in modified:
                        forbidden[prev_v] = prev_old
                    forbidden[v] = old_forbidden
                    break
                modified.append((v, old_forbidden))
            
            if can_extend:
                ans[u] = c
                if backtrack(u + 1):
                    return True
                ans[u] = 0 # Reset for backtracking
            
            # Revert changes made to 'forbidden' array if we didn't find a solution
            if can_extend:
                for prev_v, prev_old in modified:
                    forbidden[prev_v] = prev_old
                    
        return False

    # Start backtracking from the first transmitter
    if backtrack(1):
        print("YES")
        # Print the solution sequence space-separated
        print(*(ans[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()