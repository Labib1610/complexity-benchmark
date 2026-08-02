import sys

# Increase recursion depth to handle deep recursion trees if necessary
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
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
        except StopIteration:
            break
            
    # available[i] is a bitmask representing allowed colors for node i
    # Colors 1, 2, 3 correspond to bits 0, 1, 2
    # Initially, all colors are available (mask 111 binary = 7)
    available = [7] * (n + 1)
    
    # s[i] stores the color assigned to node i
    s = [0] * (n + 1)
    
    def backtrack(idx):
        # Base case: all nodes assigned
        if idx > n:
            return True
        
        # If no colors available for current node, backtrack
        if available[idx] == 0:
            return False
        
        # Try colors 1, 2, 3 in order to ensure lexicographically smallest solution
        for c in range(1, 4):
            bit = 1 << (c - 1)
            
            # Check if color c is available for node idx
            if (available[idx] & bit):
                s[idx] = c
                
                # Forward checking: update available colors for neighbors > idx
                modified = []
                valid = True
                
                for neighbor in adj[idx]:
                    if neighbor > idx:
                        # If neighbor has this color available, remove it
                        if available[neighbor] & bit:
                            available[neighbor] ^= bit
                            modified.append(neighbor)
                            # If neighbor has no colors left, this path is invalid
                            if available[neighbor] == 0:
                                valid = False
                                # We continue to mark all changes to restore later, 
                                # but we can stop checking validity if we just want to prune.
                                # However, we must ensure we record all modifications for restoration.
                                # Since we iterate all neighbors, we can just set flag.
                
                if valid:
                    if backtrack(idx + 1):
                        return True
                
                # Backtrack: restore available colors for neighbors
                for neighbor in modified:
                    available[neighbor] |= bit
        
        return False

    # Start the backtracking from the first node
    if backtrack(1):
        print("YES")
        print(*(s[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()