import sys
sys.setrecursionlimit(300000)

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    pos = [0]*(n+1)
    order = []
    visited = [False]*(n+1)
    
    def dfs(u):
        visited[u] = True
        pos[u] = len(order) + 1
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                dfs(v)
    
    dfs(1)
    
    total = 0
    for u in range(1, n+1):
        for v in adj[u]:
            if u < v:
                total += abs(pos[u] - pos[v])
    
    if total <= B:
        print("YES")
        print(" ".join(str(pos[i]) for i in range(1, n+1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()