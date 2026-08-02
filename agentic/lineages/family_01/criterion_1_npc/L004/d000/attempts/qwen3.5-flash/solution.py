import sys

# Increase recursion depth to handle deep recursion if necessary
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

    # ans array to store the assigned zone for each asset
    ans = [0] * (n + 1)
    
    # rem_colors[u] is a bitmask of allowed colors for u
    # Bit 0 represents color 1, Bit 1 represents color 2, Bit 2 represents color 3
    # Initially, all colors are allowed (111 in binary = 7)
    rem_colors = [7] * (n + 1)
    
    def backtrack(u):
        # If we have assigned zones to all assets, we found a solution
        if u > n:
            return True
        
        # If no colors are available for the current node, backtrack
        if rem_colors[u] == 0:
            return False
        
        # Try colors 1, 2, 3 in order to ensure lexicographically smallest sequence
        for c in [1, 2, 3]:
            # Check if color c is allowed for node u
            # (rem_colors[u] has bit (c-1) set)
            if not ((rem_colors[u] >> (c - 1)) & 1):
                continue
            
            # Tentatively assign c to u
            # We perform forward checking:
            # Check if assigning c to u makes any future neighbor v (v > u) impossible to color
            # (i.e., rem_colors[v] becomes 0)
            
            updates = []
            valid_assignment = True
            
            for v in adj[u]:
                if v > u:
                    old_val = rem_colors[v]
                    new_val = old_val & ~(1 << (c - 1))
                    rem_colors[v] = new_val
                    updates.append((v, old_val))
                    if new_val == 0:
                        valid_assignment = False
                        break
            
            if not valid_assignment:
                # Revert the changes to rem_colors and try next color
                for v, old_val in updates:
                    rem_colors[v] = old_val
                continue
            
            # Assign color c to u
            ans[u] = c
            
            # Recurse to the next node
            if backtrack(u + 1):
                return True
            
            # Backtrack: unassign and revert changes
            ans[u] = 0
            for v, old_val in updates:
                rem_colors[v] = old_val
        
        return False

    # Start backtracking from node 1
    if backtrack(1):
        print("YES")
        print(*(ans[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()