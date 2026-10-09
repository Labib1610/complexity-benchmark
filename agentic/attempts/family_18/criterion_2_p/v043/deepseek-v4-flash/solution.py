import sys
sys.setrecursionlimit(300000)

def solve():
    input_data = sys.stdin.read().strip().split()
    n, m, B = map(int, input_data[:3])
    edges = []
    idx = 3
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
    
    order = []
    visited = [False] * n
    
    def dfs(u):
        visited[u] = True
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                dfs(v)
    
    dfs(0)
    
    pos = [0] * n
    for slot, node in enumerate(order, start=1):
        pos[node] = slot
    
    total_len = 0
    for u in range(n):
        for v in adj[u]:
            if u < v:
                total_len += abs(pos[u] - pos[v])
    
    if total_len <= B:
        print("YES")
        print(" ".join(str(pos[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()