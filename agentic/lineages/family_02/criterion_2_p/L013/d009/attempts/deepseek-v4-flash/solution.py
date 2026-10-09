import sys
sys.setrecursionlimit(1 << 20)
input = sys.stdin.readline

n, m = map(int, input().split())
N = 2 * n  # each variable has two nodes: 2*i for false, 2*i+1 for true

def node(var, val):
    # var: 0..n-1, val: True/False
    return 2 * var + (1 if val else 0)

def neg(node_idx):
    return node_idx ^ 1

g = [[] for _ in range(N)]
gr = [[] for _ in range(N)]

def add_imp(u, v):
    g[u].append(v)
    gr[v].append(u)

def add_clause(a, b):
    # clause (a or b)
    add_imp(neg(a), b)
    add_imp(neg(b), a)

for _ in range(m):
    l1, l2 = map(int, input().split())
    # literal that causes -1 for each connection
    def lit(l):
        idx = abs(l) - 1
        if l > 0:
            return node(idx, False)  # s=0 -> -1
        else:
            return node(idx, True)   # s=1 -> -1
    A = lit(l1)
    B = lit(l2)
    # forbid A and B both true: clause (not A or not B)
    add_clause(neg(A), neg(B))

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
    if comp[2*i+1] > comp[2*i]:
        res.append(1)
    else:
        res.append(0)
print(' '.join(map(str, res)))