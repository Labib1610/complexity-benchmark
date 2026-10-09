import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
N = 2 * n  # nodes: 0..n-1 for x_i, n..2n-1 for ¬x_i

def var(i):
    return i - 1  # 0-based for positive

def neg(i):
    return i + n if i < n else i - n

g = [[] for _ in range(N)]
gr = [[] for _ in range(N)]

for _ in range(m):
    a, b = map(int, input().split())
    # a OR b
    # ¬a -> b
    # ¬b -> a
    u = var(abs(a)) if a > 0 else neg(var(abs(a)))
    v = var(abs(b)) if b > 0 else neg(var(abs(b)))
    # ¬u -> v
    g[neg(u)].append(v)
    gr[v].append(neg(u))
    # ¬v -> u
    g[neg(v)].append(u)
    gr[u].append(neg(v))

# Kosaraju SCC
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
    if comp[i] == comp[neg(i)]:
        print("NO")
        sys.exit()

print("YES")
res = [0] * n
for i in range(n):
    # If comp[i] > comp[neg(i)], set true
    res[i] = 1 if comp[i] > comp[neg(i)] else 0
print(' '.join(map(str, res)))