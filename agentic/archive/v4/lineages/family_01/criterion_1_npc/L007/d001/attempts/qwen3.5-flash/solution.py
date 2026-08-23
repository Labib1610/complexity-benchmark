import sys

# Increase recursion depth to accommodate deeper recursion if needed
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

    # Adjacency list for graph traversal
    adj = [[] for _ in range(n + 1)]
    # Adjacency matrix for efficient clique checking
    adj_mat = [[False] * (n + 1) for _ in range(n + 1)]
    
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
            adj_mat[u][v] = True
            adj_mat[v][u] = True
        except StopIteration:
            break
            
    # Check for K4 (clique of size 4)
    # If a graph contains a K4, it is not 3-colorable.
    # This is a quick necessary condition check.
    if n >= 4:
        # Iterate over all combinations of 4 nodes
        # Since n <= 40, this is roughly 40^4 / 24 operations, which is fast.
        for i in range(1, n - 2):
            for j in range(i + 1, n - 1):
                if not adj_mat[i][j]: continue
                for k in range(j + 1, n):
                    if not adj_mat[i][k] or not adj_mat[j][k]: continue
                    for l in range(k + 1, n + 1):
                        if adj_mat[i][l] and adj_mat[j][l] and adj_mat[k][l]:
                            print("NO")
                            return

    # Backtracking with Forward Checking
    # avail[i] stores a bitmask of allowed colors for node i
    # Colors: 1 -> bit 0, 2 -> bit 1, 3 -> bit 2
    # Initial available colors for all nodes: 1 | 2 | 4 = 7
    avail = [7] * (n + 1)
    ans = [0] * (n + 1)
    
    def backtrack(idx):
        # Base case: all nodes assigned
        if idx > n:
            return True
        
        # Try colors 1, 2, 3 in order
        # This ensures we find the lexicographically smallest sequence first
        for c in [1, 2, 3]:
            # Check if color c is allowed for node idx
            # avail[idx] has been updated by forward checking from previous nodes
            if not ((avail[idx] >> (c - 1)) & 1):
                continue
            
            # Assign color c
            ans[idx] = c
            mask_c = 1 << (c - 1)
            
            # Forward Check: update available colors for neighbors > idx
            modified_nodes = []
            possible = True
            
            for v in adj[idx]:
                if v > idx:
                    # If color c is still available for v, remove it
                    if (avail[v] & mask_c):
                        avail[v] &= ~mask_c
                        modified_nodes.append(v)
                        # If v has no colors left, this branch is invalid
                        if avail[v] == 0:
                            possible = False
                            break
            
            if possible:
                if backtrack(idx + 1):
                    return True
            
            # Backtrack: restore available colors for modified nodes
            for v in modified_nodes:
                avail[v] |= mask_c
                
        return False

    if backtrack(1):
        print("YES")
        # Print the assignment sequence
        print(*(ans[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()