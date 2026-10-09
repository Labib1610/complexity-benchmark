import sys
from collections import defaultdict, deque

def read_input():
    n, m, k = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
    return n, m, k, edges

def solve(n, m, k, edges):
    # Build adjacency list
    adj = defaultdict(set)
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    
    # The key insight: the voltage property means the graph is bipartite
    # So we can color it with 2 colors and pick the larger color class
    color = {}
    visited = set()
    
    def bfs(start):
        queue = deque([start])
        color[start] = 0
        visited.add(start)
        size_0 = 1
        size_1 = 0
        
        while queue:
            node = queue.popleft()
            current_color = color[node]
            
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    color[neighbor] = 1 - current_color
                    if color[neighbor] == 0:
                        size_0 += 1
                    else:
                        size_1 += 1
                    queue.append(neighbor)
                elif color[neighbor] == current_color:
                    # This should not happen in a bipartite graph
                    return -1, -1
        
        return size_0, size_1
    
    # Find all connected components and their bipartition
    total_color_0 = []
    total_color_1 = []
    
    for i in range(1, n+1):
        if i not in visited:
            size_0, size_1 = bfs(i)
            if size_0 == -1:  # Not bipartite - but problem guarantees it is
                return "NO"
            
            # Collect nodes of each color in this component
            comp_0 = []
            comp_1 = []
            for node in visited:
                if node not in color:
                    continue
                if color[node] == 0:
                    comp_0.append(node)
                else:
                    comp_1.append(node)
            
            total_color_0.extend(comp_0)
            total_color_1.extend(comp_1)
    
    # Now we have two independent sets
    # Check if we can get exactly k elements
    if len(total_color_0) >= k:
        return "YES\n" + " ".join(map(str, total_color_0[:k]))
    elif len(total_color_1) >= k:
        return "YES\n" + " ".join(map(str, total_color_1[:k]))
    else:
        return "NO"

def main():
    n, m, k, edges = read_input()
    if m == 0:
        # No edges, all nodes can be selected
        result = "YES\n" + " ".join(map(str, range(1, min(k+1, n+1))))
        print(result)
        return
    
    # Rebuild adjacency properly for the actual algorithm
    adj = defaultdict(set)
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    
    # Color the graph
    color = {}
    visited = [False] * (n + 1)
    
    def bfs_component(start):
        queue = deque([start])
        color[start] = 0
        visited[start] = True
        count_0 = 1
        count_1 = 0
        
        while queue:
            u = queue.popleft()
            curr_color = color[u]
            
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    color[v] = 1 - curr_color
                    if color[v] == 0:
                        count_0 += 1
                    else:
                        count_1 += 1
                    queue.append(v)
                elif color[v] == curr_color:
                    # Should not happen as graph is bipartite
                    pass
                    
        return count_0, count_1
    
    color_0_nodes = []
    color_1_nodes = []
    
    for i in range(1, n + 1):
        if not visited[i]:
            # Collect all nodes first for this component
            component_nodes = []
            temp_queue = deque([i])
            temp_visited = set()
            temp_visited.add(i)
            
            while temp_queue:
                node = temp_queue.popleft()
                component_nodes.append(node)
                for neighbor in adj[node]:
                    if neighbor not in temp_visited:
                        temp_visited.add(neighbor)
                        temp_queue.append(neighbor)
            
            # BFS coloring for this component
            local_color = {}
            local_queue = deque([i])
            local_color[i] = 0
            c0, c1 = 1, 0
            
            local_node_visited = {i}
            
            while local_queue:
                node = local_queue.popleft()
                curr_col = local_color[node]
                
                for neighbor in adj[node]:
                    if neighbor not in local_node_visited:
                        local_node_visited.add(neighbor)
                        local_color[neighbor] = 1 - curr_col
                        if local_color[neighbor] == 0:
                            c0 += 1
                        else:
                            c1 += 1
                        local_queue.append(neighbor)
            
            # Add to global lists based on coloring
            for node in component_nodes:
                if local_color[node] == 0:
                    color_0_nodes.append(node)
                else:
                    color_1_nodes.append(node)
    
    # Choose the color class that allows us to pick k nodes
    if len(color_0_nodes) >= k:
        print("YES")
        print(" ".join(map(str, color_0_nodes[:k])))
    elif len(color_1_nodes) >= k:
        print("YES")
        print(" ".join(map(str, color_1_nodes[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    main()