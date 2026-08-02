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

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
    
    ans = [0] * (n + 1)
    
    # Helper to count set bits
    def popcount(x):
        return bin(x).count('1')

    # Check if the current partial assignment can be extended to a full valid coloring
    def check_feasibility(current_ans):
        # avail[i] is a bitmask of available colors for node i
        # 1 << 0 for color 1, 1 << 1 for color 2, 1 << 2 for color 3
        avail = [0] * (n + 1)
        uncolored = []
        
        for i in range(1, n + 1):
            if current_ans[i] != 0:
                avail[i] = 1 << (current_ans[i] - 1)
            else:
                avail[i] = 7 # 111 in binary (colors 1, 2, 3 available)
                uncolored.append(i)
        
        # Propagate constraints from pre-colored nodes to uncolored neighbors
        # and check for immediate conflicts
        for u in range(1, n + 1):
            if current_ans[u] != 0:
                c = current_ans[u]
                for v in adj[u]:
                    if current_ans[v] == 0:
                        avail[v] &= ~(1 << (c - 1))
                        if avail[v] == 0:
                            return False
                    else:
                        # Both u and v are pre-colored
                        if current_ans[u] == current_ans[v]:
                            return False
        
        # If any uncolored node has no available colors, it's invalid
        for u in uncolored:
            if avail[u] == 0:
                return False
                
        # Recursive backtracking with MRV (Minimum Remaining Values) heuristic
        def dfs_mrv(nodes, current_avail):
            if not nodes:
                return True
            
            # Pick the node with the fewest available colors
            best_u = -1
            min_c = 4
            best_idx = -1
            
            for i, u in enumerate(nodes):
                cnt = popcount(current_avail[u])
                if cnt == 0:
                    return False
                if cnt < min_c:
                    min_c = cnt
                    best_u = u
                    best_idx = i
                    if min_c == 1: break # Optimization: can't get better than 1
            
            if best_u == -1: return True
            
            # Remove best_u from the list of nodes to color
            next_nodes = nodes[:best_idx] + nodes[best_idx+1:]
            
            # Try each available color
            for c in range(1, 4):
                if (current_avail[best_u] >> (c - 1)) & 1:
                    # Check conflict with pre-colored neighbors
                    conflict = False
                    for v in adj[best_u]:
                        if current_ans[v] != 0:
                            if current_ans[v] == c:
                                conflict = True
                                break
                    if conflict:
                        continue
                    
                    # Update domains of uncolored neighbors
                    # Create a copy of avail to backtrack
                    new_avail = list(current_avail)
                    valid = True
                    for v in adj[best_u]:
                        if current_ans[v] == 0:
                            new_avail[v] &= ~(1 << (c - 1))
                            if new_avail[v] == 0:
                                valid = False
                                break
                    
                    if valid:
                        if dfs_mrv(next_nodes, new_avail):
                            return True
            return False

        return dfs_mrv(uncolored, avail)

    # Main backtracking solver to find lexicographically smallest solution
    def solve_recursive(u):
        if u > n:
            return True
        
        # Try colors 1, 2, 3 in order to ensure lexicographically smallest
        for c in range(1, 4):
            ans[u] = c
            if check_feasibility(ans):
                if solve_recursive(u + 1):
                    return True
            ans[u] = 0
            
        return False

    if solve_recursive(1):
        print("YES")
        print(*(ans[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()