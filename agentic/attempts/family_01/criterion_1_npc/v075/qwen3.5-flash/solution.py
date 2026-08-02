import sys

# Increase recursion depth to be safe, though N=40 is small.
sys.setrecursionlimit(5000)

def solve():
    # Read all input from stdin efficiently
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

    # Remove duplicates in adjacency list if any
    for i in range(1, n + 1):
        adj[i] = list(set(adj[i]))

    color = [0] * (n + 1)
    # cnt[u][c] stores the number of colored neighbors of u that have color c
    # Indices 1, 2, 3 are used for colors
    cnt = [[0] * 4 for _ in range(n + 1)]
    
    def backtrack(idx):
        if idx > n:
            return True
        
        # Determine allowed colors for current node idx
        # A color c is allowed if cnt[idx][c] == 0
        # This means no colored neighbor has color c.
        # We check 1, 2, 3 in order to find lexicographically smallest.
        allowed = []
        for c in range(1, 4):
            if cnt[idx][c] == 0:
                allowed.append(c)
        
        if not allowed:
            return False
        
        for c in allowed:
            # Assign color c to idx
            color[idx] = c
            
            # Update cnt for neighbors and check for doomed nodes
            updates = [] 
            doomed = False
            
            for v in adj[idx]:
                if color[v] == 0: # v is uncolored
                    cnt[v][c] += 1
                    updates.append((v, c))
                    # Check if v is now doomed (all 3 colors forbidden)
                    # Forbidden means cnt[v][k] > 0
                    if cnt[v][1] > 0 and cnt[v][2] > 0 and cnt[v][3] > 0:
                        doomed = True
                        break
            
            if not doomed:
                if backtrack(idx + 1):
                    return True
            
            # Backtrack: revert cnt changes
            for v, c_val in updates:
                cnt[v][c_val] -= 1
            
            # Revert color
            color[idx] = 0
            
        return False

    if backtrack(1):
        print("YES")
        print(*(color[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()