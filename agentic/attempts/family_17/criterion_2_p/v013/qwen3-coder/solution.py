import sys
from collections import defaultdict, deque

def main():
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
    
    edges = []
    index = 2
    for _ in range(t):
        a = int(data[index])
        b = int(data[index+1])
        edges.append((a, b))
        index += 2
    
    if q == 0:
        print("YES")
        return
    
    # Build graph for matching
    graph = defaultdict(list)
    for i in range(t):
        a, b = edges[i]
        graph[a].append(i)
    
    # Try to find a matching that covers all 2*q assets
    # This is a bipartite matching problem
    # Controllers: 1 to q
    # Platforms: q+1 to 2*q
    
    match_controller = [-1] * (q + 1)  # match_controller[c] = index of edge
    match_platform = [-1] * (q + 1)    # match_platform[p - q] = index of edge
    
    def bfs():
        queue = deque()
        dist = [-1] * (q + 1)
        for c in range(1, q + 1):
            if match_controller[c] == -1:
                dist[c] = 0
                queue.append(c)
            else:
                dist[c] = -1
        dist[0] = -1  # dummy node
        
        while queue:
            c = queue.popleft()
            if dist[c] < dist[0]:  # dist[0] is infinity initially
                for edge_idx in graph[c]:
                    a, b = edges[edge_idx]
                    p = b - q
                    if match_platform[p] == -1:
                        dist[0] = dist[c] + 1
                    else:
                        next_c = edges[match_platform[p]][0]
                        if dist[next_c] == -1:
                            dist[next_c] = dist[c] + 1
                            queue.append(next_c)
        return dist[0] != -1
    
    def dfs(c):
        if c == 0:
            return True
        for edge_idx in graph[c]:
            a, b = edges[edge_idx]
            p = b - q
            next_c = 0 if match_platform[p] == -1 else edges[match_platform[p]][0]
            if dist[next_c] == dist[c] + 1 and dfs(next_c):
                match_controller[c] = edge_idx
                match_platform[p] = edge_idx
                return True
        dist[c] = -1
        return False
    
    # Hopcroft-Karp implementation
    matching = 0
    while bfs():
        for c in range(1, q + 1):
            if match_controller[c] == -1:
                if dfs(c):
                    matching += 1
    
    if matching == q:
        print("YES")
        for c in range(1, q + 1):
            edge_idx = match_controller[c]
            a, b = edges[edge_idx]
            print(a, b)
    else:
        print("NO")

if __name__ == "__main__":
    main()