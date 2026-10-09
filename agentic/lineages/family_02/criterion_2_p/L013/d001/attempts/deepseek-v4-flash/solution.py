import sys
sys.setrecursionlimit(1 << 20)
input = sys.stdin.readline

n, m = map(int, input().split())
N = 2 * n  # nodes: 0..n-1 for positive, n..2n-1 for negative

def node(var):
    # var is signed int: positive -> index var-1, negative -> index n + (-var)-1
    if var > 0:
        return var - 1
    else:
        return n + (-var) - 1

def neg_node(idx):
    # given node index, return its negation node index
    if idx < n:
        return idx + n
    else:
        return idx - n

g = [[] for _ in range(N)]
gr = [[] for _ in range(N)]

for _ in range(m):
    a, b = map(int, input().split())
    u = node(a)
    v = node(b)
    # (a OR b) => (!a -> b) and (!b -> a)
    g[neg_node(u)].append(v)
    g[neg_node(v)].append(u)
    gr[v].append(neg_node(u))
    gr[u].append(neg_node(v))

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
    if comp[i] == comp[i + n]:
        print("NO")
        sys.exit()

# Assign values: if comp[var] > comp[neg(var)] then True
res = [0] * n
for i in range(n):
    res[i] = 1 if comp[i] > comp[i + n] else 0

print("YES")
print(" ".join(map(str, res)))