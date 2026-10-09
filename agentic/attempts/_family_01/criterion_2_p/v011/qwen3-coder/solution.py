import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    edges = []
    graph = defaultdict(list)
    
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-based indexing
        v = int(data[index+1]) - 1
        edges.append((u, v))
        graph[u].append(v)
        graph[v].append(u)
        index += 2
    
    # Color array: 0 means unvisited, 1 and 2 are the two colors
    color = [0] * n
    visited = [False] * n
    
    # Check if bipartite using BFS for each component
    for start in range(n):
        if not visited[start]:
            queue = deque()
            queue.append(start)
            color[start] = 1  # Assign color 1 to the starting node
            while queue:
                node = queue.popleft()
                if visited[node]:
                    continue
                visited[node] = True
                
                for neighbor in graph[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = 3 - color[node]  # Assign opposite color
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        print("NO")
                        return
    
    # If we reach here, the graph is bipartite
    # The color array already represents the lexicographically smallest assignment
    # because we start with color 1 for the first node in each component
    
    # Convert colors back to 1 and 2 as per problem statement
    result = []
    for c in color:
        if c == 0:
            result.append('1')  # Unconnected nodes can be assigned to bus 1
        else:
            result.append(str(c))
            
    print("YES")
    print(" ".join(result))

if __name__ == "__main__":
    main()