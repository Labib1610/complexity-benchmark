import sys
from collections import deque, defaultdict

def read_input():
    n, m, s, t, B = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((u, v, w))
    return n, m, s, t, B, edges

def is_connected(graph, n, s, t):
    if s == t:
        return True
    visited = [False] * (n + 1)
    queue = deque([s])
    visited[s] = True
    while queue:
        node = queue.popleft()
        if node == t:
            return True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return False

def build_graph(n, edges, exclude_indices):
    graph = defaultdict(list)
    for i, (u, v, w) in enumerate(edges):
        if i not in exclude_indices:
            graph[u].append(v)
            graph[v].append(u)
    return graph

def solve():
    n, m, s, t, B, edges = read_input()
    
    # Try all subsets of edges with total weight <= B
    # We'll use a greedy approach: sort edges by weight and try to include cheaper edges last (keep them active)
    # This means we shut down the most expensive edges first, but we need to be more systematic
    
    # Actually, let's think differently. We want to find a subset of edges to shut down such that:
    # 1. Total cost <= B
    # 2. s and t are disconnected in the remaining graph
    
    # This is essentially: find a minimum cut between s and t, and if its cost <= B, we can shut down those edges
    # But we don't need the minimum cut, any cut with cost <= B works.
    
    # Let's try a different approach: since m is up to 20, we can enumerate all subsets
    # But 2^20 is about 1M, which might be too slow with graph construction each time
    # Actually, let's check the constraints. The problem doesn't specify, but example has m=4.
    # Let's assume m <= 20 based on typical contest constraints for exponential solutions.
    
    # Enumerate all subsets
    for mask in range(1 << m):
        selected_edges = []
        total_cost = 0
        selected_indices = set()
        for i in range(m):
            if mask & (1 << i):
                selected_edges.append(edges[i])
                total_cost += edges[i][2]
                selected_indices.add(i)
        
        if total_cost > B:
            continue
            
        # Build graph with non-selected edges
        graph = build_graph(n, edges, selected_indices)
        
        # Check if s and t are disconnected
        if not is_connected(graph, n, s, t):
            print("YES")
            print(len(selected_edges))
            for u, v, w in selected_edges:
                print(u, v)
            return
    
    print("NO")

if __name__ == "__main__":
    solve()