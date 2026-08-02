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

    # Adjacency list for the graph
    adj = [[] for _ in range(n)]
    
    for _ in range(m):
        try:
            u = int(next(iterator)) - 1
            v = int(next(iterator)) - 1
            adj[u].append(v)
            adj[v].append(u)
        except StopIteration:
            break
            
    # available[u] is a bitmask of available colors for vertex u
    # Colors are 0, 1, 2 corresponding to vaults 1, 2, 3
    # Bit 0 represents color 0, Bit 1 -> 1, Bit 2 -> 2
    # Initial available colors: 0, 1, 2 -> 1 | 2 | 4 = 7
    available = [7] * n
    
    ans = [0] * n
    
    # Recursive backtracking function with forward checking
    def backtrack(idx):
        # If we have assigned all vertices, we found a solution
        if idx == n:
            return True
        
        # If no colors available for current vertex, backtrack immediately
        if available[idx] == 0:
            return False
        
        # Try colors 0, 1, 2 in order (lexicographically smallest)
        for c in range(3):
            # Check if color c is available for vertex idx
            # (available[idx] >> c) & 1 checks if the c-th bit is set
            if (available[idx] >> c) & 1:
                # Tentatively assign color c to vertex idx
                
                # We need to update available colors for neighbors > idx
                # and check for conflicts (forward checking)
                changes = []
                valid = True
                
                for v in adj[idx]:
                    if v > idx:
                        prev = available[v]
                        available[v] &= ~(1 << c)
                        if available[v] == 0:
                            valid = False
                            # We can stop updating, but need to restore changes
                            break
                        changes.append((v, prev))
                
                if valid:
                    ans[idx] = c + 1
                    if backtrack(idx + 1):
                        return True
                    # Backtrack: undo ans assignment
                    ans[idx] = 0
                
                # Restore available colors for neighbors
                for v, prev in changes:
                    available[v] = prev
                    
        return False

    if backtrack(0):
        print("YES")
        print(*(ans))
    else:
        print("NO")

if __name__ == '__main__':
    solve()