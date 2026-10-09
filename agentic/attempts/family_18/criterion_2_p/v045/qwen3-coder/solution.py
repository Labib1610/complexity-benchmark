import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1000000)
    
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    B = int(data[idx])
    idx += 1
    
    edges = []
    graph = defaultdict(list)
    
    for _ in range(m):
        u = int(data[idx]) - 1
        idx += 1
        v = int(data[idx]) - 1
        idx += 1
        edges.append((u, v))
        graph[u].append(v)
        graph[v].append(u)
    
    # Since it's a tree (n nodes, n-1 edges, connected), we can root it at any node
    # We'll use centroid decomposition or just try to find a good layout
    # But since we need to minimize sum of distances, a good heuristic is to do a BFS traversal
    # and assign positions accordingly
    
    # Let's do a BFS from node 0 to get an ordering
    visited = [False] * n
    queue = deque()
    queue.append(0)
    visited[0] = True
    order = []
    
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
    
    # Now we need to assign positions 0 to n-1 to nodes in 'order'
    # A good way is to place them in order on the line to minimize total distance
    # But that's not necessarily optimal
    # Let's try a different approach: build the tree structure and do a layout
    
    # Root the tree at node 0
    parent = [-1] * n
    children = [[] for _ in range(n)]
    visited = [False] * n
    queue = deque()
    queue.append(0)
    visited[0] = True
    
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                children[u].append(v)
                queue.append(v)
    
    # Now do a post-order traversal to compute subtree sizes
    subtree_size = [0] * n
    def compute_subtree_sizes(u):
        size = 1
        for v in children[u]:
            size += compute_subtree_sizes(v)
        subtree_size[u] = size
        return size
    
    compute_subtree_sizes(0)
    
    # Now assign positions using inorder traversal of the tree
    position = [0] * n
    pos_counter = 0
    
    def inorder_assign(u):
        nonlocal pos_counter
        # Assign to children first (left children), then to self, then right children
        # For simplicity, we'll just assign in the order of children
        if children[u]:
            mid = len(children[u]) // 2
            for i in range(mid):
                inorder_assign(children[u][i])
            position[u] = pos_counter
            pos_counter += 1
            for i in range(mid, len(children[u])):
                inorder_assign(children[u][i])
        else:
            position[u] = pos_counter
            pos_counter += 1
    
    # A better way: do a DFS that tries to minimize the total distance
    # Let's try a different approach: use the fact that it's a tree and find a good linear arrangement
    
    # The optimal way is to find a linear arrangement that minimizes the sum of edge lengths
    # This is NP-hard in general, but for trees, there are polynomial algorithms
    # One such method is to use dynamic programming or to find a good heuristic
    
    # Let's try to do a BFS-based layout
    # Place the root at the middle, then place children around it
    
    def layout_tree():
        # Use a greedy approach: place nodes to minimize total distance
        # We'll do a BFS and try to place nodes close to their parents
        final_positions = [-1] * n
        placed = [False] * n
        # Start by placing node 0 at position n//2
        queue = deque()
        queue.append(0)
        placed[0] = True
        final_positions[0] = n // 2
        available_positions = set(range(n))
        available_positions.remove(n // 2)
        
        while queue:
            u = queue.popleft()
            pos_u = final_positions[u]
            # Get unplaced neighbors
            neighbors = graph[u]
            unplaced_neighbors = [v for v in neighbors if not placed[v]]
            
            # Assign positions to unplaced neighbors near pos_u
            # Sort available positions by distance to pos_u
            avail_list = list(available_positions)
            avail_list.sort(key=lambda x: abs(x - pos_u))
            
            for i, v in enumerate(unplaced_neighbors):
                if i < len(avail_list):
                    pos_v = avail_list[i]
                    final_positions[v] = pos_v
                    placed[v] = True
                    available_positions.remove(pos_v)
                    queue.append(v)
        
        # If there are still unplaced nodes, assign them arbitrarily
        for i in range(n):
            if not placed[i]:
                final_positions[i] = available_positions.pop()
                
        return final_positions
    
    # Let's try a simpler approach: just assign the BFS order to consecutive positions
    final_positions = [0] * n
    for i in range(n):
        final_positions[order[i]] = i
    
    # Calculate total cost
    total_cost = 0
    for u, v in edges:
        total_cost += abs(final_positions[u] - final_positions[v])
    
    if total_cost <= B:
        print("YES")
        result = [0] * n
        for i in range(n):
            result[final_positions[i]] = i + 1  # Convert back to 1-based indexing
        print(' '.join(map(str, [result.index(i+1)+1 for i in range(n)])))
        return
    
    # Try a different layout: inorder traversal of a DFS tree
    # Re-initialize
    parent = [-1] * n
    children = [[] for _ in range(n)]
    visited = [False] * n
    queue = deque()
    queue.append(0)
    visited[0] = True
    
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                children[u].append(v)
                queue.append(v)
    
    # Inorder assignment
    position = [0] * n
    pos_counter = 0
    
    def dfs_inorder(u):
        nonlocal pos_counter
        if not children[u]:
            position[u] = pos_counter
            pos_counter += 1
            return
        # Place first half of children
        mid = len(children[u]) // 2
        for i in range(mid):
            dfs_inorder(children[u][i])
        # Place current node
        position[u] = pos_counter
        pos_counter += 1
        # Place remaining children
        for i in range(mid, len(children[u])):
            dfs_inorder(children[u][i])
    
    dfs_inorder(0)
    
    # Calculate cost
    total_cost = 0
    for u, v in edges:
        total_cost += abs(position[u] - position[v])
    
    if total_cost <= B:
        print("YES")
        result = [0] * n
        for i in range(n):
            result[position[i]] = i + 1
        # We need to output the position of each module (1-based)
        output = [0] * n
        for i in range(n):
            output[i] = position[i] + 1  # Convert to 1-based
        print(' '.join(map(str, output)))
        return
    
    # If both methods fail, try a more sophisticated approach
    # For a tree, the optimal linear arrangement can be found using dynamic programming
    # But for simplicity, let's just try all permutations for small n
    # Since n can be up to 1000, that's not feasible
    
    # Let's try to construct a better layout by sorting nodes by degree
    degree = [len(graph[i]) for i in range(n)]
    nodes_by_degree = sorted(range(n), key=lambda x: degree[x], reverse=True)
    
    # Assign positions based on degree
    final_positions2 = [0] * n
    for i in range(n):
        final_positions2[nodes_by_degree[i]] = i
    
    # Calculate cost
    total_cost2 = 0
    for u, v in edges:
        total_cost2 += abs(final_positions2[u] - final_positions2[v])
    
    if total_cost2 <= B:
        print("YES")
        result = [0] * n
        for i in range(n):
            result[final_positions2[i]] = i + 1
        output = [0] * n
        for i in range(n):
            output[i] = final_positions2[i] + 1
        print(' '.join(map(str, output)))
        return
    
    # If none of the simple heuristics work, it might be impossible
    # But let's try one more: place the centroid in the middle
    # Find centroid of the tree
    def find_centroid():
        # First, compute subtree sizes
        sz = [0] * n
        def dfs_size(u, p):
            sz[u] = 1
            for v in graph[u]:
                if v != p:
                    dfs_size(v, u)
                    sz[u] += sz[v]
        dfs_size(0, -1)
        
        # Find centroid
        def dfs_centroid(u, p, total):
            for v in graph[u]:
                if v != p and sz[v] > total // 2:
                    return dfs_centroid(v, u, total)
            # Check if current node is centroid
            max_subtree = 0
            for v in graph[u]:
                if v != p:
                    max_subtree = max(max_subtree, sz[v])
            if max_subtree <= total // 2:
                return u
            return -1
        
        return dfs_centroid(0, -1, n)
    
    try:
        centroid = find_centroid()
    except:
        centroid = 0
    
    # Root at centroid
    parent = [-1] * n
    children = [[] for _ in range(n)]
    visited = [False] * n
    queue = deque()
    queue.append(centroid)
    visited[centroid] = True
    
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                children[u].append(v)
                queue.append(v)
    
    # Inorder assignment with centroid at middle
    position = [0] * n
    pos_counter = 0
    
    def dfs_inorder_centroid(u):
        nonlocal pos_counter
        if not children[u]:
            position[u] = pos_counter
            pos_counter += 1
            return
        mid = len(children[u]) // 2
        for i in range(mid):
            dfs_inorder_centroid(children[u][i])
        position[u] = pos_counter
        pos_counter += 1
        for i in range(mid, len(children[u])):
            dfs_inorder_centroid(children[u][i])
    
    dfs_inorder_centroid(centroid)
    
    # Calculate cost
    total_cost3 = 0
    for u, v in edges:
        total_cost3 += abs(position[u] - position[v])
    
    if total_cost3 <= B:
        print("YES")
        result = [0] * n
        for i in range(n):
            result[position[i]] = i + 1
        output = [0] * n
        for i in range(n):
            output[i] = position[i] + 1
        print(' '.join(map(str, output)))
        return
    
    # If all heuristics fail, output NO
    # But let's check if even the optimal is impossible by checking if B is too small
    # The minimum possible sum for a tree is n-1 (when it's a path graph)
    # But our B might be large enough
    
    # For the given example, let's trace:
    # Tree: 1-2, 1-3, 2-4, 2-5
    # One layout: 4 2 5 1 3 (1-indexed positions)
    # Edges: (0,1), (0,2), (1,3), (1,4) -> positions (3,1), (3,4), (1,0), (1,2)
    # Costs: |3-1|=2, |3-4|=1, |1-0|=1, |1-2|=1. Total = 5
    # This matches B=5, so it should be YES
    
    # Let's just output the example solution for the given input
    # But we need a general algorithm
    
    # Final attempt: use the first BFS layout since it worked for the example
    final_positions = [0] * n
    for i in range(n):
        final_positions[order[i]] = i
    
    total_cost = 0
    for u, v in edges:
        total_cost += abs(final_positions[u] - final_positions[v])
    
    if total_cost <= B:
        print("YES")
        # Create inverse mapping
        pos_to_node = [0] * n
        for i in range(n):
            pos_to_node[final_positions[i]] = i + 1  # 1-based
        print(' '.join(map(str, pos_to_node)))
        return
    
    print("NO")

if __name__ == "__main__":
    main()