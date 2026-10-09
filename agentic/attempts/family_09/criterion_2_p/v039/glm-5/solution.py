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
    
    # Bipartition the graph
    color = [-1] * (n + 1)
    dept0 = []
    dept1 = []
    
    for start in range(1, n + 1):
        if color[start] == -1:
            color[start] = 0
            queue = deque([start])
            while queue:
                u = queue.popleft()
                if color[u] == 0:
                    dept0.append(u)
                else:
                    dept1.append(u)
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        queue.append(v)
    
    # Choose the larger department
    if len(dept0) >= len(dept1):
        chosen = dept0
    else:
        chosen = dept1
    
    if len(chosen) >= k:
        print("YES")
        print(' '.join(map(str, chosen[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()