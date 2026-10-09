import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)
    visited = [False] * (n + 1)
    
    for start in range(1, n + 1):
        if not visited[start]:
            queue = deque([start])
            visited[start] = True
            color[start] = 1
            count = [0, 0]
            count[0] = 1
            
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        color[v] = 3 - color[u]
                        count[color[v] - 1] += 1
                        queue.append(v)
            
            if count[0] >= count[1]:
                larger_color = 1
            else:
                larger_color = 2
            
            for i in range(1, n + 1):
                if visited[i] and color[i] == larger_color:
                    k -= 1
                    if k == 0:
                        print("YES")
                        return
                    print(i, end=" ")
    
    print("NO")

if __name__ == "__main__":
    solve()