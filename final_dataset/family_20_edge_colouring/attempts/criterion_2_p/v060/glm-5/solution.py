import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    nT = int(next(it))
    nP = int(next(it))
    m = int(next(it))
    
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
    
    degT = [0] * (nT + 1)
    degP = [0] * (nP + 1)
    for u, v in edges:
        degT[u] += 1
        degP[v] += 1
    
    K = 0
    for i in range(1, nT + 1):
        if degT[i] > K:
            K = degT[i]
    for i in range(1, nP + 1):
        if degP[i] > K:
            K = degP[i]
    
    if m == 0:
        out = ["YES", ""]
        sys.stdout.write("\n".join(out))
        return
    
    adjT = [[] for _ in range(nT + 1)]
    adjP = [[] for _ in range(nP + 1)]
    for i, (u, v) in enumerate(edges):
        adjT[u].append(i)
        adjP[v].append(i)
    
    color = [0] * m
    usedT = [0] * (nT + 1)
    usedP = [0] * (nP + 1)
    
    for u in range(1, nT + 1):
        if not adjT[u]:
            continue
        for idx in adjT[u]:
            v = edges[idx][1]
            c = 1
            while usedT[u] & (1 << c) or usedP[v] & (1 << c):
                c += 1
            color[idx] = c
            usedT[u] |= (1 << c)
            usedP[v] |= (1 << c)
    
    out = ["YES"]
    out.append(" ".join(str(c) for c in color))
    sys.stdout.write("\n".join(out))

solve()