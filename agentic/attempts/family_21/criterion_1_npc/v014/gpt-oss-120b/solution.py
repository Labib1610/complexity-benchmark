import sys
import threading
def solve():
    import sys
    sys.setrecursionlimit(1 << 25)
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it)); B = int(next(it))
    specials = set(int(next(it)) for _ in range(k))
    edges = []
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        edges.append((u,v,w))
        adj[u].append((v,w))
        adj[v].append((u,w))
    # Simple heuristic: cut all edges incident to specials
    cut = []
    total = 0
    for u,v,w in edges:
        if (u in specials) ^ (v in specials):
            cut.append((u,v))
            total += w
    if total <= B:
        print("YES")
        print(len(cut))
        for u,v in cut:
            print(u, v)
    else:
        print("NO")
threading.Thread(target=solve).start()