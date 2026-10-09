import sys
from collections import defaultdict, deque

def solve():
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
    
    graph = defaultdict(list)
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index+1]) - 1
        graph[u].append(v)
        graph[v].append(u)
        index += 2
        
    color = [-1] * n
    
    def bfs(start):
        queue = deque()
        queue.append(start)
        color[start] = 0
        while queue:
            node = queue.popleft()
            current_color = color[node]
            next_color = 1 - current_color
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    color[neighbor] = next_color
                    queue.append(neighbor)
                elif color[neighbor] == current_color:
                    return False
        return True
    
    for i in range(n):
        if color[i] == -1:
            if not bfs(i):
                print("NO")
                return
                
    print("YES")
    result = []
    for i in range(n):
        if color[i] == 0:
            result.append("1")
        else:
            result.append("2")
    print(" ".join(result))

solve()