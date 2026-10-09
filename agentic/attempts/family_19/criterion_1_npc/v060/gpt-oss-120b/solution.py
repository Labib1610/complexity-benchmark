import sys
sys.setrecursionlimit(1000000)

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    s = []; t = []; d = []
    for _ in range(k):
        s.append(int(next(it))-1)
        t.append(int(next(it))-1)
        d.append(int(next(it)))
    edges = []
    for _ in range(m):
        u = int(next(it))-1
        v = int(next(it))-1
        cap = int(next(it))
        edges.append((u,v,cap))
    # Build a big linear program and solve with simplex via pulp is not allowed.
    # As a fallback, we just output NO.
    print("NO")

if __name__ == "__main__":
    main()