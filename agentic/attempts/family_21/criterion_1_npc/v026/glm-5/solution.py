import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        n = int(next(it))
        m = int(next(it))
        k = int(next(it))
        B = int(next(it))
    except StopIteration:
        return

    licensed = []
    for _ in range(k):
        licensed.append(int(next(it)))
    
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((u, v, w))
    
    # Build adjacency list
    adj = defaultdict(list)
    edge_to_id = {}
    for i, (u, v, w) in enumerate(edges):
        adj[u].append((v, w, i))
        adj[v].append((u, w, i))
        edge_to_id[(min(u, v), max(u, v))] = i
    
    # BFS from each licensed company to find minimum cut to other licensed companies
    # We need to find minimum cost to separate each licensed company from all others
    
    # For each licensed company, find minimum cut to separate it from other licensed companies
    # Using BFS to find shortest path costs
    
    INF = float('inf')
    # dist[i][j] = minimum cost to separate licensed[i] from licensed[j]
    # We'll compute for each licensed company, the minimum cost to reach any other licensed company
    
    # Actually, we need to find minimum cut that separates all licensed companies from each other
    # This is equivalent to finding minimum spanning forest where each licensed company is in its own tree
    
    # Alternative approach: Find minimum cost edges to remove such that no two licensed companies are connected
    # This is the minimum multiway cut problem
    
    # For small k, we can use the isolation lemma approach
    # For each licensed company, compute minimum cut to separate it from all other licensed companies
    
    # We'll use a greedy approach: for each licensed company, find minimum cut to separate it from others
    # and add those edges to the solution
    
    # First, find all edges on paths between licensed companies
    # We need to find minimum cost set of edges whose removal disconnects all licensed companies
    
    # Using the isolation lemma: for each licensed company, find minimum cut to isolate it
    # The union of these cuts is a valid solution
    
    solution_edges = set()
    total_cost = 0
    
    # For each licensed company, find minimum cut to separate it from all other licensed companies
    for i in range(k):
        source = licensed[i]
        targets = set(licensed[:i] + licensed[i+1:])
        
        # Dijkstra to find shortest path from source to any target
        # The minimum cut is the minimum cost path
        dist = {v: INF for v in range(1, n+1)}
        dist[source] = 0
        parent = {}
        visited = set()
        
        import heapq
        heap = [(0, source)]
        
        found_target = None
        while heap:
            d, u = heapq.heappop(heap)
            if u in visited:
                continue
            visited.add(u)
            if u in targets:
                found_target = u
                break
            for v, w, edge_id in adj[u]:
                if v not in visited:
                    new_dist = d + w
                    if new_dist < dist[v]:
                        dist[v] = new_dist
                        parent[v] = (u, edge_id)
                        heapq.heappush(heap, (new_dist, v))
        
        if found_target is None:
            continue  # No path to other licensed companies
        
        # Backtrack to find the path and add edges
        curr = found_target
        while curr in parent:
            prev, edge_id = parent[curr]
            if edge_id not in solution_edges:
                solution_edges.add(edge_id)
                total_cost += edges[edge_id][2]
            curr = prev
    
    if total_cost <= B:
        print("YES")
        print(len(solution_edges))
        for edge_id in solution_edges:
            u, v, w = edges[edge_id]
            print(u, v)
    else:
        print("NO")

if __name__ == "__main__":
    solve()