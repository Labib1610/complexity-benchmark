import sys

# Increase recursion depth to handle max N=40 safely
sys.setrecursionlimit(5000)

def solve():
    # Read all input from stdin
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
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        adj[u].append(v)
        adj[v].append(u)

    # available[u] is a bitmask of allowed colors for vertex u
    # Bit 0 (value 1) represents shift 1
    # Bit 1 (value 2) represents shift 2
    # Bit 2 (value 4) represents shift 3
    # Initially all colors available (7)
    available = [7] * n
    
    # assignment[u] stores the assigned color (bitmask) for vertex u
    assignment = [0] * n

    def backtrack(idx):
        if idx == n:
            return True
        
        # Optimization: If no colors available for current vertex, fail
        if available[idx] == 0:
            return False

        # Try shifts 1, 2, 3 (bits 1, 2, 4) in order to ensure lexicographically smallest
        for c in (1, 2, 4):
            # Check if shift c is compatible with already assigned neighbors (v < idx)
            # This is already encoded in available[idx]
            if not (c & available[idx]):
                continue
            
            # Tentatively assign shift c to vertex idx
            # We need to record which neighbors' available colors are modified
            # to restore them upon backtracking.
            modified = []
            valid = True
            
            for v in adj[idx]:
                if v > idx:
                    # v is an uncolored neighbor (since v > idx)
                    # Update available[v] by removing shift c
                    available[v] &= ~c
                    modified.append(v)
                    
                    # Forward checking: if v has no colors left, this assignment is invalid
                    if available[v] == 0:
                        valid = False
                        break
            
            if valid:
                assignment[idx] = c
                if backtrack(idx + 1):
                    return True
                assignment[idx] = 0
            
            # Backtrack: restore available colors for modified neighbors
            for v in modified:
                available[v] |= c
        
        return False

    if backtrack(0):
        print("YES")
        # Map color bits back to shift values: 1->1, 2->2, 4->3
        res = []
        for x in assignment:
            if x == 1: res.append(1)
            elif x == 2: res.append(2)
            elif x == 4: res.append(3)
        print(*(res))
    else:
        print("NO")

if __name__ == '__main__':
    solve()