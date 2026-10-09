import sys
import threading
def solve():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it)); B = int(next(it))
    specials = [int(next(it)) for _ in range(k)]
    edges = []
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        edges.append((u-1, v-1, w))
    if k != 2:
        print("NO")
        return
    s, t = specials[0]-1, specials[1]-1
    # build adjacency for Dinic
    N = n
    adj = [[] for _ in range(N)]
    class Edge:
        __slots__ = ('to','rev','cap','orig')
        def __init__(self,to,rev,cap,orig):
            self.to=to;self.rev=rev;self.cap=cap;self.orig=orig
    def add_edge(u,v,c):
        a=Edge(v,len(adj[v]),c,(u,v))
        b=Edge(u,len(adj[u]),c,(v,u))
        adj[u].append(a)
        adj[v].append(b)
    for u,v,w in edges:
        add_edge(u,v,w)
    INF=10**18
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
    while bfs():
        itp=[0]*N
        while True:
            f=dfs(s,INF)
            if not f: break
            flow+=f
    if flow>B:
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
    cut_edges=[]
    for u in range(N):
        if visited[u]:
            for e in adj[u]:
                if not visited[e.to] and e.orig[0]==u and e.orig[1]==e.to:
                    cut_edges.append((u+1,e.to+1))
    print("YES")
    print(len(cut_edges))
    for u,v in cut_edges:
        print(u,v)
threading.Thread(target=solve).start()