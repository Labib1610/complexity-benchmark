import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    # Check if graph is bipartite and get partition
    color = [-1] * (n + 1)
    is_bipartite = True
    left_set = []
    right_set = []
    
    for start in range(1, n + 1):
        if color[start] == -1:
            color[start] = 0
            queue = [start]
            while queue:
                u = queue.pop(0)
                if color[u] == 0:
                    left_set.append(u)
                else:
                    right_set.append(u)
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        is_bipartite = False
    
    if not is_bipartite:
        print("NO")
        return
    
    # Calculate minimum total length
    # For bipartite graph, minimum is achieved by placing one partition at one end
    # and the other partition at the other end, with internal ordering within each partition
    
    # Count edges within each partition (should be 0 for bipartite)
    # and edges between partitions
    cross_edges = 0
    for u in range(1, n + 1):
        for v in adj[u]:
            if u < v:
                if color[u] != color[v]:
                    cross_edges += 1
    
    # Minimum total length for cross edges
    # If we place left_set at positions 1..|L| and right_set at positions |L|+1..n
    # Each cross edge contributes at least 1
    # Total minimum = cross_edges * 1 + internal_left + internal_right
    
    # For internal edges within a partition, minimum is achieved by placing
    # connected components together
    # For a component of size k, minimum internal length is k*(k-1)/2 - (k-1) = (k-1)*(k-2)/2
    # But actually, for a tree on k nodes, minimum total length is k-1 (each edge length 1)
    # For a general graph, we need to find optimal ordering
    
    # Actually, for a bipartite graph, the minimum total length is:
    # cross_edges * 1 + sum over components of (size - 1) for internal edges
    
    # But this is only achievable if we can order nodes within each partition optimally
    # For a tree, we can always achieve this by BFS/DFS ordering
    
    # Let's compute the minimum achievable
    # For cross edges: minimum is cross_edges (each edge at least 1)
    # For internal edges in left partition: need to find optimal ordering
    # For internal edges in right partition: need to find optimal ordering
    
    # Actually, for a bipartite graph, there are no internal edges within each partition!
    # So minimum total length = cross_edges
    
    # Wait, that's not right. Let me reconsider.
    # In a bipartite graph, edges only go between partitions, not within.
    # So there are no internal edges to consider.
    # Minimum total length = cross_edges (each cross edge has length at least 1)
    
    # But wait, the problem says the graph might not be bipartite.
    # If it's not bipartite, we need to handle internal edges.
    
    # Let me re-read the problem...
    # The graph can have any structure. We need to find if there's an assignment
    # with total length <= B.
    
    # For a general graph:
    # - If bipartite: minimum = cross_edges (place partitions at opposite ends)
    # - If not bipartite: need to handle internal edges
    
    # For non-bipartite graphs, the minimum is higher.
    # Let's think about this more carefully.
    
    # Actually, let me reconsider the bipartite case.
    # If we place left_set at positions 1..|L| and right_set at positions |L|+1..n,
    # then each cross edge has length at least 1.
    # But the exact length depends on the ordering within each partition.
    
    # For a cross edge (u, v) where u is in left_set and v is in right_set:
    # If u is at position p and v is at position q, then length = q - p.
    # Since p <= |L| and q >= |L| + 1, we have q - p >= 1.
    
    # To minimize total length, we want to minimize sum of (q - p) for all cross edges.
    # This is equivalent to minimizing sum of q - sum of p for all cross edges.
    # Since sum of q is fixed (sum of positions in right_set) and sum of p is fixed (sum of positions in left_set),
    # the total length is fixed regardless of ordering within each partition!
    
    # Wait, that's not right either. Let me think again.
    
    # Total length = sum over all edges (u, v) of |pos[u] - pos[v]|
    # For cross edges, pos[u] < pos[v] (if u in left, v in right), so length = pos[v] - pos[u].
    # Total = sum over cross edges of pos[v] - pos[u]
    #      = sum over cross edges of pos[v] - sum over cross edges of pos[u]
    
    # For each node u in left_set, it contributes -pos[u] * (degree of u to right_set)
    # For each node v in right_set, it contributes +pos[v] * (degree of v to left_set)
    
    # To minimize this, we want:
    # - Nodes in left_set with higher degree to right_set to have higher positions (within left_set)
    # - Nodes in right_set with higher degree to left_set to have lower positions (within right_set)
    
    # This is a sorting problem!
    
    # Let's compute the degree of each node to the other partition
    deg_to_other = [0] * (n + 1)
    for u in range(1, n + 1):
        for v in adj[u]:
            if color[u] != color[v]:
                deg_to_other[u] += 1
    
    # For left_set: sort by deg_to_other in descending order (higher degree -> higher position)
    # For right_set: sort by deg_to_other in ascending order (higher degree -> lower position)
    
    left_set_sorted = sorted(left_set, key=lambda x: -deg_to_other[x])
    right_set_sorted = sorted(right_set, key=lambda x: deg_to_other[x])
    
    # Assign positions
    pos = [0] * (n + 1)
    for i, u in enumerate(left_set_sorted):
        pos[u] = i + 1
    for i, u in enumerate(right_set_sorted):
        pos[u] = len(left_set) + i + 1
    
    # Calculate total length
    total_length = 0
    for u in range(1, n + 1):
        for v in adj[u]:
            if u < v:
                total_length += abs(pos[u] - pos[v])
    
    if total_length <= B:
        print("YES")
        print(' '.join(str(pos[i]) for i in range(1, n + 1)))
    else:
        print("NO")

solve()