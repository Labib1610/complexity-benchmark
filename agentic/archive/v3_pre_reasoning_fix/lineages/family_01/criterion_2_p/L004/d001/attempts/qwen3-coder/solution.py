import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    
    color = [0] * (n + 1)  # 0 means unvisited, 1 and 2 are the two colors/environments
    
    # Check if bipartite using BFS for all components
    for start in range(1, n + 1):
        if color[start] == 0:
            queue = deque()
            queue.append(start)
            color[start] = 1  # Start coloring with 1
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                next_color = 2 if current_color == 1 else 1
                
                for neighbor in graph[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = next_color
                        queue.append(neighbor)
                    elif color[neighbor] != next_color:
                        print("NO")
                        return
    
    # If we reach here, it's bipartite
    print("YES")
    # For lexicographically smallest assignment, we prefer assigning 1 whenever possible
    # Our coloring already ensures this since we start with 1
    result = []
    for i in range(1, n + 1):
        result.append(str(color[i]))
    print(" ".join(result))

if __name__ == "__main__":
    main()