import sys
from collections import deque

# Increase recursion depth just in case
sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    
    n = int(next(iterator))
    m = int(next(iterator))
    _ = int(next(iterator))  # commodity count, which is 1
    
    s = int(next(iterator))
    t = int(next(iterator))
    d = int(next(iterator))
    
    # We can create a source with an edge to s of capacity d
    # Or simply run max flow from s to t and stop when flow reaches d
    # Alternatively, add super_source -> s with cap d, and find max flow from super_source to t.
    
    # Let nodes be 1-indexed, super_source = 0
    super_source = 0
    
    head = [-1] * (n + 1)
    to = []
    nxt = []
    cap = []
    flow = []
    
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

    super_edge = add_edge(super_source, s, d)
    
    orig_edge_indices = []
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        c = int(next(iterator))
        idx = add_edge(u, v, c)
        orig_edge_indices.append(idx)
        
    # Dinic's Algorithm
    num_nodes = n + 1
    level = [-1] * num_nodes
    ptr = [0] * num_nodes
    
    def bfs():
        for i in range(num_nodes):
            level[i] = -1
        level[super_source] = 0
        q = deque([super_source])
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
        if pushed == 0:
            return 0
        if u == t:
            return pushed
        e = ptr[u]
        while e != -1:
            v = to[e]
            tr = cap[e] - flow[e]
            if level[u] + 1 == level[v] and tr > 0:
                tr = pushed if pushed < tr else tr
                push = dfs(v, tr)
                if push > 0:
                    flow[e] += push
                    flow[e ^ 1] -= push
                    return push
            e = nxt[e]
            ptr[u] = e
        return 0

    max_flow = 0
    while bfs():
        for i in range(num_nodes):
            ptr[i] = head[i]
        while True:
            pushed = dfs(super_source, float('inf'))
            if pushed == 0:
                break
            max_flow += pushed

    if max_flow < d:
        print("NO")
    else:
        print("YES")
        ans = [str(flow[idx]) for idx in orig_edge_indices]
        print(*(ans))

if __name__ == '__main__':
    solve()