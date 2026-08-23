import sys
from collections import deque

def solve():
    input_data = sys.stdin.buffer.read().split()
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
    possible = True
    
    for start in range(1, n + 1):
        if color[start] != 0:
            continue
        # Try to color start with 1
        color[start] = 1
        queue = deque([start])
        ok = True
        while queue:
            u = queue.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = 3 - cu
                    queue.append(v)
                elif color[v] == cu:
                    ok = False
                    # We can break early, but need to drain queue or use flag
                    # Let's just set flag and break out
                    break
            if not ok:
                break
        
        if not ok:
            # Try to color start with 2
            # Reset colors for this component
            # We need to clear all nodes that were colored in this attempt
            # To do that efficiently, we can re-run BFS and collect visited nodes
            # But simpler: re-run with a fresh approach using a visited list
            # Let's reset by re-traversing
            # Actually, let's just reset the whole component by BFS from start
            # and set color to 0, then try color 2
            
            # Reset component
            queue2 = deque([start])
            color[start] = 0
            while queue2:
                u = queue2.popleft()
                for v in adj[u]:
                    if color[v] != 0:
                        color[v] = 0
                        queue2.append(v)
            
            # Now try color 2
            color[start] = 2
            queue = deque([start])
            ok = True
            while queue:
                u = queue.popleft()
                cu = color[u]
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - cu
                        queue.append(v)
                    elif color[v] == cu:
                        ok = False
                        break
                if not ok:
                    break
            
            if not ok:
                possible = False
                break
    
    if not possible:
        sys.stdout.write("NO\n")
        return
    
    sys.stdout.write("YES\n")
    # Output colors 1..n
    out = ' '.join(str(color[i]) for i in range(1, n + 1))
    sys.stdout.write(out + '\n')

solve()