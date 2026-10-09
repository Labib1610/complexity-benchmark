import sys
sys.setrecursionlimit(10000)

def solve():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it))
    edges = []
    g = [[] for _ in range(n)]
    for idx in range(m):
        u = int(next(it))-1
        v = int(next(it))-1
        edges.append((u,v))
        g[u].append((v,idx))
        g[v].append((u,idx))
    # check degree 3
    for deg in g:
        if len(deg)!=3:
            print("NO")
            return
    # find bridges
    sys.setrecursionlimit(10000)
    tin=[0]*n
    low=[0]*n
    timer=1
    bridges=False
    def dfs(v,p):
        nonlocal timer,bridges
        tin[v]=low[v]=timer; timer+=1
        for to,_ in g[v]:
            if to==p: continue
            if tin[to]:
                low[v]=min(low[v],tin[to])
            else:
                dfs(to,v)
                low[v]=min(low[v],low[to])
                if low[to]>tin[v]:
                    bridges=True
    dfs(0,-1)
    if bridges or any(tin[i]==0 for i in range(n)):
        print("NO")
        return

    # Edmonds blossom for maximum matching
    N=n
    adj=[set() for _ in range(N)]
    for u,v in edges:
        adj[u].add(v)
        adj[v].add(u)

    match=[-1]*N
    p=[-1]*N
    base=list(range(N))
    q=[]
    used=[False]*N
    blossom=[False]*N

    def lca(a,b):
        used_path=[False]*N
        while True:
            a=base[a]
            used_path[a]=True
            if match[a]==-1: break
            a=p[match[a]]
        while True:
            b=base[b]
            if used_path[b]:
                return b
            b=p[match[b]]

    def mark_path(v,b,x):
        while base[v]!=b:
            blossom[base[v]]=blossom[base[match[v]]]=True
            p[v]=x
            x=match[v]
            v=p[match[v]]

    def find_path(root):
        nonlocal q,used,p,base,blossom
        used=[False]*N
        p=[-1]*N
        base=list(range(N))
        q=[]
        q.append(root)
        used[root]=True
        head=0
        while head < len(q):
            v=q[head]; head+=1
            for to in adj[v]:
                if base[v]==base[to] or match[v]==to:
                    continue
                if to==root or (match[to]!=-1 and p[match[to]]!=-1):
                    cur=lca(v,to)
                    blossom=[False]*N
                    mark_path(v,cur,to)
                    mark_path(to,cur,v)
                    for i in range(N):
                        if blossom[base[i]]:
                            base[i]=cur
                            if not used[i]:
                                used[i]=True
                                q.append(i)
                elif p[to]==-1:
                    p[to]=v
                    if match[to]==-1:
                        return to
                    to_match=match[to]
                    used[to_match]=True
                    q.append(to_match)
        return -1

    for v in range(N):
        if match[v]==-1:
            u=find_path(v)
            if u!=-1:
                # augment
                while u!=-1:
                    pv=p[u]
                    w=match[pv] if pv!=-1 else -1
                    match[u]=pv
                    match[pv]=u
                    u=w

    if any(m==-1 for m in match):
        print("NO")
        return

    # assign colors
    color=[0]*m
    # matched edges get color 1
    for idx,(u,v) in enumerate(edges):
        if match[u]==v:
            color[idx]=1
    # build remaining adjacency of cycles
    rem_adj=[[] for _ in range(n)]
    for idx,(u,v) in enumerate(edges):
        if color[idx]==0:
            rem_adj[u].append((v,idx))
            rem_adj[v].append((u,idx))
    visited=[False]*n
    for start in range(n):
        if visited[start]: continue
        # traverse cycle
        cur=start
        prev=-1
        cyc_edges=[]
        while True:
            visited[cur]=True
            # find next edge not coming from prev
            for to,ei in rem_adj[cur]:
                if to!=prev:
                    nxt=to; eidx=ei
                    break
            cyc_edges.append(eidx)
            prev=cur
            cur=nxt
            if cur==start:
                break
        # assign alternating 2,3
        col=2
        for ei in cyc_edges:
            color[ei]=col
            col=5-col  # toggle between 2 and3

    print("YES")
    print(' '.join(map(str,color)))

if __name__=="__main__":
    solve()