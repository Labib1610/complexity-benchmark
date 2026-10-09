import sys
from collections import defaultdict
import heapq

def dijkstra(graph, start, end):
    # Find minimum cut using max flow / min cut theorem
    # We'll use a modified Dijkstra to find the minimum cut
    # Actually, we should use max flow algorithm, but let's think differently
    
    # The minimum cost to disconnect s and t is the minimum cut
    # We can model this as shortest path in the dual problem
    # But easier approach: use max flow = min cut
    
    # Let's implement a simple Ford-Fulkerson with DFS for max flow
    # But since we need specific edges, we'll use Edmonds-Karp variant
    
    def bfs_find_path(capacity, source, sink, parent):
        visited = set()
        queue = [source]
        visited.add(source)
        
        while queue:
            u = queue.pop(0)
            
            for v in capacity[u]:
                if v not in visited and capacity[u][v] > 0:
                    queue.append(v)
                    visited.add(v)
                    parent[v] = u
                    if v == sink:
                        return True
        return False
    
    def ford_fulkerson(cap_graph, source, sink):
        # Create a copy of the graph for residual network
        res_graph = defaultdict(lambda: defaultdict(int))
        for u in cap_graph:
            for v in cap_graph[u]:
                res_graph[u][v] = cap_graph[u][v]
                
        parent = {}
        max_flow = 0
        
        path_edges = []  # To store actual edges in the cut
        
        while bfs_find_path(res_graph, source, sink, parent):
            path_flow = float('inf')
            s = sink
            
            # Find minimum capacity along the path
            while s != source:
                path_flow = min(path_flow, res_graph[parent[s]][s])
                s = parent[s]
            
            # Update residual capacities
            v = sink
            while v != source:
                u = parent[v]
                res_graph[u][v] -= path_flow
                res_graph[v][u] += path_flow
                v = parent[v]
            
            max_flow += path_flow
        
        # Now we need to find which edges were cut
        # Do BFS from source in residual graph to find reachable nodes
        visited_from_source = set()
        queue = [source]
        visited_from_source.add(source)
        
        while queue:
            u = queue.pop(0)
            for v in res_graph[u]:
                if res_graph[u][v] > 0 and v not in visited_from_source:
                    queue.append(v)
                    visited_from_source.add(v)
        
        # Edges from visited to unvisited form the cut
        cut_edges = []
        for u in cap_graph:
            for v in cap_graph[u]:
                if u in visited_from_source and v not in visited_from_source:
                    cut_edges.append((u, v))
                elif v in visited_from_source and u not in visited_from_source:
                    cut_edges.append((v, u))
                    
        return max_flow, cut_edges
    
    # Build capacity graph
    cap_graph = defaultdict(lambda: defaultdict(int))
    for u in graph:
        for v in graph[u]:
            cap_graph[u][v] = graph[u][v]
            cap_graph[v][u] = graph[u][v]  # Since undirected
    
    return ford_fulkerson(cap_graph, start, end)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    s = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1
    B = int(data[idx]); idx += 1
    
    graph = defaultdict(dict)
    edge_list = []
    
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        w = int(data[idx]); idx += 1
        graph[u][v] = w
        graph[v][u] = w
        edge_list.append((u, v, w))
    
    # Use a simpler approach - find min-cut using max-flow
    # But let's implement a cleaner version
    
    # Create residual graph for max flow
    def max_flow_min_cut(source, sink):
        # Initialize flow
        flow = defaultdict(lambda: defaultdict(int))
        capacity = defaultdict(lambda: defaultdict(int))
        
        # Fill capacity matrix
        for u in graph:
            for v in graph[u]:
                capacity[u][v] = graph[u][v]
        
        def bfs():
            parent = {}
            visited = set()
            queue = [source]
            visited.add(source)
            
            while queue:
                u = queue.pop(0)
                for v in capacity[u]:
                    if v not in visited and capacity[u][v] - flow[u][v] > 0:
                        parent[v] = u
                        visited.add(v)
                        queue.append(v)
                        if v == sink:
                            return parent
            return None
        
        # Ford-Fulkerson
        while True:
            parent = bfs()
            if not parent:
                break
                
            # Find bottleneck
            path_flow = float('Inf')
            s_node = sink
            while s_node != source:
                path_flow = min(path_flow, capacity[parent[s_node]][s_node] - flow[parent[s_node]][s_node])
                s_node = parent[s_node]
            
            # Update flows
            v = sink
            while v != source:
                u = parent[v]
                flow[u][v] += path_flow
                flow[v][u] -= path_flow
                v = parent[v]
        
        # Find min-cut edges
        # BFS from source to find reachable nodes
        visited = set()
        queue = [source]
        visited.add(source)
        
        while queue:
            u = queue.pop(0)
            for v in capacity[u]:
                if v not in visited and capacity[u][v] - flow[u][v] > 0:
                    queue.append(v)
                    visited.add(v)
        
        # Collect cut edges
        cut_edges = []
        cut_value = 0
        for u in graph:
            for v in graph[u]:
                # Only count each edge once
                if u < v:  
                    if (u in visited) != (v in visited):  # One side in S, other in T
                        cut_edges.append((u, v))
                        cut_value += graph[u][v]
                        
        return cut_value, cut_edges
    
    min_cut_value, min_cut_edges = max_flow_min_cut(s, t)
    
    if min_cut_value <= B:
        print("YES")
        print(len(min_cut_edges))
        for u, v in min_cut_edges:
            print(u, v)
    else:
        print("NO")

if __name__ == "__main__":
    main()