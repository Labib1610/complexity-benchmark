import sys
from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    q = int(data[0])
    t = int(data[1])
    
    if t == 0:
        if q == 0:
            print("YES")
        else:
            print("NO")
        return
    
    index = 2
    edges = []
    adj = defaultdict(list)
    
    for i in range(t):
        a = int(data[index])
        b = int(data[index+1])
        index += 2
        edges.append((a, b))
        adj[a].append(i)
        adj[b].append(i)
    
    # Try to find a perfect matching using BFS-based augmenting paths
    # This is essentially finding a maximum matching in a bipartite graph
    
    # Flowers: 1 to q
    # Moths: q+1 to 2*q
    # Nodes: flowers on left, moths on right
    
    match_flower = [0] * (q + 1)  # match_flower[f] = moth matched to flower f, 0 if unmatched
    match_moth = [0] * (q + 1)    # match_moth[m] = flower matched to moth m+q, 0 if unmatched
    
    def bfs():
        dist = [0] * (q + 1)
        queue = deque()
        
        for f in range(1, q + 1):
            if match_flower[f] == 0:
                dist[f] = 0
                queue.append(f)
            else:
                dist[f] = float('inf')
        
        dist[0] = float('inf')
        
        while queue:
            f = queue.popleft()
            
            if dist[f] < dist[0]:
                for eid in adj[f]:
                    a, b = edges[eid]
                    m = b - q  # Convert moth id to 1-based index
                    
                    if dist[match_moth[m]] == float('inf'):
                        dist[match_moth[m]] = dist[f] + 1
                        queue.append(match_moth[m])
        
        return dist[0] != float('inf')
    
    def dfs(f):
        if f == 0:
            return True
            
        for eid in adj[f]:
            a, b = edges[eid]
            m = b - q
            
            if dist[match_moth[m]] == dist[f] + 1:
                if dfs(match_moth[m]):
                    match_flower[f] = b
                    match_moth[m] = f
                    return True
        
        dist[f] = float('inf')
        return False
    
    matching = 0
    while bfs():
        for f in range(1, q + 1):
            if match_flower[f] == 0:
                if dfs(f):
                    matching += 1
    
    if matching == q:
        print("YES")
        for f in range(1, q + 1):
            print(f, match_flower[f])
    else:
        print("NO")

solve()