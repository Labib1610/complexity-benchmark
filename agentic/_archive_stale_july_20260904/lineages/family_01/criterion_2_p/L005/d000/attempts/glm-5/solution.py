import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * n
    is_possible = True
    
    for i in range(n):
        if color[i] == 0:
            color[i] = 1
            queue = deque([i])
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        is_possible = False
                        break
                if not is_possible:
                    break
        if not is_possible:
            break
    
    if not is_possible:
        print("NO")
    else:
        print("YES")
        print(*(color[i] for i in range(n)))

if __name__ == "__main__":
    solve()