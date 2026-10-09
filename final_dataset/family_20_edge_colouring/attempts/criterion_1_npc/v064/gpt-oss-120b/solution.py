import sys
sys.setrecursionlimit(10000)

def solve():
    import sys
    input = sys.stdin.readline
    n,m = map(int,input().split())
    edges = []
    adj = [[] for _ in range(n)]
    for i in range(m):
        u,v = map(int,input().split())
        u-=1; v-=1
        edges.append((u,v))
        adj[u].append((v,i))
        adj[v].append((u,i))
    # Blossom algorithm for maximum matching
    N=n
    g=[[] for _ in range(N)]
    for u,v in edges:
        g[u].append(v)
        g[v].append(u)
    match=[-1]*N
    p=[0]*N
    base=list(range(N))
    q=[]
    used=[False]*N
    blossom=[False]*N

    def lca(a,b):
        used2=[False]*N
        while True:
            a=base[a]
            used2[a]=True
            if match[a]==-1: break
            a=p[match[a]]
        while True:
            b=base[b]
            if used2[b]:
                return b
            b=p[match[b]]

    def mark_path(v,b,x):
        while base[v]!=b:
            blossom[base[v]]=blossom[base[match[v]]]=True
            p[v]=x
            x=match[v]
            v=p[match[v]]

    def find_path(root):
        nonlocal q,used,base,p,blossom
        used=[False]*N
        p=[-1]*N
        for i in range(N):
            base[i]=i
        q=[]
        q.append(root)
        used[root]=True
        head=0
        while head < len(q):
            v=q[head]; head+=1
            for to in g[v]:
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
                        # augment
                        v=to
                        while v!=-1:
                            pv=p[v]
                            nv=match[pv] if pv!=-1 else -1
                            match[v]=pv
                            match[pv]=v
                            v=nv
                        return True
                    else:
                        used[match[to]]=True
                        q.append(match[to])
        return False

    for v in range(N):
        if match[v]==-1:
            find_path(v)

    # check perfect matching
    if any(m==-1 for m in match):
        print("NO")
        return

    # assign colors
    color=[0]*m
    # color 1 for matching edges
    for idx,(u,v) in enumerate(edges):
        if match[u]==v:
            color[idx]=1
    # build remaining graph (2-regular)
    rem_adj=[[] for _ in range(n)]
    for idx,(u,v) in enumerate(edges):
        if color[idx]==0:
            rem_adj[u].append((v,idx))
            rem_adj[v].append((u,idx))
    visited=[False]*n
    for start in range(n):
        if not visited[start]:
            # traverse cycle
            cur=start
            prev_edge=-1
            col=2
            while True:
                visited[cur]=True
                # find next edge not prev
                for to,ei in rem_adj[cur]:
                    if ei!=prev_edge:
                        break
                # assign color
                color[ei]=col
                col=5-col  # toggle between 2 and3
                prev_edge=ei
                cur=to
                if visited[cur]:
                    break
    print("YES")
    print(' '.join(map(str,color)))

if __name__=="__main__":
    solve()