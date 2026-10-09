import sys
sys.setrecursionlimit(300000)

def solve():
    n, m, B = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    
    parent = [-1]*n
    order = []
    stack = [0]
    parent[0] = 0
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if parent[v] == -1:
                parent[v] = u
                stack.append(v)
    
    size = [1]*n
    for u in reversed(order):
        for v in adj[u]:
            if v != parent[u]:
                size[u] += size[v]
    
    pos = [0]*n
    cur = 1
    def dfs(u):
        nonlocal cur
        pos[u] = cur
        cur += 1
        # visit children in increasing subtree size
        children = [v for v in adj[u] if v != parent[u]]
        children.sort(key=lambda x: size[x])
        for v in children:
            dfs(v)
    
    dfs(0)
    
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