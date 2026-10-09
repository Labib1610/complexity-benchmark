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
        u = int(data[index]) - 1  # Convert to 0-based indexing
        v = int(data[index+1]) - 1
        index += 2
        graph[u].append(v)
        graph[v].append(u)
    
    color = [-1] * n  # -1 means unvisited, 0 and 1 are the two colors
    
    def bfs(start):
        queue = deque()
        queue.append(start)
        color[start] = 0
        while queue:
            node = queue.popleft()
            current_color = color[node]
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - current_color
                    queue.append(neighbor)
                elif color[neighbor] == current_color:
                    return False
        return True
    
    for i in range(n):
        if color[i] == -1:
            if not bfs(i):
                print("NO")
                return
    
    # Convert colors to filter types (0 -> 1, 1 -> 2)
    result = []
    for c in color:
        if c == 0:
            result.append('1')
        else:
            result.append('2')
    
    print("YES")
    print(' '.join(result))

if __name__ == "__main__":
    main()