import sys

# Increase recursion depth to accommodate depth up to N=40
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

    # Use sets for adjacency to handle potential duplicate edges and then convert to lists
    adj = [set() for _ in range(n + 1)]
    
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].add(v)
            adj[v].add(u)
        except StopIteration:
            break
            
    # Convert sets to lists for iteration
    adj = [list(s) for s in adj]

    # mask[i] stores the bitmask of available colors for node i
    # Bits 0, 1, 2 correspond to colors 1, 2, 3
    # Initially all colors are available: 1 | 2 | 4 = 7 (binary 111)
    mask = [7] * (n + 1)
    
    # ans[i] stores the assigned color for node i
    ans = [0] * (n + 1)

    # Backtracking function to find the lexicographically smallest assignment
    def backtrack(idx):
        # Base case: all nodes assigned
        if idx > n:
            return True
        
        # Try colors 1, 2, 3 in order to ensure lexicographically smallest
        for c in range(1, 4):
            # Check if color c is available for node idx
            # mask[idx] reflects constraints from already assigned neighbors (u < idx)
            if not (mask[idx] & (1 << (c - 1))):
                continue
            
            # Assign color c to node idx
            ans[idx] = c
            
            # Forward checking: update masks of unassigned neighbors (v > idx)
            affected_nodes = []
            valid = True
            
            for v in adj[idx]:
                if v > idx:
                    # If color c is available for v, we remove it
                    if mask[v] & (1 << (c - 1)):
                        mask[v] &= ~(1 << (c - 1))
                        affected_nodes.append(v)
                        # If mask becomes 0, v cannot be colored
                        if mask[v] == 0:
                            valid = False
                            break
            
            if valid:
                if backtrack(idx + 1):
                    return True
            
            # Backtrack: restore mask
            for v in affected_nodes:
                mask[v] |= (1 << (c - 1))
            
            # Reset assignment
            ans[idx] = 0
            
        return False

    if backtrack(1):
        print("YES")
        print(*(ans[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()