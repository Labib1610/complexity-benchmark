import sys
sys.setrecursionlimit(1 << 20)
input = sys.stdin.readline

n, m = map(int, input().split())
N = 2 * n  # nodes: 2*i for x_i false, 2*i+1 for x_i true

def node(var):
    # var > 0: x_var true, var < 0: x_var false
    if var > 0:
        return 2 * (var - 1) + 1
    else:
        return 2 * (-var - 1)

def neg_node(u):
    return u ^ 1

g = [[] for _ in range(N)]
gr = [[] for _ in range(N)]

for _ in range(m):
    a, b = map(int, input().split())
    u = node(a)
    v = node(b)
    # clause: u OR v
    # implications: not u -> v, not v -> u
    g[neg_node(u)].append(v)
    g[neg_node(v)].append(u)
    gr[v].append(neg_node(u))
    gr[u].append(neg_node(v))

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
res = []
for i in range(n):
    # If comp[true] > comp[false], assign true (1)
    if comp[2*i+1] > comp[2*i]:
        res.append('1')
    else:
        res.append('0')
print(' '.join(res))