import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
N = 2 * n
g = [[] for _ in range(N)]
rg = [[] for _ in range(N)]

def node(lit):
    # lit is int, positive = True, negative = False
    var = abs(lit) - 1
    if lit > 0:
        return 2 * var + 1  # True
    else:
        return 2 * var      # False

def neg_node(u):
    return u ^ 1

def add_imp(u, v):
    g[u].append(v)
    rg[v].append(u)

for _ in range(m):
    a, b = map(int, input().split())
    u = node(a)
    v = node(b)
    # a -> b
    add_imp(u, v)
    # b -> a
    add_imp(v, u)
    # not a -> not b
    add_imp(neg_node(u), neg_node(v))
    # not b -> not a
    add_imp(neg_node(v), neg_node(u))

# Kosaraju SCC
visited = [False] * N
order = []

def dfs1(u):
    visited[u] = True
    for w in g[u]:
        if not visited[w]:
            dfs1(w)
    order.append(u)

for i in range(N):
    if not visited[i]:
        dfs1(i)

comp = [-1] * N

def dfs2(u, cid):
    comp[u] = cid
    for w in rg[u]:
        if comp[w] == -1:
            dfs2(w, cid)

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

# Assign values: in reverse topological order of SCCs
# comp id larger = earlier in topological order of condensation DAG
assign = [False] * n
for i in range(n):
    # If True node comes after False node in topological order, set True
    assign[i] = comp[2*i+1] > comp[2*i]

print("YES")
print(' '.join('1' if assign[i] else '0' for i in range(n)))