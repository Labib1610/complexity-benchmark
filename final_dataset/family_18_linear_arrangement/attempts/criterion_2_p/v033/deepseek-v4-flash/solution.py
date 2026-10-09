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
    
    parent = [-1] * n
    order = []
    stack = [0]
    parent[0] = 0
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            stack.append(v)
    
    size = [1] * n
    for u in reversed(order):
        for v in adj[u]:
            if v != parent[u]:
                size[u] += size[v]
    
    # Preorder assignment
    pos = [0] * n
    cur = 1
    stack = [(0, 0)]  # (node, state) state 0 = enter, 1 = exit
    while stack:
        u, state = stack.pop()
        if state == 0:
            pos[u] = cur
            cur += 1
            stack.append((u, 1))
            for v in reversed(adj[u]):
                if v != parent[u]:
                    stack.append((v, 0))
    
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