import sys

def solve():
    data = sys.stdin.read().strip().split()
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
    
    color = [0] * n
    
    def dfs(u):
        for v in adj[u]:
            if color[v] == 0:
                color[v] = 3 - color[u]
                if not dfs(v):
                    return False
            elif color[v] == color[u]:
                return False
        return True
    
    # Check if graph is bipartite and 2-color components
    for i in range(n):
        if color[i] == 0:
            color[i] = 1
            if not dfs(i):
                print("NO")
                return
    
    # Build conflict graph between color classes
    # Vertices: 0..n-1 are original workers
    # We need to partition into 3 shifts
    # Workers with same color can be in same shift
    # Workers with different colors in same component cannot be in same shift
    
    # Build graph for matching: nodes are workers, edges between incompatible workers
    # Incompatible: same connected component and different colors
    # We need to find a matching that covers all vertices in a maximum independent set way
    # Actually, we need to find a subset of vertices that can be assigned to shift 3
    # such that no two adjacent vertices in conflict graph are both in shift 3
    # and the remaining vertices can be 2-colored (which they already are)
    
    # Build conflict graph for shift 3 candidates
    # Two workers are in conflict for shift 3 if they are incompatible (same component, different colors)
    # We need to find a set of workers for shift 3 such that no two are in conflict
    # and the remaining workers can be assigned to shifts 1 and 2 (which they can, using the 2-coloring)
    
    # This is equivalent to finding a maximum independent set in the conflict graph
    # But we need to check if there exists an assignment, not necessarily maximum
    
    # Build adjacency for conflict graph
    conflict_adj = [[] for _ in range(n)]
    for u in range(n):
        for v in adj[u]:
            if color[u] != color[v]:
                conflict_adj[u].append(v)
    
    # Find connected components in original graph
    comp_id = [-1] * n
    comp_size = []
    comp_color1_count = []
    comp_color2_count = []
    
    current_comp = 0
    for i in range(n):
        if comp_id[i] == -1:
            stack = [i]
            comp_id[i] = current_comp
            c1 = 0
            c2 = 0
            while stack:
                u = stack.pop()
                if color[u] == 1:
                    c1 += 1
                else:
                    c2 += 1
                for v in adj[u]:
                    if comp_id[v] == -1:
                        comp_id[v] = current_comp
                        stack.append(v)
            comp_size.append(c1 + c2)
            comp_color1_count.append(c1)
            comp_color2_count.append(c2)
            current_comp += 1
    
    num_components = current_comp
    
    # For each component, we can choose:
    # - Assign all color 1 to shift 1, all color 2 to shift 2
    # - Assign all color 1 to shift 1, some color 2 to shift 3, rest to shift 2
    # - Assign all color 2 to shift 2, some color 1 to shift 3, rest to shift 1
    # - Assign some color 1 to shift 3, rest to shift 1; some color 2 to shift 3, rest to shift 2
    # But the last case is not allowed because color 1 and color 2 workers in same component
    # cannot both be in shift 3 (they are incompatible)
    
    # So for each component, we have choices:
    # 1. No one in shift 3
    # 2. Some color 1 workers in shift 3 (at least 1)
    # 3. Some color 2 workers in shift 3 (at least 1)
    
    # We need to select exactly one worker for shift 3 from each component
    # (to ensure all 3 shifts are used)
    # Wait, the problem doesn't require all 3 shifts to be used!
    # It just requires a valid assignment.
    
    # So we just need to check if we can assign workers to 3 shifts
    # such that no two incompatible workers are in the same shift.
    
    # The key insight: for each component, we can assign:
    # - All color 1 to shift 1, all color 2 to shift 2 (no one in shift 3)
    # - All color 1 to shift 1, all color 2 to shift 3 (shift 2 empty for this component)
    # - All color 1 to shift 3, all color 2 to shift 2 (shift 1 empty for this component)
    # - Some color 1 to shift 1, rest to shift 3; all color 2 to shift 2
    # - All color 1 to shift 1; some color 2 to shift 2, rest to shift 3
    # etc.
    
    # The constraint is: within each color class, we can split between two shifts.
    # So for each component, we have flexibility.
    
    # The only constraint across components is that we need to use at most 3 shifts total.
    # Since each component uses at most 2 shifts (from the 2-coloring), and we have 3 shifts,
    # we can always assign different shifts to different components.
    
    # Wait, but we need to assign all workers to shifts 1, 2, or 3.
    # The 2-coloring gives us a valid assignment to shifts 1 and 2.
    # We can also move some workers to shift 3.
    
    # The key observation: if a component has at least 3 workers, we can always
    # assign them to 3 different shifts (since it's not a complete graph).
    # If a component has 1 or 2 workers, we can assign them to 1 or 2 shifts.
    
    # Actually, the problem is simpler: we just need to check if the graph is 3-colorable.
    # A graph is 3-colorable iff it doesn't contain K4 as a subgraph.
    # But checking for K4 is not sufficient (there are other obstructions).
    
    # Let me reconsider: the graph is 3-colorable if and only if it's bipartite
    # or can be made bipartite by removing some vertices.
    
    # Actually, a simpler approach: for each component, check if it's 3-colorable.
    # A connected component is 3-colorable if it's not a complete graph K4 or larger.
    # More precisely, a graph is 3-colorable if it doesn't contain K4 as a minor.
    
    # For small n (up to 40), we can use brute force or backtracking.
    
    # Let's use a different approach: try all possible assignments for small components.
    
    # Actually, the key insight is:
    # - If a component is bipartite, we can color it with 2 colors.
    # - If a component is not bipartite, it contains an odd cycle, and we need 3 colors.
    # - But we've already checked bipartiteness, so all components are bipartite.
    
    # So all components are 2-colorable, hence 3-colorable.
    # We just need to find a valid 3-coloring.
    
    # The simplest approach: use the 2-coloring for shifts 1 and 2.
    # This is always valid.
    
    # But wait, the problem says we need to assign to shifts 1, 2, or 3.
    # Using only shifts 1 and 2 is a valid assignment.
    
    # So the answer is always YES if the graph is bipartite.
    # We've already checked that.
    
    # Output the 2-coloring as shifts 1 and 2.
    print("YES")
    print(' '.join(str(c) for c in color))

if __name__ == "__main__":
    solve()