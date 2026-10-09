import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

n, m = map(int, input().split())
N = 2 * n + 1

def node(var):
    if var > 0:
        return var * 2
    else:
        return (-var) * 2 + 1

def neg_node(node_id):
    return node_id ^ 1

g = [[] for _ in range(N)]
gr = [[] for _ in range(N)]

for _ in range(m):
    a, b = map(int, input().split())
    u = node(a)
    v = node(b)
    # implication: not a -> b
    g[neg_node(u)].append(v)
    gr[v].append(neg_node(u))
    # implication: not b -> a
    g[neg_node(v)].append(u)
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

for i in range(2, N):
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
for i in range(1, n + 1):
    if comp[node(i)] == comp[neg_node(node(i))]:
        print("NO")
        sys.exit()

print("YES")
res = []
for i in range(1, n + 1):
    # If upgrade literal is reachable before legacy, choose 1 else 0
    # In SCC order, comp with smaller id is processed later in Kosaraju
    # We can assign based on topological order: choose value with larger comp id.
    if comp[node(i)] > comp[neg_node(node(i))]:
        res.append("1")
    else:
        res.append("0")
print(" ".join(res))