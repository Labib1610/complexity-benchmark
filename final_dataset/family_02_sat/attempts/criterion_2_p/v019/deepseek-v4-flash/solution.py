import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
N = 2 * n  # each variable has two nodes: i*2 = false, i*2+1 = true

g = [[] for _ in range(N)]
gr = [[] for _ in range(N)]

def add_imp(u, v):
    g[u].append(v)
    gr[v].append(u)

def node(var):
    # var > 0: true node for var
    # var < 0: false node for |var|
    if var > 0:
        return (var - 1) * 2 + 1
    else:
        return (-var - 1) * 2

for _ in range(m):
    a, b = map(int, input().split())
    # clause (a OR b) => (!a -> b) and (!b -> a)
    add_imp(node(-a), node(b))
    add_imp(node(-b), node(a))

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

print("YES")
res = []
for i in range(n):
    # if true node comes after false node in topological order => assign true
    res.append('1' if comp[2*i+1] > comp[2*i] else '0')
print(' '.join(res))