import sys
sys.setrecursionlimit(1 << 20)
input = sys.stdin.readline

n, m = map(int, input().split())
N = 2 * n  # each variable has two nodes: 2*i = false, 2*i+1 = true

def node(lit):
    # lit > 0: variable (lit-1) true -> node 2*(lit-1)+1
    # lit < 0: variable (-lit-1) false -> node 2*(-lit-1)
    if lit > 0:
        return 2 * (lit - 1) + 1
    else:
        return 2 * (-lit - 1)

g = [[] for _ in range(N)]
gr = [[] for _ in range(N)]

for _ in range(m):
    a, b = map(int, input().split())
    # clause (a OR b) => (!a -> b) and (!b -> a)
    na = -a
    nb = -b
    u = node(na)
    v = node(b)
    g[u].append(v)
    gr[v].append(u)
    u = node(nb)
    v = node(a)
    g[u].append(v)
    gr[v].append(u)

# Kosaraju's SCC
visited = [False] * N
order = []

def dfs1(v):
    visited[v] = True
    for to in g[v]:
        if not visited[to]:
            dfs1(to)
    order.append(v)

for i in range(N):
    if not visited[i]:
        dfs1(i)

comp = [-1] * N

def dfs2(v, cid):
    comp[v] = cid
    for to in gr[v]:
        if comp[to] == -1:
            dfs2(to, cid)

cid = 0
for v in reversed(order):
    if comp[v] == -1:
        dfs2(v, cid)
        cid += 1

# Check satisfiability
for i in range(n):
    if comp[2*i] == comp[2*i+1]:
        print("NO")
        sys.exit()

print("YES")
res = []
for i in range(n):
    # comp[2*i+1] > comp[2*i] means true
    res.append('1' if comp[2*i+1] > comp[2*i] else '0')
print(' '.join(res))