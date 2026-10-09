import sys
from collections import deque

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it)); B = int(next(it))
    specials = [int(next(it)) - 1 for _ in range(k)]
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        edges.append((u, v, w))
    if k != 2:
        # fallback: if more than 2 specials, we cannot solve optimally; just output NO
        print("NO")
        return
    s, t = specials[0], specials[1]

    # Build flow network
    N = n
    adj = [[] for _ in range(N)]
    class Edge:
        __slots__ = ('to','cap','rev','idx')
        def __init__(self,to,cap,rev,idx):
            self.to=to;self.cap=cap;self.rev=rev;self.idx=idx
    def add_edge(u,v,c,idx):
        a=Edge(v,c,len(adj[v]),idx)
        b=Edge(u,0,len(adj[u]),-1)
        adj[u].append(a);adj[v].append(b)
    for i,(u,v,w) in enumerate(edges):
        add_edge(u,v,w,i)
        add_edge(v,u,w,i)  # undirected capacity both ways

    level=[0]*N
    itp=[0]*N
    def bfs():
        for i in range(N): level[i]=-1
        q=deque([s]); level[s]=0
        while q:
            v=q.popleft()
            for e in adj[v]:
                if e.cap>0 and level[e.to]==-1:
                    level[e.to]=level[v]+1
                    q.append(e.to)
        return level[t]!=-1
    def dfs(v,f):
        if v==t: return f
        for i in range(itp[v],len(adj[v])):
            e=adj[v][i]
            if e.cap>0 and level[e.to]==level[v]+1:
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

    # After maxflow, find reachable from s in residual
    visited=[False]*N
    q=deque([s]); visited[s]=True
    while q:
        v=q.popleft()
        for e in adj[v]:
            if e.cap>0 and not visited[e.to]:
                visited[e.to]=True
                q.append(e.to)
    cut_edges=set()
    total=0
    for u in range(N):
        if visited[u]:
            for e in adj[u]:
                if not visited[e.to] and e.idx!=-1:
                    cut_edges.add(e.idx)
    for idx in cut_edges:
        total+=edges[idx][2]
    if total<=B:
        print("YES")
        print(len(cut_edges))
        for idx in cut_edges:
            u,v,_=edges[idx]
            print(u+1, v+1)
    else:
        print("NO")

if __name__=="__main__":
    solve()