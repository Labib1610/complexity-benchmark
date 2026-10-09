import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # Check if graph is bipartite (2-colorable)
    # If not, we need 3 colors. If yes, we might still use 3 colors for lex smallest.
    
    color = [-1] * n
    is_bipartite = True
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            stack = [i]
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        stack.append(v)
                    elif color[v] == color[u]:
                        is_bipartite = False
                        break
                if not is_bipartite:
                    break
        if not is_bipartite:
            break
            
    if is_bipartite:
        # Bipartite graph: check if 2-coloring is valid (no edges within same partition)
        # Actually, 2-coloring is always valid for bipartite.
        # We just need to check if we can use colors 1 and 2.
        # The lex smallest assignment will use 1 and 2.
        # We need to find the lex smallest valid assignment.
        # Since we can use 1 and 2, we never need 3.
        # Greedy approach: assign smallest available color (1 or 2).
        
        assignment = [0] * n
        for u in range(n):
            used = set()
            for v in adj[u]:
                if v < u:
                    used.add(assignment[v])
            c = 1
            while c in used:
                c += 1
            if c > 2:
                # This should not happen in a bipartite graph
                # But let's handle it just in case
                # Actually, if the graph is bipartite, greedy 2-coloring works.
                # However, the greedy order might not respect the bipartition.
                # We need to be careful.
                # Let's use the bipartition to guide the assignment.
                pass
            assignment[u] = c
        
        # Verify the assignment
        valid = True
        for u in range(n):
            for v in adj[u]:
                if u < v and assignment[u] == assignment[v]:
                    valid = False
                    break
            if not valid:
                break
        
        if valid:
            print("YES")
            print(' '.join(map(str, assignment)))
            return
        else:
            # Fallback to 3-coloring if greedy fails (shouldn't happen for bipartite)
            pass
    
    # Not bipartite or greedy 2-coloring failed
    # We need 3 colors
    # Use backtracking with pruning
    
    assignment = [0] * n
    
    def backtrack(u):
        if u == n:
            return True
        used = set()
        for v in adj[u]:
            if v < u:
                used.add(assignment[v])
        for c in [1, 2, 3]:
            if c not in used:
                assignment[u] = c
                if backtrack(u + 1):
                    return True
        assignment[u] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(' '.join(map(str, assignment)))
    else:
        print("NO")

solve()