import sys
from collections import defaultdict

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    px, py = find(parent, x), find(parent, y)
    if px == py:
        return False
    if rank[px] < rank[py]:
        px, py = py, px
    parent[py] = px
    if rank[px] == rank[py]:
        rank[px] += 1
    return True

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
    
    required = set()
    for _ in range(t):
        required.add(int(data[idx]))
        idx += 1
    
    edges = []
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        edges.append((w, u, v))
    
    if t <= 1:
        print(0)
        return
    
    # Sort edges by weight
    edges.sort()
    
    # Initialize DSU
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    total_cost = 0
    connected_components = len(required)
    
    for w, u, v in edges:
        if find(parent, u) != find(parent, v):
            # Check if either u or v is required
            u_required = u in required
            v_required = v in required
            
            # Check if they belong to components with required nodes
            pu = find(parent, u)
            pv = find(parent, v)
            
            # Count how many required nodes would be connected by this edge
            # For efficiency, we'll use a different approach:
            # We track which components contain required nodes
            
            # Actually, let's think differently:
            # We want to connect all required nodes with minimum cost
            # This is a Steiner tree problem on a tree (since m=n-1 and unique path)
            # But since it's a tree, we can find the minimal subtree that spans all required nodes
            
            # In a tree, the minimal connected subgraph containing all required nodes
            # is the union of all paths between pairs of required nodes
            # Which is equivalent to: take all edges in the unique paths between
            # all pairs of required nodes, and take the minimal such set
            
            # But there's a simpler way:
            # In the process of Kruskal's algorithm, when we connect two components
            # and at least one of them contains a required node, we might be making progress
            # But it's complex to track
            
            # Better approach:
            # Since the graph is a tree, we can:
            # 1. Find the minimal subtree that contains all required nodes
            # 2. The cost is the sum of weights of edges in this subtree
            
            # To find the minimal subtree:
            # It's the union of paths between all pairs of required nodes
            # But since it's a tree, it's the same as:
            # Find the "Steiner tree" which is the minimal subtree containing all required nodes
            
            # There's a property: In a tree, the minimal connected subgraph containing
            # a set of vertices is the union of the paths between them
            # And the way to find it is:
            # Root the tree at any node, find the deepest required node,
            # then the minimal subtree is the set of all edges on paths from
            # root to each required node, but that overcounts
            
            # The correct way:
            # The minimal subtree containing all required nodes is the same as
            # the union of paths between them. In a tree, this is equivalent to:
            # 1. Take all leaves that are not required and remove them iteratively
            # 2. The remaining tree is the minimal subtree
            
            # But for MST approach in a tree:
            # We just run Kruskal and sum up edges that connect components with required nodes
            
            # Let's track for each component whether it contains a required node
            # Initially, each required node is in its own component with a required flag
            
            # This is getting complex. Let's reframe:
            # Since the input graph is a tree (m=n-1, and unique path between any two nodes)
            # The problem is to find the minimum cost to connect all required nodes
            # In a tree, there's only one way to connect any two nodes
            # So the solution is to take the unique paths between all pairs
            # But that's not minimal
            
            # Actually, in a tree, the minimal connected subgraph containing all required nodes
            # is unique and is called the "Steiner tree" for the set of required nodes
            # The cost is the sum of the weights of the edges in this subtree
            
            # Algorithm to find it:
            # 1. Root the tree at any node
            # 2. For each node, compute if its subtree contains any required node
            # 3. An edge should be included if both its endpoints' subtrees contain required nodes
            #    or one endpoint's subtree contains a required node and the other endpoint is required
            
            # Even simpler approach for a tree:
            # Run a DFS to find the minimal subtree containing all required nodes
            # An edge is in the minimal subtree if removing it increases the number of components
            # that contain required nodes
            
            # Let's do this properly:
            # Use Union-Find in Kruskal's order, and when we merge two components,
            # if both components contain required nodes, we must take this edge
            # We need to track for each component whether it contains any required node
            
            # Initialize: each node is its own component
            # For required nodes, their component contains a required node
            
            # But Union-Find doesn't easily track component properties
            # Let's use a different approach
            
            # Since it's a tree, we can build the minimal subtree directly
            # by marking all nodes and edges on paths between required nodes
            
            # But let's try the Union-Find with tracking approach:
            
            # Let's associate with each component a set of required nodes it contains
            # This is too memory intensive
            
            # Simpler: 
            # Each component has a flag: does it contain any required node?
            # When we merge components, if both contain required nodes, we take the edge
            # We also update the flag for the new component
            
            # But we need to be more careful:
            # We want the total number of required-node-containing components to go from |required| to 1
            # Each time we merge two such components, it decreases by 1
            # So we need to do exactly (number of required components - 1) such merges
            # And we want to minimize the total cost of edges used for these merges
            
            # This is exactly Kruskal's algorithm where we only care about connecting required nodes!
            
            # So:
            # - We have a forest initially (each node a component)
            # - Some components are "active" (contain required nodes)  
            # - We want to connect all active components with minimal cost
            # - This is exactly MST of the "active" components
            # - Since the original graph is a tree, the MST is unique and is a subtree
            # - We can simulate Kruskal: sort edges, process in order
            # - For each edge, if it connects two different active components, take it
            # - Merge the components, update active status
            
            # Implementation:
            # For each component, keep track if it contains any required node
            # Initially, component i contains required node iff i is required
            # When merging components pu and pv:
            # - If both contain required nodes, we must take the edge (add to cost)
            # - The new component contains required nodes if either old component did
            # - If we merge two components that both have required nodes, we've connected some required nodes
            #   so we decrease the count of active components
            
            # Let's track the number of active (required-containing) components
            # When it reaches 1, all required nodes are connected
            
            # But we need to know for each component whether it contains a required node
            # Let's use Union-Find with an extra field
            
            # Actually, let's think of it this way:
            # We're building a MST of the subgraph induced by required nodes
            # But since the graph is a tree, it's simpler
            
            # Let's restart with a clean approach:
            
            # The graph is a tree. The required nodes need to be connected.
            # In a tree, there's a unique path between any two nodes.
            # The minimum cost to connect all required nodes is the cost of the 
            # minimal subtree containing them.
            
            # Algorithm:
            # 1. Root the tree at any node
            # 2. For each node, compute if its subtree contains any required node
            # 3. An edge {u, v} (where v is child of u) is in the minimal subtree 
            #    iff v's subtree contains a required node
            # 4. Sum weights of all such edges
            
            # But the tree is not rooted and we don't have parent-child relationships
            
            # Let's build a proper solution:
            # Since it's a tree, we can use the fact that the minimal subtree containing
            # all required nodes can be found by:
            # 1. Starting with all required nodes marked
            # 2. Iteratively removing leaves that are not required
            # 3. The edges left are the ones we need
            
            # But to do that we need adjacency list and degrees - complex
            
            # Let's go back to Union-Find approach:
            # Key insight: we want to connect all required nodes minimally
            # In the original tree, there's only one path between any two nodes
            # So the cost of connecting all required nodes is fixed - it's the 
            # sum of weights on the edges in the minimal subtree containing them
            
            # But how to compute it?
            
            # Another insight: run Kruskal's algorithm on the tree
            # Process edges in order of weight
            # When processing an edge, if it connects two components that each 
            # contain at least one required node, we must take this edge
            # (because in the final solution, required nodes must be connected)
            
            # So we can simulate this:
            # - Keep track for each component whether it contains a required node
            # - Initially, component i contains required node iff i is required
            # - For each edge in sorted order:
            #   - If it connects two different components that both contain required nodes:
            #     - Add its weight to total cost
            #     - Merge the components
            #     - The new component contains required nodes
            #   - Else if it connects components where exactly one contains required nodes:
            #     - Merge, new component contains required nodes
            #   - Else:
            #     - Merge, new component doesn't contain required nodes
            
            # But we also need to track when all required nodes are in one component
            # Let's track number of "active" components (those containing required nodes)
            # Initially it's t. When it becomes 1, we're done
            
            # To track if component contains required nodes:
            # For component representative i, let's keep a boolean has_required[i]
            
    # Let's restart implementation with this logic
    
    # Re-read input for clean implementation
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
    
    required = set()
    for _ in range(t):
        required.add(int(data[idx]))
        idx += 1
    
    edges = []
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        edges.append((w, u, v))
    
    if t <= 1:
        print(0)
        return
    
    # Sort edges by weight
    edges.sort()
    
    # Union-Find with tracking of required nodes
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    has_required = [False] * (n + 1)
    
    # Initialize which components have required nodes
    for node in required:
        has_required[node] = True
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1
        # Update has_required for the new component
        has_required[px] = has_required[px] or has_required[py]
        return True
    
    total_cost = 0
    # Number of components that contain at least one required node
    active_components = t
    
    for w, u, v in edges:
        pu, pv = find(u), find(v)
        if pu != pv:
            # Check if we're connecting two components that both have required nodes
            if has_required[pu] and has_required[pv]:
                total_cost += w
                active_components -= 1
                if active_components == 1:
                    break
            # Perform the union
            union(u, v)
        else:
            # u and v already in same component, do nothing
            pass
    
    print(total_cost)

if __name__ == "__main__":
    main()