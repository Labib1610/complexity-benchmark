from collections import defaultdict, deque

def find_maximum_matching(graph, n):
    # Hopcroft-Karp algorithm for maximum bipartite matching
    pair_u = [0] * (n + 1)
    pair_v = [0] * (n + 1)
    dist = [0] * (n + 1)
    
    def bfs():
        queue = deque()
        for u in range(1, n + 1):
            if pair_u[u] == 0:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float('inf')
        dist[0] = float('inf')
        
        while queue:
            u = queue.popleft()
            if dist[u] < dist[0]:
                for v in graph[u]:
                    if dist[pair_v[v]] == float('inf'):
                        dist[pair_v[v]] = dist[u] + 1
                        queue.append(pair_v[v])
        return dist[0] != float('inf')
    
    def dfs(u):
        if u != 0:
            for v in graph[u]:
                if dist[pair_v[v]] == dist[u] + 1:
                    if dfs(pair_v[v]):
                        pair_v[v] = u
                        pair_u[u] = v
                        return True
            dist[u] = float('inf')
            return False
        return True
    
    matching = 0
    while bfs():
        for u in range(1, n + 1):
            if pair_u[u] == 0 and dfs(u):
                matching += 1
    return matching, pair_u

def main():
    q, t = map(int, input().split())
    
    # Build bipartite graph
    graph = defaultdict(list)
    for _ in range(t):
        a, b = map(int, input().split())
        graph[a].append(b - q)  # Convert bay ID to 1-based index in V set
    
    # Find maximum matching
    matching_size, pair_u = find_maximum_matching(graph, q)
    
    if matching_size != q:
        print("NO")
    else:
        print("YES")
        for drone in range(1, q + 1):
            bay = pair_u[drone]
            print(drone, bay + q)

if __name__ == "__main__":
    main()