import sys
import heapq
from collections import defaultdict, deque

def find_min_cut_edges(n, edges, s, t):
    # Create adjacency list with edge weights
    graph = defaultdict(list)
    edge_dict = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
        edge_dict[(u, v)].append(w)
        edge_dict[(v, u)].append(w)
    
    # First, find the minimum cut value using max flow / min cut
    # We'll use Dijkstra-based approach for max flow in this case
    
    def dijkstra_max_flow():
        # Use Dijkstra to find shortest path in residual graph
        # But we want to find min cut, so we'll use the fact that
        # min cut = max flow in this context
        dist = [float('inf')] * (n + 1)
        dist[s] = 0
        pq = [(0, s)]
        parent = [-1] * (n + 1)
        
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            if u == t:
                break
                
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    parent[v] = u
                    heapq.heappush(pq, (dist[v], v))
        
        return dist[t] if dist[t] != float('inf') else -1
    
    # Actually, let's implement a proper max flow algorithm
    # Ford-Fulkerson with DFS
    
    # Build residual graph
    res_graph = defaultdict(lambda: defaultdict(int))
    edge_index = {}  # to track original edges
    
    for i, (u, v, w) in enumerate(edges):
        res_graph[u][v] += w
        res_graph[v][u] += w
        edge_index[(u, v, i)] = w
        edge_index[(v, u, i)] = w
    
    def bfs_find_path(source, sink, parent):
        visited = [False] * (n + 1)
        queue = deque([source])
        visited[source] = True
        
        while queue:
            u = queue.popleft()
            
            for v in res_graph[u]:
                if not visited[v] and res_graph[u][v] > 0:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)
                    if v == sink:
                        return True
        return False
    
    def ford_fulkerson(source, sink):
        parent = [-1] * (n + 1)
        max_flow = 0
        
        while bfs_find_path(source, sink, parent):
            path_flow = float('inf')
            s_node = sink
            while s_node != source:
                path_flow = min(path_flow, res_graph[parent[s_node]][s_node])
                s_node = parent[s_node]
            
            # Update residual capacities
            v_node = sink
            while v_node != source:
                u_node = parent[v_node]
                res_graph[u_node][v_node] -= path_flow
                res_graph[v_node][u_node] += path_flow
                v_node = parent[v_node]
            
            max_flow += path_flow
        
        return max_flow
    
    # Find min cut edges
    max_flow_value = ford_fulkerson(s, t)
    
    # Now we need to find which edges form the min cut
    # Run BFS to find reachable nodes from source in residual graph
    visited = [False] * (n + 1)
    queue = deque([s])
    visited[s] = True
    
    while queue:
        u = queue.popleft()
        for v in res_graph[u]:
            if not visited[v] and res_graph[u][v] > 0:
                visited[v] = True
                queue.append(v)
    
    # Edges that go from visited (set S) to not visited (set T) form the min cut
    min_cut_edges = []
    total_cost = 0
    
    for i, (u, v, w) in enumerate(edges):
        # In the original graph, check if u is in S and v is in T (or vice versa)
        # But we need to be careful about direction
        if (visited[u] and not visited[v]) or (visited[v] and not visited[u]):
            min_cut_edges.append((u, v))
            total_cost += w
    
    return min_cut_edges, total_cost

def main():
    input_lines = []
    for line in sys.stdin:
        input_lines.append(line.strip())
    
    # Parse input
    first_line = list(map(int, input_lines[0].split()))
    n, m, s, t, B = first_line
    
    edges = []
    for i in range(1, m + 1):
        u, v, w = map(int, input_lines[i].split())
        edges.append((u, v, w))
    
    # Find minimum cut
    # Build graph for max flow
    graph = defaultdict(list)
    edge_weights = {}
    
    for u, v, w in edges:
        graph[u].append(v)
        graph[v].append(u)
        edge_weights[(u, v)] = edge_weights.get((u, v), 0) + w
        edge_weights[(v, u)] = edge_weights.get((v, u), 0) + w
    
    # Use Ford-Fulkerson to find max flow = min cut
    def bfs(source, sink, parent):
        visited = [False] * (n + 1)
        queue = deque([source])
        visited[source] = True
        
        while queue:
            u = queue.popleft()
            
            for v in graph[u]:
                if not visited[v] and residual_graph[u][v] > 0:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)
                    if v == sink:
                        return True
        return False
    
    # Initialize residual graph
    residual_graph = defaultdict(lambda: defaultdict(int))
    for u, v, w in edges:
        residual_graph[u][v] += w
        residual_graph[v][u] += w
    
    def ford_fulkerson(source, sink):
        parent = [-1] * (n + 1)
        max_flow = 0
        
        while bfs(source, sink, parent):
            path_flow = float('inf')
            s_node = sink
            while s_node != source:
                path_flow = min(path_flow, residual_graph[parent[s_node]][s_node])
                s_node = parent[s_node]
            
            v_node = sink
            while v_node != source:
                u_node = parent[v_node]
                residual_graph[u_node][v_node] -= path_flow
                residual_graph[v_node][u_node] += path_flow
                v_node = parent[v_node]
            
            max_flow += path_flow
        
        return max_flow
    
    # Make a copy for finding the cut edges
    original_residual = defaultdict(lambda: defaultdict(int))
    for u, v, w in edges:
        original_residual[u][v] += w
        original_residual[v][u] += w
    
    # Run max flow
    max_flow = ford_fulkerson(s, t)
    
    # Find min cut edges by checking what edges cross the cut
    # Run BFS on final residual graph to find what's reachable from source
    visited_final = [False] * (n + 1)
    queue_final = deque([s])
    visited_final[s] = True
    
    while queue_final:
        u = queue_final.popleft()
        for v in graph[u]:
            if not visited_final[v] and residual_graph[u][v] > 0:
                visited_final[v] = True
                queue_final.append(v)
    
    # Find edges crossing the cut
    cut_edges = []
    cut_cost = 0
    
    # For each original edge, check if it crosses the cut
    edge_count = {}
    for u, v, w in edges:
        key = tuple(sorted([u, v]))
        edge_count[key] = edge_count.get(key, 0) + w
    
    processed_edges = set()
    for u, v, w in edges:
        key = tuple(sorted([u, v]))
        if key in processed_edges:
            continue
        processed_edges.add(key)
        
        # Check if this edge crosses the cut
        # An edge crosses if one endpoint is visited and the other is not
        if (visited_final[u] and not visited_final[v]) or (visited_final[v] and not visited_final[u]):
            cut_edges.append((u, v))
            cut_cost += edge_count[key]
    
    if cut_cost <= B:
        print("YES")
        print(len(cut_edges))
        for u, v in cut_edges:
            print(u, v)
    else:
        print("NO")

if __name__ == "__main__":
    main()