import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1
    
    patent = [False] * (n + 1)
    for _ in range(t):
        p = int(data[idx]); idx += 1
        patent[p] = True
    
    edges = []
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        w = int(data[idx]); idx += 1
        edges.append((w, u, v))
    
    if t <= 1:
        print(0)
        return
    
    edges.sort()
    
    parent = list(range(n + 1))
    size = [1] * (n + 1)
    cnt = [1 if patent[i] else 0 for i in range(n + 1)]
    
    def find(x):
        root = x
        while parent[root] != root:
            root = parent[root]
        while parent[x] != root:
            parent[x], x = root, parent[x]
        return root
    
    total = 0
    for w, u, v in edges:
        ru = find(u)
        rv = find(v)
        if ru == rv:
            continue
        if size[ru] < size[rv]:
            ru, rv = rv, ru
        parent[rv] = ru
        size[ru] += size[rv]
        cnt[ru] += cnt[rv]
        if cnt[ru] == t:
            total += w
            break
        total += w
    
    print(total)

solve()