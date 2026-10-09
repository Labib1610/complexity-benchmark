import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1000000)
    
    n, m, B = map(int, sys.stdin.readline().split())
    
    # Build adjacency list for the tree
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Since it's a tree with n-1 edges, we can proceed
    
    # Find a root: we can pick node 1 or any node
    # But better to find the center or centroid for minimal cost
    # However, since we need to check if ANY assignment works,
    # We can try a heuristic or exhaustive approach for small n
    # For large n, we need smarter approach
    
    # Let's build the tree structure properly
    # First, determine parent-child relationships
    # Assume the input gives us a valid tree structure
    # We'll treat it as undirected first, then orient it
    
    # To minimize total distance, we should place nodes that are close in the tree
    # close in the line topology. This is essentially finding an embedding of the
    # tree into a line that minimizes sum of distances.
    
    # This is a classic problem related to optimal linear arrangement
    # which is NP-hard in general. However, for trees, there are polynomial algorithms.
    
    # A greedy approach: find a centroid of the tree, place it in the middle,
    # and recursively place subtrees on left and right.
    
    # But let's think differently. 
    # Since we just need to check if total cost <= B, and possibly return assignment,
    # we can try to find the minimum possible cost assignment.
    
    # One way: use dynamic programming on tree to compute minimum cost
    # But even simpler: use a known result that for trees, the optimal
    # linear arrangement can be computed via centroid decomposition or
    # by finding an optimal layout.
    
    # Simpler approach: since n <= 10^5, but we might not need full optimization
    # Let's implement a DFS-based layout that tries to keep the tree compact
    
    # Convert to adjacency list
    graph = [[] for _ in range(n+1)]
    for u, v in [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]:
        graph[u].append(v)
        graph[v].append(u)
    
    # Re-read input correctly
    sys.stdin.seek(0)
    lines = sys.stdin.readlines()
    n, m, B = map(int, lines[0].split())
    edges = []
    for i in range(1, m+1):
        u, v = map(int, lines[i].split())
        edges.append((u,v))
    
    # Build adjacency
    adj = [[] for _ in range(n+1)]
    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Function to compute cost of a given assignment
    def compute_cost(assignment):
        total = 0
        for u,v in edges:
            pos_u = assignment[u]
            pos_v = assignment[v]
            total += abs(pos_u - pos_v)
        return total
    
    # Try to generate a good assignment
    # Place nodes using DFS in order to keep related nodes close
    # This is a heuristic
    
    # Simple heuristic: do a DFS traversal and assign positions in order
    visited = [False] * (n+1)
    order = []
    
    def dfs(v):
        visited[v] = True
        order.append(v)
        for nei in adj[v]:
            if not visited[nei]:
                dfs(nei)
                
    # Start DFS from node 1
    dfs(1)
    
    # Assign positions 1 to n in the order of DFS
    assignment = [0] * (n+1)
    for i in range(n):
        assignment[order[i]] = i + 1
        
    cost = compute_cost(assignment)
    
    if cost <= B:
        print("YES")
        print(' '.join(map(str, assignment[1:])))
        return
    
    # Heuristic didn't work, try reverse order
    assignment_rev = [0] * (n+1)
    for i in range(n):
        assignment_rev[order[n-1-i]] = i + 1
        
    cost_rev = compute_cost(assignment_rev)
    
    if cost_rev <= B:
        print("YES")
        print(' '.join(map(str, assignment_rev[1:])))
        return
    
    # Try BFS ordering
    visited_bfs = [False] * (n+1)
    order_bfs = []
    queue = deque()
    queue.append(1)
    visited_bfs[1] = True
    
    while queue:
        v = queue.popleft()
        order_bfs.append(v)
        for nei in adj[v]:
            if not visited_bfs[nei]:
                visited_bfs[nei] = True
                queue.append(nei)
                
    assignment_bfs = [0] * (n+1)
    for i in range(n):
        assignment_bfs[order_bfs[i]] = i + 1
        
    cost_bfs = compute_cost(assignment_bfs)
    
    if cost_bfs <= B:
        print("YES")
        print(' '.join(map(str, assignment_bfs[1:])))
        return
    
    # Try placing centroid in the middle
    # For simplicity, let's just try a few heuristics
    
    # Another idea: sort nodes by degree descending, place high-degree nodes centrally
    degrees = [(len(adj[i]), i) for i in range(1, n+1)]
    degrees.sort(reverse=True)
    
    assignment_deg = [0] * (n+1)
    for i in range(n):
        node = degrees[i][1]
        assignment_deg[node] = i + 1
        
    cost_deg = compute_cost(assignment_deg)
    
    if cost_deg <= B:
        print("YES")
        print(' '.join(map(str, assignment_deg[1:])))
        return
    
    # Last resort: try random permutations for small n
    if n <= 10:
        import itertools
        for perm in itertools.permutations(range(1,n+1)):
            assgn = [0] * (n+1)
            for i in range(n):
                assgn[i+1] = perm[i]
            if compute_cost(assgn) <= B:
                print("YES")
                print(' '.join(map(str, assgn[1:])))
                return
    
    print("NO")

if __name__ == "__main__":
    main()