import sys
sys.setrecursionlimit(1 << 25)

class Dinic:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v, cap, idx=-1):
        # forward edge
        fwd = [v, cap, None, idx]
        # backward edge
        rev = [u, 0, fwd, -1]
        fwd[2] = rev
        self.adj[u].append(fwd)
        self.adj[v].append(rev)
        return fwd

    def bfs(self, s, t):
        self.level = [-1]*self.n
        q = [s]
        self.level[s]=0
        for u in q:
            for v, cap, rev, idx in self.adj[u]:
                if cap and self.level[v]==-1:
                    self.level[v]=self.level[u]+1
                    q.append(v)
        return self.level[t]!=-1

    def dfs(self, u, t, f):
        if u==t:
            return f
        for i in range(self.it[u], len(self.adj[u])):
            self.it[u]=i
            v, cap, rev, idx = self.adj[u][i]
            if cap and self.level[v]==self.level[u]+1:
                ret=self.dfs(v,t, min(f, cap))
                if ret:
                    self.adj[u][i][1]-=ret
                    rev[1]+=ret
                    return ret
        return 0

    def max_flow(self, s, t, limit=float('inf')):
        flow=0
        while flow<limit and self.bfs(s,t):
            self.it=[0]*self.n
            while flow<limit:
                f=self.dfs(s,t, limit-flow)
                if not f: break
                flow+=f
        return flow

def solve():
    data=list(map(int,sys.stdin.read().strip().split()))
    if not data: 
        return
    it=iter(data)
    n=next(it); m=next(it); _=next(it)
    s=next(it)-1; t=next(it)-1; d=next(it)
    dinic=Dinic(n)
    edge_refs=[]
    for _ in range(m):
        u=next(it)-1; v=next(it)-1; cap=next(it)
        ref=dinic.add_edge(u,v,cap, idx=len(edge_refs))
        edge_refs.append(ref)
    flow=dinic.max_flow(s,t)
    if flow<d:
        print("NO")
        return
    if flow>d:
        # reduce excess by sending flow from t to s
        dinic.max_flow(t,s, flow-d)
    # collect flows
    res=[0]*m
    for ref in edge_refs:
        # original capacity - remaining capacity = flow used
        used = ref[2][1]  # reverse edge's capacity equals flow sent
        res[ref[3]]=used
    print("YES")
    print(' '.join(map(str,res)))

if __name__=="__main__":
    solve()