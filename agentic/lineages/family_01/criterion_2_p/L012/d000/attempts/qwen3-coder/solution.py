import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    graph = defaultdict(list)
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index+1]) - 1
        graph[u].append(v)
        graph[v].append(u)
        index += 2
    
    # Color array: 0 means unvisited, 1 and 2 are the two colors
    color = [0] * n
    visited = [False] * n
    
    # Check each component
    for start in range(n):
        if visited[start]:
            continue
            
        # BFS to check bipartiteness and assign colors
        queue = deque()
        queue.append(start)
        color[start] = 1
        
        while queue:
            node = queue.popleft()
            if visited[node]:
                continue
            visited[node] = True
            
            for neighbor in graph[node]:
                if color[neighbor] == 0:
                    color[neighbor] = 3 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    print("NO")
                    return
        
    # If we reach here, the graph is bipartite
    # We need to ensure lexicographically smallest assignment
    # That means we want earlier nodes to have color 1 if possible
    # Our coloring already ensures this since we start with color 1
    
    print("YES")
    result = []
    for i in range(n):
        if color[i] == 1:
            result.append("1")
        else:
            result.append("2")
    print(" ".join(result))

if __name__ == "__main__":
    main()