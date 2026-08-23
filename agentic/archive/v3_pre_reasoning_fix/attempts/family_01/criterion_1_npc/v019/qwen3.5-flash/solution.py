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

    adj = [[] for _ in range(n)]
    for _ in range(m):
        try:
            u = int(next(iterator)) - 1
            v = int(next(iterator)) - 1
            # Check for self-loops. A node incompatible with itself is impossible.
            if u == v:
                print("NO")
                return
            adj[u].append(v)
            adj[v].append(u)
        except StopIteration:
            break

    # Remove duplicates from adjacency list to avoid redundant updates and restore issues
    for i in range(n):
        adj[i] = list(set(adj[i]))

    # s stores the color assigned to each node (0, 1, 2)
    s = [-1] * n
    # dom stores the mask of allowed colors for each node
    # Initial mask is 7 (binary 111) -> colors 0, 1, 2 are allowed
    dom = [7] * n

    # We need to find the lexicographically smallest solution.
    # We try colors 0, 1, 2 in order for node 0, then 1, etc.
    
    def backtrack(idx):
        if idx == n:
            return True
        
        # Try colors 0, 1, 2
        for color in range(3):
            # Check if color is compatible with neighbors < idx
            # dom[idx] has been updated by neighbors < idx, so we just check bits
            # (dom[idx] >> color) & 1 checks if the bit for 'color' is set
            if not ((dom[idx] >> color) & 1):
                continue
            
            # Tentatively pick `color` for `idx`.
            # We need to update `dom` for neighbors j > idx.
            # We track changes to backtrack.
            
            changes = []
            possible = True
            
            # Update neighbors j > idx
            for neighbor in adj[idx]:
                if neighbor > idx:
                    old_val = dom[neighbor]
                    # Remove color from neighbor's allowed colors
                    dom[neighbor] &= ~(1 << color)
                    changes.append((neighbor, old_val))
                    if dom[neighbor] == 0:
                        possible = False
                        break
            
            if possible:
                s[idx] = color
                if backtrack(idx + 1):
                    return True
            
            # Restore dom
            for neighbor, old_val in changes:
                dom[neighbor] = old_val
        
        return False

    if backtrack(0):
        print("YES")
        # Convert s to 1-based
        print(*(x + 1 for x in s))
    else:
        print("NO")

if __name__ == '__main__':
    solve()