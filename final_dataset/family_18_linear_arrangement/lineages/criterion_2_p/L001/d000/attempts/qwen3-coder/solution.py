import sys
from collections import defaultdict, deque

def solve():
    n, m, B = map(int, input().split())
    
    # Build adjacency list representation of the tree
    adj = defaultdict(list)
    edges = []
    
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    if n == 1:
        print("YES")
        print(1)
        return
    
    # Find the root (could be any node with degree > 1, or just pick node 1)
    # Actually, we need to build a proper rooted tree
    # Let's find degrees first
    degree = defaultdict(int)
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1
    
    # Find root - node with highest degree or just start with node 1
    root = 1
    
    # Build tree structure with parent-child relationships
    tree = defaultdict(list)
    parent = {}
    
    visited = set()
    queue = deque([root])
    visited.add(root)
    parent[root] = None
    
    while queue:
        node = queue.popleft()
        for neighbor in adj[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                tree[node].append(neighbor)
                queue.append(neighbor)
    
    # Calculate subtree sizes
    subtree_size = [0] * (n + 1)
    
    def dfs(node):
        size = 1
        for child in tree[node]:
            size += dfs(child)
        subtree_size[node] = size
        return size
    
    dfs(root)
    
    # Try to place nodes optimally to minimize total distance
    # We'll use a greedy approach placing subtrees compactly
    
    position = [0] * (n + 1)  # position[i] = position of node i
    assigned = [False] * (n + 1)
    
    # Place the root somewhere in the middle for better distribution
    # Actually, let's try a linear arrangement approach
    
    # Use post-order traversal to assign positions
    def assign_positions(node, start_pos):
        # For current subtree rooted at node, assign positions starting from start_pos
        # Return the next available position
        
        children = tree[node]
        if not children:
            # Leaf node
            position[node] = start_pos
            assigned[node] = True
            return start_pos + 1
        
        # Assign positions to children first
        current_pos = start_pos
        for child in children:
            current_pos = assign_positions(child, current_pos)
        
        # Place the current node right after its children
        position[node] = current_pos
        assigned[node] = True
        return current_pos + 1
    
    # Start assignment from root
    assign_positions(root, 1)
    
    # Calculate total cost
    total_cost = 0
    for u, v in edges:
        total_cost += abs(position[u] - position[v])
    
    if total_cost <= B:
        print("YES")
        result = [0] * n
        for i in range(1, n + 1):
            result[position[i] - 1] = i
        print(*result)
    else:
        # Try another arrangement strategy
        # Place nodes in a way that minimizes distances
        
        # Reset
        position = [0] * (n + 1)
        
        # Try placing in DFS order
        def dfs_order(node, pos):
            position[node] = pos
            next_pos = pos + 1
            for child in tree[node]:
                next_pos = dfs_order(child, next_pos)
            return next_pos
        
        dfs_order(root, 1)
        
        # Recalculate cost
        total_cost = 0
        for u, v in edges:
            total_cost += abs(position[u] - position[v])
        
        if total_cost <= B:
            print("YES")
            result = [0] * n
            for i in range(1, n + 1):
                result[position[i] - 1] = i
            print(*result)
        else:
            # Try a different approach - heavy path decomposition style
            
            # Reset positions
            position = [0] * (n + 1)
            
            # Place nodes trying to keep parent-child close
            def place_nodes_optimally(node, anchor):
                # Place node near its anchor
                # Try to place children compactly
                
                # Place current node at anchor
                position[node] = anchor
                next_anchor = anchor + 1
                
                # Sort children by subtree size (largest first - heavy-light style)
                children_sorted = sorted(tree[node], key=lambda x: -subtree_size[x])
                
                for child in children_sorted:
                    next_anchor = place_nodes_optimally(child, next_anchor)
                
                return next_anchor
            
            place_nodes_optimally(root, 1)
            
            # Recalculate cost
            total_cost = 0
            for u, v in edges:
                total_cost += abs(position[u] - position[v])
            
            if total_cost <= B:
                print("YES")
                # Create result array
                result = [0] * n
                for i in range(1, n + 1):
                    result[position[i] - 1] = i
                print(*result)
            else:
                # Last attempt - just sequential ordering based on component sizes
                position = [0] * (n + 1)
                
                # Simple linear arrangement according to DFS visit order
                order = []
                def simple_dfs(node):
                    order.append(node)
                    for child in tree[node]:
                        simple_dfs(child)
                
                simple_dfs(root)
                
                for idx, node in enumerate(order):
                    position[node] = idx + 1
                
                # Recalculate cost
                total_cost = 0
                for u, v in edges:
                    total_cost += abs(position[u] - position[v])
                
                if total_cost <= B:
                    print("YES")
                    result = [0] * n
                    for i in range(1, n + 1):
                        result[position[i] - 1] = i
                    print(*result)
                else:
                    print("NO")

solve()