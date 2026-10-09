import sys
sys.setrecursionlimit(1 << 20)
input = sys.stdin.readline

n, m = map(int, input().split())
N = 2 * n  # nodes: 0..n-1 for x, n..2n-1 for ¬x

def node(var):
    # var > 0 => x, var < 0 => ¬x
    if var > 0:
        return (var - 1) * 2      # even index for x
    else:
        return (-var - 1) * 2 + 1 # odd index for ¬x

def neg(idx):
    return idx ^ 1

g = [[] for _ in range(N)]
gr = [[] for _ in range(N)]

for _ in range(m):
    a, b = map(int, input().split())
    u = node(a)
    v = node(b)
    # ¬a -> b
    g[neg(u)].append(v)
    gr[v].append(neg(u))
    # ¬b -> a
    g[neg(v)].append(u)
    gr[u].append(neg(v))

# Kosaraju's SCC
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
    for w in gr[u]:
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

print("YES")
res = [0] * n
for i in range(n):
    # If ¬x is in a later SCC than x, set x = 1
    if comp[2*i] > comp[2*i+1]:
        res[i] = 1
    else:
        res[i] = 0

print(' '.join(map(str, res)))