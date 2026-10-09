import sys
from itertools import combinations

def find_min_cost(n, m, t, priority_languages, translators):
    # Create a graph representation
    graph = {}
    for i in range(1, n + 1):
        graph[i] = []
    
    # Add edges to the graph
    for u, v, w in translators:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Function to find shortest paths from a source using Dijkstra's algorithm
    def dijkstra(source):
        import heapq
        dist = {i: float('inf') for i in range(1, n + 1)}
        dist[source] = 0
        pq = [(0, source)]
        
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
        
        return dist
    
    # Calculate minimum cost for each possible starting language
    min_total_cost = float('inf')
    
    # Try starting with each language
    for start_lang in range(1, n + 1):
        # Find shortest distances from start_lang to all other languages
        distances = dijkstra(start_lang)
        
        # Calculate cost to reach all priority languages
        total_cost = 0
        reachable = True
        
        # If we start with a priority language, no cost for that language
        for lang in priority_languages:
            if lang != start_lang:
                if distances[lang] == float('inf'):
                    reachable = False
                    break
                total_cost += distances[lang]
        
        if reachable:
            min_total_cost = min(min_total_cost, total_cost)
    
    return min_total_cost

# Read input
input_lines = []
for line in sys.stdin:
    input_lines.append(line.strip())

# Parse input
first_line = list(map(int, input_lines[0].split()))
n, m, t = first_line[0], first_line[1], first_line[2]

priority_languages = list(map(int, input_lines[1].split()))

translators = []
for i in range(2, 2 + m):
    u, v, w = map(int, input_lines[i].split())
    translators.append((u, v, w))

# Solve and output
result = find_min_cost(n, m, t, priority_languages, translators)
print(result)