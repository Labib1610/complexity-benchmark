import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    critical = set()
    for i in range(t):
        critical.add(int(input_data[idx])); idx += 1
    
    edges = []
    for i in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        w = int(input_data[idx]); idx += 1
        edges.append((w, u, v))
    
    if t <= 1:
        print(0)
        return
    
    edges.sort()
    
    parent = list(range(n + 1))
    has_critical = [False] * (n + 1)
    for c in critical:
        has_critical[c] = True
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    total_cost = 0
    critical_count = t  # number of components containing critical vertices
    
    for w, u, v in edges:
        ru = find(u)
        rv = find(v)
        if ru == rv:
            continue
        if not has_critical[ru] and not has_critical[rv]:
            continue
        # At least one has critical
        parent[ru] = rv
        has_critical[rv] = has_critical[rv] or has_critical[ru]
        total_cost += w
        if has_critical[ru] and has_critical[rv]:
            critical_count -= 1
        if critical_count == 1:
            break
    
    print(total_cost)

solve()