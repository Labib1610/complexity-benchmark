import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    _ = next(iterator) # 1
    
    s = int(next(iterator))
    t = int(next(iterator))
    d = int(next(iterator))
    
    head = [-1] * (n + 1)
    to = []
    cap = []
    flow = []
    nxt = []
    
    def add_edge(u, v, c):
        idx = len(to)
        to.append(v)
        cap.append(c)
        flow.append(0)
        nxt.append(head[u])
        head[u] = idx
        
        to.append(u)
        cap.append(0)
        flow.append(0)
        nxt.append(head[v])
        head[v] = idx + 1

    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        c = int(next(iterator))
        add_edge(u, v, c)
        
    if s == t:
        if d == 0:
            print("YES")
            print(*(0 for _ in range(m)))
        else:
            # Transferring to self? Net flow from s is 0. If d > 0, net flow requirement is d != 0.
            print("NO")
        return

    level = [-1] * (n + 1)
    ptr = [-1] * (n + 1)
    
    def bfs():
        for i in range(1, n + 1):
            level[i] = -1
        level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            e = head[u]
            while e != -1:
                v = to[e]
                if cap[e] - flow[e] > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    q.append(v)
                e = nxt[e]
        return level[t] != -1

    def dfs(u, pushed):
        if pushed == 0 or u == t:
            return pushed
        e = ptr[u]
        while e != -1:
            v = to[e]
            tr = cap[e] - flow[e]
            if level[v] == level[u] + 1 and tr > 0:
                push = pushed if pushed < tr else tr
                res = dfs(v, push)
                if res > 0:
                    flow[e] += res
                    flow[e ^ 1] -= res
                    ptr[u] = e
                    return res
            e = nxt[e]
            ptr[u] = e
        return 0

    total_flow = 0
    while total_flow < d and bfs():
        for i in range(1, n + 1):
            ptr[i] = head[i]
        while total_flow < d:
            pushed = dfs(s, d - total_flow)
            if pushed == 0:
                break
            total_flow += pushed

    if total_flow == d:
        print("YES")
        ans = [flow[2 * i] for i in range(m)]
        print(*(ans[i] for i in range(m)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()