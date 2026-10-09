import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(10**6)
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    adj = defaultdict(list)
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        adj[u].append(v)
        adj[v].append(u)
        index += 2
    
    color = [0] * (n + 1)  # 0: unvisited, 1: color 1, 2: color 2
    
    # Check each component
    for start in range(1, n + 1):
        if color[start] == 0:
            # BFS to check bipartiteness and assign colors
            queue = deque()
            queue.append(start)
            color[start] = 1
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                next_color = 2 if current_color == 1 else 1
                
                for neighbor in adj[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = next_color
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        print("NO")
                        return
    
    # If we reach here, the graph is bipartite
    print("YES")
    result = []
    for i in range(1, n + 1):
        result.append(str(color[i]))
    print(" ".join(result))

if __name__ == "__main__":
    main()