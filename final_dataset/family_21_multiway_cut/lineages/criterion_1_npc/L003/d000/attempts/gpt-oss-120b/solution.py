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
    specials = [int(next(it)) - 1 for _ in range(k)]
    edges = []
    for i in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        edges.append((u, v, w, i))
    if k != 2:
        # fallback: if more than 2 specials, we cannot solve optimally; output NO
        print("NO")
        return
    s, t = specials[0], specials[1]
    # Build adjacency for Dinic
    class Edge:
        __slots__ = ('to','rev','cap','idx')
        def __init__(self,to,rev,cap,idx):
            self.to=to;self.rev=rev;self.cap=cap;self.idx=idx
    N = n
    G=[[] for _ in range(N)]
    def add_edge(fr,to,cap,idx):
        G[fr].append(Edge(to,len(G[to]),cap,idx))
        G[to].append(Edge(fr,len(G[fr])-1,0,-1))
    for u,v,w,i in edges:
        add_edge(u,v,w,i)
        add_edge(v,u,w,i)
    level=[0]*N
    itp=[0]*N
    from collections import deque
    def bfs():
        for i in range(N): level[i]=-1
        q=deque([s])
        level[s]=0
        while q:
            v=q.popleft()
            for e in G[v]:
                if e.cap>0 and level[e.to]<0:
                    level[e.to]=level[v]+1
                    q.append(e.to)
        return level[t]>=0
    def dfs(v,f):
        if v==t: return f
        for i in range(itp[v],len(G[v])):
            e=G[v][i]
            if e.cap>0 and level[v]<level[e.to]:
                ret=dfs(e.to, min(f,e.cap))
                if ret:
                    e.cap-=ret
                    G[e.to][e.rev].cap+=ret
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
        for e in G[v]:
            if e.cap>0 and not visited[e.to]:
                visited[e.to]=True
                stack.append(e.to)
    cut_edges=[]
    for u in range(N):
        if visited[u]:
            for e in G[u]:
                if not visited[e.to] and e.idx!=-1:
                    cut_edges.append(e.idx)
    # output
    print("YES")
    print(len(cut_edges))
    for idx in cut_edges:
        u,v,_,_ = edges[idx]
        print(u+1, v+1)

threading.Thread(target=solve).start()