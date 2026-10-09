import sys
from collections import deque

def dinic(n, adj, s, t):
    level = [0]*n
    it = [0]*n
    INF = 10**18
    def bfs():
        for i in range(n):
            level[i] = -1
        q = deque([s])
        level[s]=0
        while q:
            v=q.popleft()
            for to, cap, rev in adj[v]:
                if cap>0 and level[to]<0:
                    level[to]=level[v]+1
                    q.append(to)
        return level[t]>=0
    def dfs(v, f):
        if v==t:
            return f
        for i in range(it[v], len(adj[v])):
            it[v]=i
            to, cap, rev = adj[v][i]
            if cap>0 and level[v]<level[to]:
                d=dfs(to, min(f, cap))
                if d>0:
                    adj[v][i][1]-=d
                    adj[to][rev][1]+=d
                    return d
        return 0
    flow=0
    while bfs():
        it=[0]*n
        while True:
            f=dfs(s, INF)
            if f==0: break
            flow+=f
    return flow

def solve():
    data=sys.stdin.read().strip().split()
    if not data: 
        return
    it=iter(data)
    n=int(next(it)); m=int(next(it)); k=int(next(it)); B=int(next(it))
    specials=[int(next(it))-1 for _ in range(k)]
    edges=[]
    for _ in range(m):
        u=int(next(it))-1; v=int(next(it))-1; w=int(next(it))
        edges.append((u,v,w))
    if k!=2:
        print("NO")
        return
    s,t=specials
    # build flow network
    N=n
    adj=[[ ] for _ in range(N)]
    def add_edge(u,v,c):
        adj[u].append([v,c,len(adj[v])])
        adj[v].append([u,0,len(adj[u])-1])
    for u,v,w in edges:
        add_edge(u,v,w)
        add_edge(v,u,w)
    mincost=dinic(N,adj,s,t)
    if mincost<=B:
        # need to output actual cut edges: find reachable from s in residual
        visited=[False]*N
        q=deque([s])
        visited[s]=True
        while q:
            v=q.popleft()
            for to,cap,rev in adj[v]:
                if cap>0 and not visited[to]:
                    visited[to]=True
                    q.append(to)
        cut=[]
        for u,v,w in edges:
            if visited[u] and not visited[v] or visited[v] and not visited[u]:
                cut.append((u+1,v+1))
        print("YES")
        print(len(cut))
        for u,v in cut:
            print(u,v)
    else:
        print("NO")

if __name__=="__main__":
    solve()