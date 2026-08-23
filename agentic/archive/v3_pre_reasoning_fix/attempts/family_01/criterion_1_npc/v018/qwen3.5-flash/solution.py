import sys

# Increase recursion depth to handle deep recursion for N=40
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

    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    # Check if the graph is bipartite
    # If it is bipartite, we can solve it in O(N+M) and it's guaranteed to be 3-colorable.
    # The lexicographically smallest 3-coloring for a bipartite graph is a 2-coloring.
    temp_color = [0] * (n + 1)
    is_bipartite = True
    
    for i in range(1, n + 1):
        if temp_color[i] == 0:
            stack = [i]
            temp_color[i] = 1
            while stack:
                u = stack.pop()
                c = temp_color[u]
                for v in adj[u]:
                    if temp_color[v] == 0:
                        temp_color[v] = 3 - c
                        stack.append(v)
                    elif temp_color[v] == c:
                        is_bipartite = False
                        break
                if not is_bipartite:
                    break
        if not is_bipartite:
            break
            
    if is_bipartite:
        # Construct the lexicographically smallest 2-coloring
        # For each component, the node with the smallest index gets color 1.
        final_color = [0] * (n + 1)
        visited = [False] * (n + 1)
        
        for i in range(1, n + 1):
            if not visited[i]:
                # BFS to traverse the component
                # i is the smallest index in this component, so assign 1
                final_color[i] = 1
                visited[i] = True
                q = [i]
                idx = 0
                while idx < len(q):
                    u = q[idx]
                    idx += 1
                    for v in adj[u]:
                        if not visited[v]:
                            visited[v] = True
                            final_color[v] = 3 - final_color[u]
                            q.append(v)
        
        print("YES")
        print(*(final_color[1:]))
        return

    # If not bipartite, use backtracking with Forward Checking
    # Forward Checking prunes branches where an uncolored node has no valid colors left.
    color = [0] * (n + 1)
    # forbidden_count[v][c] stores the number of already colored neighbors of v that have color c
    forbidden_count = [[0] * 4 for _ in range(n + 1)]
    
    def backtrack(u):
        if u > n:
            return True
        
        # Try colors 1, 2, 3 in order to ensure lexicographically smallest solution
        for c in range(1, 4):
            # Check validity: no neighbor < u has color c
            valid = True
            for v in adj[u]:
                if v < u:
                    if color[v] == c:
                        valid = False
                        break
            if not valid:
                continue
            
            # Forward Checking: check if assigning c to u makes any neighbor v > u have 0 valid colors
            affected_nodes = []
            possible = True
            
            for v in adj[u]:
                if v > u:
                    forbidden_count[v][c] += 1
                    affected_nodes.append(v)
                    # If all 3 colors are forbidden for v, then v cannot be colored
                    if forbidden_count[v][1] > 0 and forbidden_count[v][2] > 0 and forbidden_count[v][3] > 0:
                        possible = False
                        break
            
            if possible:
                color[u] = c
                if backtrack(u + 1):
                    return True
                color[u] = 0
            
            # Backtrack: revert forbidden_count changes
            for v in affected_nodes:
                forbidden_count[v][c] -= 1
                
        return False

    if backtrack(1):
        print("YES")
        print(*(color[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()