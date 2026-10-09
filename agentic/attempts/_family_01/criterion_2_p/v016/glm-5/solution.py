import sys

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
    
    for start in range(1, n + 1):
        if color[start] != 0:
            continue
        
        # Try to color this component starting with color 1 at 'start'
        color[start] = 1
        stack = [start]
        comp_nodes = [start]
        ok = True
        
        while stack:
            u = stack.pop()
            cu = color[u]
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = 3 - cu
                    stack.append(v)
                    comp_nodes.append(v)
                elif color[v] == cu:
                    ok = False
                    # don't break immediately to keep traversal consistent,
                    # but we can break since we'll undo anyway
                    break
            if not ok:
                break
        
        if ok:
            continue
        
        # Undo coloring for this component
        for v in comp_nodes:
            color[v] = 0
        
        # Try coloring starting with color 2 at 'start'
        color[start] = 2
        stack = [start]
        comp_nodes = [start]
        ok = True
        
        while stack:
            u = stack.pop()
            cu = color[u]
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = 3 - cu
                    stack.append(v)
                    comp_nodes.append(v)
                elif color[v] == cu:
                    ok = False
                    break
            if not ok:
                break
        
        if not ok:
            print("NO")
            return
    
    print("YES")
    print(' '.join(map(str, color[1:])))

solve()