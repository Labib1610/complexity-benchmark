import sys

# Increase recursion depth to handle depth up to N=40
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

    # c[i] stores the assigned color for transmitter i (0 if unassigned)
    c = [0] * (n + 1)
    # rem[i] stores a bitmask of available colors for transmitter i
    # Bit 0 (1) -> Color 1, Bit 1 (2) -> Color 2, Bit 2 (4) -> Color 3
    # Initially all colors are available (7 = 111 in binary)
    rem = [7] * (n + 1)

    def dfs(u):
        # If we have successfully assigned colors to all n transmitters
        if u > n:
            return True

        # Try assigning colors 1, 2, 3 in order to find the lexicographically smallest solution
        for color in range(1, 4):
            # Check if 'color' is valid for u based on already assigned neighbors (v < u)
            is_valid = True
            for v in adj[u]:
                if v < u:
                    if c[v] == color:
                        is_valid = False
                        break
            
            if not is_valid:
                continue
            
            # Tentatively assign color
            c[u] = color
            
            # Forward checking: update available colors for unassigned neighbors (v > u)
            failed = False
            updates = []
            
            for v in adj[u]:
                if v > u:
                    old_rem = rem[v]
                    # Remove the current color from rem[v]
                    rem[v] &= ~(1 << (color - 1))
                    
                    # We record the update to restore it later
                    updates.append((v, old_rem))
                    
                    if rem[v] == 0:
                        failed = True
                        break
            
            if failed:
                # Backtrack: restore rem for neighbors we modified
                for v, old in updates:
                    rem[v] = old
                c[u] = 0
                continue
            
            # If valid, recurse
            if dfs(u + 1):
                return True
            
            # Backtrack: restore rem and c
            for v, old in updates:
                rem[v] = old
            c[u] = 0
            
        return False

    if dfs(1):
        print("YES")
        print(*(c[i] for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()