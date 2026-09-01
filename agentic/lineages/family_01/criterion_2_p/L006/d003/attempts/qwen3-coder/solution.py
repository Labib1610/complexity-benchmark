import sys
from collections import defaultdict, deque

def main():
    import sys
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
        u = int(data[index]) - 1
        v = int(data[index+1]) - 1
        edges.append((u, v))
        graph[u].append(v)
        graph[v].append(u)
        index += 2
    
    # 0 means unset, 1 and 2 are the two pressure settings
    color = [0] * n
    visited = [False] * n
    
    # Check each component
    for start in range(n):
        if visited[start]:
            continue
            
        # BFS to check bipartiteness and assign values
        queue = deque()
        queue.append(start)
        color[start] = 1
        visited[start] = True
        
        while queue:
            node = queue.popleft()
            current_color = color[node]
            next_color = 3 - current_color  # flips 1->2 and 2->1
            
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    color[neighbor] = next_color
                    queue.append(neighbor)
                elif color[neighbor] != next_color:
                    print("NO")
                    return
    
    # Verify all edges have sum 3
    for u, v in edges:
        if color[u] + color[v] != 3:
            print("NO")
            return
            
    print("YES")
    result = []
    for c in color:
        result.append(str(c))
    print(" ".join(result))

if __name__ == "__main__":
    main()