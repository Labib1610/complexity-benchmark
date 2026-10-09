import sys
from collections import defaultdict
import heapq

def dijkstra(graph, start, end):
    # Find shortest path from start to end
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0
    prev = {}
    visited = set()
    pq = [(0, start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        
        if u == end:
            # Reconstruct path
            path = []
            current = end
            while current in prev:
                path.append((prev[current], current))
                current = prev[current]
            return path[::-1]  # Return path edges
        
        for v, w in graph[u]:
            if v not in visited and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))
    
    return []  # No path found

def solve():
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
    
    edge_map = {}  # Map (u,v) or (v,u) to (original_u, original_v, weight)
    
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
        edge_map[(min(u,v), max(u,v))] = (u, v, w)
    
    # Find shortest path between s and t
    path_edges = dijkstra(graph, s, t)
    
    if not path_edges:
        # Already disconnected
        print("YES")
        print(0)
        return
    
    # Try removing each edge in the path and see if we can disconnect s and t within budget
    min_cost = float('inf')
    best_removal = []
    
    # For each edge in the shortest path, remove it and check connectivity
    for i in range(len(path_edges)):
        # Create a new graph without the i-th edge in the path
        temp_graph = defaultdict(list)
        removed_edge = path_edges[i]
        ru, rv = removed_edge
        
        # Add all edges except the one we're removing
        for u, v, w in edges:
            if not ((u == ru and v == rv) or (u == rv and v == ru)):
                temp_graph[u].append((v, w))
                temp_graph[v].append((u, w))
        
        # Check if s and t are still connected in temp_graph
        # Do a BFS/DFS from s to see if we can reach t
        visited = set()
        stack = [s]
        visited.add(s)
        still_connected = False
        
        while stack:
            node = stack.pop()
            if node == t:
                still_connected = True
                break
            for neighbor, _ in temp_graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        
        if not still_connected:
            # This edge alone disconnects s and t
            if edge_map[(min(ru,rv), max(ru,rv))][2] <= B:
                print("YES")
                print(1)
                print(ru, rv)
                return
        else:
            # Need to find another edge to remove
            # Let's try removing this edge plus one more from the remaining path
            for j in range(i+1, len(path_edges)):
                # Remove both edges
                removed_edge2 = path_edges[j]
                ru2, rv2 = removed_edge2
                
                # Create graph without both edges
                temp_graph2 = defaultdict(list)
                removed_edges = set([(ru, rv), (ru2, rv2)])
                
                total_cost = edge_map[(min(ru,rv), max(ru,rv))][2] + edge_map[(min(ru2,rv2), max(ru2,rv2))][2]
                
                if total_cost > B:
                    continue
                
                # Add all edges except the two we're removing
                valid = True
                for u, v, w in edges:
                    if (u, v) in removed_edges or (v, u) in removed_edges:
                        continue
                    temp_graph2[u].append((v, w))
                    temp_graph2[v].append((u, w))
                
                # Check if s and t are still connected
                visited2 = set()
                stack2 = [s]
                visited2.add(s)
                still_connected2 = False
                
                while stack2:
                    node = stack2.pop()
                    if node == t:
                        still_connected2 = True
                        break
                    for neighbor, _ in temp_graph2[node]:
                        if neighbor not in visited2:
                            visited2.add(neighbor)
                            stack2.append(neighbor)
                
                if not still_connected2:
                    # Found a valid solution
                    if total_cost < min_cost:
                        min_cost = total_cost
                        best_removal = [(ru, rv), (ru2, rv2)]
    
    # If we found a valid solution
    if best_removal:
        print("YES")
        print(len(best_removal))
        for u, v in best_removal:
            print(u, v)
        return
    
    # Try all pairs of edges
    for i in range(len(edges)):
        u1, v1, w1 = edges[i]
        if w1 > B:
            continue
            
        # Graph without first edge
        temp_graph1 = defaultdict(list)
        for j in range(len(edges)):
            if i == j:
                continue
            u, v, w = edges[j]
            temp_graph1[u].append((v, w))
            temp_graph1[v].append((u, w))
            
        # Check if already disconnected
        visited = set()
        stack = [s]
        visited.add(s)
        still_connected = False
        
        while stack:
            node = stack.pop()
            if node == t:
                still_connected = True
                break
            for neighbor, _ in temp_graph1[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        
        if not still_connected:
            print("YES")
            print(1)
            print(u1, v1)
            return
            
        # Try adding one more edge to remove
        for j in range(i+1, len(edges)):
            u2, v2, w2 = edges[j]
            if w1 + w2 > B:
                continue
                
            # Graph without both edges
            temp_graph2 = defaultdict(list)
            for k in range(len(edges)):
                if k == i or k == j:
                    continue
                u, v, w = edges[k]
                temp_graph2[u].append((v, w))
                temp_graph2[v].append((u, w))
                
            # Check if disconnected
            visited2 = set()
            stack2 = [s]
            visited2.add(s)
            still_connected2 = False
            
            while stack2:
                node = stack2.pop()
                if node == t:
                    still_connected2 = True
                    break
                for neighbor, _ in temp_graph2[node]:
                    if neighbor not in visited2:
                        visited2.add(neighbor)
                        stack2.append(neighbor)
            
            if not still_connected2:
                print("YES")
                print(2)
                print(u1, v1)
                print(u2, v2)
                return
    
    # Special case: check if s and t are already disconnected
    # Build initial graph
    initial_graph = defaultdict(list)
    for u, v, w in edges:
        initial_graph[u].append((v, w))
        initial_graph[v].append((u, w))
    
    # Check connectivity
    visited_initial = set()
    stack_initial = [s]
    visited_initial.add(s)
    can_reach = False
    
    while stack_initial:
        node = stack_initial.pop()
        if node == t:
            can_reach = True
            break
        for neighbor, _ in initial_graph[node]:
            if neighbor not in visited_initial:
                visited_initial.add(neighbor)
                stack_initial.append(neighbor)
    
    if not can_reach:
        print("YES")
        print(0)
        return
    
    print("NO")

solve()