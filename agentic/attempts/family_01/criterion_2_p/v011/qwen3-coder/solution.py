import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    graph = [[] for _ in range(n + 1)]
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        graph[u].append(v)
        graph[v].append(u)
        index += 2
    
    # Color array: 0 means unvisited, 1 and 2 are the two colors/channels
    color = [0] * (n + 1)
    
    # Check if the graph is bipartite using BFS
    def bfs(start):
        queue = deque([start])
        color[start] = 1
        while queue:
            node = queue.popleft()
            current_color = color[node]
            next_color = 3 - current_color  # flips 1->2 and 2->1
            for neighbor in graph[node]:
                if color[neighbor] == 0:
                    color[neighbor] = next_color
                    queue.append(neighbor)
                elif color[neighbor] != next_color:
                    return False
        return True
    
    # Process each connected component
    for i in range(1, n + 1):
        if color[i] == 0:
            if not bfs(i):
                print("NO")
                return
    
    # If we reach here, a valid coloring exists
    # The coloring we have is already lexicographically smallest 
    # because we process nodes in order and always prefer color 1 over 2
    print("YES")
    print(' '.join(str(color[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    main()