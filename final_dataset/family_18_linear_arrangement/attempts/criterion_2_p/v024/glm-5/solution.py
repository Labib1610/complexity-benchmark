import sys
sys.setrecursionlimit(200000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # Find root (node with degree 1, or node 0 if n=1)
    root = 0
    for i in range(n):
        if len(adj[i]) == 1:
            root = i
            break
    
    # Build tree structure
    children = [[] for _ in range(n)]
    parent = [-1] * n
    stack = [root]
    order = []
    parent[root] = root
    
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if v != parent[u]:
                parent[v] = u
                children[u].append(v)
                stack.append(v)
    
    # Process in reverse order (leaves first)
    order.reverse()
    
    # dp[u] = set of possible sizes for subtree rooted at u
    dp = [set() for _ in range(n)]
    
    for u in order:
        if not children[u]:
            dp[u].add(1)
        else:
            # Merge children one by one
            dp[u].add(1)
            for v in children[u]:
                new_set = set()
                for sz_u in dp[u]:
                    for sz_v in dp[v]:
                        new_set.add(sz_u + sz_v)
                dp[u] = new_set
    
    # Check if total size n is achievable
    if n not in dp[root]:
        print("NO")
        return
    
    # Reconstruct assignment
    assignment = [0] * n
    available = list(range(1, n + 1))
    
    def assign(u, avail):
        """Assign subtree rooted at u using positions in avail, return total cost"""
        if not children[u]:
            assignment[u] = avail[0]
            return 0
        
        # Find valid partition
        target = len(avail)
        for sz_u in dp[u]:
            if sz_u == target:
                break
        
        # sz_u = 1 + sum of children sizes
        # Need to partition avail into parts for each child
        # Try greedy: assign smallest positions to smallest subtrees
        
        child_sizes = []
        for v in children[u]:
            for sz_v in dp[v]:
                child_sizes.append((v, sz_v))
                break
        
        # Sort children by size (smallest first)
        child_sizes.sort(key=lambda x: x[1])
        
        # Assign position for u (median position minimizes total distance)
        # For simplicity, assign u to middle position
        pos_u = avail[(len(avail) - 1) // 2]
        assignment[u] = pos_u
        remaining = [x for x in avail if x != pos_u]
        
        total_cost = 0
        for v, sz_v in child_sizes:
            # Assign first sz_v positions to child v
            child_avail = remaining[:sz_v]
            remaining = remaining[sz_v:]
            child_cost = assign(v, child_avail)
            total_cost += child_cost + sum(abs(assignment[v] - pos_u) for _ in [1])
        
        return total_cost
    
    # Actually, let's do a cleaner reconstruction
    # Assign positions in order: process tree, assign contiguous ranges
    
    def assign_range(u, L, R):
        """Assign subtree rooted at u to positions [L, R], return total cost"""
        if L > R:
            return 0
        
        if not children[u]:
            assignment[u] = L
            return 0
        
        # Find valid partition
        target = R - L + 1
        valid_sz = None
        for sz in dp[u]:
            if sz == target:
                valid_sz = sz
                break
        
        # Assign u to a position, partition rest among children
        # For minimum cost, u should be at median of children's ranges
        # Try all valid partitions
        
        child_list = children[u]
        k = len(child_list)
        
        # Try each position for u
        best_cost = float('inf')
        best_assignment = None
        best_child_assignments = None
        
        # Get child sizes
        child_info = []
        for v in child_list:
            for sz in dp[v]:
                child_info.append((v, sz))
                break
        
        # Sort by size for deterministic partitioning
        child_info.sort(key=lambda x: x[1])
        sizes = [sz for v, sz in child_info]
        nodes = [v for v, sz in child_info]
        
        # Try each position for u
        for pos_u in range(L, R + 1):
            # Remaining positions
            remaining = [x for x in range(L, R + 1) if x != pos_u]
            if len(remaining) != sum(sizes):
                continue
            
            # Partition remaining positions
            idx = 0
            valid = True
            total_cost = 0
            child_ranges = []
            
            for i, (v, sz) in enumerate(child_info):
                if sz in dp[v]:
                    child_L = remaining[idx]
                    child_R = remaining[idx + sz - 1]
                    child_ranges.append((v, child_L, child_R))
                    idx += sz
                else:
                    valid = False
                    break
            
            if not valid:
                continue
            
            # Calculate cost
            total_cost = 0
            for v, cL, cR in child_ranges:
                total_cost += assign_range(v, cL, cR)
                total_cost += abs(assignment[v] - pos_u)
            
            if total_cost < best_cost:
                best_cost = total_cost
                best_assignment = pos_u
                best_child_assignments = child_ranges
        
        if best_assignment is not None:
            assignment[u] = best_assignment
            for v, cL, cR in best_child_assignments:
                pass  # Already assigned in recursive calls
            return best_cost
        
        return float('inf')
    
    # Simpler approach: assign positions greedily
    # Use DFS order and assign positions to minimize cost
    
    def get_subtree_size(u, p):
        sz = 1
        for v in adj[u]:
            if v != p:
                sz += get_subtree_size(v, u)
        return sz
    
    def assign_greedy(u, p, positions):
        """Assign subtree rooted at u using given positions"""
        if not positions:
            return 0
        
        positions.sort()
        assignment[u] = positions[len(positions) // 2]  # Median position
        
        total_cost = 0
        remaining = [x for x in positions if x != assignment[u]]
        
        for v in adj[u]:
            if v != p:
                child_sz = get_subtree_size(v, u)
                # Assign first child_sz positions
                child_positions = remaining[:child_sz]
                remaining = remaining[child_sz:]
                child_cost = assign_greedy(v, u, child_positions)
                total_cost += child_cost + abs(assignment[v] - assignment[u])
        
        return total_cost
    
    # Use greedy assignment
    positions = list(range(1, n + 1))
    total_cost = assign_greedy(root, -1, positions)
    
    if total_cost <= B:
        print("YES")
        print(' '.join(map(str, assignment)))
    else:
        print("NO")

solve()