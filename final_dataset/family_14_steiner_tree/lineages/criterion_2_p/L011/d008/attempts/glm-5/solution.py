import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    targets = [int(next(it)) for _ in range(t)]
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t == 1:
        print(0)
        return
    
    target_count = [0] * (n+1)
    for node in targets:
        target_count[node] = 1
    
    parent = [0] * (n+1)
    parent_weight = [0] * (n+1)
    order = []
    q = deque([1])
    parent[1] = -1
    while q:
        u = q.popleft()
        order.append(u)
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                parent_weight[v] = w
                q.append(v)
    
    for u in reversed(order):
        p = parent[u]
        if p != -1:
            target_count[p] += target_count[u]
    
    ans = 0
    for u in range(2, n+1):
        cnt = target_count[u]
        if 1 <= cnt <= t - 1:
            ans += parent_weight[u]
    
    print(ans)

if __name__ == "__main__":
    main()