import sys
sys.setrecursionlimit(1 << 20)
input = sys.stdin.readline

n, m = map(int, input().split())
N = 2 * n  # nodes: 0..n-1 for x, n..2n-1 for ~x

def var(x):
    if x > 0:
        return (x - 1) * 2      # even index for positive
    else:
        return (-x - 1) * 2 + 1 # odd index for negative

def neg(v):
    return v ^ 1

g = [[] for _ in range(N)]
gr = [[] for _ in range(N)]

for _ in range(m):
    a, b = map(int, input().split())
    u = var(a)
    v = var(b)
    # (a or b) and (~a or ~b)
    # (u or v)
    g[neg(u)].append(v)
    g[neg(v)].append(u)
    gr[v].append(neg(u))
    gr[u].append(neg(v))
    # (~u or ~v)
    g[u].append(neg(v))
    g[v].append(neg(u))
    gr[neg(v)].append(u)
    gr[neg(u)].append(v)

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
    # if comp[2*i] > comp[2*i+1] => true (energized)
    res.append('1' if comp[2*i] > comp[2*i+1] else '0')
print(' '.join(res))