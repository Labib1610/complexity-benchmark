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
    
    # assigned[i] stores the color of worker i (0 if unassigned)
    assigned = [0] * (n + 1)
    
    # rem[i] stores a bitmask of available colors for worker i
    # Colors are 1, 2, 3 corresponding to bits 0, 1, 2
    # Initially all colors are available (111 binary = 7)
    rem = [7] * (n + 1)
    
    def backtrack(u):
        # Base case: all workers assigned
        if u > n:
            return True
        
        # Try colors 1, 2, 3 in increasing order to ensure lexicographically smallest sequence
        for c in range(1, 4):
            # Check if color c is available for worker u
            # rem[u] has been updated by neighbors assigned so far
            if (rem[u] >> (c - 1)) & 1:
                modified = []
                valid = True
                
                # Forward checking: ensure this choice doesn't make any neighbor have 0 options
                for v in adj[u]:
                    if assigned[v] == 0:
                        # If v is unassigned, check if c is available for v
                        if (rem[v] >> (c - 1)) & 1:
                            rem[v] &= ~(1 << (c - 1)) # Remove color c from v's available colors
                            modified.append(v)
                            if rem[v] == 0:
                                valid = False
                                break
                
                if valid:
                    assigned[u] = c
                    if backtrack(u + 1):
                        return True
                    assigned[u] = 0  # Backtrack
                
                # Restore available colors for neighbors
                for v in modified:
                    rem[v] |= (1 << (c - 1))
        
        return False

    if backtrack(1):
        print("YES")
        print(*(assigned[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()