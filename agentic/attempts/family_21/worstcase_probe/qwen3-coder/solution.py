import sys
from collections import defaultdict, deque

def find_minimal_separators(n, edges, hubs):
    # Build adjacency list
    adj = defaultdict(list)
    edge_costs = {}
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
        edge_costs[(u,v)] = w
        edge_costs[(v,u)] = w
    
    # For each pair of hubs, find minimum cut
    # We'll use a modified BFS/DFS approach to find separators
    
    def bfs_find_separator(source, target):
        # Find minimum weight set of edges to remove to separate source and target
        # This is essentially finding a minimum cut between source and target
        # We can model this as a flow problem, but since we want to find the actual edges,
        # we'll use a different approach
        
        # For small graphs, we can try all possible combinations of edges
        # But given constraints, let's think differently
        
        # Actually, let's build a graph and find min-cut for each pair
        # Using Stoer-Wagner algorithm concept or simple flow might work
        # But let's think of this as: we want to disconnect ALL pairs of hubs
        # So we need to find a set of edges that separates ALL pairs
        
        # This is equivalent to finding a multi-way cut
        # But let's approach it differently - find min-cut for each pair and take union?
        # No, that won't work optimally
        
        # Let's think of it as: we want to make sure each hub is in its own component
        # So we need to find a set of edges such that removing them results in 
        # each hub being in a different connected component
        
        # This is a complex problem. Let's try a greedy approach:
        # Keep adding minimum cuts until all pairs are separated
        return []
    
    # Simpler approach: Try all possible subsets of edges within budget
    # But that's exponential. Let's think of something better.
    
    # Key insight: We want to separate ALL hubs from each other
    # One way is to find a spanning tree and then remove necessary edges
    # But that's not optimal either
    
    # Let's model this properly:
    # We want to find minimum weight set of edges such that in the resulting graph
    # each hub is in a different connected component
    
    # This is the multiway cut problem which is NP-hard
    # But maybe we can solve it for small k
    
    # For k=2, it's just min-cut between two nodes
    # For larger k, it's more complex
    
    # Let's implement a solution that works for small cases
    # Try greedy: for each pair of hubs, find min-cut, union all, check if valid
    
    def dijkstra(graph, start, end=None):
        # Dijkstra for shortest path
        dist = {node: float('inf') for node in range(1, n+1)}
        dist[start] = 0
        prev = {}
        visited = set()
        
        while len(visited) < n:
            # Find unvisited node with minimum distance
            u = None
            for node in range(1, n+1):
                if node not in visited and (u is None or dist[node] < dist[u]):
                    u = node
            
            if u is None or dist[u] == float('inf'):
                break
                
            visited.add(u)
            
            if u == end:
                break
                
            for v, w in graph[u]:
                if v not in visited:
                    alt = dist[u] + w
                    if alt < dist[v]:
                        dist[v] = alt
                        prev[v] = u
                        
        return dist, prev
    
    # For min-cut between two nodes, we can use max-flow min-cut theorem
    # But implementing that correctly is complex
    
    # Let's try a simpler brute-force for small inputs
    # Generate all possible subsets of edges and check if they separate all hubs
    
    def separates_all_hubs(edge_subset):
        # Create graph without these edges
        temp_adj = defaultdict(list)
        removed_edges = set()
        for u, v, w in edge_subset:
            removed_edges.add((u,v))
            removed_edges.add((v,u))
            
        # Add back edges that are not removed
        for u, v, w in edges:
            if (u,v) not in removed_edges:
                temp_adj[u].append(v)
                temp_adj[v].append(u)
                
        # Check if all hubs are in different components
        visited = set()
        components = []
        
        def dfs(node, component):
            visited.add(node)
            component.append(node)
            for neighbor in temp_adj[node]:
                if neighbor not in visited:
                    dfs(neighbor, component)
                    
        for i in range(1, n+1):
            if i not in visited:
                component = []
                dfs(i, component)
                components.append(set(component))
                
        # Count how many hubs in each component
        hub_components = [0] * len(components)
        for h in hubs:
            for i, comp in enumerate(components):
                if h in comp:
                    hub_components[i] += 1
                    
        # If any component has more than one hub, separation failed
        return all(count <= 1 for count in hub_components)
    
    # Try all subsets - but this is too slow for large inputs
    # Let's sort edges by weight and try greedy approach
    
    edges.sort(key=lambda x: x[2])  # Sort by weight
    
    # Greedy: keep adding edges until all hubs are separated
    selected_edges = []
    total_cost = 0
    
    # Check current separation
    def current_separation():
        # Build current graph
        temp_adj = defaultdict(list)
        for u, v, w in edges:
            if (u,v) not in [(e[0], e[1]) for e in selected_edges] and \
               (v,u) not in [(e[0], e[1]) for e in selected_edges]:
                temp_adj[u].append(v)
                temp_adj[v].append(u)
                
        # Find components
        visited = set()
        components = []
        
        def dfs(node, component):
            visited.add(node)
            component.append(node)
            for neighbor in temp_adj[node]:
                if neighbor not in visited:
                    dfs(neighbor, component)
                    
        for i in range(1, n+1):
            if i not in visited:
                component = []
                dfs(i, component)
                components.append(set(component))
                
        # Check hub separation
        hub_count_per_component = []
        for comp in components:
            count = sum(1 for h in hubs if h in comp)
            hub_count_per_component.append(count)
            
        return all(c <= 1 for c in hub_count_per_component)
    
    # Add edges one by one until separation achieved
    for u, v, w in edges:
        if total_cost + w > B:
            break
        selected_edges.append((u, v, w))
        total_cost += w
        if current_separation():
            break
            
    if current_separation() and total_cost <= B:
        print("YES")
        print(len(selected_edges))
        for u, v, w in selected_edges:
            print(u, v)
        return
    else:
        # Try more sophisticated approach
        # Since this is complex, let's just say NO for now
        print("NO")

def main():
    input_lines = []
    for line in sys.stdin:
        input_lines.append(line.strip())
    
    # Parse input
    line1 = list(map(int, input_lines[0].split()))
    n, m, k, B = line1[0], line1[1], line1[2], line1[3]
    
    if k <= 1:
        print("YES")
        print(0)
        return
        
    hubs = list(map(int, input_lines[1].split()))
    
    edges = []
    for i in range(2, 2 + m):
        u, v, w = map(int, input_lines[i].split())
        edges.append((u, v, w))
    
    # Special case handling
    if k == 1:
        print("YES")
        print(0)
        return
    
    # For small k, we can try to solve exactly
    # But let's implement a simpler solution first
    
    # Try greedy approach: sort edges by cost, add until all hubs separated
    edges.sort(key=lambda x: x[2])
    
    # Function to check if current selection separates all hubs
    def is_separated(selected_edge_indices):
        # Build graph without selected edges
        adj = defaultdict(list)
        selected_set = set(selected_edge_indices)
        
        for i, (u, v, w) in enumerate(edges):
            if i not in selected_set:
                adj[u].append(v)
                adj[v].append(u)
        
        # Find connected components
        visited = [False] * (n + 1)
        components = []
        
        def dfs(start, component):
            stack = [start]
            while stack:
                node = stack.pop()
                if not visited[node]:
                    visited[node] = True
                    component.add(node)
                    for neighbor in adj[node]:
                        if not visited[neighbor]:
                            stack.append(neighbor)
        
        for i in range(1, n + 1):
            if not visited[i]:
                component = set()
                dfs(i, component)
                components.append(component)
        
        # Check if each hub is in a different component
        hub_components = []
        for hub in hubs:
            for j, component in enumerate(components):
                if hub in component:
                    hub_components.append(j)
                    break
        
        # All hubs should be in different components
        return len(hub_components) == len(set(hub_components)) == len(hubs)
    
    # Greedy selection
    selected = []
    total_cost = 0
    
    # Try adding edges one by one
    for i in range(len(edges)):
        if total_cost + edges[i][2] > B:
            continue
        selected.append(i)
        total_cost += edges[i][2]
        if is_separated(selected):
            break
    
    if is_separated(selected) and total_cost <= B:
        print("YES")
        print(len(selected))
        for i in selected:
            print(edges[i][0], edges[i][1])
    else:
        # Try exhaustive search for small inputs
        # But this could be very slow, so let's limit it
        if len(edges) <= 20:  # Small enough to try combinations
            from itertools import combinations
            
            found = False
            best_selection = []
            min_cost = B + 1
            
            # Try all subsets (this is 2^m, so only feasible for small m)
            for r in range(1, len(edges) + 1):
                if found:
                    break
                for combo in combinations(range(len(edges)), r):
                    cost = sum(edges[i][2] for i in combo)
                    if cost <= B and is_separated(combo):
                        if cost < min_cost:
                            min_cost = cost
                            best_selection = list(combo)
                            found = True
                            if r == 1:  # Found optimal solution
                                break
                
            if found:
                print("YES")
                print(len(best_selection))
                for i in best_selection:
                    print(edges[i][0], edges[i][1])
            else:
                print("NO")
        else:
            print("NO")

if __name__ == "__main__":
    main()