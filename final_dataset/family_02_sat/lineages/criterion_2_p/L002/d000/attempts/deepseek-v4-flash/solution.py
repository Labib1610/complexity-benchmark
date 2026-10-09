import sys
sys.setrecursionlimit(1 << 20)
input = sys.stdin.readline

n, m = map(int, input().split())
N = 2 * n  # nodes: 2*i for false, 2*i+1 for true

def node(var):
    # var > 0: machine var in mode 1
    # var < 0: machine |var| in mode 0
    if var > 0:
        return 2 * (var - 1) + 1
    else:
        return 2 * (-var - 1)

g = [[] for _ in range(N)]
gr = [[] for _ in range(N)]

for _ in range(m):
    a, b = map(int, input().split())
    # clause (a OR b) => (!a -> b) and (!b -> a)
    na = node(-a)
    nb = node(-b)
    va = node(a)
    vb = node(b)
    g[na].append(vb)
    gr[vb].append(na)
    g[nb].append(va)
    gr[va].append(nb)

# Kosaraju SCC
visited = [False] * N
order = []

def dfs1(u):
    visited[u] = True
    for v in g[u]:
        if not visited[v]:
            dfs1(v)
    order.append(u)

for i in range(N):
    if not visited[i]:
        dfs1(i)

comp = [-1] * N
def dfs2(u, cid):
    comp[u] = cid
    for v in gr[u]:
        if comp[v] == -1:
            dfs2(v, cid)

cid = 0
for u in reversed(order):
    if comp[u] == -1:
        dfs2(u, cid)
        cid += 1

# Check satisfiability
for i in range(n):
    if comp[2*i] == comp[2*i+1]:
        print("NO")
        sys.exit()

# Assign values: if comp[true] < comp[false] => true
res = [0] * n
for i in range(n):
    # true node: 2*i+1, false node: 2*i
    res[i] = 1 if comp[2*i+1] < comp[2*i] else 0

print("YES")
print(" ".join(map(str, res)))