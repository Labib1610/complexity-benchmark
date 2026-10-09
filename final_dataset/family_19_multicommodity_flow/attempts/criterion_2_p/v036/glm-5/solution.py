import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx+=1
    m = int(data[idx]); idx+=1
    _ = int(data[idx]); idx+=1  # pallet types = 1
    s = int(data[idx]); idx+=1
    t = int(data[idx]); idx+=1
    d = int(data[idx]); idx+=1
    
    edges = []  # (u, v, cap)
    for _ in range(m):
        u = int(data[idx]); idx+=1
        v = int(data[idx]); idx+=1
        cap = int(data[idx]); idx+=1
        edges.append((u, v, cap))
    
    if d == 0:
        print("YES")
        print(" ".join(["0"]*m))
        return
    
    if s == t:
        print("NO")
        return
    
    # Dinic
    # graph: adjacency list mapping node -> list of edge indices
    # edge arrays: to[], cap[] (residual), and record original edge index mapping
    graph = {}
    def add_node(x):
        if x not in graph:
            graph[x] = []
        return x
    
    add_node(s); add_node(t)
    for (u,v,c) in edges:
        add_node(u); add_node(v)
    
    to = []
    cap = []
    # for each input edge i, its forward edge index is 2*i, backward is 2*i+1
    for (u, v, c) in edges:
        graph[u].append(len(to)); to.append(v); cap.append(c)
        graph[v].append(len(to)); to.append(u); cap.append(0)
    
    # BFS level
    def bfs():
        level = {x: -1 for x in graph}
        level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for e in graph[u]:
                if cap[e] > 0 and level[to[e]] == -1:
                    level[to[e]] = level[u] + 1
                    q.append(to[e])
        return level if level[t] != -1 else None
    
    INF = float('inf')
    
    def dfs_iterative(level):
        # iterative DFS with iterator stack
        it = {x: 0 for x in graph}
        stack = [s]
        # We'll implement blocking flow with explicit stack
        # push flow along path
        total = 0
        # min cap along path
        path_edges = []
        while stack:
            u = stack[-1]
            if u == t:
                # find min
                f = min(cap[e] for e in path_edges)
                # apply
                for e in path_edges:
                    cap[e] -= f
                    cap[e^1] += f
                total += f
                # retreat to the first saturated edge
                # pop back until we find an edge with remaining cap
                while path_edges and cap[path_edges[-1]] == 0:
                    path_edges.pop()
                    stack.pop()
                continue
            advanced = False
            while it[u] < len(graph[u]):
                e = graph[u][it[u]]
                v = to[e]
                if cap[e] > 0 and level[v] == level[u] + 1:
                    stack.append(v)
                    path_edges.append(e)
                    advanced = True
                    break
                it[u] += 1
            if not advanced:
                level[u] = -1  # dead
                stack.pop()
                if path_edges:
                    path_edges.pop()
                # hmm careful: if stack becomes empty we're done
        return total