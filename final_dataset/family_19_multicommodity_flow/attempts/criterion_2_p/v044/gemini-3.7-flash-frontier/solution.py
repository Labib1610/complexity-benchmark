import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    # input_data[2] is 1 (item types)
    
    S = int(input_data[3])
    T = int(input_data[4])
    D = int(input_data[5])
    
    if S == T:
        if D == 0:
            print("YES")
            print(" ".join(["0"] * m))
        else:
            print("NO")
        return

    # Dinic's algorithm
    # Graph representation
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
        head[v] = idx ^ 1
        return idx

    edge_indices = []
    idx = 6
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        c = int(input_data[idx+2])
        idx += 3
        e_idx = add_edge(u, v, c)
        edge_indices.append(e_idx)

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
                if cap[e] - flow[e] > 0 and level[v] < 0:
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
            tr = cap[e] - flow[e]
            if level[u] + 1 == level[v] and tr > 0:
                push = pushed if pushed < tr else tr
                tr_pushed = dfs(v, push)
                if tr_pushed > 0:
                    flow[e] += tr_pushed
                    flow[e ^ 1] -= tr_pushed
                    return tr_pushed
            e = nxt[e]
            ptr[u] = e
        return 0

    total_flow = 0
    while total_flow < D and bfs():
        for i in range(n + 1):
            ptr[i] = head[i]
        while total_flow < D:
            pushed = dfs(S, D - total_flow)
            if pushed == 0:
                break
            total_flow += pushed

    if total_flow == D:
        print("YES")
        ans = [str(flow[e_idx]) for e_idx in edge_indices]
        print(" ".join(ans))
    else:
        print("NO")

if __name__ == '__main__':
    solve()