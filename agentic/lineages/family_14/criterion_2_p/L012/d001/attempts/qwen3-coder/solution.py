import sys
from collections import defaultdict, deque

def find_path_edges(graph, start, end, n):
    if start == end:
        return []
    
    visited = [False] * (n + 1)
    parent = [-1] * (n + 1)
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
        # Find the edge weight between prev and current
        for neighbor, weight in graph[prev]:
            if neighbor == current:
                path_edges.append(weight)
                break
        current = prev
    
    return path_edges

def main():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    n = int(data[index])
    index += 1
    m = int(data[index])
    index += 1
    t = int(data[index])
    index += 1
    
    primary_hubs = list(map(int, data[index:index+t]))
    index += t
    
    # Build graph
    graph = defaultdict(list)
    edges = []
    
    for _ in range(m):
        u = int(data[index])
        index += 1
        v = int(data[index])
        index += 1
        w = int(data[index])
        index += 1
        
        graph[u].append((v, w))
        graph[v].append((u, w))
        edges.append((u, v, w))
    
    if t <= 1:
        print(0)
        return
    
    # For each pair of primary hubs, find the path between them
    # and collect all edges on these paths
    edge_count = defaultdict(int)
    
    # Since it's a tree, there's exactly one path between any two nodes
    for i in range(t):
        for j in range(i + 1, t):
            hub1 = primary_hubs[i]
            hub2 = primary_hubs[j]
            
            # Find path between hub1 and hub2
            visited = [False] * (n + 1)
            parent = [-1] * (n + 1)
            queue = deque([hub1])
            visited[hub1] = True
            
            while queue:
                node = queue.popleft()
                if node == hub2:
                    break
                for neighbor, weight in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        parent[neighbor] = (node, weight)
                        queue.append(neighbor)
            
            # Reconstruct path and count edges
            current = hub2
            while parent[current] != -1:
                prev, weight = parent[current]
                edge_count[(min(prev, current), max(prev, current))] += 1
                current = prev
    
    # Sum up the weights of edges that are used in any path
    total_cost = 0
    for u, v, w in edges:
        key = (min(u, v), max(u, v))
        if edge_count[key] > 0:
            total_cost += w
    
    print(total_cost)

if __name__ == "__main__":
    main()