from collections import defaultdict, deque

def find_maximum_matching(q, pairs):
    # Build graph
    graph = defaultdict(list)
    for a, b in pairs:
        graph[a].append(b)
    
    # Hopcroft-Karp implementation for maximum bipartite matching
    pair_u = {}
    pair_v = {}
    dist = {}
    
    def bfs():
        queue = deque()
        for u in range(1, q + 1):
            if u not in pair_u:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float('inf')
        dist[None] = float('inf')
        
        while queue:
            u = queue.popleft()
            if dist[u] < dist[None]:
                for v in graph[u]:
                    if v not in pair_v:
                        pair_v[v] = u
                        pair_u[u] = v
                        dist[None] = dist[u] + 1
                        return True
                    else:
                        pu = pair_v[v]
                        if dist[pu] == float('inf'):
                            dist[pu] = dist[u] + 1
                            queue.append(pu)
        return False
    
    def dfs(u):
        if u is not None:
            for v in graph[u]:
                if pair_v.get(v) == u:
                    continue
                if dist.get(pair_v.get(v)) == dist[u] + 1:
                    if dfs(pair_v.get(v)):
                        pair_v[v] = u
                        pair_u[u] = v
                        return True
            dist[u] = float('inf')
            return False
        return True
    
    matching = 0
    while bfs():
        for u in range(1, q + 1):
            if u not in pair_u:
                if dfs(u):
                    matching += 1
    
    if matching == q:
        print("YES")
        for u in range(1, q + 1):
            print(u, pair_u[u])
    else:
        print("NO")

# Read input
q, t = map(int, input().split())
pairs = []
for _ in range(t):
    a, b = map(int, input().split())
    pairs.append((a, b))

find_maximum_matching(q, pairs)