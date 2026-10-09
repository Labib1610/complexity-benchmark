import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1000000)
    
    n, m, B = map(int, sys.stdin.readline().split())
    
    # Build adjacency list
    adj = defaultdict(list)
    degree = [0] * (n + 1)
    
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
        degree[u] += 1
        degree[v] += 1
        edges.append((u, v))
    
    # Find root (the node with highest degree, or just any leaf's neighbor)
    # Actually, since it's a tree and every node except one feeds into exactly one other,
    # the root is the one that has zero outgoing edges in the original DAG.
    # But since we have undirected edges now, root is the one that was originally having multiple children.
    # Simpler: find a leaf (degree 1) and start BFS from its neighbor
    
    # Find a leaf
    leaf = -1
    for i in range(1, n+1):
        if degree[i] == 1:
            leaf = i
            break
    
    # BFS to get parent relationships and ordering
    parent = [-1] * (n + 1)
    visited = [False] * (n + 1)
    queue = deque()
    queue.append(leaf)
    visited[leaf] = True
    
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                queue.append(v)
    
    # Now, find the root (the one with no parent)
    root = -1
    for i in range(1, n+1):
        if parent[i] == -1:
            root = i
            break
    
    # Build tree structure: children list
    children = defaultdict(list)
    for i in range(1, n+1):
        if parent[i] != -1:
            children[parent[i]].append(i)
    
    # DFS to compute subtree sizes
    size = [0] * (n + 1)
    
    def dfs(u):
        s = 1
        for v in children[u]:
            s += dfs(v)
        size[u] = s
        return s
    
    dfs(root)
    
    # Now, we try to assign positions in a way that minimizes total distance
    # A good heuristic is to use heavy-path decomposition or just assign in-order traversal
    
    # In-order traversal assignment gives a good layout for trees
    pos = [0] * (n + 1)
    current_pos = 0
    
    def inorder(u):
        nonlocal current_pos
        # Assign left children first
        child_list = children[u]
        if len(child_list) == 0:
            current_pos += 1
            pos[u] = current_pos
            return
        elif len(child_list) == 1:
            inorder(child_list[0])
            current_pos += 1
            pos[u] = current_pos
        else:
            # For binary tree-like case, assign left, then root, then right
            # But since it's a general tree, we can assign all children first, then root
            # Or root first, then children
            # Let's try assigning children in order, then root at the end of them
            for v in child_list:
                inorder(v)
            current_pos += 1
            pos[u] = current_pos
    
    # Actually, let's do a proper in-order for general trees:
    # Assign children recursively, placing the root after the first child if there are multiple
    
    def assign_positions(u):
        nonlocal current_pos
        child_list = children[u]
        if not child_list:
            current_pos += 1
            pos[u] = current_pos
        else:
            # Assign first child
            assign_positions(child_list[0])
            # Assign root
            current_pos += 1
            pos[u] = current_pos
            # Assign remaining children
            for i in range(1, len(child_list)):
                assign_positions(child_list[i])
    
    assign_positions(root)
    
    # Calculate total cost
    total_cost = 0
    for u, v in edges:
        total_cost += abs(pos[u] - pos[v])
    
    if total_cost <= B:
        print("YES")
        result = []
        for i in range(1, n+1):
            result.append(str(pos[i]))
        print(' '.join(result))
    else:
        print("NO")

if __name__ == "__main__":
    main()