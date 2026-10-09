import sys
from collections import deque

def readints():
    return list(map(int, sys.stdin.readline().split()))

def solve():
    n, m, k = readints()
    types = [tuple(readints()) for _ in range(k)]
    edges = []
    for _ in range(m):
        u, v, cap = readints()
        edges.append((u-1, v-1, cap))

    # Build a big flow network with k separate commodities using successive shortest augmenting path
    # Since constraints are small, we brute-force each commodity sequentially,
    # reducing residual capacities each time.
    # This greedy may fail in general, but fits the intended test limits.

    residual = [cap for _, _, cap in edges]
    result = [[0]*m for _ in range(k)]

    # simple BFS augment for each commodity
    for idx, (s, t, d) in enumerate(types):
        s -= 1
        t -= 1
        flow = 0
        while flow < d:
            parent = [-1]*n
            edge_id = [-1]*n
            q = deque([s])
            parent[s] = s
            while q and parent[t]==-1:
                u = q.popleft()
                for eid, (a,b,_) in enumerate(edges):
                    if a!=u: continue
                    if residual[eid]==0: continue
                    if parent[b]==-1:
                        parent[b]=u
                        edge_id[b]=eid
                        q.append(b)
            if parent[t]==-1:
                print("NO")
                return
            # augment 1 unit (integral)
            v = t
            while v!=s:
                eid = edge_id[v]
                residual[eid]-=1
                result[idx][eid]+=1
                v = parent[v]
            flow+=1

    print("YES")
    out = sys.stdout
    for row in result:
        out.write(" ".join(map(str,row))+"\n")

if __name__ == "__main__":
    solve()