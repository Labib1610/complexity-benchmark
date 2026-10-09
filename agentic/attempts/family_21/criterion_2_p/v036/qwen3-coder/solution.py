import sys
from collections import deque, defaultdict
import heapq

def dijkstra(graph, start, end):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    prev = {node: None for node in graph}
    pq = [(0, start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if u == end:
            break
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))
    
    path = []
    curr = end
    while curr is not None:
        path.append(curr)
        curr = prev[curr]
    path.reverse()
    
    return dist[end], path if dist[end] != float('inf') else []

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    s = int(data[idx])
    idx += 1
    t = int(data[idx])
    idx += 1
    B = int(data[idx])
    idx += 1
    
    edges = []
    graph = defaultdict(list)
    
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        edges.append((u, v, w))
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Find shortest path from s to t
    dist, path_nodes = dijkstra(graph, s, t)
    
    if dist == float('inf'):
        # Already disconnected
        print("YES")
        print(0)
        return
    
    if dist <= B:
        # We can block the entire shortest path
        path_edges = []
        for i in range(len(path_nodes) - 1):
            u = path_nodes[i]
            v = path_nodes[i+1]
            path_edges.append((u, v))
        
        # Now we need to find the actual edges to block
        blocked = []
        total_cost = 0
        
        for i in range(len(path_nodes) - 1):
            u = path_nodes[i]
            v = path_nodes[i+1]
            # Find the edge between u and v with minimum weight
            min_w = float('inf')
            min_edge = None
            for edge in edges:
                if (edge[0] == u and edge[1] == v) or (edge[0] == v and edge[1] == u):
                    if edge[2] < min_w:
                        min_w = edge[2]
                        min_edge = edge
            
            if min_edge:
                blocked.append(min_edge)
                total_cost += min_edge[2]
        
        if total_cost <= B:
            print("YES")
            print(len(blocked))
            for edge in blocked:
                print(edge[0], edge[1])
            return
    
    # Try to find minimum cut
    # Use max flow / min cut algorithm
    # But since this is undirected weighted graph, we can model it as max flow
    
    # Create residual graph for max flow
    # But let's try a different approach: enumerate cuts
    
    # Let's use a more direct approach: find min cut using max flow
    
    # Ford-Fulkerson with BFS (Edmonds-Karp)
    def bfs_flow(capacity, source, sink, parent):
        visited = set()
        queue = deque([source])
        visited.add(source)
        parent[source] = -1
        
        while queue:
            u = queue.popleft()
            for v in capacity[u]:
                if v not in visited and capacity[u][v] > 0:
                    queue.append(v)
                    visited.add(v)
                    parent[v] = u
                    if v == sink:
                        return True
        return False
    
    def ford_fulkerson(capacity, source, sink):
        parent = {}
        max_flow = 0
        
        while bfs_flow(capacity, source, sink, parent):
            path_flow = float('inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, capacity[parent[s]][s])
                s = parent[s]
            
            max_flow += path_flow
            
            v = sink
            while v != source:
                u = parent[v]
                capacity[u][v] -= path_flow
                if v not in capacity:
                    capacity[v] = {}
                if u not in capacity[v]:
                    capacity[v][u] = 0
                capacity[v][u] += path_flow
                v = parent[v]
        
        return max_flow
    
    # Build capacity graph
    capacity = {}
    for u in range(1, n+1):
        capacity[u] = {}
    
    for u, v, w in edges:
        if v not in capacity[u]:
            capacity[u][v] = 0
        if u not in capacity[v]:
            capacity[v][u] = 0
        capacity[u][v] += w
        capacity[v][u] += w
    
    # Make a copy for finding the cut
    import copy
    original_capacity = copy.deepcopy(capacity)
    
    # Compute max flow
    max_flow = ford_fulkerson(copy.deepcopy(original_capacity), s, t)
    
    if max_flow > B:
        print("NO")
        return
    
    # Reconstruct the cut
    # Run BFS on residual graph to find which nodes are reachable from s
    residual = copy.deepcopy(original_capacity)
    
    def get_reachable(residual_graph, source):
        visited = set()
        queue = deque([source])
        visited.add(source)
        
        while queue:
            u = queue.popleft()
            for v in residual_graph[u]:
                if v not in visited and residual_graph[u][v] > 0:
                    queue.append(v)
                    visited.add(v)
        return visited
    
    reachable_from_s = get_reachable(residual, s)
    
    # Edges crossing the cut
    cut_edges = []
    total_cut_cost = 0
    
    for u, v, w in edges:
        # If u is reachable from s and v is not, or vice versa, then this edge crosses the cut
        u_in_s = u in reachable_from_s
        v_in_s = v in reachable_from_s
        
        if u_in_s != v_in_s:
            cut_edges.append((u, v))
            total_cut_cost += w
    
    if total_cut_cost <= B:
        print("YES")
        print(len(cut_edges))
        for u, v in cut_edges:
            print(u, v)
    else:
        print("NO")

if __name__ == "__main__":
    main()