import sys
from collections import deque

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
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
        # BFS to find component and check bipartiteness
        comp = []
        q = deque()
        color[start] = 1
        q.append(start)
        comp.append(start)
        ok = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = 3 - color[u]
                    q.append(v)
                    comp.append(v)
                elif color[v] == color[u]:
                    ok = False
        if not ok:
            possible = False
            break
        # We want lexicographically smallest: try to assign color 1 to the smallest index in component.
        # Since we started BFS from the smallest uncolored index, it already has color 1.
        # But we need to ensure that flipping the component (if it gives smaller lex order) is considered.
        # Actually, since the smallest index in the component is 'start' and it has color 1, 
        # flipping would make it color 2, which is lexicographically larger. So current assignment is optimal.
        pass
    
    if not possible:
        sys.stdout.write("NO\n")
        return
    
    # Verify all edges (safety, though BFS already checked)
    # Not needed if we trust BFS, but let's keep it for safety.
    # Actually BFS already checks, so skip.
    
    sys.stdout.write("YES\n")
    out = []
    for i in range(1, n + 1):
        out.append(str(color[i]))
    sys.stdout.write(" ".join(out) + "\n")

solve()