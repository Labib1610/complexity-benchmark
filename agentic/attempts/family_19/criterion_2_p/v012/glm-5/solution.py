import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx+=1
    m = int(data[idx]); idx+=1
    _ = int(data[idx]); idx+=1  # k = 1
    s = int(data[idx]); idx+=1
    t = int(data[idx]); idx+=1
    d = int(data[idx]); idx+=1
    
    # edges
    # graph: adjacency list of edge ids
    graph = [[] for _ in range(n+1)]
    eto = [0]*(2*m)
    ecap = [0]*(2*m)
    pos = 0
    for i in range(m):
        u = int(data[idx]); idx+=1
        v = int(data[idx]); idx+=1
        c = int(data[idx]); idx+=1
        graph[u].append(pos)
        eto[pos] = v
        ecap[pos] = c
        pos += 1
        graph[v].append(pos)
        eto[pos] = u
        ecap[pos] = 0
        pos += 1
    
    if s == t:
        if d == 0:
            print("YES")
            print(' '.join(['0']*m))
        else:
            print("NO")
        return
    
    if d == 0:
        print("YES")
        print(' '.join(['0']*m))
        return
    
    INF = float('inf')
    
    level = [0]*(n+1)
    it = [0]*(n+1)
    
    def bfs():
        for i in range(n+1):
            level[i] = -1
        level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            lu = level[u] + 1
            for eid in graph[u]:
                if ecap[eid] > 0:
                    v = eto[eid]
                    if level[v] == -1:
                        level[v] = lu
                        q.append(v)
        return level[t] != -1
    
    # iterative DFS blocking flow, capped at need
    total = 0
    
    while total < d and bfs():
        # reset iterators
        for i in range(n+1):
            it[i] = 0
        # iterative DFS
        # stack of (node, edge chosen) — we need path reconstruction
        # Standard approach: use explicit stack with path edges.
        while total < d:
            # find augmenting path from s to t in level graph
            path = []  # list of edge ids
            u = s
            while True:
                if u == t:
                    # augment
                    f = d - total
                    for eid in path:
                        if ecap[eid] < f:
                            f = ecap[eid]
                    for eid in path:
                        ecap[eid] -= f
                        ecap[eid ^ 1] += f
                    total += f
                    # backtrack: remove edges from path until we find an edge with remaining capacity... 
                    # Actually after augmenting, at least one edge on path is saturated.
                    # We need to backtrack to the first saturated edge.
                    # Pop edges from path until the last edge has cap > 0.
                    while path:
                        eid = path[-1]
                        if ecap[eid] == 0:
                            path.pop()
                            # also need to advance iterator at the node... hmm
                        else:
                            break
                    u = ... # need to track current node
                    ...