import sys

# Increase recursion depth to handle N=40 safely
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
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    # Find connected components
    visited = [False] * (n + 1)
    components = []
    for i in range(1, n + 1):
        if not visited[i]:
            comp = []
            stack = [i]
            visited[i] = True
            while stack:
                u = stack.pop()
                comp.append(u)
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
            # Sort vertices to ensure lexicographical processing order within component
            # Since components are independent, solving each independently for lexicographically
            # smallest assignment (ordered by vertex index) yields the global lexicographically smallest assignment.
            comp.sort()
            components.append(comp)
    
    # Global state arrays
    # color[u] stores the assigned color for u (0 if unassigned, 1..3 otherwise)
    color = [0] * (n + 1)
    # count_forbidden[u][c] stores how many neighbors of u have color c (0, 1, 2)
    # c=0 corresponds to color 1, c=1 to color 2, c=2 to color 3
    count_forbidden = [[0] * 3 for _ in range(n + 1)]
    # forbidden_mask[u] stores a bitmask of forbidden colors for u
    # bit 0 -> color 1 forbidden, bit 1 -> color 2 forbidden, bit 2 -> color 3 forbidden
    forbidden_mask = [0] * (n + 1)
    
    # DFS function to find lexicographically smallest coloring for a component
    def dfs(nodes, idx):
        if idx == len(nodes):
            return True
        
        u = nodes[idx]
        
        # Try colors 0, 1, 2 (corresponding to 1, 2, 3)
        for c in range(3):
            # Check if color c is valid for u
            # Valid if no neighbor has color c (i.e., count_forbidden[u][c] == 0)
            if count_forbidden[u][c] == 0:
                # Assign color
                color[u] = c + 1
                
                # Update neighbors
                # We need to propagate constraints to unassigned neighbors
                fail_mask = False
                for v in adj[u]:
                    if color[v] == 0:
                        if count_forbidden[v][c] == 0:
                            forbidden_mask[v] |= (1 << c)
                        count_forbidden[v][c] += 1
                        if forbidden_mask[v] == 7:
                            fail_mask = True
                
                # If we didn't prune any unassigned neighbor (none have all colors forbidden)
                if not fail_mask:
                    if dfs(nodes, idx + 1):
                        return True
                
                # Backtrack / Revert
                # We need to revert the updates made to neighbors
                for v in adj[u]:
                    if color[v] == 0:
                        count_forbidden[v][c] -= 1
                        if count_forbidden[v][c] == 0:
                            forbidden_mask[v] &= ~(1 << c)
                
                color[u] = 0
        
        return False

    # Process each component
    for comp in components:
        # We assume state is clean for the new component.
        # Since components are disjoint, vertices in the current component have no neighbors in previously processed components.
        # Thus, their count_forbidden and forbidden_mask entries are 0 (unless modified by the current component's backtracking).
        # If we failed in a previous component, we backtracked and restored state to 0.
        # If we succeeded, we left state dirty for that component, but it doesn't affect the current one.
        
        if not dfs(comp, 0):
            print("NO")
            return

    print("YES")
    # Output s_1, s_2, ..., s_n
    print(*(color[1:]))

if __name__ == '__main__':
    solve()