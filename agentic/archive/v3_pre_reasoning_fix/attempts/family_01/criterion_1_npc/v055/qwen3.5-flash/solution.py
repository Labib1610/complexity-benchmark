import sys

# Increase recursion depth to handle N=40 safely, though default is usually 1000
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
    
    # Adjacency list
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
    
    # Pre-filter adjacency list for forward checking
    # We only care about neighbors v > u when assigning u
    # This avoids checking 'v > u' inside the recursive loop repeatedly
    adj_filtered = [[] for _ in range(n + 1)]
    for u in range(1, n + 1):
        for v in adj[u]:
            if v > u:
                adj_filtered[u].append(v)
    
    # domains[i] is a bitmask of allowed colors for task i
    # Colors 1, 2, 3 correspond to bits 0, 1, 2
    # Initially all colors allowed (mask 7 = 111 binary)
    # We use index 1 to n
    domains = [7] * (n + 1)
    
    # To store the result assignment
    assignment = [0] * (n + 1)
    
    # Backtracking function with forward checking
    # We use in-place modification of 'domains' and backtrack (restore) to avoid list copying overhead
    def backtrack(u):
        if u > n:
            return True
        
        # Try colors 1, 2, 3 in increasing order to ensure lexicographically smallest solution
        for c in range(1, 4):
            # Check if color c is allowed for task u
            # (c-1) is the bit index
            if (domains[u] >> (c - 1)) & 1:
                
                # Try assigning color c to u
                # We need to update domains for neighbors v > u (Forward Checking)
                modified = []
                possible = True
                
                for v in adj_filtered[u]:
                    old = domains[v]
                    # Remove color c from v's allowed colors
                    # mask has 0 at bit (c-1) and 1 elsewhere
                    mask = ~(1 << (c - 1))
                    new = old & mask
                    domains[v] = new
                    modified.append((v, old))
                    
                    # If any neighbor has no allowed colors left, this assignment is invalid
                    if new == 0:
                        possible = False
                        break
                
                if possible:
                    assignment[u] = c
                    # Recurse to next task
                    if backtrack(u + 1):
                        return True
                    # If backtrack returns False, we continue to next color for u
                    # domains will be restored below
                    
                # Backtrack: restore domains for neighbors
                for v, old in modified:
                    domains[v] = old
        
        return False

    # Start backtracking from task 1
    if backtrack(1):
        print("YES")
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()