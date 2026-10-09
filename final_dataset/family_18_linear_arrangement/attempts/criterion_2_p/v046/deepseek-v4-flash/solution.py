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
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # Minimum possible sum is n-1 (DFS order)
    if B < n - 1:
        print("NO")
        return
    
    # DFS order
    visited = [False] * n
    order = []
    
    def dfs(u):
        visited[u] = True
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                dfs(v)
    
    dfs(0)
    
    # Assign pads 1..n in order
    pos = [0] * n
    for i, node in enumerate(order):
        pos[node] = i + 1
    
    print("YES")
    print(" ".join(map(str, pos)))

if __name__ == "__main__":
    solve()