import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        edges.append((u, v))
        index += 2
    
    # Build adjacency list and degree count
    adj = defaultdict(list)
    degree = [0] * (n + 1)
    
    for i, (u, v) in enumerate(edges):
        adj[u].append((v, i))
        adj[v].append((u, i))
        degree[u] += 1
        degree[v] += 1
    
    # Check if every vertex has degree exactly 3
    for i in range(1, n + 1):
        if degree[i] != 3:
            print("NO")
            return
    
    # We need to assign each edge to one of three colors {1,2,3}
    # such that each vertex has edges of all three colors
    
    # This is equivalent to edge-coloring a 3-regular graph with 3 colors
    # Since the graph is 3-regular and we have exactly 3n/2 edges,
    # and we want each vertex to have edges of all 3 colors,
    # this is possible if and only if such a coloring exists.
    
    # We can model this as finding a proper edge coloring of a 3-regular graph with 3 colors.
    # A 3-regular graph is 3-edge-colorable if and only if it doesn't contain a bridge
    # (by Petersen's theorem for 3-regular graphs), but that's hard to check.
    # However, the problem guarantees a solution exists if possible.
    
    # Let's try a greedy approach:
    # For each vertex, assign its three edges to colors 1, 2, 3.
    # But we need to be consistent.
    
    # Better approach: Try to build a valid coloring.
    # Since each vertex has degree 3, we can assign colors 1,2,3 to its edges.
    # The challenge is to do this consistently.
    
    # Let's think of this as a graph where each vertex has exactly 3 edges.
    # We want to color edges with {1,2,3} such that at each vertex, all 3 colors are present.
    
    # This is equivalent to decomposing the graph into 3 perfect matchings.
    # Since n is even and the graph is 3-regular, this is possible if the graph is class 1.
    
    # Let's try a constructive approach:
    # 1. Find a perfect matching in the graph.
    # 2. Remove it, find another perfect matching.
    # 3. The remaining edges form the third perfect matching.
    
    # To find a perfect matching in a 3-regular graph:
    # We can use a randomized or heuristic approach, but let's try a systematic one.
    
    # Build edge list with indices
    edge_list = []
    for i, (u, v) in enumerate(edges):
        edge_list.append((u, v, i))
    
    # Build adjacency list with edge indices
    adj_list = [[] for _ in range(n + 1)]
    for u, v, idx in edge_list:
        adj_list[u].append((v, idx))
        adj_list[v].append((u, idx))
    
    # To avoid confusion, let's work with indices
    # Each vertex has exactly 3 edges
    vertex_edges = [[] for _ in range(n + 1)]
    for i, (u, v) in enumerate(edges):
        vertex_edges[u].append(i)
        vertex_edges[v].append(i)
    
    # Try to assign colors to edges
    # color[edge_index] = color (1, 2, or 3)
    color = [0] * m
    
    # For each vertex, assign colors 1,2,3 to its three edges
    # But we need to do this consistently
    
    # Let's try a greedy method:
    # Process vertices one by one
    # For each vertex, look at its uncolored edges and assign available colors
    
    # Actually, let's think of this differently.
    # Since the graph is 3-regular, it's a cubic graph.
    # A cubic graph is 3-edge-colorable if and only if it's class 1.
    # For our purposes, let's assume it is and try to find a coloring.
    
    # We can use backtracking or a more systematic approach.
    # Let's try to find three perfect matchings.
    
    # Since n is even and graph is 3-regular, it has a perfect matching (by Tutte's theorem).
    # Let's find one using a greedy approach:
    # 1. Pick an unmatched vertex, match it with a neighbor that can still be matched.
    
    def find_perfect_matching(used_edges):
        matched = [False] * (n + 1)
        matching = []
        
        # Create a list of available edges
        available = [True] * m
        for e in used_edges:
            available[e] = False
            
        # Build adjacency for available edges
        adj_avail = [[] for _ in range(n + 1)]
        for i, (u, v) in enumerate(edges):
            if available[i]:
                adj_avail[u].append((v, i))
                adj_avail[v].append((u, i))
        
        # Greedy matching
        for u in range(1, n + 1):
            if not matched[u]:
                for v, idx in adj_avail[u]:
                    if not matched[v]:
                        matched[u] = True
                        matched[v] = True
                        matching.append(idx)
                        break
        return matching if len(matching) == n // 2 else None
    
    # Find first perfect matching
    matching1 = find_perfect_matching([])
    if matching1 is None:
        print("NO")
        return
        
    # Find second perfect matching
    matching2 = find_perfect_matching(matching1)
    if matching2 is None:
        print("NO")
        return
    
    # The remaining edges form the third perfect matching
    used = set(matching1 + matching2)
    matching3 = [i for i in range(m) if i not in used]
    
    if len(matching3) != n // 2:
        print("NO")
        return
    
    # Assign colors
    for i in matching1:
        color[i] = 1
    for i in matching2:
        color[i] = 2
    for i in matching3:
        color[i] = 3
    
    print("YES")
    print(' '.join(map(str, color)))

if __name__ == "__main__":
    main()