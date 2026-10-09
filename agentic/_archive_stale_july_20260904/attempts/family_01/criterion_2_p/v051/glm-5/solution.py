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
    
    # Sort adjacency lists to process neighbors in increasing order
    for i in range(1, n + 1):
        adj[i].sort()
    
    color = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # BFS starting from i
            # We want lexicographically smallest, so start with color 1
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
    print(' '.join(map(str, color[1:])))

if __name__ == '__main__':
    solve()