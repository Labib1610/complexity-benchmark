import sys

# Increase recursion depth just in case
sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    it = iter(input_data)
    
    n = int(next(it))
    m = int(next(it))
    _ = int(next(it))  # single directive indicator (1)
    
    s = int(next(it))
    t = int(next(it))
    d = int(next(it))
    
    # Graph representation for Dinic's algorithm
    adj = [[] for _ in range(n + 1)]
    edges = []
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        cap = int(next(it))
        
        # Forward edge
        e1 = [v, cap, 0, len(adj[v])]
        # Backward edge
        e2 = [u, 0, 0, len(adj[u])]
        
        adj[u].append(e1)
        adj[v].append(e2)
        
        # Link reverse indices
        e1[3] = len(adj[v]) - 1
        
        edges.append(e1)

    if s == t:
        if d == 0:
            print("YES")
            print(*(0 for _ in range(m)))
        else:
            print("NO")
        return

    level = [-1] * (n + 1)
    
    def bfs():
        for i in range(n + 1):
            level[i] = -1
        level[s] = 0
        queue = [s]
        head = 0
        while head < len(queue):
            u = queue[head]
            head += 1
            for e in adj[u]:
                v, cap, flow, _ = e
                if cap - flow > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    queue.append(v)
        return level[t] != -1

    ptr = [0] * (n + 1)

    def dfs(u, pushed):
        if pushed == 0 or u == t:
            return pushed
        for cid in range(ptr[u], len(adj[u])):
            ptr[u] = cid
            e = adj[u][cid]
            v, cap, flow, rev_idx = e
            tr = cap - flow
            if level[u] + 1 != level[v] or tr == 0:
                continue
            push = min(pushed, tr)
            tr_pushed = dfs(v, push)
            if tr_pushed == 0:
                continue
            e[2] += tr_pushed
            adj[v][rev_idx][2] -= tr_pushed
            return tr_pushed
        return 0

    total_flow = 0
    while total_flow < d and bfs():
        for i in range(n + 1):
            ptr[i] = 0
        while total_flow < d:
            pushed = dfs(s, d - total_flow)
            if pushed == 0:
                break
            total_flow += pushed

    if total_flow == d:
        print("YES")
        print(*(e[2] for e in edges))
    else:
        print("NO")

if __name__ == '__main__':
    solve()