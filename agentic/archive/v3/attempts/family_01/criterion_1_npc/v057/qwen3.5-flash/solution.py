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

    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
        except StopIteration:
            break
            
    # Remove duplicates in adjacency list to optimize
    for i in range(1, n + 1):
        adj[i] = list(set(adj[i]))
    
    # allowed[i] is a bitmask of available colors for node i
    # 1 -> bit 0 (value 1), 2 -> bit 1 (value 2), 3 -> bit 2 (value 4)
    # Initially all colors are allowed (7 = 1 | 2 | 4)
    allowed = [7] * (n + 1)
    assignment = [0] * (n + 1)
    
    # We need to find the lexicographically smallest sequence.
    # This corresponds to trying colors 1, 2, 3 for node 1, then node 2, etc.
    # The first valid full assignment we find is the answer.
    
    def backtrack(u):
        if u > n:
            return True
        
        # Try colors 1, 2, 3 in order to ensure lexicographically smallest
        for color in [1, 2, 3]:
            bit = 1 << (color - 1)
            
            # Check conflict with already assigned neighbors (v < u)
            conflict = False
            for v in adj[u]:
                if assignment[v] == color:
                    conflict = True
                    break
            if conflict:
                continue
            
            # Check if assigning this color makes any unassigned neighbor impossible
            # We need to track which neighbors we modified to restore them later.
            
            affected_nodes = []
            possible = True
            
            for v in adj[u]:
                if assignment[v] == 0:
                    # v is unassigned (v > u)
                    # Check if 'color' is allowed for v
                    if (allowed[v] & bit) == 0:
                        continue
                    
                    # Update allowed: remove 'color' from v's allowed set
                    allowed[v] &= ~bit
                    if allowed[v] == 0:
                        possible = False
                        affected_nodes.append(v)
                        break
                    affected_nodes.append(v)
            
            if not possible:
                # Restore allowed for affected nodes
                for v in affected_nodes:
                    allowed[v] |= bit
                continue
            
            # Valid move
            assignment[u] = color
            
            if backtrack(u + 1):
                return True
            
            # Backtrack
            assignment[u] = 0
            for v in affected_nodes:
                allowed[v] |= bit
                
        return False

    if backtrack(1):
        print("YES")
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()