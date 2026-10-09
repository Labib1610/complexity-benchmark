import sys
sys.setrecursionlimit(1 << 20)
input = sys.stdin.readline

n, m = map(int, input().split())
N = 2 * n
g = [[] for _ in range(N)]
gr = [[] for _ in range(N)]

def node(var):
    # var is int, positive means True, negative means False
    if var > 0:
        return 2 * (var - 1)      # True node
    else:
        return 2 * (-var - 1) + 1 # False node

def add_imp(u, v):
    g[u].append(v)
    gr[v].append(u)

for _ in range(m):
    a, b = map(int, input().split())
    # (a OR b) => (!a -> b) and (!b -> a)
    na = -a
    nb = -b
    add_imp(node(na), node(b))
    add_imp(node(nb), node(a))

# Kosaraju's SCC
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
# Assign values: if comp[True] > comp[False] then True, else False
res = []
for i in range(n):
    if comp[2*i] > comp[2*i+1]:
        res.append('1')
    else:
        res.append('0')
print(' '.join(res))