import sys

# Increase recursion depth to accommodate deep recursion if necessary
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
    # Using 1-based indexing for positions 1 to n
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
        except StopIteration:
            break
    
    # Precompute neighbors with index > u to speed up forward checking
    # This avoids checking 'if v > idx' inside the recursive function repeatedly
    adj_greater = [[] for _ in range(n + 1)]
    for u in range(1, n + 1):
        for v in adj[u]:
            if v > u:
                adj_greater[u].append(v)
                
    # valid[u] stores a bitmask of available colors for vertex u
    # Colors are 1, 2, 3. We map them to bits 0, 1, 2.
    # Bit 0 corresponds to color 1 (value 1)
    # Bit 1 corresponds to color 2 (value 2)
    # Bit 2 corresponds to color 3 (value 4)
    # Initially all colors are available (mask 7 = 111 binary)
    valid = [7] * (n + 1)
    
    # assignment array to store the result
    assignment = [0] * (n + 1)
    
    # Flag to indicate if a solution has been found
    solved = False
    
    def backtrack(idx):
        nonlocal solved
        if solved:
            return
        
        if idx > n:
            # All positions assigned successfully
            print("YES")
            print(*(assignment[1:]))
            solved = True
            return
        
        # valid[idx] contains the bitmask of allowed colors for current position
        # We iterate through possible colors 1, 2, 3 (bits 0, 1, 2)
        mask = valid[idx]
        
        # Try each color in increasing order to ensure lexicographically smallest
        for bit in range(3):
            c_mask = 1 << bit  # 1, 2, 4
            if mask & c_mask:
                c_val = bit + 1  # 1, 2, 3
                
                # Check constraints with neighbors > idx
                # We need to record changes to valid masks to backtrack
                changes = []
                possible = True
                
                for v in adj_greater[idx]:
                    old_mask = valid[v]
                    new_mask = old_mask & ~c_mask
                    if old_mask != new_mask:
                        valid[v] = new_mask
                        changes.append((v, old_mask))
                        if new_mask == 0:
                            possible = False
                            break
                
                if possible:
                    assignment[idx] = c_val
                    backtrack(idx + 1)
                    if solved:
                        return
                
                # Backtrack: restore valid masks
                for v, old_mask in changes:
                    valid[v] = old_mask
    
    backtrack(1)
    
    if not solved:
        print("NO")

if __name__ == '__main__':
    solve()