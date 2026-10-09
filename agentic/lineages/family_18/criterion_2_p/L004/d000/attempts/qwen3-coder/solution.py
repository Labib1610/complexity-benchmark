import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1000000)
    
    n, m, B = map(int, sys.stdin.readline().split())
    
    # Build adjacency list
    adj = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # Since m = n-1 and graph is connected, it's a tree
    # We need to find a layout (permutation) of nodes on a line such that
    # sum of |position[u] - position[v]| over all edges <= B
    
    # Try all possible layouts? No, that's n! which is too large
    # Instead, we can try to find an optimal layout
    
    # For trees, one approach is to do a DFS and try to layout in a way that minimizes total distance
    # But even better, since we're laying out on a line, this is essentially finding an optimal linear arrangement
    # This is NP-hard in general, but for small n we might be able to enumerate
    
    # Let's try a backtracking approach with pruning
    
    def calculate_cost(perm):
        pos = {module: idx for idx, module in enumerate(perm)}
        total = 0
        for u, v in edges:
            total += abs(pos[u] - pos[v])
        return total
    
    # For small n, we can try all permutations
    if n <= 8:
        from itertools import permutations
        for perm in permutations(range(1, n+1)):
            cost = calculate_cost(perm)
            if cost <= B:
                print("YES")
                print(*perm)
                return
        print("NO")
        return
    
    # For larger n, we need a heuristic
    # One good heuristic is to root the tree and do a BFS/DFS ordering
    # Or do a centroid decomposition kind of approach
    
    # Let's try rooting at each node and doing a DFS traversal
    def dfs_order(start):
        order = []
        visited = [False] * (n+1)
        stack = [start]
        visited[start] = True
        while stack:
            node = stack.pop()
            order.append(node)
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)
        return order
    
    # Try BFS order as well
    def bfs_order(start):
        order = []
        visited = [False] * (n+1)
        queue = deque([start])
        visited[start] = True
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return order
    
    best_order = None
    best_cost = float('inf')
    
    # Try different starting points
    for start_node in range(1, min(n+1, 10)):  # Limit to avoid too much computation
        # DFS order
        order1 = dfs_order(start_node)
        cost1 = calculate_cost(order1)
        if cost1 <= B:
            print("YES")
            print(*order1)
            return
        if cost1 < best_cost:
            best_cost = cost1
            best_order = order1
            
        # BFS order  
        order2 = bfs_order(start_node)
        cost2 = calculate_cost(order2)
        if cost2 <= B:
            print("YES")
            print(*order2)
            return
        if cost2 < best_cost:
            best_cost = cost2
            best_order = order2
    
    # If none work, try reverse order
    if best_order:
        rev_order = best_order[::-1]
        rev_cost = calculate_cost(rev_order)
        if rev_cost <= B:
            print("YES")
            print(*rev_order)
            return
        if rev_cost < best_cost:
            best_cost = rev_cost
            best_order = rev_order
    
    # Still not working, let's try a more sophisticated approach
    # Try to find a path that includes all nodes (Hamiltonian path approximation)
    # For trees, there's always a Hamiltonian path
    
    def find_hamiltonian_path():
        # Find a leaf to start
        leaves = [node for node in range(1, n+1) if len(adj[node]) == 1]
        if not leaves:
            # Only happens when n=1
            return [1] if n == 1 else []
            
        start = leaves[0]
        visited = [False] * (n+1)
        path = []
        
        def build_path(node):
            visited[node] = True
            path.append(node)
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    build_path(neighbor)
                    
        build_path(start)
        return path
    
    ham_path = find_hamiltonian_path()
    if ham_path:
        ham_cost = calculate_cost(ham_path)
        if ham_cost <= B:
            print("YES")
            print(*ham_path)
            return
        
        # Try reverse
        rev_ham = ham_path[::-1]
        rev_ham_cost = calculate_cost(rev_ham)
        if rev_ham_cost <= B:
            print("YES")
            print(*rev_ham)
            return
    
    print("NO")

if __name__ == "__main__":
    main()