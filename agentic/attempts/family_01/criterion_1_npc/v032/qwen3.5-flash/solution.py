import sys

# Increase recursion depth to handle potential deep recursion
sys.setrecursionlimit(5000)

def solve():
    # Read all input from standard input efficiently
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
    # We use 1-based indexing for convenience
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
    
    # Remove duplicate edges and sort to optimize
    for i in range(1, n + 1):
        adj[i] = sorted(list(set(adj[i])))
    
    # State variables
    colors = [0] * (n + 1) # 0 means uncolored
    # cnt1[u] stores the number of colored neighbors of u that have color 1
    cnt1 = [0] * (n + 1)
    cnt2 = [0] * (n + 1)
    cnt3 = [0] * (n + 1)
    
    res = [0] * (n + 1) # To store the result sequence
    
    def dfs(u):
        # Base case: all nodes colored
        if u > n:
            return True
        
        # Try assigning colors 1, 2, 3 to node u
        # We try in increasing order to ensure lexicographically smallest sequence
        for c in [1, 2, 3]:
            # Check if color c is valid for u (i.e., no neighbor has color c)
            if c == 1 and cnt1[u] > 0: continue
            if c == 2 and cnt2[u] > 0: continue
            if c == 3 and cnt3[u] > 0: continue
            
            # Assign color c to u
            colors[u] = c
            res[u] = c
            
            # Update constraints for neighbors
            doomed = False
            
            # Update counts for uncolored neighbors
            # We update all neighbors first to maintain consistent state before checking doom
            for v in adj[u]:
                if colors[v] == 0:
                    if c == 1:
                        cnt1[v] += 1
                    elif c == 2:
                        cnt2[v] += 1
                    else:
                        cnt3[v] += 1
            
            # Check if any uncolored neighbor is doomed (has all 3 colors forbidden)
            for v in adj[u]:
                if colors[v] == 0:
                    if cnt1[v] > 0 and cnt2[v] > 0 and cnt3[v] > 0:
                        doomed = True
                        break
            
            if doomed:
                # Rollback updates
                for v in adj[u]:
                    if colors[v] == 0:
                        if c == 1:
                            cnt1[v] -= 1
                        elif c == 2:
                            cnt2[v] -= 1
                        else:
                            cnt3[v] -= 1
                colors[u] = 0
                continue
            
            # Recurse to next node
            if dfs(u + 1):
                return True
            
            # Backtrack: undo updates
            for v in adj[u]:
                if colors[v] == 0:
                    if c == 1:
                        cnt1[v] -= 1
                    elif c == 2:
                        cnt2[v] -= 1
                    else:
                        cnt3[v] -= 1
            colors[u] = 0
            
        return False

    # Start DFS from node 1
    if dfs(1):
        print("YES")
        # Print the sequence s_1, s_2, ..., s_n
        print(*(res[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()