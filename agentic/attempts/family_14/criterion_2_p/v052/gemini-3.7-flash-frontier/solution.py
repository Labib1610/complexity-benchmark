import sys
from collections import deque

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    t = int(data[2])
    
    idx = 3
    key_rooms = [int(data[idx + i]) for i in range(t)]
    idx += t
    
    if t <= 1:
        print(0)
        return
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        w = int(data[idx + 2])
        adj[u].append((v, w))
        adj[v].append((u, w))
        idx += 3
        
    cnt = [0] * (n + 1)
    for k in key_rooms:
        cnt[k] = 1
        
    parent = [0] * (n + 1)
    parent_weight = [0] * (n + 1)
    visited = [False] * (n + 1)
    
    order = []
    queue = deque([1])
    visited[1] = True
    
    while queue:
        u = queue.popleft()
        order.append(u)
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                parent_weight[v] = w
                queue.append(v)
                
    ans = 0
    for u in reversed(order):
        if u != 1:
            p = parent[u]
            cnt[p] += cnt[u]
            if 0 < cnt[u] < t:
                ans += parent_weight[u]
                
    print(ans)

if __name__ == '__main__':
    main()