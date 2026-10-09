import sys
input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(2 * n + 1)]

def node(var):
    if var > 0:
        return (var - 1) * 2
    else:
        return (-var - 1) * 2 + 1

def neg_node(u):
    return u ^ 1

for _ in range(m):
    a, b = map(int, input().split())
    u = node(a)
    v = node(b)
    # (not u) -> v
    g[neg_node(u)].append(v)
    # (not v) -> u
    g[neg_node(v)].append(u)

# Kosaraju SCC
N = 2 * n
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

gr = [[] for _ in range(N)]
for u in range(N):
    for v in g[u]:
        gr[v].append(u)

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

for i in range(n):
    if comp[2 * i] == comp[2 * i + 1]:
        print("NO")
        sys.exit()

print("YES")
res = []
for i in range(n):
    # if comp[2i] > comp[2i+1] then true
    res.append('1' if comp[2 * i] > comp[2 * i + 1] else '0')
print(' '.join(res))