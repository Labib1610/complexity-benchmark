import sys
sys.setrecursionlimit(1000000)

def solve():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    clients = []
    for _ in range(k):
        s = int(next(it))-1
        t = int(next(it))-1
        d = int(next(it))
        clients.append((s,t,d))
    edges = []
    for _ in range(m):
        u = int(next(it))-1
        v = int(next(it))-1
        cap = int(next(it))
        edges.append((u,v,cap))
    # adjacency for flow
    class Dinic:
        def __init__(self,N):
            self.N=N
            self.adj=[[] for _ in range(N)]
        def add_edge(self,u,v,c):
            self.adj[u].append([v,c,len(self.adj[v])])
            self.adj[v].append([u,0,len(self.adj[u])-1])
        def bfs(self,s,t,level):
            from collections import deque
            q=deque([s])
            level[s]=0
            while q:
                u=q.popleft()
                for v,c,_ in self.adj[u]:
                    if c>0 and level[v]<0:
                        level[v]=level[u]+1
                        q.append(v)
            return level[t]>=0
        def dfs(self,u,t,f,level,it):
            if u==t:
                return f
            for i in range(it[u],len(self.adj[u])):
                it[u]=i
                v,c,rev=self.adj[u][i]
                if c>0 and level[v]==level[u]+1:
                    ret=self.dfs(v,t,min(f,c),level,it)
                    if ret:
                        self.adj[u][i][1]-=ret
                        self.adj[v][rev][1]+=ret
                        return ret
            return 0
        def max_flow(self,s,t):
            flow=0
            N=self.N
            level=[-1]*N
            INF=10**18
            while self.bfs(s,t,level):
                it=[0]*N
                while True:
                    f=self.dfs(s,t,INF,level,it)
                    if not f: break
                    flow+=f
                level=[-1]*N
            return flow
        def get_edge_flow(self, idx_map):
            # idx_map: (u,v) -> edge index in original list
            res=[0]*len(idx_map)
            for (u,v,i) in idx_map:
                # find edge in adj[u] that goes to v and is original
                for to,cap,rev in self.adj[u]:
                    if to==v:
                        # original capacity - remaining capacity
                        orig = edges[i][2]
                        used = orig - cap
                        res[i]=used
                        break
            return res

    # remaining capacities
    rem = [c for _,_,c in edges]

    # store per client flows
    client_flows = [None]*k

    # backtracking
    def dfs_client(ci):
        if ci==k:
            return True
        s,t,d = clients[ci]
        # build dinic with current remaining caps
        din = Dinic(n)
        idx_map = []
        for i,(u,v,_) in enumerate(edges):
            cap = rem[i]
            if cap>0:
                din.add_edge(u,v,cap)
            idx_map.append((u,v,i))
        flow = din.max_flow(s,t)
        if flow<d:
            return False
        # we need to extract one feasible flow of value d
        # run again but limit to d
        din = Dinic(n)
        for i,(u,v,_) in enumerate(edges):
            cap = rem[i]
            if cap>0:
                din.add_edge(u,v,cap)
        # add super source/sink trick to get exact d? just run max flow and then take d units
        got = din.max_flow(s,t)
        # get flows
        used = [0]*m
        for i,(u,v,_) in enumerate(edges):
            # find edge in din
            for to,cap,rev in din.adj[u]:
                if to==v:
                    orig = rem[i]
                    used[i]=orig - cap
                    break
        # we may have sent more than d, trim proportionally (since integer, we can just reduce excess arbitrarily)
        excess = got - d
        if excess>0:
            # reduce excess from any edge with used>0
            for i in range(m):
                while excess>0 and used[i]>0:
                    used[i]-=1
                    excess-=1
        # record
        client_flows[ci]=used[:]
        # update rem
        for i in range(m):
            rem[i]-=used[i]
        if dfs_client(ci+1):
            return True
        # backtrack
        for i in range(m):
            rem[i]+=used[i]
        return False

    possible = dfs_client(0)
    out = sys.stdout
    if not possible:
        out.write("NO")
    else:
        out.write("YES\n")
        for i in range(k):
            out.write(" ".join(str(x) for x in client_flows[i]))
            if i!=k-1:
                out.write("\n")

if __name__=="__main__":
    solve()