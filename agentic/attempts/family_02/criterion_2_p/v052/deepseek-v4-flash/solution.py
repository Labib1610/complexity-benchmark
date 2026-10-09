import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
N = 2 * n  # variables: 0..n-1 for x_i, n..2n-1 for not x_i

def var(x):
    # x is int literal: positive -> x-1, negative -> n + (-x-1)
    if x > 0:
        return x - 1
    else:
        return n + (-x - 1)

def neg(v):
    if v < n:
        return v + n
    else:
        return v - n

g = [[] for _ in range(N)]
gr = [[] for _ in range(N)]

for _ in range(m):
    a, b = map(int, input().split())
    u = var(a)
    v = var(b)
    # (u or v) => (!u -> v) and (!v -> u)
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
    if comp[i] == comp[i + n]:
        print("NO")
        sys.exit()

# Assign values: if comp[x] > comp[not x] -> True
res = [0] * n
for i in range(n):
    res[i] = 1 if comp[i] > comp[i + n] else 0

print("YES")
print(" ".join(map(str, res)))