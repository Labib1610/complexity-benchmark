import sys
import heapq
from collections import defaultdict, deque

def find_mincut_edges(n, edges, source, sink):
    # Edmonds-Karp implementation to find min-cut edges
    graph = defaultdict(list)
    capacity = defaultdict(int)
    
    for u, v, w in edges:
        graph[u].append(v)
        graph[v].append(u)
        capacity[(u, v)] += w
        capacity[(v, u)] += w
    
    def bfs():
        parent = [-1] * (n + 1)
        visited = [False] * (n + 1)
        queue = deque([source])
        visited[source] = True
        
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if not visited[v] and capacity[(u, v)] > 0:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)
                    if v == sink:
                        path = []
                        curr = sink
                        while curr != source:
                            path.append((parent[curr], curr))
                            curr = parent[curr]
                        return path[::-1]
        return None
    
    # Find max flow
    max_flow = 0
    while True:
        path = bfs()
        if not path:
            break
            
        # Find minimum capacity along the path
        min_cap = float('inf')
        for u, v in path:
            min_cap = min(min_cap, capacity[(u, v)])
            
        # Update capacities
        for u, v in path:
            capacity[(u, v)] -= min_cap
            capacity[(v, u)] += min_cap
            
        max_flow += min_cap
    
    # Find min-cut edges
    # Run BFS from source to find reachable nodes
    visited = [False] * (n + 1)
    queue = deque([source])
    visited[source] = True
    
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if not visited[v] and capacity[(u, v)] > 0:
                visited[v] = True
                queue.append(v)
    
    # Edges crossing the cut
    cut_edges = []
    for u, v, w in edges:
        # If u is reachable but v is not, or vice versa
        if (visited[u] and not visited[v]) or (visited[v] and not visited[u]):
            cut_edges.append((u, v))
            
    return max_flow, cut_edges

def main():
    input_lines = []
    for line in sys.stdin:
        input_lines.append(line.strip())
    
    line_idx = 0
    
    # Read first line
    n, m, k, B = map(int, input_lines[line_idx].split())
    line_idx += 1
    
    # Read reactive anchors
    anchors = list(map(int, input_lines[line_idx].split()))
    line_idx += 1
    
    # Read edges
    edges = []
    for _ in range(m):
        u, v, w = map(int, input_lines[line_idx].split())
        edges.append((u, v, w))
        line_idx += 1
    
    if k <= 1:
        print("YES")
        print(0)
        return
    
    # Create a super source and super sink
    # Connect super source to all anchors except last
    # Connect all anchors except first to super sink
    super_source = 0
    super_sink = n + 1
    
    extended_edges = edges[:]
    
    # Add edges from super_source to all anchors
    for anchor in anchors[:-1]:
        extended_edges.append((super_source, anchor, B + 1))
    
    # Add edges from all anchors to super_sink
    for anchor in anchors[1:]:
        extended_edges.append((anchor, super_sink, B + 1))
    
    # Find min-cut in this extended graph
    flow, cut_edges = find_mincut_edges(n + 2, extended_edges, super_source, super_sink)
    
    if flow > B:
        print("NO")
        return
    
    # Filter out the artificial edges
    real_cut_edges = []
    for u, v in cut_edges:
        if u != super_source and v != super_sink and u != super_sink and v != super_source:
            real_cut_edges.append((u, v))
    
    print("YES")
    print(len(real_cut_edges))
    for u, v in real_cut_edges:
        print(u, v)

if __name__ == "__main__":
    main()