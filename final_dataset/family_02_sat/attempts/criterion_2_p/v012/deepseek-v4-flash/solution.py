import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
N = 2 * n

def node(lit):
    # lit > 0: vent lit is 1 -> variable (lit-1)*2 + 1
    # lit < 0: vent -lit is 0 -> variable (-lit-1)*2
    v = abs(lit) - 1
    if lit > 0:
        return 2 * v + 1
    else:
        return 2 * v

def neg(x):
    return x ^ 1

g = [[] for _ in range(N)]
gr = [[] for _ in range(N)]

for _ in range(m):
    a, b = map(int, input().split())
    u = node(a)
    v = node(b)
    # (a OR b) => (!a -> b) and (!b -> a)
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

# Assign values: if comp[var] > comp[!var] then true
ans = [0] * n
for i in range(n):
    # variable true if comp[2*i+1] > comp[2*i]
    ans[i] = 1 if comp[2*i+1] > comp[2*i] else 0

print("YES")
print(" ".join(map(str, ans)))