import sys

# Increase recursion depth to handle N=40 safely, though default is usually 1000.
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

    # Adjacency list for the graph
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
        except StopIteration:
            break

    # color[i] stores the vault assigned to substance i (1, 2, or 3)
    # 0 indicates unassigned
    color = [0] * (n + 1)
    
    # forbidden[i] stores a bitmask of colors forbidden for substance i
    # by its neighbors that have already been assigned.
    # bit 0 corresponds to color 1, bit 1 to color 2, bit 2 to color 3.
    # If forbidden[i] == 7 (binary 111), substance i cannot be assigned any color.
    forbidden = [0] * (n + 1)

    # Backtracking function to find the lexicographically smallest assignment
    def backtrack(idx):
        if idx > n:
            return True
        
        # Try assigning vaults 1, 2, 3 in order to ensure lexicographical smallest
        for c in range(1, 4):
            mask = 1 << (c - 1)
            
            # Check if color c is valid for idx (i.e., not forbidden by neighbors < idx)
            if forbidden[idx] & mask:
                continue
            
            # Assign color c to idx
            color[idx] = c
            
            # Update forbidden masks for neighbors v > idx
            # We need to track changes to revert them if we backtrack
            updates = []
            blocked = False
            
            for v in adj[idx]:
                if v > idx:
                    # Store current value to revert later
                    updates.append((v, forbidden[v]))
                    forbidden[v] |= mask
                    
                    # If any neighbor becomes blocked (all 3 colors forbidden), prune this branch
                    if forbidden[v] == 7:
                        blocked = True
                        break
            
            if not blocked:
                if backtrack(idx + 1):
                    return True
            
            # Backtrack: revert forbidden masks
            for v, old_val in updates:
                forbidden[v] = old_val
        
        return False

    # Start the backtracking
    if backtrack(1):
        print("YES")
        # Print the assignment sequence
        print(*(color[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()