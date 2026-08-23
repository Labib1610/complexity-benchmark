import sys
from sys import stdin

def solve():
    input_data = stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n+1)
    
    for start in range(1, n+1):
        if color[start] == 0:
            # BFS to find component and check bipartiteness
            # Try color[start] = 1 (lexicographically smallest)
            color[start] = 1
            queue = [start]
            head = 0
            comp = [start]
            ok = True
            while head < len(queue) and ok:
                u = queue[head]
                head += 1
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        queue.append(v)
                        comp.append(v)
                    elif color[v] == color[u]:
                        ok = False
                        break
            
            if not ok:
                # Try flipping: color[start] = 2
                for node in comp:
                    color[node] = 0
                color[start] = 2
                queue = [start]
                head = 0
                ok = True
                while head < len(queue) and ok:
                    u = queue[head]
                    head += 1
                    for v in adj[u]:
                        if color[v] == 0:
                            color[v] = 3 - color[u]
                            queue.append(v)
                        elif color[v] == color[u]:
                            ok = False
                            break
                
                if not ok:
                    print("NO")
                    return
    
    print("YES")
    print(' '.join(str(color[i]) for i in range(1, n+1)))

solve()