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
    deg = [0] * (n + 1)
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
        deg[u] += 1
        deg[v] += 1
    
    # r[i] = 0: unassigned, 1: state 1, 2: state 2
    r = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if r[i] == 0:
            # BFS to assign component
            queue = deque([i])
            r[i] = 1  # Try to assign 1 first (lexicographically smallest)
            component = [i]
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if r[v] == 0:
                        r[v] = 3 - r[u]  # Assign opposite state
                        queue.append(v)
                        component.append(v)
            
            # Check if this component is valid
            valid = True
            for u in component:
                # Check constraint: deg[u] * r[u] must be even
                if (deg[u] * r[u]) % 2 != 0:
                    valid = False
                    break
            
            if not valid:
                # Try the other assignment
                queue = deque([i])
                r[i] = 2
                while queue:
                    u = queue.popleft()
                    for v in adj[u]:
                        if r[v] != r[u]:
                            continue
                        r[v] = 3 - r[u]
                        queue.append(v)
                
                # Check again
                for u in component:
                    if (deg[u] * r[u]) % 2 != 0:
                        print("NO")
                        return
    
    # Verify the solution
    E = 0
    for i in range(1, n + 1):
        E += 6 * deg[i] * r[i] * r[i]
    
    for u in range(1, n + 1):
        for v in adj[u]:
            if u <= v:  # Count each edge once
                E -= 14 * r[u] * r[v]
    
    if E == 2 * m:
        print("YES")
        print(' '.join(map(str, r[1:])))
    else:
        print("NO")

solve()