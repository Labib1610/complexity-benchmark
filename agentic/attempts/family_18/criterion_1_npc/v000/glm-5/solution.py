import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    try:
        n = int(next(it))
        m = int(next(it))
        B = int(next(it))
    except StopIteration:
        return
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # Greedy placement: place nodes in order 0..n-1 at positions 1..n
    # This minimizes total stretch for edges (u,v) with u<v
    pos = list(range(1, n + 1))
    
    total = 0
    for u in range(n):
        for v in adj[u]:
            if u < v:
                total += abs(pos[u] - pos[v])
    
    if total <= B:
        print("YES")
        print(' '.join(map(str, pos)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()