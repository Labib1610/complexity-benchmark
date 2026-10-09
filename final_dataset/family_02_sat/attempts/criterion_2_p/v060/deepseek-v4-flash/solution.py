import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
N = 2 * n  # each variable has two nodes: x -> 2*(x-1), ~x -> 2*(x-1)+1

def node(var):
    if var > 0:
        return 2 * (var - 1)
    else:
        return 2 * (-var - 1) + 1

g = [[] for _ in range(N)]
gr = [[] for _ in range(N)]

for _ in range(m):
    a, b = map(int, input().split())
    u = node(a)
    v = node(b)
    # ~u -> v
    g[u ^ 1].append(v)
    gr[v].append(u ^ 1)
    # ~v -> u
    g[v ^ 1].append(u)
    gr[u].append(v ^ 1)

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
    # If comp[2*i] > comp[2*i+1], assign true (1), else false (0)
    res.append('1' if comp[2*i] > comp[2*i+1] else '0')
print(' '.join(res))