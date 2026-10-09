import sys
from collections import defaultdict, deque

def main():
    import sys
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
    degree = [0] * (n + 1)
    
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        edges.append((u, v))
        graph[u].append(v)
        graph[v].append(u)
        degree[u] += 1
        degree[v] += 1
    
    # Since m = n - 1 and it's a tree (as per problem statement), we can perform BFS/DFS to get a traversal order
    # We'll root the tree at node 1 and build a BFS ordering
    visited = [False] * (n + 1)
    queue = deque()
    queue.append(1)
    visited[1] = True
    order = []
    
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    # Now assign positions greedily based on BFS order
    # Assign the root to position (n+1)//2 to minimize distances
    pos = [0] * (n + 1)
    current_pos = 1
    
    # Assign positions in BFS order
    for node in order:
        pos[node] = current_pos
        current_pos += 1
    
    # Calculate total degradation
    total_degradation = 0
    for u, v in edges:
        total_degradation += abs(pos[u] - pos[v])
    
    if total_degradation <= B:
        print("YES")
        result = []
        for i in range(1, n + 1):
            result.append(str(pos[i]))
        print(' '.join(result))
        return
    
    # Try another approach: place nodes on a line minimizing total distance
    # Use DFS to create a linear arrangement
    visited = [False] * (n + 1)
    linear_order = []
    
    def dfs(u):
        visited[u] = True
        linear_order.append(u)
        for v in graph[u]:
            if not visited[v]:
                dfs(v)
                
    dfs(1)
    
    # Assign positions 1 to n in this order
    pos = [0] * (n + 1)
    for i in range(n):
        pos[linear_order[i]] = i + 1
        
    total_degradation = 0
    for u, v in edges:
        total_degradation += abs(pos[u] - pos[v])
        
    if total_degradation <= B:
        print("YES")
        result = []
        for i in range(1, n + 1):
            result.append(str(pos[i]))
        print(' '.join(result))
        return
        
    # If still not working, try reversing the order
    pos = [0] * (n + 1)
    for i in range(n):
        pos[linear_order[i]] = n - i
        
    total_degradation = 0
    for u, v in edges:
        total_degradation += abs(pos[u] - pos[v])
        
    if total_degradation <= B:
        print("YES")
        result = []
        for i in range(1, n + 1):
            result.append(str(pos[i]))
        print(' '.join(result))
        return
    
    # As a last resort, check if there's any valid permutation by trying a simple sorted assignment
    # But since time complexity matters, let's just output NO if none of the above worked
    # However, given the constraints and guarantees, one of the above should work
    
    # Let's try placing them optimally using a greedy method
    # Root at node with highest degree
    max_degree = 0
    root = 1
    for i in range(1, n+1):
        if degree[i] > max_degree:
            max_degree = degree[i]
            root = i
            
    visited = [False] * (n + 1)
    linear_order = []
    
    def dfs_root(u):
        visited[u] = True
        linear_order.append(u)
        for v in graph[u]:
            if not visited[v]:
                dfs_root(v)
                
    dfs_root(root)
    
    pos = [0] * (n + 1)
    for i in range(n):
        pos[linear_order[i]] = i + 1
        
    total_degradation = 0
    for u, v in edges:
        total_degradation += abs(pos[u] - pos[v])
        
    if total_degradation <= B:
        print("YES")
        result = []
        for i in range(1, n + 1):
            result.append(str(pos[i]))
        print(' '.join(result))
        return
    
    print("NO")

if __name__ == "__main__":
    main()