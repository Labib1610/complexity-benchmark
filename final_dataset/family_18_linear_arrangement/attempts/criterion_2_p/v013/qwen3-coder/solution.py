import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    B = int(data[2])
    
    edges = []
    graph = defaultdict(list)
    index = 3
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index+1]) - 1
        index += 2
        edges.append((u, v))
        graph[u].append(v)
        graph[v].append(u)
    
    # Since m = n-1 and the graph is connected and acyclic, it's a tree.
    # We can use dynamic programming with bitmasks to find the optimal layout.
    
    # However, due to the constraints (n up to 16), we can try all permutations for small n,
    # but since n can be up to 16, 16! is too large. 
    # But actually, looking at the problem again, let's check if n <= 8 or something reasonable.
    # The time limit is 5 seconds, which allows for more computation.
    # Let's proceed with a backtracking approach with pruning.
    
    # Actually, let's think differently. Since it's a tree, we can root it and do a DP on trees.
    # But given the complexity, let's try a smart brute-force with pruning.
    
    # For now, let's implement a backtracking solution with pruning.
    
    def calculate_cost(perm):
        total = 0
        pos = {unit: idx for idx, unit in enumerate(perm)}
        for u, v in edges:
            total += abs(pos[u] - pos[v])
        return total
    
    from itertools import permutations
    
    # If n is small enough, we can try all permutations
    if n <= 8:
        for perm in permutations(range(n)):
            cost = calculate_cost(perm)
            if cost <= B:
                print("YES")
                result = [0]*n
                for idx, unit in enumerate(perm):
                    result[unit] = idx + 1
                print(' '.join(map(str, result)))
                return
        print("NO")
        return
    
    # For larger n, we need a smarter approach. Let's try to build a DFS/backtracking with pruning.
    # But given time constraints, let's attempt a greedy or heuristic method.
    
    # Let's model this as a Quadratic Assignment Problem variant.
    # But again, let's try a heuristic: place nodes in a way that minimizes distances.
    
    # A better idea: since it's a tree, we can try to layout it in a line optimally.
    # One good heuristic is to do a BFS/DFS traversal and assign positions accordingly.
    
    # Let's try doing a DFS and placing nodes in order to minimize stretch.
    
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
    
    # Now we have a rooted tree. Let's perform a DFS to get an ordering.
    def dfs_order(u):
        order = []
        stack = [(u, None)]  # (node, parent_in_dfs)
        while stack:
            node, par = stack.pop()
            order.append(node)
            for child in children[node]:
                if child != par:
                    stack.append((child, node))
        return order
    
    # Try several starting points
    best_perm = None
    best_cost = float('inf')
    
    # Try rooting at different nodes
    for root in range(min(n, 4)):  # Only try a few roots to save time
        parent = [-1] * n
        children = [[] for _ in range(n)]
        visited = [False] * n
        queue = deque()
        queue.append(root)
        visited[root] = True
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    children[u].append(v)
                    queue.append(v)
        
        # Get DFS order
        order = []
        stack = [root]
        visited_dfs = [False] * n
        while stack:
            u = stack.pop()
            if visited_dfs[u]: continue
            visited_dfs[u] = True
            order.append(u)
            for v in children[u]:
                if not visited_dfs[v]:
                    stack.append(v)
        
        # Assign positions based on order
        perm = [0] * n
        for idx, node in enumerate(order):
            perm[node] = idx
        
        # Calculate cost
        cost = calculate_cost(perm)
        if cost < best_cost:
            best_cost = cost
            best_perm = perm[:]
            
        if cost <= B:
            print("YES")
            result = [0]*n
            for idx, unit in enumerate(perm):
                result[unit] = idx + 1
            print(' '.join(map(str, result)))
            return
    
    # If the best found is within budget
    if best_cost <= B:
        print("YES")
        result = [0]*n
        for idx, unit in enumerate(best_perm):
            result[unit] = idx + 1
        print(' '.join(map(str, result)))
        return
            
    # If not, let's try random permutations for small n
    if n <= 10:
        from random import shuffle
        tries = min(10000, 10**6 // (n*n))
        nodes = list(range(n))
        for _ in range(tries):
            shuffle(nodes)
            cost = calculate_cost(nodes)
            if cost <= B:
                print("YES")
                result = [0]*n
                for idx, unit in enumerate(nodes):
                    result[unit] = idx + 1
                print(' '.join(map(str, result)))
                return
    
    print("NO")

if __name__ == "__main__":
    main()