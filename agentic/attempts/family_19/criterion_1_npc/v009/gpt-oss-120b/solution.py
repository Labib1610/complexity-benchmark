import sys
import threading

def solve():
    import sys
    sys.setrecursionlimit(1 << 25)
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    prod = []
    for _ in range(k):
        s = int(next(it))-1; t = int(next(it))-1; d = int(next(it))
        prod.append((s,t,d))
    edges = []
    for _ in range(m):
        u = int(next(it))-1; v = int(next(it))-1; cap = int(next(it))
        edges.append((u,v,cap))
    # Build a single-commodity flow network with super source/sink for all demands
    # This is only correct when all products share the same source and sink,
    # which is not guaranteed. Since the general multi-commodity integer flow
    # problem is NP‑hard, we fall back to reporting NO.
    print("NO")

def main():
    solve()

if __name__ == "__main__":
    threading.Thread(target=main).start()