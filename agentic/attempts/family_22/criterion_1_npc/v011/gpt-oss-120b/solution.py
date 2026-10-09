import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); M = int(next(it)); T = int(next(it)); m = int(next(it))
    adj = [[] for _ in range(n)]
    radj = [[] for _ in range(n)]
    indeg = [0]*n
    for _ in range(m):
        a = int(next(it))-1
        b = int(next(it))-1
        adj[a].append(b)
        radj[b].append(a)
        indeg[b] += 1

    # topological order
    from collections import deque
    q = deque([i for i in range(n) if indeg[i]==0])
    topo = []
    while q:
        v = q.popleft()
        topo.append(v)
        for to in adj[v]:
            indeg[to] -= 1
            if indeg[to]==0:
                q.append(to)
    if len(topo)!=n:
        print("NO")
        return

    # earliest
    earliest = [1]*n
    for v in topo:
        for to in adj[v]:
            if earliest[to] < earliest[v] + 1:
                earliest[to] = earliest[v] + 1

    # longest path to end (len_to_end)
    len_to_end = [1]*n
    for v in reversed(topo):
        for to in adj[v]:
            if len_to_end[v] < len_to_end[to] + 1:
                len_to_end[v] = len_to_end[to] + 1

    latest = [T - (len_to_end[i]-1) for i in range(n)]

    for i in range(n):
        if earliest[i] > latest[i] or earliest[i] > T or latest[i] < 1:
            print("NO")
            return

    # ----- Dinic -----
    class Edge:
        __slots__ = ('to','cap','rev')
        def __init__(self,to,cap,rev):
            self.to=to;self.cap=cap;self.rev=rev

    N = 1 + n + T + 1
    SRC = 0
    MOD_START = 1
    TERM_START = 1 + n
    SNK = N-1
    graph = [[] for _ in range(N)]

    def add_edge(fr,to,cap):
        graph[fr].append(Edge(to,cap,len(graph[to])))
        graph[to].append(Edge(fr,0,len(graph[fr])-1))

    for i in range(n):
        add_edge(SRC, MOD_START+i, 1)
        for term in range(earliest[i], latest[i]+1):
            add_edge(MOD_START+i, TERM_START+term-1, 1)

    for term in range(1, T+1):
        add_edge(TERM_START+term-1, SNK, M)

    level = [0]*N
    itp = [0]*N
    from collections import deque
    def bfs():
        for i in range(N):
            level[i] = -1
        q = deque([SRC])
        level[SRC]=0
        while q:
            v=q.popleft()
            for e in graph[v]:
                if e.cap and level[e.to]==-1:
                    level[e.to]=level[v]+1
                    q.append(e.to)
        return level[SNK]!=-1

    def dfs(v, f):
        if v==SNK:
            return f
        for i in range(itp[v], len(graph[v])):
            e = graph[v][i]
            if e.cap and level[e.to]==level[v]+1:
                ret = dfs(e.to, min(f, e.cap))
                if ret:
                    e.cap -= ret
                    graph[e.to][e.rev].cap += ret
                    return ret
            itp[v]+=1
        return 0

    flow=0
    INF=10**9
    while bfs():
        itp = [0]*N
        while True:
            pushed = dfs(SRC, INF)
            if not pushed:
                break
            flow += pushed

    if flow!=n:
        print("NO")
        return

    # retrieve assignment
    ans = [0]*n
    for i in range(n):
        v = MOD_START+i
        for e in graph[v]:
            if TERM_START <= e.to < TERM_START+T and e.cap==0:  # used edge
                term = e.to - TERM_START + 1
                ans[i]=term
                break
    print("YES")
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()