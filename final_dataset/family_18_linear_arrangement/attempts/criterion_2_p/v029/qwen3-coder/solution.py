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
    
    if m != n - 1:
        print("NO")
        return
    
    # Build adjacency list for the tree
    adj = defaultdict(list)
    for _ in range(m):
        u = int(data[idx]) - 1  # Convert to 0-indexed
        idx += 1
        v = int(data[idx]) - 1
        idx += 1
        adj[u].append(v)
        adj[v].append(u)
    
    # Find the center of the tree
    # First, find one end of the diameter
    def bfs_farthest(start):
        visited = [False] * n
        queue = deque()
        queue.append((start, 0))
        visited[start] = True
        farthest_node = start
        max_dist = 0
        parent = [-1] * n
        
        while queue:
            node, dist = queue.popleft()
            if dist > max_dist:
                max_dist = dist
                farthest_node = node
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    parent[neighbor] = node
                    queue.append((neighbor, dist + 1))
        return farthest_node, parent
    
    # Find one end of the diameter
    end1, _ = bfs_farthest(0)
    # Find the other end and get parent array
    end2, parent = bfs_farthest(end1)
    
    # Reconstruct the diameter path
    diameter_path = []
    current = end2
    while current != -1:
        diameter_path.append(current)
        current = parent[current]
    
    diameter_path.reverse()
    d = len(diameter_path) - 1  # diameter length
    
    # If diameter > B, impossible
    if d > B:
        print("NO")
        return
    
    # Place the diameter path on a contiguous segment of the line
    # Try to place it optimally to minimize total cost
    
    # The optimal placement of the diameter path of length d on line of length n:
    # Place it starting at position s, ending at s+d
    # The positions are s, s+1, ..., s+d
    
    # To minimize the cost of attaching the rest of the tree, we should place
    # the diameter in the middle of the line if possible.
    
    # But we also need to compute the total cost.
    
    # Let's root the tree at the center of the diameter
    center_idx = len(diameter_path) // 2
    root = diameter_path[center_idx]
    
    # Build tree rooted at 'root'
    tree = defaultdict(list)
    visited = [False] * n
    queue = deque()
    queue.append(root)
    visited[root] = True
    
    while queue:
        node = queue.popleft()
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                tree[node].append(neighbor)
                queue.append(neighbor)
    
    # Compute subtree sizes
    subtree_size = [0] * n
    
    def dfs_size(u):
        size = 1
        for v in tree[u]:
            size += dfs_size(v)
        subtree_size[u] = size
        return size
    
    dfs_size(root)
    
    # Now, we need to assign positions to nodes to minimize total cost
    # We'll place the diameter path optimally and then hang the subtrees
    
    # Let's try placing the diameter path centered on the line
    # Positions are 0 to n-1
    positions = [-1] * n
    
    # Place diameter path
    start_pos = (n - 1 - d) // 2
    for i in range(len(diameter_path)):
        positions[diameter_path[i]] = start_pos + i
    
    # Now, assign positions to the rest of the nodes via DFS
    # For each node not on diameter, we assign it a position
    # We'll do a DFS from each node on the diameter to assign positions to its subtree
    
    # Nodes on diameter
    on_diameter = set(diameter_path)
    
    def assign_positions(u, min_pos, max_pos):
        # Assign positions to subtree rooted at u
        # u already has a position
        my_pos = positions[u]
        # Assign positions to children
        children = tree[u]
        # We need to place children in the ranges [min_pos, my_pos-1] and [my_pos+1, max_pos]
        # We'll place them greedily to minimize cost
        # For now, let's do a simple assignment: place them consecutively
        
        # Collect all nodes in subtree
        def collect_subtree(v):
            nodes = [v]
            for w in tree[v]:
                nodes.extend(collect_subtree(w))
            return nodes
        
        # For each child, determine which side to place it
        left_nodes = []
        right_nodes = []
        
        # We'll place left children in decreasing order from my_pos-1 down
        # and right children in increasing order from my_pos+1 up
        
        # To minimize cost, we should place larger subtrees closer
        # Sort children by subtree size descending
        children_sorted = sorted(children, key=lambda x: subtree_size[x], reverse=True)
        
        # Alternate placing on left and right, starting with the side that has more room
        left_room = my_pos - min_pos
        right_room = max_pos - my_pos
        
        # Assign sides to children
        left_list = []
        right_list = []
        
        for child in children_sorted:
            # Assign to side with more room
            if left_room > right_room:
                left_list.append(child)
                left_room -= subtree_size[child]
            else:
                right_list.append(child)
                right_room -= subtree_size[child]
        
        # Assign positions to left children
        pos = my_pos - 1
        stack_list = []
        for child in left_list:
            nodes_in_subtree = collect_subtree(child)
            stack_list.append((child, pos - len(nodes_in_subtree) + 1, pos))
            pos -= len(nodes_in_subtree)
        
        # Assign positions to right children
        pos = my_pos + 1
        for child in right_list:
            nodes_in_subtree = collect_subtree(child)
            stack_list.append((child, pos, pos + len(nodes_in_subtree) - 1))
            pos += len(nodes_in_subtree)
            
        # Process subtrees
        while stack_list:
            u_sub, min_p, max_p = stack_list.pop()
            # Assign position to u_sub (e.g., middle of range)
            positions[u_sub] = (min_p + max_p) // 2
            nodes_sub = collect_subtree(u_sub)
            # Sort nodes by some order and assign consecutive positions
            # Simple approach: assign consecutive positions starting from min_p
            sorted_nodes = sorted(nodes_sub, key=lambda x: subtree_size[x], reverse=True)
            # Actually, let's just assign them consecutively
            for i, node in enumerate(nodes_sub):
                if positions[node] == -1:
                    # Find a free position
                    for p in range(min_p, max_p + 1):
                        if p not in positions:
                            positions[node] = p
                            break
            # This is getting complex. Let's use a different approach.
            
        # Simpler approach: do DFS and assign positions greedily
        def dfs_assign(v, start_p, direction):
            # direction: -1 for left, 1 for right
            pos_v = start_p
            positions[v] = pos_v
            children_v = tree[v]
            if direction == -1:
                # Assign children to the left
                next_pos = pos_v - 1
                for child in children_v:
                    dfs_assign(child, next_pos, -1)
                    # Update next_pos based on size of subtree
                    next_pos -= subtree_size[child]
            else:
                # Assign children to the right
                next_pos = pos_v + 1
                for child in children_v:
                    dfs_assign(child, next_pos, 1)
                    next_pos += subtree_size[child]
        
        # This is still complex. Let's think differently.
        
    # Let's try a simpler greedy approach:
    # 1. Place the diameter path in the middle
    # 2. For each node on diameter, assign positions to its subtrees
    
    # Re-initialize positions
    positions = [-1] * n
    
    # Place diameter path centered
    start_pos = (n - d - 1) // 2  # 0-based indexing
    for i in range(len(diameter_path)):
        positions[diameter_path[i]] = start_pos + i
    
    # For each node on diameter, assign positions to children not on diameter
    def assign_subtree(u, start_position, step):
        # Assign positions to subtree rooted at u, starting from start_position
        # step is +1 or -1
        queue_assign = deque()
        queue_assign.append((u, start_position, step))
        assigned = set([u])
        
        while queue_assign:
            node, pos_start, step_dir = queue_assign.popleft()
            children = [v for v in tree[node] if positions[v] == -1]
            current_pos = pos_start
            for child in children:
                positions[child] = current_pos
                assigned.add(child)
                # Add grandchildren to queue
                grandchildren = [v for v in tree[child] if positions[v] == -1]
                if grandchildren:
                    queue_assign.append((child, current_pos + step_dir, step_dir))
                current_pos += step_dir * len(grandchildren)
    
    # Assign positions to subtrees of nodes on diameter
    for i in range(len(diameter_path)):
        u = diameter_path[i]
        pos_u = positions[u]
        children = tree[u]
        # Children not on diameter
        off_diameter_children = [v for v in children if v not in on_diameter]
        
        # Assign to left and right
        left_start = pos_u - 1
        right_start = pos_u + 1
        left_count = 0
        right_count = 0
        
        # Alternate or assign based on subtree size
        off_sorted = sorted(off_diameter_children, key=lambda x: subtree_size[x], reverse=True)
        left = True
        for child in off_sorted:
            if left:
                # Assign to left
                # Simple: just mark position and do DFS
                queue_dfs = deque()
                queue_dfs.append((child, left_start - left_count))
                while queue_dfs:
                    node, pos = queue_dfs.popleft()
                    if positions[node] == -1:
                        positions[node] = pos
                        # Assign children
                        child_nodes = tree[node]
                        for j, ch in enumerate(child_nodes):
                            if positions[ch] == -1:
                                queue_dfs.append((ch, pos - 1 - j))
                left_count += subtree_size[child]
            else:
                # Assign to right
                queue_dfs = deque()
                queue_dfs.append((child, right_start + right_count))
                while queue_dfs:
                    node, pos = queue_dfs.popleft()
                    if positions[node] == -1:
                        positions[node] = pos
                        # Assign children
                        child_nodes = tree[node]
                        for j, ch in enumerate(child_nodes):
                            if positions[ch] == -1:
                                queue_dfs.append((ch, pos + 1 + j))
                right_count += subtree_size[child]
            left = not left
    
    # Check if all positions assigned and valid
    if -1 in positions:
        print("NO")
        return
        
    # Convert positions to 1-based
    pos_1based = [p + 1 for p in positions]
    
    # Calculate total cost
    total_cost = 0
    for u in range(n):
        for v in adj[u]:
            if u < v:  # Count each edge once
                total_cost += abs(positions[u] - positions[v])
    
    if total_cost <= B:
        print("YES")
        print(' '.join(map(str, pos_1based)))
    else:
        # Try a different approach: greedy linear arrangement
        # Place nodes to minimize total edge length
        # This is the Minimum Linear Arrangement problem, which is NP-hard
        # But for trees, there are polynomial algorithms
        
        # Let's try a simpler greedy method
        # DFS and place children consecutively
        
        positions_greedy = [-1] * n
        # Find a leaf to start
        degrees = [len(adj[i]) for i in range(n)]
        start_node = 0
        for i in range(n):
            if degrees[i] == 1:
                start_node = i
                break
        
        # DFS placement
        def dfs_place(u, pos, used):
            positions_greedy[u] = pos
            used.add(u)
            next_pos = pos + 1
            for v in adj[u]:
                if v not in used:
                    dfs_place(v, next_pos, used)
                    next_pos += 1
        
        used_set = set()
        dfs_place(start_node, 0, used_set)
        
        # Calculate cost
        total_cost_greedy = 0
        for u in range(n):
            for v in adj[u]:
                if u < v:
                    total_cost_greedy += abs(positions_greedy[u] - positions_greedy[v])
        
        if total_cost_greedy <= B:
            # Convert to 1-based
            pos_1based_greedy = [p + 1 for p in positions_greedy]
            print("YES")
            print(' '.join(map(str, pos_1based_greedy)))
        else:
            print("NO")

if __name__ == "__main__":
    main()