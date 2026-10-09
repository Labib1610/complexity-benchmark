import sys
from itertools import permutations

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
    
    # Try all permutations if n is small
    if n <= 8:
        for perm in permutations(range(n)):
            total_length = 0
            for u, v in edges:
                pos_u = perm[u]
                pos_v = perm[v]
                total_length += abs(pos_u - pos_v)
                if total_length > B:
                    break
            if total_length <= B:
                print("YES")
                result = [0] * n
                for i in range(n):
                    result[perm[i]] = i + 1  # Convert back to 1-based slot numbering
                print(' '.join(map(str, [perm[i] + 1 for i in range(n)])))
                return
        print("NO")
        return
    
    # For larger n, use a greedy approach or other heuristic
    # Here we'll try a simple greedy: place nodes in order to minimize total distance
    # This is not optimal but might work for some cases
    
    # Since the graph structure isn't specified, let's try a few heuristics
    # One good heuristic for paths: place in order if it's a path graph
    # Let's check if the graph is a path
    
    # Build adjacency list
    adj = [[] for _ in range(n)]
    degree = [0] * n
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        degree[u] += 1
        degree[v] += 1
    
    # Check if it's a path graph
    leaves = [i for i in range(n) if degree[i] == 1]
    if len(leaves) == 2 and m == n - 1:
        # It's a tree and has exactly 2 leaves => it's a path
        # Find one endpoint and do BFS to get the path order
        start = leaves[0]
        queue = [start]
        visited = [False] * n
        visited[start] = True
        parent = [-1] * n
        order = []
        
        while queue:
            node = queue.pop(0)
            order.append(node)
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    parent[neighbor] = node
                    queue.append(neighbor)
        
        # Check the cost of this arrangement
        perm = order
        total_length = 0
        pos = [0] * n
        for i in range(n):
            pos[perm[i]] = i
        
        for u, v in edges:
            total_length += abs(pos[u] - pos[v])
        
        if total_length <= B:
            print("YES")
            result = [0] * n
            for i in range(n):
                result[perm[i]] = i + 1
            print(' '.join(map(str, [result[i] for i in range(n)])))
            return
    
    # If not a path or path doesn't work, try placing in sorted order by degree
    nodes = list(range(n))
    nodes.sort(key=lambda x: degree[x])
    perm = nodes
    total_length = 0
    pos = [0] * n
    for i in range(n):
        pos[perm[i]] = i
    
    for u, v in edges:
        total_length += abs(pos[u] - pos[v])
    
    if total_length <= B:
        print("YES")
        result = [0] * n
        for i in range(n):
            result[perm[i]] = i + 1
        print(' '.join(map(str, [result[i] for i in range(n)])))
        return
    
    # Try reverse order
    nodes.reverse()
    perm = nodes
    total_length = 0
    pos = [0] * n
    for i in range(n):
        pos[perm[i]] = i
    
    for u, v in edges:
        total_length += abs(pos[u] - pos[v])
    
    if total_length <= B:
        print("YES")
        result = [0] * n
        for i in range(n):
            result[perm[i]] = i + 1
        print(' '.join(map(str, [result[i] for i in range(n)])))
        return
    
    print("NO")

if __name__ == "__main__":
    main()