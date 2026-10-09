import sys
sys.setrecursionlimit(1 << 20)
input = sys.stdin.readline

n, m = map(int, input().split())
N = 2 * n  # each variable has two nodes: i*2 = false, i*2+1 = true

g = [[] for _ in range(N)]
gr = [[] for _ in range(N)]

def add_imp(u, v):
    g[u].append(v)
    gr[v].append(u)

def add_clause(a, b):
    # clause (a or b)
    # ~a -> b, ~b -> a
    add_imp(a ^ 1, b)
    add_imp(b ^ 1, a)

def node(lit):
    # lit > 0: variable = lit-1, true
    # lit < 0: variable = -lit-1, false
    var = abs(lit) - 1
    if lit > 0:
        return 2 * var + 1  # true
    else:
        return 2 * var      # false

for _ in range(m):
    l1, l2 = map(int, input().split())
    a = node(l1)
    b = node(l2)
    # forbid both true: (~a or ~b)
    add_clause(a ^ 1, b ^ 1)

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
    # if true node comes after false node in topological order, assign true
    res.append('1' if comp[2*i+1] > comp[2*i] else '0')
print(' '.join(res))