import sys
import threading
def solve():
    import sys
    sys.setrecursionlimit(1 << 25)
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it)); B = int(next(it))
    specials = [int(next(it)) - 1 for _ in range(k)]
    edges = []
    adj = [[] for _ in range(n)]
    for idx in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        edges.append((u, v, w))
        adj[u].append((v, w, idx))
        adj[v].append((u, w, idx))
    # If k <= 1, nothing to cut
    if k <= 1:
        print("YES")
        print(0)
        return
    # For k=2 we can solve via min cut (max flow) using Dinic
    if k == 2:
        s, t = specials[0], specials[1]
        # Build flow network
        N = n
        class Edge:
            __slots__ = ('to','cap','rev','idx')
            def __init__(self,to,cap,rev,idx):
                self.to=to;self.cap=cap;self.rev=rev;self.idx=idx
        G=[[] for _ in range(N)]
        def add_edge(fr,to,cap,idx):
            G[fr].append(Edge(to,cap,len(G[to]),idx))
            G[to].append(Edge(fr,0,len(G[fr])-1,-1))
        for i,(u,v,w) in enumerate(edges):
            add_edge(u,v,w,i)
            add_edge(v,u,w,i)
        level=[0]*N
        itp=[0]*N
        from collections import deque
        def bfs():
            for i in range(N): level[i]=-1
            q=deque([s]); level[s]=0
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
                    d=dfs(e.to, min(f,e.cap))
                    if d:
                        e.cap-=d
                        G[e.to][e.rev].cap+=d
                        return d
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
        # After maxflow, find reachable from s in residual graph
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
        total=0
        for u in range(N):
            if visited[u]:
                for e in G[u]:
                    if not visited[e.to] and e.idx!=-1:
                        cut_edges.append(e.idx)
                        total+=edges[e.idx][2]
        if total<=B:
            print("YES")
            print(len(cut_edges))
            for idx in cut_edges:
                u,v,w=edges[idx]
                print(u+1, v+1)
        else:
            print("NO")
        return
    # General case: fallback heuristic - cut all edges incident to specials
    cut_edges=set()
    total=0
    for s in specials:
        for v,w,idx in adj[s]:
            if idx not in cut_edges:
                cut_edges.add(idx)
                total+=w
    if total<=B:
        print("YES")
        print(len(cut_edges))
        for idx in cut_edges:
            u,v,w=edges[idx]
            print(u+1, v+1)
    else:
        print("NO")
threading.Thread(target=solve).start()