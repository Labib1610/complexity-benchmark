import sys
from collections import deque

# Increase recursion depth just in case, though we use iterative BFS
sys.setrecursionlimit(1 << 25)

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    iterator = iter(data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    adj = [[] for _ in range(n + 1)]
    degrees = [0] * (n + 1)
    
    edges = []
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
        degrees[u] += 1
        degrees[v] += 1
        
    # s[i] = 1 means C_i = d_i (Emitter for all incident edges)
    # s[i] = 2 means C_i = -d_i (Absorber for all incident edges)
    # We want lexicographically smallest s array, so we prefer s[i] = 1.
    # We try to assign s[i] = 1. If this creates a conflict (neighbor already 1), we must assign s[i] = 2.
    # This is equivalent to finding a valid 2-coloring of the conflict graph.
    
    s = [0] * (n + 1)
    possible = True
    
    for i in range(1, n + 1):
        if s[i] == 0:
            # Start BFS for this component
            queue = deque([i])
            s[i] = 1
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if s[v] == 0:
                        s[v] = 3 - s[u]
                        queue.append(v)
                    elif s[v] == s[u]:
                        possible = False
                        break
                if not possible:
                    break
        if not possible:
            break
            
    if not possible:
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, s[1:])))

if __name__ == '__main__':
    solve()