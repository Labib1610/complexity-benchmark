import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    # Solutions to 3x_u + 3x_v - 2x_u x_v = 5
    # (x_u, x_v) can be (1, 2) or (2, 1)
    
    # We use BFS to assign values.
    # 0: unvisited, 1: assigned value 1, 2: assigned value 2
    color = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # Start BFS from node i
            # To get lexicographically smallest, we prefer assigning 1 to the smallest index
            # Since we iterate i from 1 to n, and i is the smallest in its component,
            # assigning 1 to i is optimal.
            queue = deque([i])
            color[i] = 1
            
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
    
    print("YES")
    print(*(color[1:]))

if __name__ == '__main__':
    solve()