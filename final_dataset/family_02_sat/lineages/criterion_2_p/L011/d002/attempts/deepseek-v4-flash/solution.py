import sys
sys.setrecursionlimit(1 << 20)
input = sys.stdin.readline

n, m = map(int, input().split())

# 2-SAT: variable i (1..n) -> node 2*i for True, 2*i+1 for False
# We'll use 0-based indexing: node 2*i = True, 2*i+1 = False for i in 0..n-1

def node(var):
    # var is int, positive = True, negative = False
    idx = abs(var) - 1
    if var > 0:
        return 2 * idx
    else:
        return 2 * idx + 1

N = 2 * n
g = [[] for _ in range(N)]
gr = [[] for _ in range(N)]

def add_imp(u, v):
    g[u].append(v)
    gr[v].append(u)

for _ in range(m):
    a, b = map(int, input().split())
    # clause (a or b) => (!a -> b) and (!b -> a)
    na = node(-a)
    nb = node(-b)
    add_imp(na, node(b))
    add_imp(nb, node(a))

# Kosaraju SCC
visited = [False] * N
order = []

def dfs1(u):
    visited[u] = True
    for v in g[u]:
        if not visited[v]:
            dfs1(v)
    order.append(u)

for i in range(N):
    if not visited[i]:
        dfs1(i)

comp = [-1] * N
def dfs2(u, cid):
    comp[u] = cid
    for v in gr[u]:
        if comp[v] == -1:
            dfs2(v, cid)

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
ans = []
for i in range(n):
    # If True node has higher comp id, assign True (1)
    if comp[2*i] > comp[2*i+1]:
        ans.append(1)
    else:
        ans.append(0)
print(*ans)