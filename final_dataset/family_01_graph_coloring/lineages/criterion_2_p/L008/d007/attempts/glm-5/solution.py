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
    degree = [0] * n
    
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
        degree[u] += 1
        degree[v] += 1
    
    # c[i] = 1 means target_in = 0
    # c[i] = 2 means target_in = degree[i]
    # We want to find c such that the graph is bipartite with edges going from 1 to 2.
    # This is equivalent to checking if the graph is bipartite.
    
    color = [-1] * n
    possible = True
    
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            q = deque([i])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        possible = False
                        break
                if not possible:
                    break
        if not possible:
            break
            
    if not possible:
        print("NO")
        return
    
    # Check if the 0-1 coloring is valid (edges go from 0 to 1)
    # If valid, this is lexicographically smallest (0 maps to c=1)
    # If not valid, we must flip (edges go from 1 to 0)
    # But if not valid, the 1-0 coloring must be valid (since graph is bipartite)
    
    valid_01 = True
    for u in range(n):
        if color[u] == 0:
            for v in adj[u]:
                if color[v] == 0:
                    valid_01 = False
                    break
            if not valid_01:
                break
    
    if valid_01:
        # color 0 -> c=1, color 1 -> c=2
        result = [1 if c == 0 else 2 for c in color]
    else:
        # color 0 -> c=2, color 1 -> c=1
        result = [2 if c == 0 else 1 for c in color]
    
    print("YES")
    print(' '.join(map(str, result)))

if __name__ == '__main__':
    solve()