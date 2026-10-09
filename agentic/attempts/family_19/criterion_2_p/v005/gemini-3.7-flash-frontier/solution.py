import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    # input_data[2] is 1
    s = int(input_data[3])
    t = int(input_data[4])
    d = int(input_data[5])
    
    idx = 6
    edges = []
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        c = int(input_data[idx+2])
        idx += 3
        edges.append((u, v, c))
        
    if d == 0:
        print("YES")
        print(*(0 for _ in range(m)))
        return

    if s == t:
        print("NO")
        return

    # Dinic's Algorithm with super-source
    # Nodes: 1 to n, super source S = 0
    S = 0
    T = t
    
    head = [-1] * (n + 1)
    to = []
    cap = []
    nxt = []
    
    def add_edge(u, v, c):
        to.append(v)
        cap.append(c)
        nxt.append(head[u])
        head[u] = len(to) - 1
        
        to.append(u)
        cap.append(0)
        nxt.append(head[v])
        head[v] = len(to) - 1

    add_edge(S, s, d)
    
    original_edge_idx = []
    for u, v, c in edges:
        original_edge_idx.append(len(to))
        add_edge(u, v, c)
        
    level = [-1] * (n + 1)
    
    def bfs():
        for i in range(n + 1):
            level[i] = -1
        level[S] = 0
        q = deque([S])
        while q:
            u = q.popleft()
            e = head[u]
            while e != -1:
                v = to[e]
                if cap[e] > 0 and level[v] < 0:
                    level[v] = level[u] + 1
                    q.append(v)
                e = nxt[e]
        return level[T] >= 0

    ptr = [0] * (n + 1)

    def dfs(u, pushed):
        if pushed == 0 or u == T:
            return pushed
        e = ptr[u]
        while e != -1:
            v = to[e]
            tr = cap[e]
            if level[u] + 1 == level[v] and tr > 0:
                tr_pushed = dfs(v, min(pushed, tr))
                if tr_pushed > 0:
                    cap[e] -= tr_pushed
                    cap[e ^ 1] += tr_pushed
                    return tr_pushed
            e = nxt[e]
            ptr[u] = e
        return 0

    flow = 0
    while bfs():
        for i in range(n + 1):
            ptr[i] = head[i]
        while True:
            pushed = dfs(S, d - flow)
            if pushed == 0:
                break
            flow += pushed
            if flow == d:
                break
        if flow == d:
            break

    if flow == d:
        print("YES")
        ans = []
        for e_idx in original_edge_idx:
            ans.append(cap[e_idx ^ 1])
        print(*ans)
    else:
        print("NO")

if __name__ == '__main__':
    solve()