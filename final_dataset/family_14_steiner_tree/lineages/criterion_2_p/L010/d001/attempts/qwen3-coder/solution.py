import sys
from collections import defaultdict, deque

def find_path(parent, start, end):
    path = []
    current = end
    while current != start:
        path.append(current)
        current = parent[current]
    path.append(start)
    return path[::-1]

def bfs_get_path(graph, start, end):
    if start == end:
        return [start]
    visited = set()
    queue = deque([start])
    parent = {start: None}
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        if node == end:
            return find_path(parent, start, end)
        
        for neighbor, _ in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)
    return []

def get_edges_in_path(graph, path):
    edges = []
    for i in range(len(path) - 1):
        u, v = path[i], path[i+1]
        # Find the edge weight
        for neighbor, weight in graph[u]:
            if neighbor == v:
                edges.append((u, v, weight))
                break
    return edges

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    t = int(data[idx])
    idx += 1
    
    spores = list(map(int, data[idx:idx+t]))
    idx += t
    
    # Build graph
    graph = defaultdict(list)
    edges = []
    
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        graph[u].append((v, w))
        graph[v].append((u, w))
        edges.append((u, v, w))
    
    # If only one spore, cost is 0
    if t == 1:
        print(0)
        return
    
    # For each pair of spores, find path and collect all edges
    required_edges = set()
    
    # We need to connect all spores, so we can build a tree of spores
    # We'll do this by finding paths between spores and taking the union of edges
    # But to minimize cost, we should find the minimum spanning tree of the spore nodes
    # This is essentially finding the Steiner tree, which is hard
    # But since the original graph is a tree, we can do the following:
    # Find the union of paths between all pairs of spores, then find the MST of that
    
    # Simpler approach for a tree: 
    # The minimal set of edges to connect all spore nodes is the set of edges
    # in the subgraph formed by taking the union of paths between all pairs
    # But since it's a tree, the minimal connection is just the paths needed
    # A better way: find the minimal subtree that connects all spores
    
    # In a tree, the minimal set of edges to connect a subset of nodes
    # is the set of edges in the paths between consecutive nodes in some ordering
    # But the optimal is the edges in the minimal subtree spanning all spore nodes
    
    # Algorithm:
    # 1. Find the "Steiner tree" for the spore nodes in the tree
    # Since the graph is a tree, we can:
    # - Find all nodes that are on paths between spore nodes
    # - The minimal cost is the sum of weights of edges in this subtree
    
    # Approach:
    # Find the union of all paths between pairs of spores
    # But that might be inefficient
    # Better: find the minimal subtree containing all spores
    
    # In a tree, this is equivalent to:
    # 1. Find all paths between consecutive spores in some order
    # 2. Take the union of edges
    # But to minimize, we should find the minimal connected subtree containing all spores
    
    # Efficient approach:
    # Since the original graph is a tree, the minimal way to connect spores
    # is to find the "smallest subtree" that contains all of them
    # This can be found by:
    # 1. Starting with all spore nodes
    # 2. Adding all nodes that are on paths between spore nodes
    # 3. The cost is the sum of edge weights in this subtree
    
    # Even simpler for a tree:
    # The edges we need are exactly those edges that are on paths between spore nodes
    # But we need to be careful not to double count
    
    # Let's use the fact that in a tree, to connect k nodes,
    # we need exactly k-1 paths, and the minimal way is the subtree
    # spanning these nodes
    
    # Algorithm:
    # 1. Root the tree at any node
    # 2. Find the lowest common ancestors of all spore pairs
    # 3. The minimal subtree has edges that are on paths from each spore to the root
    #    and their LCA
    
    # Simpler:
    # Since it's a tree, we can:
    # 1. Pick any spore as root
    # 2. For each other spore, find the path to the root
    # 3. Union all these paths
    # But this might not be minimal
    
    # Most direct approach:
    # Find the subtree that spans all spore nodes
    # In a tree, this is unique
    
    # Algorithm:
    # 1. Do BFS from one spore to find distances and parents
    # 2. Find the furthest spore from it
    # 3. Find the furthest spore from that one
    # 4. The path between these two is the "diameter"
    # 5. All spores must be within distance 0 from this path
    # No, that's not right either
    
    # Correct approach:
    # Since the graph is a tree, we can find the minimal subtree containing all spores
    # by:
    # 1. Starting with a set of "required" nodes = spore nodes
    # 2. Repeatedly add parents until we have a connected subtree
    # But in a tree, it's easier:
    # The minimal subtree containing a set of nodes is the union of paths
    # between all pairs of those nodes. But since it's a tree, there's a simpler way.
    
    # The key insight: in a tree, the minimal cost to connect a set of nodes
    # is the total weight of the minimal subtree that contains all of them.
    
    # Algorithm to find this:
    # 1. Root the tree at node 1
    # 2. For each node, compute:
    #    - parent
    #    - depth
    #    - subtree that contains spores
    # 3. A node is in the minimal subtree if:
    #    - it is a spore node, OR
    #    - it has a child whose subtree contains a spore
    
    # Let's implement a cleaner solution:
    
    # Since the graph is a tree, we can use the following approach:
    # 1. Root the tree at node 1
    # 2. Do a DFS to compute parent and depth for each node
    # 3. Mark which nodes are spores
    # 4. Do another DFS to determine which edges are in the minimal subtree
    
    # But let's think differently:
    # In a tree, to connect k nodes minimally, we take the union of paths
    # between them. But since it's a tree, there's a unique minimal subtree.
    
    # Simpler idea:
    # 1. Build a set of all spore nodes
    # 2. Find all edges that must be included to connect them
    # 3. In a tree, this is the set of edges in the paths between spore nodes
    
    # Even simpler for implementation:
    # Use the fact that in the minimal subtree connecting spores,
    # an edge is included if and only if removing it separates the tree
    # into two components, each containing at least one spore.
    
    # Algorithm:
    # 1. Root the tree
    # 2. For each node, count how many spores are in its subtree
    # 3. An edge from parent to child is needed if:
    #    - The subtree of child contains at least one spore, AND
    #    - The subtree of child contains less than t spores
    
    # Implementation:
    
    # First, root the tree at node 1 and build parent/children structure
    adj = defaultdict(list)
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # DFS to build tree structure
    parent = [-1] * (n + 1)
    children = defaultdict(list)
    edge_weight = {}  # (u, v) -> weight where u is parent of v
    
    def dfs(u, par):
        parent[u] = par
        for v, w in adj[u]:
            if v != par:
                children[u].append(v)
                edge_weight[(u, v)] = w
                dfs(v, u)
    
    dfs(1, -1)
    
    # Count spores in each subtree
    spore_set = set(spores)
    spore_count = [0] * (n + 1)
    
    def count_spores(u):
        if u in spore_set:
            spore_count[u] = 1
        for v in children[u]:
            spore_count[u] += count_spores(v)
        return spore_count[u]
    
    count_spores(1)
    
    # Calculate total cost
    total_cost = 0
    for u in range(1, n + 1):
        for v in children[u]:
            # Edge from u to v
            # Include this edge if subtree of v has at least 1 spore
            # and at most t-1 spores
            if 1 <= spore_count[v] < t:
                total_cost += edge_weight[(u, v)]
    
    print(total_cost)

if __name__ == "__main__":
    main()