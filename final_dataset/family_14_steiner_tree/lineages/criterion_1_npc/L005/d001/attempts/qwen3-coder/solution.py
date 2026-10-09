import sys
import heapq
from itertools import combinations

def dijkstra(graph, start, n):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    
    return dist

def main():
    n, m, t = map(int, sys.stdin.readline().split())
    delegated = list(map(int, sys.stdin.readline().split()))
    
    if t <= 1:
        print(0)
        return
    
    graph = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Compute shortest paths from each delegated language to all nodes
    dists = {}
    for lang in delegated:
        dists[lang] = dijkstra(graph, lang, n)
    
    # Create a complete graph on delegated languages with edge weights as shortest paths
    # Then find the minimum spanning tree of this complete graph
    # The weight of edge (u,v) is dists[u][v]
    
    # We need to find the minimum cost to connect all delegated languages
    # This is a Steiner tree problem, but since t <= 10, we can use dynamic programming
    
    # dp[mask][i] = minimum cost to connect languages in mask, rooted at delegated[i]
    # But actually, we want the minimum cost to connect all delegated languages,
    # which is the minimum spanning tree of the metric completion of delegated languages
    
    # Let's compute all pairwise distances between delegated languages
    k = len(delegated)
    distances = [[0] * k for _ in range(k)]
    
    for i in range(k):
        for j in range(k):
            if i != j:
                distances[i][j] = dists[delegated[i]][delegated[j]]
    
    # Now we need to find the minimum spanning tree of this complete graph
    # We can use Prim's or Kruskal's algorithm
    # But since k <= 10, we can also try all spanning trees, but that's too much
    # Let's use Prim's
    
    # Prim's algorithm for MST
    in_tree = [False] * k
    min_edge = [float('inf')] * k
    min_edge[0] = 0
    total_cost = 0
    
    for _ in range(k):
        # Find vertex with minimum edge weight not yet in tree
        u = -1
        for v in range(k):
            if not in_tree[v] and (u == -1 or min_edge[v] < min_edge[u]):
                u = v
        
        in_tree[u] = True
        total_cost += min_edge[u]
        
        # Update min_edge for vertices adjacent to u
        for v in range(k):
            if not in_tree[v] and distances[u][v] < min_edge[v]:
                min_edge[v] = distances[u][v]
    
    print(total_cost)

if __name__ == "__main__":
    main()