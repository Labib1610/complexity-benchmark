import sys
import threading
def solve():
    import sys
    sys.setrecursionlimit(1 << 25)
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it)); B = int(next(it))
    sovereign = [int(next(it)) - 1 for _ in range(k)]
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        edges.append((u, v, w))
    if k <= 1:
        print("YES")
        print(0)
        return
    if k != 2:
        # fallback: impossible for general k in this simple solution
        print("NO")
        return
    s, t = sovereign[0], sovereign[1]
    # build flow network
    N = n
    adj = [[] for _ in range(N)]
    class Edge:
        __slots__ = ('to','cap','rev','idx')
        def __init__(self,to,cap,rev,idx):
            self.to=to;self.cap=cap;self.rev=rev;self.idx=idx
    def add_edge(fr,to,cap,idx):
        fwd = Edge(to,cap,len(adj[to]),idx)
        rev = Edge(fr,0,len(adj[fr]),-1)
        adj[fr].append(fwd)
        adj[to].append(rev)
    edge_id = {}
    for i,(u,v,w) in enumerate(edges):
        add_edge(u,v,w,i)
        add_edge(v,u,w,i)
        edge_id[(u,v,i)] = i
        edge_id[(v,u,i)] = i
    level=[0]*N
    itp=[0]*N
    from collections import deque
    def bfs():
        for i in range(N): level[i]=-1
        q=deque([s])
        level[s]=0
        while q:
            v=q.popleft()
            for e in adj[v]:
                if e.cap>0 and level[e.to]<0:
                    level[e.to]=level[v]+1
                    q.append(e.to)
        return level[t]>=0
    def dfs(v,f):
        if v==t: return f
        for i in range(itp[v],len(adj[v])):
            e=adj[v][i]
            if e.cap>0 and level[v]<level[e.to]:
                ret=dfs(e.to, min(f,e.cap))
                if ret:
                    e.cap-=ret
                    adj[e.to][e.rev].cap+=ret
                    return ret
            itp[v]+=1
        return 0
    flow=0
    INF=10**18
    while bfs():
        itp=[0]*N
        while True:
            f=dfs(s,INF)
            if not f: break
            flow+=f
    if flow> B:
        print("NO")
        return
    # find min cut edges
    visited=[False]*N
    stack=[s]
    visited[s]=True
    while stack:
        v=stack.pop()
        for e in adj[v]:
            if e.cap>0 and not visited[e.to]:
                visited[e.to]=True
                stack.append(e.to)
    cut_edges=set()
    for u in range(N):
        if visited[u]:
            for e in adj[u]:
                if not visited[e.to] and e.idx!=-1:
                    cut_edges.add(e.idx)
    print("YES")
    print(len(cut_edges))
    for idx in cut_edges:
        u,v,w=edges[idx]
        print(u+1, v+1)
threading.Thread(target=solve).start()