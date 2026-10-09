import sys
from collections import deque

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    _ = int(input_data[idx]); idx += 1  # the "1"
    
    s = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    d = int(input_data[idx]); idx += 1
    
    edges_u = [0] * m
    edges_v = [0] * m
    edges_w = [0] * m
    
    # Dinic's setup
    # graph[node] = list of edge indices in our edge array
    # edge array: [to, cap, flow] for each directed edge; paired reverse edge follows
    graph = [[] for _ in range(n + 1)]
    edge_list = []  # each entry: [to, cap]
    
    def add_edge(u, v, w):
        graph[u].append(len(edge_list))
        edge_list.append([v, w])
        graph[v].append(len(edge_list))
        edge_list.append([u, 0])
    
    for j in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        w = int(input_data[idx]); idx += 1
        edges_u[j] = u
        edges_v[j] = v
        edges_w[j] = w
        add_edge(u, v, w)
    
    # Dinic's algorithm
    level = [0] * (n + 1)
    ptr = [0] * (n + 1)
    
    def bfs():
        nonlocal level
        level = [-1] * (n + 1)
        level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for eid in graph[u]:
                to, cap = edge_list[eid]
                if cap > 0 and level[to] < 0:
                    level[to] = level[u] + 1
                    q.append(to)
        return level[t] >= 0
    
    def dfs(u, pushed):
        if u == t:
            return pushed
        while ptr[u] < len(graph[u]):
            eid = graph[u][ptr[u]]
            to, cap = edge_list[eid]
            if cap > 0 and level[to] == level[u] + 1:
                tr = dfs(to, min(pushed, cap))
                if tr > 0:
                    edge_list[eid][1] -= tr
                    edge_list[eid ^ 1][1] += tr
                    return tr
            ptr[u] += 1
        return 0
    
    flow = 0
    while flow < d and bfs():
        ptr = [0] * (n + 1)
        while True:
            f = dfs(s, d - flow)
            if f == 0:
                break
            flow += f
            if flow >= d:
                break
    
    if flow < d:
        print("NO")
        return
    
    # Extract per-edge flows
    # For original edge j, it was added at index 2*j (forward), reverse at 2*j+1
    # Flow on edge = original_cap - remaining_cap = w - edge_list[2*j][1]
    result = []
    for j in range(m):
        remaining = edge_list[2 * j][1]
        used = edges_w[j] - remaining
        result.append(str(used))
    
    print("YES")
    print(" ".join(result))

solve()