import sys
from collections import defaultdict, deque

def find_subtree_nodes(graph, start, exclude_node):
    """Find all nodes in the subtree starting from 'start' excluding 'exclude_node'"""
    visited = set()
    queue = deque([start])
    visited.add(start)
    nodes = []
    
    while queue:
        node = queue.popleft()
        nodes.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited and neighbor != exclude_node:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return nodes

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
    
    keyholders = set()
    for _ in range(t):
        keyholders.add(int(data[idx]))
        idx += 1
    
    # If there's only one keyholder, no communication needed
    if t <= 1:
        print(0)
        return
    
    edges = []
    graph = defaultdict(list)
    
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        edges.append((w, u, v))
        graph[u].append(v)
        graph[v].append(u)
    
    # Sort edges by weight for Kruskal's algorithm
    edges.sort()
    
    # Union-Find data structure
    parent = list(range(n + 1))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
            return True
        return False
    
    # First, let's find the minimal subtree that connects all keyholders
    # We'll use a modified approach: we need to find the minimum spanning tree
    # but only consider the edges that are necessary to connect all keyholders
    
    # However, there's a simpler approach:
    # Since the input forms a tree (m = n-1), we just need to find the minimal
    # subtree that spans all keyholders. This is equivalent to finding the
    # minimum Steiner tree on a tree, which can be solved efficiently.
    
    # For a tree, the minimum Steiner tree can be found by:
    # 1. Consider all paths between pairs of keyholders
    # 2. Take the union of these paths
    # 3. The cost is the sum of weights of unique edges in this union
    
    # But there's an even simpler approach for trees:
    # Root the tree at any node, compute for each node whether its subtree
    # contains any keyholder. An edge should be included if it connects
    # two subtrees that both contain at least one keyholder.
    
    # Let's implement this approach:
    
    # Build adjacency list with weights
    adj = defaultdict(list)
    for w, u, v in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Root the tree at node 1 (arbitrary choice)
    root = 1
    
    # DFS to compute for each node, whether its subtree contains keyholders
    # and which edges need to be included
    visited = [False] * (n + 1)
    key_in_subtree = [0] * (n + 1)  # Number of keyholders in subtree
    total_cost = 0
    
    def dfs(node, parent):
        visited[node] = True
        count = 1 if node in keyholders else 0
        
        for neighbor, weight in adj[node]:
            if neighbor == parent:
                continue
            if not visited[neighbor]:
                child_count = dfs(neighbor, node)
                count += child_count
                # If both current subtree and child subtree have keyholders,
                # we need this edge
                if child_count > 0 and (count - child_count) > 0:
                    nonlocal total_cost
                    total_cost += weight
        
        key_in_subtree[node] = count
        return count
    
    dfs(root, -1)
    print(total_cost)

if __name__ == "__main__":
    main()