import sys
sys.setrecursionlimit(300000)

def solve():
    input_data = sys.stdin.read().strip().split()
    n, m, B = map(int, input_data[:3])
    adj = [[] for _ in range(n)]
    idx = 3
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
    
    order = []
    parent = [-1] * n
    
    def dfs(u):
        order.append(u)
        for v in adj[u]:
            if v != parent[u]:
                parent[v] = u
                dfs(v)
    
    dfs(0)
    
    label = [0] * n
    for i, node in enumerate(order):
        label[node] = i + 1
    
    total = 0
    for u in range(n):
        for v in adj[u]:
            if u < v:
                total += abs(label[u] - label[v])
    
    if total <= B:
        print("YES")
        print(" ".join(map(str, label)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()