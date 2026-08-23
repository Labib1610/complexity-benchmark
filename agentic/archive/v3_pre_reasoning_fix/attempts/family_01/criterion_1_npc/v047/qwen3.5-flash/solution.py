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

    # Adjacency list to store the graph
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
    
    # Precompute next_adj for forward checking
    # next_adj[u] contains only neighbors v such that v > u
    # This helps in efficiently updating constraints for future nodes
    next_adj = [[] for _ in range(n + 1)]
    for u in range(1, n + 1):
        for v in adj[u]:
            if v > u:
                next_adj[u].append(v)
    
    # forbidden[u] is a bitmask where bit k is 1 if color (k+1) is forbidden for worker u
    # Colors are 1, 2, 3 mapped to bits 0, 1, 2
    forbidden = [0] * (n + 1)
    
    # assignment[i] stores the color assigned to worker i
    assignment = [0] * (n + 1)
    
    # Recursive backtracking function
    def backtrack(u):
        # Base case: all workers assigned
        if u > n:
            return True
        
        # Try colors 1, 2, 3 in order to find lexicographically smallest assignment
        for c in range(1, 4):
            # Check if color c is forbidden for worker u
            # bit (c-1) corresponds to color c
            if (forbidden[u] >> (c - 1)) & 1:
                continue
            
            # Tentative assignment
            assignment[u] = c
            
            # Forward checking: update forbidden colors for neighbors v > u
            # We track which neighbors we modified to revert changes during backtracking
            changes = []
            possible = True
            
            for v in next_adj[u]:
                # If color c is not already forbidden for v
                if not ((forbidden[v] >> (c - 1)) & 1):
                    forbidden[v] |= (1 << (c - 1))
                    changes.append(v)
                    # If all colors (1, 2, 3) become forbidden for v, this branch is invalid
                    # 7 is binary 111
                    if forbidden[v] == 7:
                        possible = False
                        break
            
            if possible:
                # Recurse to the next worker
                if backtrack(u + 1):
                    return True
            
            # Backtrack: revert the changes made to forbidden array
            for v in changes:
                forbidden[v] &= ~(1 << (c - 1))
            
            # Reset assignment (optional, but good practice)
            assignment[u] = 0
        
        return False

    # Start backtracking from worker 1
    if backtrack(1):
        print("YES")
        # Print the assignment for workers 1 to n
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()