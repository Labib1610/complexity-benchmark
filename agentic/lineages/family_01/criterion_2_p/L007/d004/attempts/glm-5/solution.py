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
    
    # We need to assign values 1 or 2 such that for every edge (u, v),
    # |s[u]^2 - s[v]^2| = 3.
    # Since 1^2 = 1 and 2^2 = 4, |1 - 4| = 3.
    # So connected nodes must have different values (one is 1, other is 2).
    # This is a bipartite graph check.
    
    color = [0] * (n + 1)  # 0: uncolored, 1: color 1, 2: color 2
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # BFS to color this component
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