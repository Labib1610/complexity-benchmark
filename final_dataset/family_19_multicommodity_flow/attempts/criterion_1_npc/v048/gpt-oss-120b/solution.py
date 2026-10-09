import sys
sys.setrecursionlimit(1 << 25)

class Dinic:
    __slots__ = ('n', 'g', 'level', 'it')
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]

    def add_edge(self, fr, to, cap, idx=-1):
        # forward edge
        f = [to, cap, None, idx]
        # backward edge
        b = [fr, 0, f, -1]
        f[2] = b
        self.g[fr].append(f)
        self.g[to].append(b)

    def bfs(self, s, t):
        level = [-1]*self.n
        q = [s]
        level[s]=0
        for v in q:
            for to, cap, rev, _ in self.g[v]:
                if cap and level[to]==-1:
                    level[to]=level[v]+1
                    q.append(to)
        self.level=level
        return level[t]!=-1

    def dfs(self, v, t, f):
        if v==t:
            return f
        for i in range(self.it[v], len(self.g[v])):
            self.it[v]=i
            to, cap, rev, _ = self.g[v][i]
            if cap and self.level[v]+1==self.level[to]:
                ret=self.dfs(to, t, min(f, cap))
                if ret:
                    self.g[v][i][1]-=ret
                    rev[1]+=ret
                    return ret
        return 0

    def max_flow(self, s, t, limit=None):
        flow=0
        INF=10**18
        while self.bfs(s,t):
            self.it=[0]*self.n
            while True:
                f=self.dfs(s,t, INF if limit is None else limit-flow)
                if not f: break
                flow+=f
                if limit is not None and flow==limit:
                    return flow
        return flow

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    s = [0]*k; t = [0]*k; d = [0]*k
    for i in range(k):
        s[i]=int(next(it))-1
        t[i]=int(next(it))-1
        d[i]=int(next(it))
    edges = []
    for j in range(m):
        u=int(next(it))-1; v=int(next(it))-1; cap=int(next(it))
        edges.append((u,v,cap))

    # compute supplies
    b=[0]*n
    for i in range(k):
        b[s[i]]+=d[i]
        b[t[i]]-=d[i]
    total=sum(x for x in b if x>0)

    # first flow
    S=n; T=n+1
    din=Dinic(n+2)
    for idx,(u,v,cap) in enumerate(edges):
        din.add_edge(u,v,cap,idx)
    for v in range(n):
        if b[v]>0:
            din.add_edge(S,v,b[v])
        elif b[v]<0:
            din.add_edge(v,T,-b[v])
    flow=din.max_flow(S,T)
    if flow!=total:
        print("NO")
        return

    # retrieve flow on original edges
    F=[0]*m
    for u in range(n):
        for e in din.g[u]:
            idx=e[3]
            if idx!=-1:
                used = edges[idx][2] - e[1]   # original cap - residual
                F[idx]=used

    # prepare answer matrix
    ans=[[0]*m for _ in range(k)]
    remaining=F[:]

    for i in range(k):
        # build graph with capacities = remaining
        dflow=Dinic(n)
        for idx,(u,v,_) in enumerate(edges):
            if remaining[idx]:
                dflow.add_edge(u,v,remaining[idx],idx)
        got = dflow.max_flow(s[i], t[i], d[i])
        if got!=d[i]:
            # should not happen
            print("NO")
            return
        # read used amount per edge
        for u in range(n):
            for e in dflow.g[u]:
                idx=e[3]
                if idx!=-1:
                    used = edges[idx][2] - e[1]  # original cap (here = remaining) - residual
                    if used:
                        ans[i][idx]=used
                        remaining[idx]-=used

    print("YES")
    out_lines = []
    for i in range(k):
        out_lines.append(' '.join(str(x) for x in ans[i]))
    sys.stdout.write('\n'.join(out_lines))

if __name__ == "__main__":
    solve()