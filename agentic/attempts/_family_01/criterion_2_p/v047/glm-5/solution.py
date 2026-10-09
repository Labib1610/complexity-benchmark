import sys
from collections import deque

def solve():
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
    degree = [0] * (n + 1)
    
    edges = []
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        degree[u] += 1
        degree[v] += 1
        edges.append((u, v))

    color = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if color[i] == 0:
            color[i] = 1
            queue = deque([i])
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return

    # Check if graph is bipartite with exactly two components
    # and all edges are cross edges (k=m condition)
    # This is equivalent to checking if the graph is a complete bipartite graph
    # formed by two connected components with all edges between them.
    
    # To satisfy k=m, every edge must be a cross-edge.
    # This means for every edge (u, v), color[u] != color[v].
    # Since we already checked bipartiteness, this condition is satisfied.
    # However, we must also ensure that the graph structure allows such a coloring
    # where the partition sets P1 and P2 correspond to the two components.
    
    # The condition sum(c_x for x in P1) + sum(c_y for y in P2) = 2m is always true
    # because it sums degrees of all vertices, which is 2m.
    
    # The critical condition is k=m.
    # k is the number of cross-edges. We need k=m, meaning all edges are cross-edges.
    # This implies that for every edge (u, v), u and v must be in different sets.
    # This means the graph must be bipartite, and the partition must be such that
    # all edges go across the partition.
    
    # However, the problem asks for a specific partition P1 and P2.
    # The condition k=m implies that the graph's edges must all be between P1 and P2.
    # This is possible if and only if the graph is bipartite and the two sets P1 and P2
    # are the two partitions of the bipartite graph.
    
    # But we also need to consider the lexicographically smallest partition.
    # The initial coloring gives us a valid bipartition.
    # We need to check if this bipartition satisfies k=m.
    # Since we ensured color[u] != color[v] for all edges, k=m is satisfied.
    
    # However, there's a catch: the graph might have multiple connected components.
    # For k=m to hold, the entire graph must be bipartite with the given partition.
    # But the problem might imply that the graph must be a complete bipartite graph
    # between two sets, which is not necessarily the case.
    
    # Wait, the condition k=m means every edge is a cross-edge.
    # This is satisfied if the graph is bipartite and we assign colors such that
    # all edges are between different colors.
    # The initial BFS coloring ensures this.
    
    # But the problem might have additional constraints.
    # Let's re-examine the conditions.
    
    # The condition sum(c_x for x in P1) + sum(c_y for y in P2) = 2m is always true.
    # The condition k=m is satisfied if the graph is bipartite and we color it properly.
    
    # So the only condition we need to check is bipartiteness.
    # If the graph is bipartite, we can output the coloring.
    # But we need the lexicographically smallest coloring.
    
    # The initial coloring might not be lexicographically smallest.
    # We can flip colors within connected components to get a smaller sequence.
    
    # For each connected component, we can choose to flip colors or not.
    # We need to find the combination that gives the lexicographically smallest sequence.
    
    # To do this, we can process components in order of their smallest vertex.
    # For each component, we choose the coloring that makes the smallest vertex color 1.
    
    # Let's re-color the graph with this in mind.
    
    # Re-initialize color array
    color = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # BFS to find the component
            component = []
            queue = deque([i])
            color[i] = 1  # temporary color for BFS
            component.append(i)
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        queue.append(v)
                        component.append(v)
            
            # Now, we have the component with colors 1 and 2.
            # We need to decide whether to flip the colors.
            # The lexicographically smallest sequence is achieved by making the
            # smallest vertex in the component have color 1.
            
            # Find the smallest vertex in the component
            min_vertex = min(component)
            
            # If the current color of min_vertex is 2, flip all colors in the component
            if color[min_vertex] == 2:
                for u in component:
                    color[u] = 3 - color[u]
    
    # Now, we have the lexicographically smallest valid coloring.
    # We need to verify that this coloring satisfies all conditions.
    
    # Check bipartiteness again (though it should be satisfied)
    for u in range(1, n + 1):
        for v in adj[u]:
            if color[u] == color[v]:
                print("NO")
                return
    
    # Check k=m condition
    # Since we ensured color[u] != color[v] for all edges, k=m is satisfied.
    
    # Output the result
    print("YES")
    print(' '.join(map(str, color[1:])))

solve()