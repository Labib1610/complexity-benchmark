import sys

# Increase recursion depth to accommodate N=40
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
    
    # Ensure unique neighbors
    for i in range(n + 1):
        adj[i] = list(set(adj[i]))

    # available colors for each node, bitmask
    # Colors: 1 -> 1 (bit 0), 2 -> 2 (bit 1), 3 -> 4 (bit 2)
    # Initially all available: 1 | 2 | 4 = 7
    available = [7] * (n + 1)
    colors = [0] * (n + 1)

    # DFS function to find lexicographically smallest assignment
    def dfs(u):
        if u > n:
            return True

        # Try colors 1, 2, 3 (represented as 1, 2, 4)
        # We iterate in order to ensure lexicographically smallest sequence
        for c in [1, 2, 4]:
            if c & available[u]:
                # c is a valid color for u (consistent with 1..u-1)
                # Now check constraints with unassigned neighbors (v > u)
                changes = []
                possible = True
                
                for v in adj[u]:
                    if v > u:
                        # If v can take color c, we must forbid it for v
                        if c & available[v]:
                            old_avail = available[v]
                            available[v] &= ~c
                            changes.append((v, old_avail))
                            if available[v] == 0:
                                possible = False
                                break
                
                if possible:
                    colors[u] = c
                    if dfs(u + 1):
                        return True
                    # Backtrack: restore available colors for neighbors
                    for v, old_avail in changes:
                        available[v] = old_avail
                    colors[u] = 0
                else:
                    # If we broke out due to conflict, restore partial changes
                    for v, old_avail in changes:
                        available[v] = old_avail
        
        return False

    if dfs(1):
        print("YES")
        # Output colors 1 to n
        # Convert bitmasks back to integers
        result = []
        for i in range(1, n + 1):
            if colors[i] == 1:
                result.append(1)
            elif colors[i] == 2:
                result.append(2)
            else:
                result.append(3)
        print(" ".join(map(str, result)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()