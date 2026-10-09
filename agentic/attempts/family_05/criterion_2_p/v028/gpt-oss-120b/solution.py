import sys
from collections import deque

def hopcroft_karp(adj, n_left, n_right):
    # vertices are 1-indexed
    INF = 10**9
    pair_u = [0]*(n_left+1)
    pair_v = [0]*(n_right+1)
    dist = [0]*(n_left+1)

    def bfs():
        q = deque()
        for u in range(1, n_left+1):
            if pair_u[u]==0:
                dist[u]=0
                q.append(u)
            else:
                dist[u]=INF
        dist[0]=INF
        while q:
            u=q.popleft()
            if dist[u]<dist[0]:
                for v in adj[u]:
                    if dist[pair_v[v]]==INF:
                        dist[pair_v[v]]=dist[u]+1
                        q.append(pair_v[v])
        return dist[0]!=INF

    def dfs(u):
        if u==0:
            return True
        for v in adj[u]:
            if dist[pair_v[v]]==dist[u]+1 and dfs(pair_v[v]):
                pair_u[u]=v
                pair_v[v]=u
                return True
        dist[u]=INF
        return False

    matching=0
    while bfs():
        for u in range(1, n_left+1):
            if pair_u[u]==0 and dfs(u):
                matching+=1
    return matching, pair_u, pair_v

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    adj = [[] for _ in range(k+1)]
    y_of_x = [0]*(k+1)
    triple_exists = {}
    for _ in range(t):
        x = int(next(it)); y = int(next(it)); z = int(next(it))
        if y_of_x[x]==0:
            y_of_x[x]=y
        # store edge
        adj[x].append(z)
        triple_exists[(x,z)] = (x,y,z)

    # quick check: any x without edges -> impossible
    for x in range(1, k+1):
        if not adj[x]:
            print("NO")
            return

    matching, pair_u, _ = hopcroft_karp(adj, k, k)
    if matching!=k:
        print("NO")
        return

    print("YES")
    out_lines = []
    for x in range(1, k+1):
        z = pair_u[x]
        # retrieve original triple (x, y_of_x[x], z)
        # it must exist
        triple = triple_exists.get((x,z))
        if triple is None:
            # fallback, construct using stored y
            triple = (x, y_of_x[x], z)
        out_lines.append(f"{triple[0]} {triple[1]} {triple[2]}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()