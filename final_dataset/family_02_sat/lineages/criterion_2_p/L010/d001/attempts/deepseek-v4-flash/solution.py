import sys
sys.setrecursionlimit(1 << 20)
input = sys.stdin.readline

n, m = map(int, input().split())
N = 2 * n  # each variable has two nodes: x_i and ~x_i

def node(var):
    # var is signed int: positive -> true literal, negative -> false literal
    if var > 0:
        return (var - 1) * 2      # true node
    else:
        return (-var - 1) * 2 + 1 # false node

g = [[] for _ in range(N)]
gr = [[] for _ in range(N)]

for _ in range(m):
    a, b = map(int, input().split())
    # clause: (a) OR (b)
    # implication: ~a -> b, ~b -> a
    na = node(-a)
    nb = node(-b)
    a_node = node(a)
    b_node = node(b)
    g[na].append(b_node)
    gr[b_node].append(na)
    g[nb].append(a_node)
    gr[a_node].append(nb)

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
ans = [0] * n
for i in range(n):
    # If true node has higher comp id, assign true (1)
    ans[i] = 1 if comp[2*i] > comp[2*i+1] else 0
print(' '.join(map(str, ans)))