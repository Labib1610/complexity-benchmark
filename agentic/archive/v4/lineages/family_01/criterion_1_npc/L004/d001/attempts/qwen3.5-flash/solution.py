import sys

# Increase recursion depth to handle maximum N=40 safely
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
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        adj[u].append(v)
        adj[v].append(u)

    # colors array: 0 means unassigned, 1, 2, 3 are the channel IDs
    colors = [0] * n
    # possible array: bitmask of allowed colors for each node
    # initially all nodes can have any of {1, 2, 3} -> binary 111 = 7
    possible = [7] * n

    # DFS function to find the lexicographically smallest valid assignment
    def dfs(idx):
        # If we have assigned all nodes, we found a solution
        if idx == n:
            return True
        
        # If current node has no possible colors left, backtrack
        if possible[idx] == 0:
            return False
        
        p = possible[idx]
        
        # Try colors 1, 2, 3 in order to ensure lexicographically smallest result
        
        # Try color 1 (corresponds to bit 0)
        if (p & 1):
            c = 1
            colors[idx] = c
            changes = []
            valid = True
            
            # Forward checking: update allowed colors for neighbors
            for v in adj[idx]:
                if colors[v] == 0: # Neighbor is unassigned
                    old = possible[v]
                    possible[v] &= ~(1 << (c - 1)) # Remove color c from allowed set
                    if possible[v] == 0: # If no colors left for neighbor, invalid
                        valid = False
                        break
                    changes.append((v, old)) # Store change for backtracking
                else: # Neighbor is already assigned
                    if colors[v] == c: # Conflict with assigned color
                        valid = False
                        break
            
            if valid:
                if dfs(idx + 1):
                    return True
            
            # Backtrack: restore changes
            for v, old in changes:
                possible[v] = old
            colors[idx] = 0

        # Try color 2 (corresponds to bit 1)
        if (p & 2):
            c = 2
            colors[idx] = c
            changes = []
            valid = True
            
            for v in adj[idx]:
                if colors[v] == 0:
                    old = possible[v]
                    possible[v] &= ~(1 << (c - 1))
                    if possible[v] == 0:
                        valid = False
                        break
                    changes.append((v, old))
                else:
                    if colors[v] == c:
                        valid = False
                        break
            
            if valid:
                if dfs(idx + 1):
                    return True
            
            for v, old in changes:
                possible[v] = old
            colors[idx] = 0

        # Try color 3 (corresponds to bit 2)
        if (p & 4):
            c = 3
            colors[idx] = c
            changes = []
            valid = True
            
            for v in adj[idx]:
                if colors[v] == 0:
                    old = possible[v]
                    possible[v] &= ~(1 << (c - 1))
                    if possible[v] == 0:
                        valid = False
                        break
                    changes.append((v, old))
                else:
                    if colors[v] == c:
                        valid = False
                        break
            
            if valid:
                if dfs(idx + 1):
                    return True
            
            for v, old in changes:
                possible[v] = old
            colors[idx] = 0
            
        return False

    if dfs(0):
        print("YES")
        print(*(colors))
    else:
        print("NO")

if __name__ == '__main__':
    solve()