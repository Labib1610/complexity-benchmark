import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    _ = int(next(it)) # 1
    
    s = int(next(it))
    t = int(next(it))
    d = int(next(it))
    
    if d < 0:
        print("NO")
        return
        
    if s == t:
        if d == 0:
            print("YES")
            print(" ".join(["0"] * m))
        else:
            print("NO")
        return

    # Dinic's Algorithm
    # Nodes: 1 to n. Super-source: 0, sink: t
    # Edge from 0 to s with capacity d
    
    source = 0
    sink = t
    num_nodes = n + 1
    
    head = [-1] * num_nodes
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
        return idx

    add_edge(source, s, d)
    
    original_edge_indices = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        c = int(next(it))
        e_idx = add_edge(u, v, c)
        original_edge_indices.append(e_idx)
        
    level = [-1] * num_nodes
    ptr = [0] * num_nodes
    
    def bfs():
        for i in range(num_nodes):
            level[i] = -1
        level[source] = 0
        q = deque([source])
        while q:
            u = q.popleft()
            e = head[u]
            while e != -1:
                v = to[e]
                if cap[e] - flow[e] > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    q.append(v)
                e = nxt[e]
        return level[sink] != -1

    def dfs(u, pushed):
        if pushed == 0 or u == sink:
            return pushed
        e = ptr[u]
        while e != -1:
            v = to[e]
            tr = cap[e] - flow[e]
            if level[u] + 1 == level[v] and tr > 0:
                push = dfs(v, min(pushed, tr))
                if push > 0:
                    flow[e] += push
                    flow[e ^ 1] -= push
                    return push
            ptr[u] = nxt[e]
            e = nxt[e]
        return 0

    max_flow = 0
    while bfs():
        for i in range(num_nodes):
            ptr[i] = head[i]
        while True:
            pushed = dfs(source, float('inf'))
            if pushed == 0:
                break
            max_flow += pushed

    if max_flow == d:
        print("YES")
        ans = [str(flow[idx]) for idx in original_edge_indices]
        print(" ".join(ans))
    else:
        print("NO")

if __name__ == '__main__':
    solve()