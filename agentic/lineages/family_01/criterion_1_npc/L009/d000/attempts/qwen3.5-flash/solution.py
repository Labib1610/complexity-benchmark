import sys

# Increase recursion depth to handle up to N=40 safely (though default is usually 1000)
sys.setrecursionlimit(2000)

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

    # We only need to store neighbors with index > current node for forward checking
    # adj_greater[u] will contain list of v such that v > u and (u, v) is an edge
    # This optimization avoids checking neighbors < u during the update step.
    adj_greater = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        if u < v:
            adj_greater[u].append(v)
        else:
            adj_greater[v].append(u)
    
    # assignment array, 1-based index, 0 means unassigned
    assignment = [0] * (n + 1)
    
    # forbidden masks: 0 means no colors forbidden. 
    # Bit 0 (1) for color 1, Bit 1 (2) for color 2, Bit 2 (4) for color 3.
    # forbidden[u] stores the colors forbidden for u by neighbors < u
    forbidden = [0] * (n + 1)
    
    # We want to find the lexicographically smallest assignment.
    # We try colors 1, 2, 3 in order for each person 1..n.
    
    def backtrack(idx):
        # If we have assigned all n personnel, we found a solution
        if idx > n:
            return True
        
        # If forbidden mask for current node is 7 (111 binary), then it has no valid colors.
        # This can happen if neighbors < idx have used all 3 colors.
        if forbidden[idx] == 7:
            return False
        
        # Try colors 1, 2, 3
        for c in range(1, 4):
            # Check if color c is forbidden for idx by neighbors < idx
            if (forbidden[idx] >> (c - 1)) & 1:
                continue
            
            # Assign c to idx
            assignment[idx] = c
            
            # We need to update forbidden masks for neighbors > idx (Forward Checking).
            # We also need to check if any neighbor becomes impossible (mask == 7).
            # We store changes to revert them later (backtracking).
            
            changes = []
            possible = True
            
            # Iterate only over neighbors > idx
            for neighbor in adj_greater[idx]:
                old_mask = forbidden[neighbor]
                new_mask = old_mask | (1 << (c - 1))
                
                # If new_mask is 7, this neighbor cannot be colored with any color
                # given the current assignment of idx.
                # This means the current branch is invalid.
                
                forbidden[neighbor] = new_mask
                changes.append((neighbor, old_mask))
                
                if new_mask == 7:
                    possible = False
                    # We break here to save time, but we must revert changes.
                    break 
            
            if possible:
                if backtrack(idx + 1):
                    return True
            
            # Backtrack: revert changes to forbidden masks
            for neighbor, old_mask in changes:
                forbidden[neighbor] = old_mask
            
            # Reset assignment (optional, as it will be overwritten)
            assignment[idx] = 0
            
        return False

    if backtrack(1):
        print("YES")
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()