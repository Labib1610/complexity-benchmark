import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    q = int(data[0])
    t = int(data[1])
    
    edges = []
    index = 2
    for _ in range(t):
        a = int(data[index])
        b = int(data[index+1])
        edges.append((a, b))
        index += 2
    
    # Build graph
    # Controllers: 1 to q
    # Platforms: q+1 to 2*q
    # We can model this as a bipartite graph matching problem
    # Let's use a standard max matching algorithm (Hopcroft-Karp style)
    
    # Adjacency list for controllers to platforms
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
    
    # Try to find a perfect matching
    # Using a simplified Ford-Fulkerson / BFS-based approach for bipartite matching
    
    match_controller = [0] * (q + 1)  # match_controller[c] = matched platform
    match_platform = [0] * (q + 1)    # match_platform[p - q] = matched controller
    
    def bfs():
        queue = deque()
        dist = [-1] * (q + 1)
        for c in range(1, q + 1):
            if match_controller[c] == 0:
                dist[c] = 0
                queue.append(c)
        
        found = False
        while queue:
            c = queue.popleft()
            for p in graph[c]:
                pc = p - q  # platform index in 1..q
                mate = match_platform[pc]
                if mate == 0:
                    found = True
                elif dist[mate] == -1:
                    dist[mate] = dist[c] + 1
                    queue.append(mate)
        return found
    
    def dfs(c):
        for p in graph[c]:
            pc = p - q
            mate = match_platform[pc]
            if mate == 0 or (dist[mate] == dist[c] + 1 and dfs(mate)):
                match_controller[c] = p
                match_platform[pc] = c
                return True
        return False
    
    matching = 0
    while bfs():
        for c in range(1, q + 1):
            if match_controller[c] == 0:
                if dfs(c):
                    matching += 1
    
    if matching == q:
        print("YES")
        for c in range(1, q + 1):
            print(c, match_controller[c])
    else:
        print("NO")

if __name__ == "__main__":
    main()