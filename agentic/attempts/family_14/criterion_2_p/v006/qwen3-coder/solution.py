import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m, t = map(int, sys.stdin.readline().split())
    hubs = set(map(int, sys.stdin.readline().split()))
    
    # If there's only one hub, cost is 0
    if t <= 1:
        print(0)
        return
    
    # Build the tree
    adj = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # We need to find the minimal subtree that connects all hubs
    # This is the Steiner tree problem on a tree, which can be solved efficiently
    
    # Approach:
    # 1. Find the subtree that contains all hubs
    # 2. The minimal way to connect all hubs is to take the edges of this subtree
    
    # First, let's find all nodes that are on paths between any two hubs
    # We can do this by finding the union of paths between all pairs of hubs
    # But since it's a tree, we can find the "smallest subtree" containing all hubs
    
    # A more efficient approach:
    # Root the tree at some node, compute for each node whether its subtree contains any hub
    # Then, the minimal subtree connecting all hubs consists of all edges where both endpoints 
    # have subtrees containing at least one hub (or one endpoint is a hub and the other's subtree has a hub)
    
    # Even simpler approach for a tree:
    # The minimal subtree connecting all the hubs is the union of paths between them
    # In a tree, this is equivalent to taking all edges in the subtree formed by:
    # - All hubs
    # - All nodes that lie on paths between pairs of hubs
    
    # Efficient algorithm:
    # 1. Root the tree at an arbitrary node
    # 2. For each node, compute if its subtree contains any hub
    # 3. An edge should be included if it connects two parts of the tree that both contain hubs
    
    # Let's root at node 1
    parent = [-1] * (n + 1)
    depth = [-1] * (n + 1)
    subtree_has_hub = [False] * (n + 1)
    
    # BFS to build parent and depth
    queue = deque([1])
    depth[1] = 0
    parent[1] = -1
    
    order = []
    while queue:
        u = queue.popleft()
        order.append(u)
        for v, w in adj[u]:
            if depth[v] == -1:
                depth[v] = depth[u] + 1
                parent[v] = u
                queue.append(v)
    
    # Mark which nodes are hubs
    is_hub = [False] * (n + 1)
    for h in hubs:
        is_hub[h] = True
    
    # Compute subtree_has_hub in reverse order
    for u in reversed(order):
        subtree_has_hub[u] = is_hub[u]
        for v, w in adj[u]:
            if v != parent[u]:
                subtree_has_hub[u] = subtree_has_hub[u] or subtree_has_hub[v]
    
    # Now, count the total weight of edges where both sides of the edge have hubs in their subtrees
    total_cost = 0
    for u in range(1, n + 1):
        for v, w in adj[u]:
            if v == parent[u]:  # Only consider each edge once
                # Edge from v to u (u is parent of v)
                # Does v's subtree have a hub? Does the rest of the tree (including u's other subtrees) have a hub?
                # subtree_has_hub[v] tells us if v's subtree has a hub
                # We need to check if there's a hub outside v's subtree
                # That's true if the total number of hubs > number in v's subtree
                # But actually, we want both sides of the edge to have at least one hub
                # subtree_has_hub[v] and (subtree_has_hub[u] considering removal of v's subtree)
                
                # Simpler logic:
                # The edge {u,v} should be included if:
                # 1. v's subtree contains at least one hub AND 
                # 2. the rest of the tree (including u and its other children) contains at least one hub
                
                # But since we're working up the tree, when we look at edge (v,u) where u=parent[v],
                # we want: 
                # 1. subtree of v contains a hub (subtree_has_hub[v])  
                # 2. the part of tree not in subtree of v also contains a hub
                
                # subtree_has_hub[u] will be true if u's subtree (which includes v's subtree) has a hub
                # So the part outside v's subtree has a hub if subtree_has_hub[u] is true but only due to other branches
                
                # Actually, let's think differently:
                # An edge should be kept if removing it disconnects two components, each containing at least one hub.
                
                # When we remove edge (u,v) where u=parent[v], we get two components:
                # 1. The subtree of v
                # 2. The rest of the tree
                # Keep the edge if both components contain at least one hub.
                
                component_v = subtree_has_hub[v]
                # Does the other component have a hub?
                # It's the whole tree minus v's subtree
                # So it has a hub if total_hubs > hubs_in_v_subtree
                # But we don't know the count, just the boolean.
                
                # Let's precompute how many hubs are in each subtree
                # No, we just need to know if the complement has a hub.
                # subtree_has_hub[root] will tell us if the whole tree has a hub (it should be True)
                # So the complement of v's subtree has a hub if:
                # Either u has a hub and is not in v's subtree (but it is in u's subtree which includes v),
                # Or another child of u (not v) has a hub in its subtree,
                # Or u's parent has a hub accessible through another branch...
                
                # This is getting complex. Let me try a cleaner approach.
                
                # Cleaner idea:
                # Root the tree. For each node u, keep track of whether the subtree of u contains a hub.
                # For each edge from u to its child v, include the edge in our solution if:
                # 1. v's subtree contains a hub
                # 2. The part of the tree outside v's subtree also contains a hub.
                
                # To check condition 2:
                # The part outside v's subtree contains a hub if:
                # - u itself is a hub, OR
                # - some other child of u has a subtree with a hub, OR  
                # - u's parent side has a hub.
                
                # We can compute for each node u a value: does the part of the tree above u (and siblings) contain a hub?
                # Let's call it 'has_hub_above'
                
    # Let's reorganize with a clearer approach:
    # 1. Root the tree
    # 2. Compute for each node: subtree_contains_hub
    # 3. Compute for each node: contains_hub_from_parent_side (i.e., part of tree not in node's subtree that has a hub)
    # 4. For each edge (u,v) where u is parent of v: include it if subtree_contains_hub[v] AND contains_hub_from_parent_side[u] 
    
    # Actually, even simpler:
    # The edges we want are exactly those in the minimal subtree spanning all hubs.
    # In a tree, this is unique. 
    # We can compute it as: orient all edges away from a root, then an edge is used iff
    # the removal of that edge places the two hubs in different components.
    
    # So for each edge (u,v), with u being parent of v:
    # Use the edge if v's subtree contains >= 1 hub and (total hubs - hubs in v's subtree) >= 1
    
    # We need to count hubs in each subtree.
    hub_count = [0] * (n + 1)
    for u in reversed(order):
        hub_count[u] = 1 if is_hub[u] else 0
        for v, w in adj[u]:
            if v != parent[u]:
                hub_count[u] += hub_count[v]
    
    total_hubs = hub_count[1]  # Should be t
    
    # Now calculate the cost
    total_cost = 0
    for u in range(1, n + 1):
        for v, w in adj[u]:
            if v == parent[u]:  # Each edge considered once
                # If we remove edge (v, u), we get two components:
                # 1. Component of v: has hub_count[v] hubs
                # 2. Rest: has (total_hubs - hub_count[v]) hubs
                # Include edge if both > 0
                if hub_count[v] > 0 and (total_hubs - hub_count[v]) > 0:
                    total_cost += w
                    
    print(total_cost)

if __name__ == "__main__":
    main()