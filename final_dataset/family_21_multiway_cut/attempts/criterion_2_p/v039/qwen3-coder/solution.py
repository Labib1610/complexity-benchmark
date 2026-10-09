import sys
from collections import defaultdict, deque

def find_min_cut(n, m, s, t, edges):
    # Build adjacency list with capacities
    graph = defaultdict(lambda: defaultdict(int))
    edge_list = {}
    
    for u, v, w in edges:
        # For undirected graph, add capacity in both directions
        graph[u][v] += w
        graph[v][u] += w
        edge_list[(u, v)] = edge_list.get((u, v), 0) + w
        edge_list[(v, u)] = edge_list.get((v, u), 0) + w
    
    # Ford-Fulkerson with DFS to find max flow/min cut
    def bfs_find_path(source, sink, parent):
        visited = set()
        queue = deque([source])
        visited.add(source)
        
        while queue:
            u = queue.popleft()
            
            for v in graph[u]:
                if v not in visited and graph[u][v] > 0:
                    visited.add(v)
                    parent[v] = u
                    queue.append(v)
                    if v == sink:
                        return True
        return False
    
    def ford_fulkerson(source, sink):
        parent = {}
        max_flow = 0
        
        while bfs_find_path(source, sink, parent):
            path_flow = float('inf')
            s_node = sink
            
            # Find minimum capacity along the path
            while s_node != source:
                prev = parent[s_node]
                path_flow = min(path_flow, graph[prev][s_node])
                s_node = prev
            
            # Update residual capacities
            v = sink
            while v != source:
                u = parent[v]
                graph[u][v] -= path_flow
                graph[v][u] += path_flow
                v = parent[v]
            
            max_flow += path_flow
        
        return max_flow
    
    # Find minimum cut
    original_graph = defaultdict(lambda: defaultdict(int))
    for u, v, w in edges:
        original_graph[u][v] += w
        original_graph[v][u] += w
    
    max_flow = ford_fulkerson(s, t)
    
    # Find the cut by BFS from source in residual graph
    visited_in_residual = set()
    queue = deque([s])
    visited_in_residual.add(s)
    
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if v not in visited_in_residual and graph[u][v] > 0:
                visited_in_residual.add(v)
                queue.append(v)
    
    # Edges crossing the cut
    cut_edges = []
    cut_value = 0
    
    for u, v, w in edges:
        # Check if this edge crosses the cut
        # u is reachable from s, v is not reachable (or vice versa)
        u_reachable = u in visited_in_residual
        v_reachable = v in visited_in_residual
        
        if u_reachable != v_reachable:
            cut_edges.append((u, v))
            cut_value += w
    
    return max_flow, cut_edges

def main():
    input_lines = []
    for line in sys.stdin:
        input_lines.append(line.strip())
    
    n, m, s, t, B = map(int, input_lines[0].split())
    
    edges = []
    for i in range(1, m + 1):
        u, v, w = map(int, input_lines[i].split())
        edges.append((u, v, w))
    
    min_cost, cut_edges = find_min_cut(n, m, s, t, edges)
    
    if min_cost <= B:
        print("YES")
        print(len(cut_edges))
        for u, v in cut_edges:
            print(u, v)
    else:
        print("NO")

if __name__ == "__main__":
    main()