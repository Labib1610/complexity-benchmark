import sys
sys.setrecursionlimit(300000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    pos = [0] * n
    order = []
    visited = [False] * n
    
    def dfs(u):
        visited[u] = True
        order.append(u)
        for w in adj[u]:
            if not visited[w]:
                dfs(w)
    
    dfs(0)
    
    # assign bay numbers in order
    for i, node in enumerate(order):
        pos[node] = i + 1
    
    total = 0
    for u in range(n):
        for v in adj[u]:
            if u < v:
                total += abs(pos[u] - pos[v])
    
    if total <= B:
        print("YES")
        print(" ".join(str(pos[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()