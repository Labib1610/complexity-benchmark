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
    
    color = [-1] * (n + 1)
    
    def bfs(start):
        queue = deque()
        queue.append(start)
        color[start] = 1
        while queue:
            node = queue.popleft()
            current_color = color[node]
            next_color = 3 - current_color
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    color[neighbor] = next_color
                    queue.append(neighbor)
                elif color[neighbor] != next_color:
                    return False
        return True
    
    for i in range(1, n + 1):
        if color[i] == -1:
            if not bfs(i):
                print("NO")
                return
    
    print("YES")
    result = []
    for i in range(1, n + 1):
        if color[i] == -1:
            result.append("1")
        else:
            result.append(str(color[i]))
    print(" ".join(result))

if __name__ == "__main__":
    main()