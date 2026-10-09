import sys

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    t = int(data[2])
    
    if t <= 1:
        print(0)
        return
    
    ptr = 3
    flagged = set()
    for _ in range(t):
        flagged.add(int(data[ptr]))
        ptr += 1
        
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[ptr])
        v = int(data[ptr+1])
        w = int(data[ptr+2])
        ptr += 3
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    root = 1
    parent = [0] * (n + 1)
    parent_weight = [0] * (n + 1)
    order = []
    
    stack = [root]
    visited = [False] * (n + 1)
    visited[root] = True
    
    head = 0
    bfs_order = [root]
    while head < len(bfs_order):
        u = bfs_order[head]
        head += 1
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                parent_weight[v] = w
                bfs_order.append(v)
                
    cnt = [0] * (n + 1)
    for u in flagged:
        cnt[u] = 1
        
    ans = 0
    for i in range(n - 1, 0, -1):
        u = bfs_order[i]
        p = parent[u]
        if 0 < cnt[u] < t:
            ans += parent_weight[u]
        cnt[p] += cnt[u]
        
    print(ans)

if __name__ == '__main__':
    main()