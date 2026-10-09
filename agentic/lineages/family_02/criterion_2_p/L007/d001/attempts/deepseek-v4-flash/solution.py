import sys
sys.setrecursionlimit(1 << 20)
input = sys.stdin.readline

n, m = map(int, input().split())
N = 2 * n  # each variable has two nodes: 2*i for false, 2*i+1 for true

def node(var, val):
    # var: 1-based zone index, val: 0 or 1
    return 2 * (var - 1) + val

g = [[] for _ in range(N)]
gr = [[] for _ in range(N)]

def add_imp(u, v):
    g[u].append(v)
    gr[v].append(u)

for _ in range(m):
    l1, l2 = map(int, input().split())
    a = abs(l1)
    b = abs(l2)
    da = 1 if l1 > 0 else 0
    db = 1 if l2 > 0 else 0
    # Forbidden: (x_a == 1-da) AND (x_b == 1-db)
    # Clause: (x_a == da) OR (x_b == db)
    # Implications:
    # not (x_a == da) -> (x_b == db)
    # not (x_b == db) -> (x_a == da)
    add_imp(node(a, 1 - da), node(b, db))
    add_imp(node(b, 1 - db), node(a, da))

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
    # If false node comes after true node in topological order, assign true
    if comp[2*i] > comp[2*i+1]:
        res.append(1)
    else:
        res.append(0)
print(' '.join(map(str, res)))