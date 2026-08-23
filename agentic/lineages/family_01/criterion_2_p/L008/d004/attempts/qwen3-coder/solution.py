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
        u = int(data[index]) - 1  # Convert to 0-indexed
        v = int(data[index+1]) - 1
        edges.append((u, v))
        graph[u].append(v)
        graph[v].append(u)
        index += 2
    
    # For each component, we need to check bipartiteness
    color = [-1] * n  # -1: unvisited, 0: color 0, 1: color 1
    result = [1] * n  # Default assignment
    
    for i in range(n):
        if color[i] == -1:
            queue = deque()
            queue.append(i)
            color[i] = 0
            result[i] = 1  # Assign mode 1 to color 0
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - current_color
                        result[neighbor] = 2 if color[neighbor] == 1 else 1
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        print("NO")
                        return
    
    # Verify all constraints
    for u, v in edges:
        if result[u] * result[v] != 2:
            print("NO")
            return
    
    print("YES")
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()