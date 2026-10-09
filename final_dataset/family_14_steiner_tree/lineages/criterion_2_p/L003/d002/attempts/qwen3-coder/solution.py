import sys
from collections import defaultdict, deque

def find_path_edges(graph, start, end, n):
    # BFS to find the unique path between start and end in tree
    parent = [-1] * (n + 1)
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        if node == end:
            break
        for neighbor, weight in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = node
                queue.append(neighbor)
    
    # Reconstruct path edges
    path_edges = []
    current = end
    while parent[current] != -1:
        prev = parent[current]
        # Find the weight of edge between prev and current
        for neighbor, weight in graph[prev]:
            if neighbor == current:
                path_edges.append(weight)
                break
        current = prev
    
    return path_edges

def main():
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    t = int(data[idx])
    idx += 1
    
    critical = list(map(int, data[idx:idx+t]))
    idx += t
    
    # Build graph
    graph = defaultdict(list)
    edges = []
    
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        
        graph[u].append((v, w))
        graph[v].append((u, w))
        edges.append((u, v, w))
    
    if t <= 1:
        print(0)
        return
    
    # For each pair of critical nodes, find the path and collect edge weights
    edge_count = defaultdict(int)
    
    for i in range(t):
        for j in range(i + 1, t):
            # Find path between critical[i] and critical[j]
            path_edges = find_path_edges(graph, critical[i], critical[j], n)
            # Add each edge in this path to our count
            for weight in path_edges:
                edge_count[weight] += 1
    
    # Calculate minimum cost - we need to include enough edges to connect all critical nodes
    # In a tree, to connect k nodes, we need exactly k-1 edges in the minimal subtree
    # The minimum cost is the sum of the k-1 smallest edge weights in the paths
    
    # But we need to be more careful - we want the minimum cost to connect all critical nodes
    # This is equivalent to finding the minimum spanning tree of the induced subgraph
    # However, since we're in a tree, the MST is unique and consists of the paths between nodes
    
    # A simpler approach: each edge in the tree has a certain "importance" - how many 
    # critical node pairs need it. We want to minimize the total cost, so we don't 
    # exclude any necessary edges. All edges that lie on paths between critical nodes 
    # must be included.
    
    total_cost = 0
    for weight, count in edge_count.items():
        if count > 0:
            total_cost += weight
    
    print(total_cost)

if __name__ == "__main__":
    main()