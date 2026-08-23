import sys

# Increase recursion depth to handle deep recursion trees
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
        
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        
    # Remove duplicate edges if any
    for i in range(1, n + 1):
        adj[i] = list(set(adj[i]))
        
    # assignment[i] stores the color assigned to node i (0 if unassigned)
    assignment = [0] * (n + 1)
    
    # forbidden_counts[u][c] stores the number of assigned neighbors of u that have color c
    # c is in 1..3, so we use size 4
    forbidden_counts = [[0] * 4 for _ in range(n + 1)]
    
    # available_colors[u] is a bitmask of valid colors for u
    # 1 -> bit 0, 2 -> bit 1, 3 -> bit 2
    # Initially, all colors are available (7 = 111 in binary)
    available_colors = [7] * (n + 1)
    
    def backtrack(idx):
        # If we have assigned colors to all nodes, we found a solution
        if idx > n:
            return True
        
        # If no color is available for the current node, prune this branch
        if available_colors[idx] == 0:
            return False
        
        # Try colors 1, 2, 3 in order to ensure lexicographically smallest solution
        for c in range(1, 4):
            # Check if color c is available for the current node idx
            if not (available_colors[idx] & (1 << (c - 1))):
                continue
            
            # Assign color c to idx
            assignment[idx] = c
            
            # Forward checking: update constraints for unassigned neighbors
            changes = []
            possible = True
            
            for v in adj[idx]:
                if assignment[v] == 0: # v is unassigned
                    # If forbidden_counts[v][c] is 0, it means color c was available for v
                    # Now it becomes forbidden
                    if forbidden_counts[v][c] == 0:
                        available_colors[v] &= ~(1 << (c - 1))
                        # If available_colors[v] becomes 0, then v cannot be colored
                        if available_colors[v] == 0:
                            possible = False
                            break
                    
                    forbidden_counts[v][c] += 1
                    changes.append(v)
            
            if possible:
                if backtrack(idx + 1):
                    return True
            
            # Backtrack: undo the assignment and constraint updates
            assignment[idx] = 0
            for v in changes:
                forbidden_counts[v][c] -= 1
                if forbidden_counts[v][c] == 0:
                    available_colors[v] |= (1 << (c - 1))
                        
        return False

    if backtrack(1):
        print("YES")
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()