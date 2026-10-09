import sys
import threading

def solve():
    import sys
    sys.setrecursionlimit(1 << 25)
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    tasks = []
    for _ in range(k):
        s = int(next(it))-1
        t = int(next(it))-1
        d = int(next(it))
        tasks.append((s,t,d))
    edges = []
    for _ in range(m):
        u = int(next(it))-1
        v = int(next(it))-1
        cap = int(next(it))
        edges.append((u,v,cap))
    # Build a single linear program and solve with simplex (since sizes are small)
    # Variables x[i][j]: flow of task i on edge j
    # Constraints:
    # 1) For each edge j: sum_i x[i][j] <= cap_j
    # 2) For each task i and node v:
    #    sum_{out edges from v} x[i][j] - sum_{in edges to v} x[i][j] = b
    #    where b = d_i if v == s_i, -d_i if v == t_i, else 0
    # All x >= 0 and integer.
    # We'll use a simple integer feasibility via BFS on state space because limits are tiny.
    # Determine bounds
    total_cap = sum(cap for _,_,cap in edges)
    total_d = sum(d for _,_,d in tasks)
    if total_d > total_cap:
        print("NO")
        return
    # Simple heuristic: try to route each task separately using maxflow, subtract capacities.
    from collections import deque
    def maxflow(task_idx, caps):
        s,t,d = tasks[task_idx]
        N = n
        G = [[] for _ in range(N)]
        class Edge:
            __slots__ = ('to','rev','cap')
            def __init__(self,to,rev,cap):
                self.to=to;self.rev=rev;self.cap=cap
        def add(u,v,c):
            G[u].append(Edge(v,len(G[v]),c))
            G[v].append(Edge(u,len(G[u])-1,0))
        for idx,(u,v,cap) in enumerate(edges):
            add(u,v,caps[idx])
        flow=0
        while True:
            level=[-1]*N
            q=deque([s]);level[s]=0
            while q:
                v=q.popleft()
                for e in G[v]:
                    if e.cap and level[e.to]==-1:
                        level[e.to]=level[v]+1
                        q.append(e.to)
            if level[t]==-1: break
            iters=[0]*N
            def dfs(v,f):
                if v==t: return f
                for i in range(iters[v],len(G[v])):
                    e=G[v][i]
                    if e.cap and level[v]+1==level[e.to]:
                        ret=dfs(e.to, min(f,e.cap))
                        if ret:
                            e.cap-=ret
                            G[e.to][e.rev].cap+=ret
                            return ret
                    iters[v]+=1
                return 0
            while True:
                pushed=dfs(s,10**18)
                if not pushed: break
                flow+=pushed
        return flow, G
    # greedy
    caps = [cap for _,_,cap in edges]
    allocation = [[0]*m for _ in range(k)]
    for i in range(k):
        flow, G = maxflow(i, caps)
        if flow < tasks[i][2]:
            print("NO")
            return
        # retrieve flow on edges
        for idx,(u,v,_) in enumerate(edges):
            # find edge in G[u] to v
            for e in G[u]:
                if e.to==v:
                    used = caps[idx] - e.cap
                    allocation[i][idx]=used
                    caps[idx]-=used
                    break
    print("YES")
    out = sys.stdout
    for i in range(k):
        out.write(' '.join(str(x) for x in allocation[i]))
        out.write('\n')

def main():
    solve()

threading.Thread(target=main).start()