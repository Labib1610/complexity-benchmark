import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m, t = map(int, sys.stdin.readline().split())
    active = set(map(int, sys.stdin.readline().split()))
    
    # Since m = n-1 and there's exactly one path between any two nodes,
    # the graph is a tree.
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # If there's only one active node, cost is 0
    if t <= 1:
        print(0)
        return
    
    # Find the minimal subtree that connects all active nodes.
    # This is the Steiner tree problem on a tree, which can be solved
    # by finding the minimal connected subgraph containing all active nodes.
    
    # Approach:
    # 1. Mark all active nodes.
    # 2. Perform a traversal to find all edges that must be included
    #    to connect the active nodes. These are the edges on paths
    #    between active nodes, but we can compute this more efficiently.
    
    # Efficient approach:
    # Since it's a tree, the minimal connecting subgraph is the union
    # of paths between all pairs of active nodes. But since it's a tree,
    # it's equivalent to finding the minimal subtree that contains all
    # active nodes. This can be done by:
    # - Marking all active nodes
    # - Finding all nodes that lie on paths between active nodes
    # - The edges needed are those connecting these nodes
    
    # Simpler method:
    # Root the tree at some node, compute for each node whether its
    # subtree contains any active node. An edge should be included
    # if it separates active nodes (i.e., both endpoints' subtrees
    # contain active nodes or one endpoint is active and the other's
    # subtree contains active nodes).
    
    # Even simpler: 
    # Use the fact that in a tree, the minimal cost to connect a set
    # of nodes is the sum of edge weights in the minimal subtree
    # connecting them. We can compute this by:
    # 1. Rooting the tree at an arbitrary node
    # 2. For each node, compute how many active nodes are in its subtree
    # 3. An edge {u,v} (where v is child of u) contributes to the cost
    #    if both u's subtree and the rest of the tree contain active nodes.
    #    But actually, in the minimal subtree connecting all active nodes,
    #    an edge is included if removing it disconnects the graph into
    #    two components each containing at least one active node.
    
    # Let's use DFS to determine for each node how many active nodes
    # are in its subtree. Then for each edge, if it connects a subtree
    # with `k` active nodes to the rest with `t-k` active nodes, and
    # both k > 0 and t-k > 0, then this edge must be included.
    
    # Root the tree at node 1
    parent = [0] * (n+1)
    children = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    
    # BFS to build rooted tree
    queue = deque([1])
    visited[1] = True
    while queue:
        u = queue.popleft()
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                children[u].append((v, w))
                queue.append(v)
    
    # Count active nodes in each subtree
    count_active = [0] * (n+1)
    # Leaf to root pass
    stack = []
    # Topological order for processing
    temp_visited = [False] * (n+1)
    topo_queue = deque([1])
    while topo_queue:
        u = topo_queue.popleft()
        if temp_visited[u]:
            continue
        temp_visited[u] = True
        stack.append(u)
        for v, w in children[u]:
            if not temp_visited[v]:
                topo_queue.appendleft(v)
                topo_queue.appendleft(u)
                break
        else:
            continue
        for v, w in children[u]:
            if not temp_visited[v]:
                topo_queue.appendleft(v)
    
    # Actually, let's just do post-order DFS
    def dfs_count(u):
        count = 1 if u in active else 0
        for v, w in children[u]:
            count += dfs_count(v)
        count_active[u] = count
        return count_active[u]
    
    dfs_count(1)
    
    # Now calculate the total cost
    total_cost = 0
    for u in range(1, n+1):
        for v, w in children[u]:
            # Edge from u to v
            count_v_subtree = count_active[v]
            count_rest = t - count_v_subtree
            if count_v_subtree > 0 and count_rest > 0:
                total_cost += w
                
    print(total_cost)

if __name__ == "__main__":
    main()