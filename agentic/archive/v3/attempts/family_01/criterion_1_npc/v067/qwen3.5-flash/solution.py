import sys

# Increase recursion depth to handle N=40 safely
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

    # available[u] stores a bitmask of available colors for node u
    # Colors are 1, 2, 3. We map them to bits 0, 1, 2.
    # 1<<0 = 1 (color 1), 1<<1 = 2 (color 2), 1<<2 = 4 (color 3)
    # Initially all colors are available, so mask is 7 (binary 111)
    available = [7] * (n + 1)
    
    # color[u] stores the assigned color for node u (0 if unassigned)
    color = [0] * (n + 1)
    
    # result array to store the solution
    result = [0] * (n + 1)
    
    # Recursive function to find the lexicographically smallest valid assignment
    def dfs(k):
        # Base case: all individuals assigned
        if k > n:
            return True
        
        # If no colors available for current individual k, backtrack
        if available[k] == 0:
            return False
        
        # Try assigning colors 1, 2, 3 in order to satisfy lexicographical requirement
        for c in [1, 2, 3]:
            c_bit = 1 << (c - 1)
            
            # Check if color c is available for k
            if not (available[k] & c_bit):
                continue
            
            # Tentatively assign color c to k
            # We need to update the available colors of neighbors
            # We only need to update neighbors v > k because neighbors < k are already assigned
            # and their constraints are already reflected in available[k]
            affected = []
            possible = True
            
            for v in adj[k]:
                if v <= k:
                    continue
                
                # If neighbor v has color c available, we remove it
                if (available[v] & c_bit):
                    old_avail = available[v]
                    available[v] &= ~c_bit
                    affected.append((v, old_avail))
                    
                    # Forward checking: if any neighbor has no colors left, this branch is invalid
                    if available[v] == 0:
                        possible = False
                        break
            
            if possible:
                color[k] = c
                if dfs(k + 1):
                    result[k] = c
                    return True
                
                # Backtrack: restore color and available colors
                color[k] = 0
                # Restore in reverse order
                for v, old_avail in reversed(affected):
                    available[v] = old_avail
            else:
                # Rollback changes to available colors if branch failed
                for v, old_avail in reversed(affected):
                    available[v] = old_avail
        
        return False

    # Start DFS from the first individual
    if dfs(1):
        print("YES")
        # Print the sequence of colors for individuals 1 to n
        print(*(result[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()