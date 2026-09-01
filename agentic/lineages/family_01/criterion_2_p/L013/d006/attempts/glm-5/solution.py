import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # We need to assign values 0 or 1 to each node.
    # For an edge (u, v), we need val[u] + val[v] == 1 (mod 2).
    # This is a bipartite graph check with 2-coloring.
    
    color = [-1] * n
    possible = True
    
    for i in range(n):
        if color[i] == -1:
            # Start BFS from node i
            # To get lexicographically smallest assignment, we prefer color 0 (transformation 1)
            # for the starting node of each component.
            queue = deque([i])
            color[i] = 0
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        possible = False
                        break
                if not possible:
                    break
        if not possible:
            break
            
    if not possible:
        print("NO")
    else:
        # color[i] is 0 or 1. Transformation is color[i] + 1.
        print("YES")
        print(*(c + 1 for c in color))

if __name__ == '__main__':
    solve()