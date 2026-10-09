import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    B = int(data[2])
    
    edges = []
    index = 3
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-based indexing
        v = int(data[index+1]) - 1
        edges.append((u, v))
        index += 2
    
    # We need to find a permutation of nodes 0..n-1 such that 
    # sum of |perm[u] - perm[v]| over all edges (u,v) is <= B
    
    # Since the graph is a tree (n nodes, n-1 edges, connected), we can use DFS to get a BFS ordering
    # which often gives a good layout. But since n<=16, we can try all permutations.
    
    # However, let's first try a greedy approach:
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Try to build a BFS-like layout starting from the node with highest degree
    degrees = [len(adj[i]) for i in range(n)]
    max_degree = max(degrees)
    start_node = degrees.index(max_degree)
    
    # BFS ordering
    from collections import deque
    queue = deque()
    visited = [False]*n
    order = []
    queue.append(start_node)
    visited[start_node] = True
    order.append(start_node)
    
    while queue:
        node = queue.popleft()
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                order.append(neighbor)
    
    # Assign positions based on BFS order
    perm_bfs = [-1]*n
    for i in range(n):
        perm_bfs[order[i]] = i+1  # Positions 1 to n
    
    # Calculate cost for BFS assignment
    def calculate_cost(perm):
        cost = 0
        for u, v in edges:
            pos_u = perm[u]
            pos_v = perm[v]
            cost += abs(pos_u - pos_v)
        return cost
    
    cost_bfs = calculate_cost(perm_bfs)
    
    if cost_bfs <= B:
        print("YES")
        print(' '.join(map(str, perm_bfs)))
        return
    
    # If BFS doesn't work, try all permutations for small n
    if n <= 8:  # Only feasible for very small n
        import itertools
        for p in itertools.permutations(range(1, n+1)):
            perm_test = list(p)
            mapping = [0]*n
            for i in range(n):
                mapping[order[i]] = perm_test[i]
            
            cost = calculate_cost(mapping)
            if cost <= B:
                print("YES")
                print(' '.join(map(str, mapping)))
                return
    
    # For larger n, we might need more sophisticated approaches
    # Let's try a few random permutations
    import random
    random.seed(42)  # For reproducibility
    
    for _ in range(10000):
        perm_list = list(range(1, n+1))
        random.shuffle(perm_list)
        mapping = [0]*n
        for i in range(n):
            mapping[order[i]] = perm_list[i]
        
        cost = calculate_cost(mapping)
        if cost <= B:
            print("YES")
            print(' '.join(map(str, mapping)))
            return
    
    print("NO")

if __name__ == "__main__":
    main()