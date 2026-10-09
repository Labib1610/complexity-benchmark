import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1000000)
    
    n, m, t = map(int, sys.stdin.readline().split())
    priority = set(map(int, sys.stdin.readline().split()))
    
    # Since it's a tree, we can represent it as an adjacency list
    tree = defaultdict(list)
    edges = []
    
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        tree[u].append((v, w))
        tree[v].append((u, w))
        edges.append((w, u, v))
    
    # If there's only one priority node, cost is 0
    if t <= 1:
        print(0)
        return
    
    # Find the subtree that connects all priority nodes
    # We can do this by finding all edges that are on paths between priority nodes
    
    # First, find all nodes in the subtree spanning the priority nodes
    # We'll do this by finding the "Steiner tree" of the priority nodes in the tree
    
    # In a tree, the minimal connected subgraph containing a set of nodes
    # is the union of all paths between pairs of those nodes.
    # But there's a simpler way: find all edges such that removing them
    # would disconnect the priority nodes.
    
    # A simpler approach:
    # Root the tree at any node, compute for each node whether its subtree contains
    # any priority nodes. An edge is needed if it connects two subtrees that both
    # contain priority nodes.
    
    # Let's root the tree at node 1
    parent = [-1] * (n + 1)
    parent_weight = [-1] * (n + 1)  # weight of edge to parent
    children = defaultdict(list)
    
    # BFS to build rooted tree
    visited = [False] * (n + 1)
    queue = deque([1])
    visited[1] = True
    
    while queue:
        u = queue.popleft()
        for v, w in tree[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                parent_weight[v] = w
                children[u].append(v)
                queue.append(v)
    
    # Count priority nodes in each subtree
    priority_count = [0] * (n + 1)
    
    # Post-order traversal to count priority nodes in subtrees
    def dfs_count(u):
        if u in priority:
            priority_count[u] = 1
        else:
            priority_count[u] = 0
            
        for v in children[u]:
            dfs_count(v)
            priority_count[u] += priority_count[v]
    
    dfs_count(1)
    
    # Now find the total cost of edges connecting the priority nodes
    total_cost = 0
    # For each node (except root), if both the node's subtree and the rest of the tree
    # contain priority nodes, then the edge to its parent is needed
    for u in range(2, n + 1):
        count_in_subtree = priority_count[u]
        count_outside_subtree = t - count_in_subtree
        
        if count_in_subtree > 0 and count_outside_subtree > 0:
            total_cost += parent_weight[u]
    
    print(total_cost)

if __name__ == "__main__":
    main()