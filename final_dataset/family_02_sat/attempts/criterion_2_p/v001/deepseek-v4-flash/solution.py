import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
N = 2 * n  # nodes: 2*i for False, 2*i+1 for True

def var(x):
    # x is signed int: positive -> True, negative -> False
    v = abs(x) - 1
    return 2 * v + (1 if x > 0 else 0)

def neg(node):
    return node ^ 1

g = [[] for _ in range(N)]
gr = [[] for _ in range(N)]

for _ in range(m):
    a, b = map(int, input().split())
    u = var(a)
    v = var(b)
    # clause (u or v) => (!u -> v) and (!v -> u)
    g[neg(u)].append(v)
    g[neg(v)].append(u)
    gr[v].append(neg(u))
    gr[u].append(neg(v))

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
ans = [0] * n
for i in range(n):
    # In Kosaraju, comp id order gives topological order of SCCs.
    # If comp[True] > comp[False], then True is reachable from False => set True.
    ans[i] = 1 if comp[2*i+1] > comp[2*i] else 0

print(' '.join(map(str, ans)))