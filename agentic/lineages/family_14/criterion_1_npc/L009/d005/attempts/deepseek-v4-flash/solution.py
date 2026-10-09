import sys

def main():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    targets = list(map(int, input().split()))
    target_set = set(targets)
    
    # Use a large number for missing edges
    INF = 10**18
    # adjacency matrix for min edge cost
    min_cost = [[INF] * (n+1) for _ in range(n+1)]
    
    for _ in range(m):
        u, v, w = map(int, input().split())
        if w < min_cost[u][v]:
            min_cost[u][v] = w
            min_cost[v][u] = w
    
    # Build edge list
    edges = []
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if min_cost[i][j] != INF:
                edges.append((min_cost[i][j], i, j))
    
    edges.sort()
    
    parent = list(range(n+1))
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[ry] = rx
            return True
        return False
    
    # Initially each target is its own component
    # We'll union all targets together using edges until they are all connected
    total_cost = 0
    edges_used = 0
    target_count = len(targets)
    
    for w, u, v in edges:
        if find(u) != find(v):
            # Check if this edge connects two components that each contain at least one target
            # We can just union and then check if all targets are connected
            union(u, v)
            total_cost += w
            edges_used += 1
            # Check if all targets are in the same component
            root = find(targets[0])
            all_connected = True
            for tgt in targets:
                if find(tgt) != root:
                    all_connected = False
                    break
            if all_connected:
                print(total_cost)
                return
    
    # If not all connected (shouldn't happen per problem guarantee)
    print(total_cost)

if __name__ == "__main__":
    main()