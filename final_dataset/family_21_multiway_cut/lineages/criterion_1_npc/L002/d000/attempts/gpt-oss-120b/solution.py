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
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        edges.append((w, u, v))
    # Simple heuristic: block all edges incident to specials
    blocked = []
    total = 0
    for w,u,v in edges:
        if u in specials or v in specials:
            blocked.append((u,v,w))
            total += w
    if total <= B:
        print("YES")
        print(len(blocked))
        for u,v,_ in blocked:
            print(u, v)
    else:
        print("NO")

def main():
    solve()

threading.Thread(target=main).start()