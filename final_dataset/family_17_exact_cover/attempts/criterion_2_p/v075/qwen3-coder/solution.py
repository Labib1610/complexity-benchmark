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
    graph = [[] for _ in range(q + 1)]  # 1-indexed
    
    for i in range(t):
        a = int(data[index])
        b = int(data[index + 1])
        index += 2
        edges.append((a, b))
        graph[a].append(i)
    
    # Try to find a matching that covers all q controllers
    # This is a maximum matching problem in a bipartite graph
    # Controllers: 1 to q
    # Platforms: q+1 to 2q (but we'll map them to 1 to q for simplicity in matching)
    
    match_controller = [None] * (q + 1)  # match_controller[c] = index of edge
    match_platform = [None] * (q + 1)    # match_platform[p] = index of edge
    
    def augment(c):
        if visited[c]:
            return False
        visited[c] = True
        
        for edge_idx in graph[c]:
            a, b = edges[edge_idx]
            p = b - q  # Map platform to 1..q
            
            if match_platform[p] is None:
                match_controller[c] = edge_idx
                match_platform[p] = edge_idx
                return True
        
        for edge_idx in graph[c]:
            a, b = edges[edge_idx]
            p = b - q  # Map platform to 1..q
            
            if match_platform[p] is not None:
                prev_edge = match_platform[p]
                prev_controller = edges[prev_edge][0]
                if augment(prev_controller):
                    match_controller[c] = edge_idx
                    match_platform[p] = edge_idx
                    return True
        return False
    
    matched = 0
    for c in range(1, q + 1):
        visited = [False] * (q + 1)
        if augment(c):
            matched += 1
    
    if matched < q:
        print("NO")
        return
    
    print("YES")
    for c in range(1, q + 1):
        edge_idx = match_controller[c]
        a, b = edges[edge_idx]
        print(a, b)

solve()