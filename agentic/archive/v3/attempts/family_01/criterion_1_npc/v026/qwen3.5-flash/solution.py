import sys

# Increase recursion depth to handle N=40 safely
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
    
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # Filter adj to only store neighbors > u for forward checking
    # This optimization reduces the number of checks we need to perform
    # when updating constraints for unassigned nodes.
    adj_filtered = [[] for _ in range(n)]
    for u in range(n):
        for v in adj[u]:
            if v > u:
                adj_filtered[u].append(v)
    
    # forbidden[u] is a bitmask of colors forbidden for node u by already assigned neighbors.
    # Colors are 1, 2, 3. We map them to bits 0, 1, 2.
    # Initially 0 (no colors forbidden).
    forbidden = [0] * n
    
    # color[u] stores the assigned color for node u (1, 2, or 3).
    color = [0] * n
    
    # history tracks changes to 'forbidden' array to allow efficient backtracking.
    # It stores tuples of (v, old_forbidden_value).
    # This avoids recreating lists or deep copying during backtracking.
    history = []
    
    def backtrack(u):
        # If we have assigned colors to all nodes, we found a solution.
        if u == n:
            return True
        
        # Try to assign colors 1, 2, 3 to node u in order.
        # This ensures lexicographically smallest sequence.
        for c in range(1, 4):
            # Check if color c is already forbidden by neighbors < u
            # If bit (c-1) is set in forbidden[u], then color c is forbidden.
            if (forbidden[u] >> (c - 1)) & 1:
                continue
            
            color[u] = c
            
            # Record history length to restore 'forbidden' state later
            history_len = len(history)
            fail = False
            
            # Forward checking: update forbidden masks for neighbors v > u
            for v in adj_filtered[u]:
                old_val = forbidden[v]
                forbidden[v] |= (1 << (c - 1))
                history.append((v, old_val))
                
                # If all colors are forbidden for any unassigned neighbor, this path is invalid.
                # 7 is binary 111 (all bits 0, 1, 2 set).
                if forbidden[v] == 7: 
                    fail = True
                    break
            
            # If not failed by forward checking, recurse
            if not fail:
                if backtrack(u + 1):
                    return True
            
            # Backtrack: restore 'forbidden' array to state before this step
            # We remove changes from history to revert forbidden array
            del history[history_len:]
        
        return False

    # Start backtracking from node 0
    if backtrack(0):
        print("YES")
        print(*(color))
    else:
        print("NO")

if __name__ == '__main__':
    solve()