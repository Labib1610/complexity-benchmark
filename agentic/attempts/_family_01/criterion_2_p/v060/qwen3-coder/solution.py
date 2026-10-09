import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    graph = defaultdict(list)
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        graph[u].append(v)
        graph[v].append(u)
        index += 2
    
    # Color array: 0 = unvisited, 1 and 2 are the two colors
    color = [0] * (n + 1)
    
    # Check if the graph is bipartite and find the lexicographically smallest coloring
    for start in range(1, n + 1):
        if color[start] == 0:
            # BFS to color the component
            queue = deque()
            queue.append(start)
            color[start] = 1  # Start with color 1
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                next_color = 3 - current_color  # flips 1->2 and 2->1
                
                for neighbor in graph[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = next_color
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        print("NO")
                        return
    
    # If we reach here, a valid coloring exists
    print("YES")
    print(' '.join(str(color[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    main()