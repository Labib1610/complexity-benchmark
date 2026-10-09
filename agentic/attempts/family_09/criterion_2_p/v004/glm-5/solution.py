import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
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
    color = [0] * (n + 1)
    sets = [[], []]
    valid = True
    
    for start in range(1, n + 1):
        if color[start] == 0:
            color[start] = 1
            queue = deque([start])
            while queue:
                u = queue.popleft()
                sets[color[u] - 1].append(u)
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        queue.append(v)
    
    # Choose the larger set
    if len(sets[0]) >= len(sets[1]):
        chosen = sets[0]
    else:
        chosen = sets[1]
    
    if len(chosen) >= k:
        print("YES")
        print(' '.join(map(str, chosen[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()