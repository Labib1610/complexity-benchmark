import sys
sys.setrecursionlimit(1 << 20)
input = sys.stdin.readline

n, m = map(int, input().split())
N = 2 * n  # each variable has two nodes: x and not x

def node(var):
    # var is signed integer: positive x -> (x-1)*2 for true, negative -> (x-1)*2+1 for false
    if var > 0:
        return (var - 1) * 2
    else:
        return (-var - 1) * 2 + 1

def neg_node(idx):
    return idx ^ 1

g = [[] for _ in range(N)]
gr = [[] for _ in range(N)]

for _ in range(m):
    a, b = map(int, input().split())
    u = node(a)
    v = node(b)
    # clause (a OR b) => (not a -> b) and (not b -> a)
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
res = [0] * n
for i in range(n):
    # If comp[true] > comp[false], assign true
    res[i] = 1 if comp[2*i] > comp[2*i+1] else 0
print(' '.join(map(str, res)))