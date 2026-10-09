import sys
input = sys.stdin.readline

def solve():
    n, m, k = map(int, input().split())
    
    # Adjacency list for the graph
    adj = [[] for _ in range(n)]
    # Adjacency set for O(1) lookups
    adj_set = [set() for _ in range(n)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
        adj_set[u].add(v)
        adj_set[v].add(u)
    
    # Greedy heuristic: repeatedly pick the vertex with the smallest degree
    # This is a standard strategy to find a large independent set
    # We maintain degrees dynamically
    deg = [len(adj[i]) for i in range(n)]
    alive = [True] * n
    
    # We need to select n - k vertices to remove
    # The remaining k vertices will form an independent set
    removed_count = 0
    
    # Using a simple list and scanning for minimum is O(n^2) which is fine for n <= 46
    for _ in range(n):
        if removed_count == n - k:
            break
        
        # Find vertex with minimum degree among alive vertices
        min_deg = n + 1
        min_node = -1
        for i in range(n):
            if alive[i] and deg[i] < min_deg:
                min_deg = deg[i]
                min_node = i
        
        if min_node == -1:
            break
            
        # Remove this vertex
        alive[min_node] = False
        removed_count += 1
        
        # Update degrees of neighbors
        for neighbor in adj[min_node]:
            if alive[neighbor]:
                deg[neighbor] -= 1
    
    # Collect the remaining vertices
    result = [i + 1 for i in range(n) if alive[i]]
    
    # Verify the solution (safety check)
    valid = True
    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            u = result[i] - 1
            v = result[j] - 1
            if v in adj_set[u]:
                valid = False
                break
        if not valid:
            break
    
    if valid and len(result) == k:
        print("YES")
        print(' '.join(map(str, result)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()