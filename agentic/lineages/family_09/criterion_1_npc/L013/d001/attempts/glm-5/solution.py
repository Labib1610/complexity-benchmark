import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    adj = [set() for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].add(v)
        adj[v].add(u)
    
    # Greedy selection: pick vertices with smallest degree first
    vertices = list(range(1, n + 1))
    vertices.sort(key=lambda x: len(adj[x]))
    
    selected = []
    for v in vertices:
        ok = True
        for u in selected:
            if u in adj[v]:
                ok = False
                break
        if ok:
            selected.append(v)
            if len(selected) == k:
                break
    
    if len(selected) == k:
        print("YES")
        print(' '.join(map(str, selected)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()