import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    s = [0]*k; t = [0]*k; d = [0]*k
    bal = [0]*(n+1)
    for i in range(k):
        s[i]=int(next(it)); t[i]=int(next(it)); d[i]=int(next(it))
        bal[s[i]]+=d[i]
        bal[t[i]]-=d[i]
    edges = []
    for idx in range(m):
        u=int(next(it)); v=int(next(it)); cap=int(next(it))
        edges.append((u,v,cap))
    # Build flow network with super source 0 and super sink n+1
    N = n+2
    S = 0; T = n+1
    adj=[[] for _ in range(N)]
    class Edge:
        __slots__=('to','rev','cap','orig')
        def __init__(self,to,rev,cap,orig):
            self.to=to;self.rev=rev;self.cap=cap;self.orig=orig
    def add_edge(fr,to,cap,orig=False):
        f=Edge(to,len(adj[to]),cap,orig)
        b=Edge(fr,len(adj[fr]),0,orig)
        adj[fr].append(f); adj[to].append(b)
        return f,b
    # original edges store reference
    edge_refs=[None]*m
    for idx,(u,v,cap) in enumerate(edges):
        f,b=add_edge(u,v,cap,orig=True)
        edge_refs[idx]=f
    total_supply=0
    for v in range(1,n+1):
        if bal[v]>0:
            add_edge(S,v,bal[v])
            total_supply+=bal[v]
        elif bal[v]<0:
            add_edge(v,T,-bal[v])
    # Dinic
    level=[0]*N
    itp=[0]*N
    from collections import deque
    def bfs():
        for i in range(N): level[i]=-1
        q=deque([S]); level[S]=0
        while q:
            v=q.popleft()
            for e in adj[v]:
                if e.cap>0 and level[e.to]==-1:
                    level[e.to]=level[v]+1
                    q.append(e.to)
        return level[T]!=-1
    def dfs(v,f):
        if v==T: return f
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
            f=dfs(S,10**18)
            if not f: break
            flow+=f
    if flow!=total_supply:
        print("NO")
        return
    # extract flow on original edges
    edge_flow=[0]*m
    for idx,ref in enumerate(edge_refs):
        used = edges[idx][2] - ref.cap  # original capacity - residual = flow sent
        edge_flow[idx]=used
    # Build adjacency of flow edges for decomposition
    flow_adj=[[] for _ in range(n+1)]
    for idx,(u,v,cap) in enumerate(edges):
        f=edge_flow[idx]
        if f>0:
            flow_adj[u].append([v,idx,f])  # mutable list for flow amount
    # answer matrix
    ans=[[0]*m for _ in range(k)]
    # helper to find path using DFS
    sys.setrecursionlimit(1000000)
    def find_path(sv,tv,visited):
        if sv==tv:
            return []
        visited[sv]=True
        for e in flow_adj[sv]:
            if e[2]==0: continue
            if visited[e[0]]: continue
            sub=find_path(e[0],tv,visited)
            if sub is not None:
                return [(sv,e[0],e[2],e[1])]+sub
        return None
    for i in range(k):
        need=d[i]
        while need>0:
            visited=[False]*(n+1)
            path=find_path(s[i],t[i],visited)
            if not path:
                print("NO")
                return
            bottleneck=min(need, min(p[2] for p in path))
            need-=bottleneck
            for u,v,avail,eid in path:
                # reduce flow
                for e in flow_adj[u]:
                    if e[1]==eid:
                        e[2]-=bottleneck
                        break
                ans[i][eid]+=bottleneck
    print("YES")
    out_lines=[]
    for i in range(k):
        out_lines.append(' '.join(str(x) for x in ans[i]))
    sys.stdout.write('\n'.join(out_lines))

if __name__=="__main__":
    solve()