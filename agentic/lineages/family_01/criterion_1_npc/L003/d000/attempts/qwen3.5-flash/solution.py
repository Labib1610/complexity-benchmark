import sys

# Increase recursion depth to handle N=40 safely
sys.setrecursionlimit(2000)

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

    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    # colors[i] will store the shift assigned to employee i (1, 2, or 3)
    colors = [0] * (n + 1)
    
    # forbidden[i] is a bitmask representing shifts forbidden for employee i
    # due to already assigned neighbors.
    # Bit 0 corresponds to shift 1, Bit 1 to shift 2, Bit 2 to shift 3.
    forbidden = [0] * (n + 1)
    
    def backtrack(u):
        # If we have assigned shifts for all employees, we found a solution
        if u > n:
            return True
        
        # Try shifts 1, 2, 3 in order to ensure lexicographically smallest sequence
        for c in range(1, 4):
            # Check if shift c is forbidden for employee u
            if (forbidden[u] >> (c - 1)) & 1:
                continue
            
            # Tentatively assign shift c to employee u
            colors[u] = c
            
            # We need to update the forbidden sets for neighbors v > u
            # and check for consistency (forward checking)
            changes = []
            valid_branch = True
            
            for v in adj[u]:
                if v > u:
                    old_val = forbidden[v]
                    forbidden[v] |= (1 << (c - 1))
                    changes.append((v, old_val))
                    
                    # If any uncolored neighbor has all 3 shifts forbidden, this branch is dead
                    if forbidden[v] == 7:
                        valid_branch = False
                        break
            
            if valid_branch:
                if backtrack(u + 1):
                    return True
            
            # Backtrack: restore the forbidden sets
            for v, old_val in changes:
                forbidden[v] = old_val
            colors[u] = 0
            
        return False

    if backtrack(1):
        print("YES")
        # Print the assignments for employees 1 to n
        print(*(colors[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()