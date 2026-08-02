import sys

# Increase recursion depth to handle depth up to N=40 safely
sys.setrecursionlimit(5000)

def solve():
    # Read all input from standard input at once
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
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        adj[u].append(v)
        adj[v].append(u)

    # colors array stores the assigned vault (1, 2, or 3) for each compound
    # 0 indicates uncolored
    colors = [0] * n 
    
    # forbidden array stores a bitmask of forbidden colors for each compound
    # bit 0 corresponds to vault 1, bit 1 to vault 2, bit 2 to vault 3
    forbidden = [0] * n 
    
    # Recursive backtracking function to find the lexicographically smallest assignment
    def backtrack(idx):
        # Base case: all compounds assigned
        if idx == n:
            return True
        
        # Try assigning vaults 1, 2, 3 (mapped to 0, 1, 2 for bitmasks)
        # Iterating in order ensures we find the lexicographically smallest solution
        for c in range(3):
            # Check if color c is allowed for current compound idx
            # If bit c is set in forbidden[idx], then c is forbidden
            if (forbidden[idx] >> c) & 1:
                continue
            
            # Assign color c+1 to idx
            colors[idx] = c + 1
            
            # Update forbidden colors for neighbors
            changed = []
            conflict = False
            
            for v in adj[idx]:
                # We only need to update forbidden for uncolored neighbors
                if colors[v] == 0:
                    old_val = forbidden[v]
                    forbidden[v] |= (1 << c)
                    changed.append((v, old_val))
                    # Pruning: if any uncolored neighbor has all 3 colors forbidden, backtrack immediately
                    if forbidden[v] == 7: # 7 is 111 in binary (bits 0, 1, 2 set)
                        conflict = True
                        break
            
            if conflict:
                # Revert changes to forbidden array
                for v, old_val in changed:
                    forbidden[v] = old_val
                colors[idx] = 0
                continue
            
            # Recurse to the next compound
            if backtrack(idx + 1):
                return True
            
            # Backtrack: revert changes
            colors[idx] = 0
            for v, old_val in changed:
                forbidden[v] = old_val
        
        return False

    if backtrack(0):
        print("YES")
        print(*(colors))
    else:
        print("NO")

if __name__ == '__main__':
    solve()