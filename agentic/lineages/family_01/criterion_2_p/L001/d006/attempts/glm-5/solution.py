import sys
sys.setrecursionlimit(1 << 25)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    # We need to find lexicographically smallest assignment.
    # Greedy approach: try to assign 1 to each node if possible.
    # A node can be assigned 1 if:
    # - It's not forced to be 2 by a neighbor already assigned 1 (constraint: no edge with both endpoints 1)
    # - After assigning 1, the remaining graph is still solvable.
    # The remaining graph is solvable if it's bipartite (no odd cycle).
    
    # We'll use a DSU with parity to check bipartiteness dynamically.
    # But since we assign values greedily, we can use a simpler approach:
    # For each node, try to assign 1, then check if the remaining graph is bipartite.
    # If not, assign 2.
    
    # To check bipartiteness efficiently, we can use DSU with parity.
    # But implementing it from scratch is complex. Instead, we can use a simpler approach:
    # After each assignment, we can run BFS/DFS to check bipartiteness.
    # However, this would be O(n*m) in the worst case, which is too slow.
    
    # Alternative: Use DSU with parity to maintain constraints.
    # When we assign a value to a node, we add constraints to its neighbors.
    # If a conflict arises, we backtrack.
    
    # Let's implement DSU with parity.
    
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    parity = [0] * (n + 1)  # parity[x] is the parity of the path from x to its parent
    
    def find(x):
        if parent[x] != x:
            orig_parent = parent[x]
            parent[x] = find(parent[x])
            parity[x] ^= parity[orig_parent]
        return parent[x]
    
    # Returns (root, parity from x to root)
    def find_with_parity(x):
        if parent[x] != x:
            orig_parent = parent[x]
            parent[x] = find(parent[x])
            parity[x] ^= parity[orig_parent]
        return parent[x], parity[x]
    
    # Union x and y with parity p (x and y should have parity p between them)
    # Returns True if successful, False if conflict
    def union(x, y, p):
        root_x, px = find_with_parity(x)
        root_y, py = find_with_parity(y)
        if root_x == root_y:
            # Check if existing parity matches
            return (px ^ py) == p
        # Union by rank
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
            parity[root_x] = px ^ py ^ p
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
            parity[root_y] = px ^ py ^ p
        else:
            parent[root_y] = root_x
            parity[root_y] = px ^ py ^ p
            rank[root_x] += 1
        return True
    
    # Now, we'll assign values greedily.
    # For each node, we try to assign 1.
    # If assigning 1 creates a conflict (i.e., some neighbor is already 1), we assign 2.
    # Otherwise, we check if the remaining graph is still bipartite.
    # If not, we assign 2.
    
    # But how to check if the remaining graph is bipartite after assigning 1?
    # We can use the DSU with parity to check if adding constraints for all edges
    # involving the current node would create a conflict.
    
    # Actually, the constraint is: for each edge (u, v), r_u and r_v cannot both be 1.
    # This is equivalent to: r_u + r_v >= 3, or r_u != 1 or r_v != 1.
    # In terms of parity, if we define x_i = r_i - 1 (so x_i is 0 or 1),
    # then the constraint is x_u + x_v >= 1, or x_u | x_v == 1.
    # This is not a simple parity constraint.
    
    # Wait, the constraint is: for each edge (u, v), not (r_u == 1 and r_v == 1).
    # This is equivalent to: r_u != 1 or r_v != 1.
    # In terms of x_i = r_i - 1, this is: x_u != 0 or x_v != 0, i.e., x_u + x_v >= 1.
    # This is not a parity constraint, but a "not both 0" constraint.
    
    # Hmm, this is different. Let me re-read the problem.
    
    # The stability score for an edge (u, v) is 3(r_u + r_v) - 2 r_u r_v.
    # We need the sum over all edges to be exactly 5m.
    # Let's compute the possible values:
    # - If r_u = 1, r_v = 1: score = 3(1+1) - 2*1*1 = 6 - 2 = 4
    # - If r_u = 1, r_v = 2: score = 3(1+2) - 2*1*2 = 9 - 4 = 5
    # - If r_u = 2, r_v = 1: score = 3(2+1) - 2*2*1 = 9 - 4 = 5
    # - If r_u = 2, r_v = 2: score = 3(2+2) - 2*2*2 = 12 - 8 = 4
    
    # So the score is 4 if both are same, 5 if different.
    # We need the sum to be 5m, so each edge must contribute 5.
    # Therefore, for each edge, r_u != r_v.
    
    # Ah! So the constraint is that for each edge, the two endpoints must have different values.
    # This is a bipartite graph constraint!
    
    # So the problem reduces to: find a valid 2-coloring of the graph.
    # If the graph is not bipartite, output NO.
    # Otherwise, output the lexicographically smallest valid coloring.
    
    # Lexicographically smallest means we prefer 1 over 2 for each node.
    # So we can use a greedy approach: for each node, try to assign 1, then check if the remaining graph is still bipartite.
    
    # But since the constraint is that adjacent nodes must have different colors,
    # once we assign a value to a node, all its neighbors are forced to have the opposite value.
    
    # So we can use a simple approach:
    # 1. Check if the graph is bipartite.
    # 2. If yes, find the lexicographically smallest valid coloring.
    
    # To find the lexicographically smallest coloring, we can use a greedy approach:
    # For each node from 1 to n, if it's not yet colored, try to color it with 1.
    # Then, propagate the coloring to all connected nodes (BFS/DFS).
    # If a conflict arises, the graph is not bipartite.
    
    # But this might not give the lexicographically smallest coloring.
    # For example, consider a graph 1-2-3. The greedy approach would color 1 as 1, then 2 as 2, then 3 as 1.
    # This is correct. But consider a graph 1-3-2. The greedy approach would color 1 as 1, then 3 as 2, then 2 as 1.
    # This is also correct.
    
    # Actually, the greedy approach should work because we process nodes in order.
    # When we encounter an uncolored node, we color it with 1 (the smallest possible).
    # Then, all its neighbors are forced to be 2, and so on.
    # This ensures that we always use the smallest possible color for each node.
    
    # Let's implement this.
    
    color = [0] * (n + 1)  # 0: uncolored, 1 or 2: colored
    
    # Check if the graph is bipartite and find the lexicographically smallest coloring.
    for i in range(1, n + 1):
        if color[i] == 0:
            # Start BFS from i
            queue = [i]
            color[i] = 1  # Try to color with 1
            is_bipartite = True
            while queue and is_bipartite:
                u = queue.pop()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]  # Opposite color
                        queue.append(v)
                    elif color[v] == color[u]:
                        is_bipartite = False
                        break
            if not is_bipartite:
                print("NO")
                return
    
    # Verify the solution
    # for u in range(1, n + 1):
    #     for v in adj[u]:
    #         if color[u] == color[v]:
    #             print("NO")
    #             return
    
    print("YES")
    print(' '.join(map(str, color[1:])))

solve()