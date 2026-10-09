import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1000000)
    
    n, m, B = map(int, sys.stdin.readline().split())
    
    # Build adjacency list for the tree
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Find the root (any node can be root since it's a tree)
    # We'll use node 1 as root for consistency
    root = 1
    
    # Build parent relationships and children list via BFS
    parent = {root: None}
    children = defaultdict(list)
    queue = deque([root])
    
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if v not in parent:
                parent[v] = u
                children[u].append(v)
                queue.append(v)
    
    # Try all permutations? No, that's too slow for large n
    # We need a smarter approach
    
    # Since it's a tree, we can use dynamic programming or branch and bound
    # But given the constraints, let's try a heuristic or small-exact approach
    
    # For small n (n <= 8 or so), we can try all permutations
    # But n can be up to 1000, so we need something better
    
    # Let's try a greedy approach:
    # Place the root somewhere, then place children to minimize total length
    
    # Actually, let's try a different approach:
    # Since it's a tree, we can do a post-order traversal and for each subtree,
    # try to find the best interval to place it.
    
    # But that's complex. Let's try a simpler idea:
    # Use branch and bound with pruning.
    
    # For now, let's implement a backtracking solution with pruning
    
    # But even that might be too slow. Let's think of the structure.
    
    # The tree is small in the example (n=5), so maybe intended for small inputs.
    # But time limit is 5s, so maybe larger inputs are possible.
    
    # Let's try a recursive backtracking with memoization
    
    # First, let's see if we can model this as placing nodes on a line
    # to minimize sum of distances for edges.
    
    # This is similar to the "minimum linear arrangement" problem, which is NP-hard.
    # But we have a tree, and a budget.
    
    # Let's try a branch-and-bound approach
    
    # We'll represent a partial assignment as a list where position[i] = node at position i+1
    # or None if not assigned yet.
    
    # But let's think of constraints:
    # Each node must be placed exactly once.
    # The sum of edge lengths must be <= B.
    
    # Let's try a recursive backtracking:
    # At each step, pick an unplaced node and try placing it in each available position,
    # keeping track of current cost.
    
    # But we need to be smart about the order of placing nodes.
    # Maybe place nodes in BFS order from root?
    
    # Let's try placing nodes one by one in all possible positions, with pruning.
    
    # To make it faster, let's compute a lower bound at each step.
    
    # But first, let's handle the small case properly.
    
    # Let's try a different approach: since n can be up to 1000, but 5s time limit,
    # maybe intended solution is O(n^2) or O(n^3).
    
    # Wait, let's re-read: "The reporting relationships between units form a strict hierarchy"
    # So it's a rooted tree.
    
    # Let's try to model this properly.
    
    # Idea: Use a greedy embedding or dynamic programming on the tree structure.
    
    # For a tree, there are known algorithms for minimum linear arrangement.
    # But let's try a simpler approach.
    
    # Let's do a DFS and try to place subtrees consecutively.
    
    # But that's not guaranteed to be optimal.
    
    # Let's try a backtracking solution for small n, and see if it passes.
    
    # Actually, let's think of the example:
    # Tree: 1-2, 1-3, 3-4, 3-5
    # Output: 4 5 3 1 2
    # Positions: 1 2 3 4 5
    #           4 5 3 1 2
    # So node 4 at pos 1, node 5 at pos 2, node 3 at pos 3, node 1 at pos 4, node 2 at pos 5
    # Edges:
    # (1,2): pos 4 to 5 -> distance 1
    # (1,3): pos 4 to 3 -> distance 1
    # (3,4): pos 3 to 1 -> distance 2
    # (3,5): pos 3 to 2 -> distance 1
    # Total: 5
    
    # So it's possible.
    
    # Let's implement a backtracking solution.
    
    # But to make it efficient, let's:
    # 1. Try placing nodes in a smart order (e.g., BFS from root)
    # 2. Keep track of current total cost
    # 3. Prune if current cost > B
    # 4. Precompute all edges
    
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
    
    # Re-read edges to list
    sys.stdin.seek(0)
    n, m, B = map(int, sys.stdin.readline().split())
    edges = []
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
    
    # Build tree structure with root
    root = 1
    parent = {root: None}
    children = defaultdict(list)
    queue = deque([root])
    
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if v not in parent:
                parent[v] = u
                children[u].append(v)
                queue.append(v)
    
    # Get all nodes
    nodes = list(range(1, n+1))
    
    # Try all permutations for small n
    if n <= 8:
        import itertools
        for perm in itertools.permutations(nodes):
            pos = {node: i for i, node in enumerate(perm)}
            total = 0
            for u, v in edges:
                total += abs(pos[u] - pos[v])
            if total <= B:
                print("YES")
                print(' '.join(map(str, [perm.index(i)+1 for i in nodes])))
                return
        print("NO")
        return
    
    # For larger n, we need a better approach
    # Let's try a greedy embedding or local search
    
    # Simple greedy: start with root in the middle, place children greedily
    
    # But let's try a more systematic approach: branch and bound
    
    # This is getting complex. Let's see if there's a simpler way.
    
    # Since it's a tree, one approach is to do a DFS and place subtrees optimally.
    # But that requires solving subproblems.
    
    # Let's try a different idea: since the time limit is 5s, maybe a smart backtracking works.
    
    # Let's implement a backtracking that places nodes one by one.
    
    # To make it faster:
    # 1. Place nodes in BFS order
    # 2. For each node, try all unoccupied positions
    # 3. Keep a running cost and prune if it exceeds B
    
    # Get BFS ordering
    bfs_order = []
    visited = set()
    queue = deque([root])
    visited.add(root)
    
    while queue:
        u = queue.popleft()
        bfs_order.append(u)
        for v in adj[u]:
            if v not in visited:
                visited.add(v)
                queue.append(v)
    
    # Backtracking function
    position = [0] * (n + 1)  # position[i] = position of node i
    placed = [False] * (n + 1)
    best_cost = [float('inf')]
    result = [None]
    
    def calculate_current_cost():
        cost = 0
        for u, v in edges:
            if position[u] > 0 and position[v] > 0:
                cost += abs(position[u] - position[v])
        return cost
    
    def backtrack(idx):
        if idx == n:
            cost = calculate_current_cost()
            if cost <= B:
                best_cost[0] = cost
                result[0] = position[1:]
            return
        
        node = bfs_order[idx]
        current_cost = calculate_current_cost()
        if current_cost > B:
            return
            
        for pos in range(1, n + 1):
            if not placed[pos]:
                position[node] = pos
                placed[pos] = True
                backtrack(idx + 1)
                placed[pos] = False
                position[node] = 0
    
    # This is still O(n!), too slow.
    
    # Let's try a smarter pruning or a different approach.
    
    # Since the problem is to find any solution within budget,
    # we can try a greedy embedding or local search.
    
    # Let's try a simple greedy:
    # 1. Place root in the middle
    # 2. For each child, place it adjacent to its parent if possible
    
    def greedy_embedding():
        pos = [-1] * (n + 1)
        used = [False] * (n + 1)
        
        # Place root in the middle
        root_pos = (n + 1) // 2
        pos[root] = root_pos
        used[root_pos] = True
        
        # BFS to place children
        queue = deque([root])
        placed = {root}
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if v not in placed:
                    # Find best adjacent free spot
                    best_pos = -1
                    best_dist = float('inf')
                    for p in range(1, n + 1):
                        if not used[p]:
                            dist = abs(p - pos[u])
                            if dist < best_dist:
                                best_dist = dist
                                best_pos = p
                    if best_pos != -1:
                        pos[v] = best_pos
                        used[best_pos] = True
                        placed.add(v)
                        queue.append(v)
        
        # Check if all placed
        if len(placed) != n:
            return None
            
        # Calculate cost
        total = 0
        for u, v in edges:
            total += abs(pos[u] - pos[v])
            
        if total <= B:
            # Create permutation
            perm = [0] * n
            for node in range(1, n + 1):
                perm[pos[node] - 1] = node
            return perm
        return None
    
    # Try greedy
    greedy_result = greedy_embedding()
    if greedy_result:
        print("YES")
        # Convert to required format: for each node 1..n, give its position
        node_to_pos = {node: i+1 for i, node in enumerate(greedy_result)}
        print(' '.join(str(node_to_pos[i]) for i in range(1, n + 1)))
        return
    
    # If greedy fails, try more exhaustive search for small n
    if n <= 10:
        import itertools
        for perm in itertools.permutations(range(1, n + 1)):
            pos_map = {node: i+1 for i, node in enumerate(perm)}
            total = 0
            for u, v in edges:
                total += abs(pos_map[u] - pos_map[v])
            if total <= B:
                print("YES")
                print(' '.join(map(str, perm)))
                return
        print("NO")
        return
        
    # For larger n, this problem is hard. Let's try one more heuristic.
    
    # Try placing in order of decreasing degree?
    degrees = [(len(adj[i]), i) for i in range(1, n + 1)]
    degrees.sort(reverse=True)
    degree_order = [i for _, i in degrees]
    
    def heuristic_embedding(order):
        pos = [-1] * (n + 1)
        used = [False] * (n + 1)
        
        # Place first node in the middle
        first = order[0]
        root_pos = (n + 1) // 2
        pos[first] = root_pos
        used[root_pos] = True
        placed = {first}
        
        # Place rest one by one
        for node in order[1:]:
            # Find best position adjacent to any already placed neighbor
            best_pos = -1
            best_dist = float('inf')
            for u in adj[node]:
                if u in placed:
                    for p in range(1, n + 1):
                        if not used[p]:
                            dist = abs(p - pos[u])
                            if dist < best_dist:
                                best_dist = dist
                                best_pos = p
            if best_pos == -1:
                # No neighbor placed, find any free spot
                for p in range(1, n + 1):
                    if not used[p]:
                        best_pos = p
                        break
            if best_pos != -1:
                pos[node] = best_pos
                used[best_pos] = True
                placed.add(node)
        
        if len(placed) != n:
            return None
            
        total = 0
        for u, v in edges:
            total += abs(pos[u] - pos[v])
            
        if total <= B:
            perm = [0] * n
            for node in range(1, n + 1):
                perm[pos[node] - 1] = node
            return perm
        return None
    
    # Try degree-based heuristic
    heuristic_result = heuristic_embedding(degree_order)
    if heuristic_result:
        print("YES")
        node_to_pos = {node: i+1 for i, node in enumerate(heuristic_result)}
        print(' '.join(str(node_to_pos[i]) for i in range(1, n + 1)))
        return
        
    print("NO")

if __name__ == "__main__":
    main()