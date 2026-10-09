import sys
sys.setrecursionlimit(1 << 20)
input = sys.stdin.readline

n, m = map(int, input().split())
N = 2 * n  # each variable has two nodes: 2*i = false, 2*i+1 = true

g = [[] for _ in range(N)]
gr = [[] for _ in range(N)]

def add_imp(u, v):
    g[u].append(v)
    gr[v].append(u)

def add_clause(a, b):
    # a and b are literals: positive = true, negative = false
    # clause: (a OR b)
    # implications: !a -> b, !b -> a
    def node(lit):
        var = abs(lit) - 1
        if lit > 0:
            return 2 * var + 1
        else:
            return 2 * var
    def neg_node(lit):
        var = abs(lit) - 1
        if lit > 0:
            return 2 * var
        else:
            return 2 * var + 1
    add_imp(neg_node(a), node(b))
    add_imp(neg_node(b), node(a))

for _ in range(m):
    a, b = map(int, input().split())
    add_clause(a, b)

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
res = [0] * n
for i in range(n):
    # If true node has higher comp id, assign true
    res[i] = 1 if comp[2*i+1] > comp[2*i] else 0
print(' '.join(map(str, res)))