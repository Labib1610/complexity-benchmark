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
    
    color = [0] * (n + 1)
    
    for start in range(1, n + 1):
        if color[start] != 0:
            continue
        
        # BFS to check bipartiteness and assign colors
        # color 1 is preferred for lexicographically smallest
        color[start] = 1
        q = deque([start])
        ok = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = 3 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    ok = False
                    # We can break early, but need to drain queue or just set flag
                    # To ensure we don't miss other components, we continue checking
                    # but it's fine to break since answer is NO anyway
                    q.clear()
                    break
            if not ok:
                break
        
        if not ok:
            print("NO")
            return
    
    print("YES")
    print(' '.join(str(color[i]) for i in range(1, n + 1)))

solve()